English Accent Training Telegram Bot
This repository contains the source code for a Telegram bot (bot.py) that automates access to an English Accent Training course. The bot integrates with Gumroad for payment verification and grants access to a private Telegram channel upon successful purchase. It’s designed to deliver a seamless experience for students learning English accents, with potential extensibility for Mandarin and web development courses.
Features

Payment Verification: Verifies Gumroad purchases using the Gumroad API.
Automated Channel Access: Sends private Telegram channel invite links to verified buyers.
User-Friendly Interface: Provides clear instructions and error handling for a smooth user experience.
Secure Configuration: Uses environment variables to store sensitive data like bot tokens and API keys.
Extensible: Easily adaptable for other courses (e.g., Mandarin, web development).

Prerequisites

Python 3.8+
Telegram Bot: Created via @BotFather with a bot token.
Gumroad Account: With a product set up and API key for payment verification.
Telegram Channel: A private channel (e.g., @EnglishAccentTraining) for course delivery.
Dependencies:pip install python-telegram-bot flask requests python-dotenv



Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/english-accent-training-bot.git
cd english-accent-training-bot

2. Configure Environment Variables
Create a .env file in the project root with the following:
TELEGRAM_TOKEN=your_bot_token_from_botfather
GUMROAD_ACCESS_TOKEN=your_gumroad_api_key
GUMROAD_PRODUCT_ID=your_gumroad_product_id
CHANNEL_INVITE_LINK=your_channel_invite_link
PORT=5000


TELEGRAM_TOKEN: Get from @BotFather.
GUMROAD_ACCESS_TOKEN: Find in Gumroad Settings > Advanced > API.
GUMROAD_PRODUCT_ID: Get from your Gumroad product URL or API.
CHANNEL_INVITE_LINK: Create in your Telegram channel settings (set to expire for security).

3. Install Dependencies
pip install -r requirements.txt

4. Add Bot to Telegram Channel

Open your private Telegram channel (e.g., @EnglishAccentTraining).
Go to Channel Settings > Administrators > Add Admin.
Add your bot (e.g., @AccentTrainingBot) with Invite Users via Link and Send Messages permissions.

5. Run Locally (Testing)

Start the bot:python bot.py


Use ngrok to expose your local server:ngrok http 5000


Set the Telegram webhook:curl https://api.telegram.org/bot$TELEGRAM_TOKEN/setWebhook?url=https://your-ngrok-url.ngrok.io/$TELEGRAM_TOKEN



6. Deploy to Production
Use a cloud platform like Render:

Create a new Web Service on Render and connect this GitHub repository.
Set environment variables in Render’s dashboard (from .env).
Set the start command: python bot.py.
Deploy and get the public URL (e.g., https://your-bot.onrender.com).
Update the Telegram webhook:curl https://api.telegram.org/bot$TELEGRAM_TOKEN/setWebhook?url=https://your-bot.onrender.com/$TELEGRAM_TOKEN



7. Configure Gumroad

In Gumroad, create a product for your course (e.g., “English Accent Training - $19.99”).
Enable Custom Fields to collect the buyer’s Telegram username (e.g., “Telegram ID: @username”).
In Post-Purchase Message, add:🎉 Thanks for purchasing English Accent Training! To access your course:
1. Ensure your Telegram username is set.
2. Click here: t.me/AccentTrainingBot
3. Send the receipt code (from your email) to the bot.



8. Test the Bot

Start the bot with /start.
Make a test purchase on Gumroad.
Send the receipt code to the bot.
Verify that the bot responds with the channel invite link.
Test edge cases (e.g., invalid receipt, no Telegram username).

File Structure

bot.py: Main bot script handling Telegram updates and Gumroad verification.
.env: Environment variables (not tracked in Git).
requirements.txt: Python dependencies.
README.md: This file.

Example Usage

User starts the bot: /start
Bot responds: “🎉 Welcome to English Accent Training! Please send your Gumroad receipt code.”
User sends receipt code.
Bot verifies via Gumroad API and sends the channel invite link: “✅ Payment verified! Join here: [link]”.

Extending for Other Courses
To adapt for Mandarin or web development courses:

Create new Telegram channels (e.g., @MandarinMastery, @WebDevBootcamp).
Update CHANNEL_INVITE_LINK and GUMROAD_PRODUCT_ID in .env.
Modify bot messages in bot.py to reflect the course (e.g., “Welcome to Mandarin Mastery!”).
Add course-specific commands (e.g., /lesson for lesson previews).

Future Improvements

Drip Content: Schedule lessons using Telegram’s scheduleMessage API.
Progress Tracking: Store user progress in a database (e.g., SQLite).
Voice Feedback: Add a /submit command for pronunciation practice uploads.
Multilingual Support: Add bot responses in Mandarin or other languages.

Troubleshooting

Bot not responding: Check webhook status with curl https://api.telegram.org/bot$TELEGRAM_TOKEN/getWebhookInfo.
Invalid receipt: Ensure Gumroad API key and product ID are correct.
Webhook errors: Verify your server URL is accessible and the port matches .env.

Contributing
Contributions are welcome! Please:

Fork the repository.
Create a feature branch (git checkout -b feature/new-feature).
Commit changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Open a pull request.

License
MIT License. See LICENSE for details.
Contact
For support, contact [Your Name] via [your.email@example.com] or Telegram: @YourUsername.
