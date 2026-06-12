# 🎌 ARIA - AI Anime Bot

A cute anime-themed AI assistant that can chat and execute system commands!

## ✨ Features
- 💬 **Smart conversations** powered by OpenAI GPT-4
- 🎀 **Kawaii personality** with anime expressions and emojis
- ⚙️ **Command execution** - run shell commands directly
- 📝 **Conversation memory** - remembers chat history
- 🔒 **Safe** - secure command execution with timeout protection

## 🚀 Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup OpenAI API Key
```bash
# Create .env file in the project root
cp .env.example .env

# Edit .env and add your OpenAI API key
OPENAI_API_KEY=sk-your_api_key_here
```

Get your API key: https://platform.openai.com/api-keys

### 3. Run the Bot
```bash
python anime_bot.py
```

## 💬 Usage Examples

### Chat
```
You: Hey ARIA, what's your favorite anime?
ARIA: Sugoi! I love so many anime! My favorites include Demon Slayer and Jujutsu Kaisen! 💕✨
```

### Execute Commands
Use any of these formats:

```
You: run ls -la
You: ! pwd
You: execute python --version
You: command mkdir my_folder
You: ls -la
```

### Chat and Command Mix
```
You: show me current directory
ARIA: Sure! Let me check for you~ 💫
📤 Command Output:
[lists current directory contents]
```

## 🎮 Commands
- `run <command>` - Execute a shell command
- `!<command>` - Quick command execution
- `execute <command>` - Execute command
- `command <command>` - Execute command
- `exit` or `quit` - Close the bot

## ⚙️ Features
- ✅ Multi-turn conversations
- ✅ Command execution with output capture
- ✅ Timeout protection (10 seconds per command)
- ✅ Error handling
- ✅ Anime personality and kawaii responses

## 📌 Notes
- Each command times out after 10 seconds
- Conversation history is kept during the session
- Commands execute in your current shell environment
- For safety, dangerous commands should be handled with care

## 💕 Anime Personality
ARIA uses:
- Japanese expressions (arigatou, sugoi, kawaii, etc)
- Cute emojis (💕, ✨, 🎀, etc)
- Friendly and supportive tone
- Anime girl character roleplay

Enjoy chatting with your cute AI bot! アリアとお話しましょう! 💫
