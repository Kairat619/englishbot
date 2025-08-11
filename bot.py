import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, Filters, ContextTypes
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
app = Flask(__name__)
bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
GUMROAD_ACCESS_TOKEN = os.getenv("GUMROAD_ACCESS_TOKEN")
CHANNEL_INVITE_LINK = os.getenv("CHANNEL_INVITE_LINK")  # e.g., https://t.me/+abc123xyz

# Verify Gumroad purchase
def verify_purchase(receipt_code, telegram_username):
    url = "https://api.gumroad.com/v2/sales"
    headers = {"Authorization": f"Bearer {GUMROAD_ACCESS_TOKEN}"}
    params = {"product_id": os.getenv("GUMROAD_PRODUCT_ID")}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        sales = response.json().get("sales", [])
        for sale in sales:
            if sale.get("receipt") == receipt_code and telegram_username in sale.get("custom_fields", {}).get("Telegram ID", ""):
                return True
    return False

# Telegram bot handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Welcome to English Accent Training! Please send your Gumroad receipt code to access the course."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    text = update.message.text
    telegram_username = update.message.from_user.username or ""

    if not telegram_username:
        await update.message.reply_text("⚠️ Please set a Telegram username in your profile settings and try again.")
        return

    try:
        if verify_purchase(text, telegram_username):
            await update.message.reply_text("✅ Payment verified! Join your course here:")
            await update.message.reply_text(CHANNEL_INVITE_LINK)
        else:
            await update.message.reply_text("❌ Invalid receipt or Telegram username. Please check and try again.")
    except Exception as e:
        await update.message.reply_text("⚠️ An error occurred. Please contact support or try again later.")
        print(f"Error: {e}")

# Flask webhook endpoint
@app.route(f"/{os.getenv('TELEGRAM_TOKEN')}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    app.dispatcher.process_update(update)
    return "ok"

if __name__ == "__main__":
    # Set up Telegram bot application
    application = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
    app.dispatcher = application  # Store application for webhook processing
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(Filters.TEXT & ~Filters.COMMAND, handle_message))
    
    # Run Flask app with gunicorn-compatible settings
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)