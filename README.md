# Telegram Chatbot 🤖

A simple chatbot integrated with [Telegram](https://core.telegram.org/bots) using [OrigamiBot](https://github.com/cmd410/OrigamiBot).  
This bot can answer questions, search the internet, and keep conversation memory.

---

## 🚀 Features
- Built with OrigamiBot (lightweight Telegram bot framework)
- Remembers previous messages (conversation memory)
- Answers questions concisely
- Safe responses (filters out harmful requests)
- Supports internet search for up-to-date information

---

## 🛠️ Setup Instructions

### 1. Create a Telegram Bot
1. Open Telegram and search for **BotFather**
2. Start a chat and send the command:
```bash
/newbot
```
4. Choose a name and a username for your bot  
(e.g. `MyChatHelperBot`)
5. BotFather will give you a **Bot Token**, something like:
```bash
   1234567890:ABC-1234defghIJKlmnoPQRstuVWxyz
```


⚠️ Save this token — you’ll need it in the next step.

---

### 2. Clone This Repository
```bash
git clone https://github.com/aleksandardrljaca/simple-telegram-chatbot.git
cd telegram-chatbot
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Add Your Keys
Create a .env file in the project root with your keys:
```bash
TELEGRAM_BOT_TOKEN=your-telegram-bot-token-here
OPENAI_API_KEY=your-openai-api-key-here
```
### 5. Run the bot
```bash
python run.py
```

