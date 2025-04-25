# Advanced-Discord-Webhook-Spammer
Advanced Webhook Spammer built in Python for high-speed message spamming to Discord webhooks. Features include message variants, embeds, rate-limit bypass, threading, and file input support. Customize delays, add random emojis, and control thread count for efficient spamming. Use responsibly!


# 🔥 Advanced Webhook Spammer

A powerful and high-speed **Webhook Spammer** built in Python to send multiple messages to Discord webhooks. Features include **message variants**, **embeds**, **rate-limit bypass**, and **threading** for efficient spamming. Use it responsibly! ⚠️

## ⚙️ Features:
- **Message Variants**: Send messages with random emojis like 🔥, 💥, 🚀, etc.
- **Embeds**: Option to send messages as Discord embeds. 🧱
- **Rate-Limit Bypass**: Handles Discord's rate-limiting automatically with retries. ⏱️
- **Threading**: Uses multiple threads for high-speed spamming. 🧵
- **File Input Support**: Load messages from a file and spam random lines. 📄
- **Customizable Delay**: Control the delay between messages to avoid rate-limiting. ⏳

## 📦 Requirements:
- Python 3.x
- `requests` library: Install via `pip install requests`
- `colorama` library: Install via `pip install colorama`

## 🚀 Usage:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ryuk-LOL/Advanced-Discord-Webhook-Spammer.git
   cd Advanced-Discord-Webhook-Spammer

Install Dependencies:


pip install -r requirements.txt
Run the Script:


python spammer.py
Follow the prompts to enter the webhook URL, message settings, and spam parameters. 🎯

📝 How It Works:
After running the script, you'll be prompted to enter your Discord webhook URL.

Choose whether to input the message directly or load it from a file.

Set the number of messages, delay between messages, and threads to use.

The script will automatically handle sending messages and bypass rate limits. ⚡

⚠️ Disclaimer:
Use responsibly! Do not spam webhooks that you do not own or have permission to use.

Avoid using on public webhooks as it may violate Discord's Terms of Service. 🚫

👨‍💻 Made By:
ryuk.lyy 🧑‍💻

🎨 Example:
🔗 Webhook URL: https://discord.com/api/webhooks/...
📄 Use message from (1) input or (2) file? [1/2]: 1
💬 Message to spam: Hello World! 🔥
🎲 Add random emoji after message? (y/n): y
🧱 Send as embed? (y/n): y
🔁 Number of messages to send: 100
⏱ Delay between messages (in seconds): 0.5
🧵 Number of threads to use: 4
💡 Tips:
Adjust the delay to avoid rate-limiting.

Use a file for diverse messages to make the spam look more natural. 📂

Be cautious when using this tool to avoid being flagged by Discord. ⚠️
