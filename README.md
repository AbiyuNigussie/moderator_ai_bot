# Discord AI Moderator Bot

**Discord AI Moderator Bot** is a powerful and intelligent moderation bot for Discord servers, leveraging a custom-trained AI model to detect and mitigate hate speech in real time. This ensures a safer and more inclusive community for all members.

## 🛠 Features

- 🚨 **Real-time Message Moderation** – Detects and removes hate speech automatically.
- 🤖 **AI-Powered Detection** – Uses a trained Python AI model (SimpleRNN, LSTM, or fine-tuned BERT) for accurate text analysis.
- 🔌 **Easy Integration** – Simple setup with Discord bot API.

## 🏗 Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `discord.py` library
- `transformers`, `nltk`, `scikit-learn`, and other dependencies

### Setup Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/discord-ai-moderator.git
   cd discord-ai-moderator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your bot token in a `.env` file:
   ```env
   TOKEN=your_discord_token_here
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## 🧠 AI Model
The model is trained on a curated dataset to ensure high accuracy and minimal false positives.

## 🚀 Usage
- The bot will automatically scan messages in all channels.
- If hate speech is detected, it can take actions like deleting messages, warning users, or kicking them based on the configuration.
- Admins can review flagged messages via logs.

## 🤝 Contributing
Pull requests are welcome! If you'd like to contribute, please fork the repository and submit a PR.

## 📞 Contact
For any issues or feature requests, open an issue on the [GitHub repo](https://github.com/AbiyuNigussie/moderator_ai_bot).
