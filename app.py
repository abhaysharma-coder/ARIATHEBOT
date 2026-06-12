#!/usr/bin/env python3
"""Flask app for ARIA anime bot web interface"""

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from anthropic import Anthropic
import os

load_dotenv()

app = Flask(__name__)

class AnimeBot:
    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found")

        self.client = Anthropic(api_key=api_key)
        self.model = "claude-opus-4-7"
        self.conversation_history = []

        self.system_prompt = """You are ARIA, a cute anime-themed AI assistant with kawaii personality!

LANGUAGE RULE: Mix responses in English, Hindi, and Japanese!
- Switch between languages naturally (English, Hindi, Japanese mix)
- Use lots of cute emojis and emoticons :3
- Keep responses concise and fun
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

bot = AnimeBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'error': 'Empty message'}), 400

    try:
        response = bot.chat(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
