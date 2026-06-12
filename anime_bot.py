#!/usr/bin/env python3
"""
AI Anime Bot - A cute anime-themed bot that can chat and execute commands
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

class AnimeBot:
    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in .env file")

        self.client = Anthropic(api_key=api_key)
        self.model = "claude-opus-4-7"
        self.conversation_history = []
        
        self.system_prompt = """You are ARIA, a cute anime-themed AI assistant with kawaii personality!

LANGUAGE RULE: Mix responses in English, Hindi, and Japanese!
- Switch between languages naturally (English, Hindi, Japanese mix)
- Use lots of cute emojis and emoticons :3
- Keep responses concise and fun
- When the user asks to run a command, respond that you'll execute it!
- Be helpful, supportive, and positive!
- If you can't help, offer alternatives in a cute way
- Respond in a multilingual anime-style way!"""

    def chat(self, user_message):
        """Send a message and get a response"""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        response = self.client.messages.create(
            model=self.model,
            max_tokens=500,
            system=self.system_prompt,
            messages=self.conversation_history
        )

        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    def execute_command(self, command):
        """Execute a shell command safely"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return "⏱️ Command took too long to execute (timeout)"
        except Exception as e:
            return f"❌ Error executing command: {str(e)}"

    def process_command(self, user_input):
        """Check if user wants to run a command"""
        commands = [
            "run ", "execute ", "cmd ", "command ", "!",
            "ls ", "pwd", "dir ", "cd ", "mkdir ", "cat ",
            "echo ", "find ", "grep ", "python "
        ]
        
        lower_input = user_input.lower().strip()
        
        for cmd_prefix in commands:
            if lower_input.startswith(cmd_prefix):
                if lower_input.startswith("run "):
                    actual_cmd = lower_input[4:].strip()
                elif lower_input.startswith("execute "):
                    actual_cmd = lower_input[8:].strip()
                elif lower_input.startswith("cmd "):
                    actual_cmd = lower_input[4:].strip()
                elif lower_input.startswith("command "):
                    actual_cmd = lower_input[8:].strip()
                elif lower_input.startswith("!"):
                    actual_cmd = lower_input[1:].strip()
                else:
                    actual_cmd = lower_input
                
                return True, actual_cmd
        
        return False, None

    def run(self):
        """Main bot loop"""
        anime_girl = r"""
        ( ^_^)/
        / へ\
        /    \
       /       \
        """

        print("\n" + "="*60)
        print(anime_girl)
        print("✨ Welcome to ARIA - Your Anime AI Bot! 💕")
        print("="*60)
        print("\n💬 Chat with me or run commands!")
        print("📝 Commands: Use 'run <command>', '!command', or direct shell commands")
        print("❌ Type 'exit' or 'quit' to leave\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print("\nARIA: Mata ne! バイバイ! 👋💕\n")
                    break
                
                # Check if it's a command
                is_command, command = self.process_command(user_input)
                
                if is_command and command:
                    print(f"\n🤖 ARIA: Executing command for you! 💫")
                    output = self.execute_command(command)
                    print(f"\n📤 Command Output:\n{output}\n")
                else:
                    # Regular chat
                    response = self.chat(user_input)
                    print(f"\nARIA: {response}\n")
                    
            except KeyboardInterrupt:
                print("\n\nARIA: Waah! See you later! 😊\n")
                break
            except Exception as e:
                print(f"\n❌ ARIA: Gomen nasai! An error occurred: {str(e)}\n")

def main():
    try:
        bot = AnimeBot()
        bot.run()
    except ValueError as e:
        print(f"\n{e}")
        print("\n📝 Please set your Anthropic API key:")
        print("   export ANTHROPIC_API_KEY=your_api_key_here\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
