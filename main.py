from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# ===================== CONFIG =====================
API_ID = 24340073
API_HASH = "eae7861e71a66363aaec3db717f41d3a"
BOT_TOKEN = "8271406239:AAF1VnJsBVGBWHfhBMNFMgrbonYX1Z7B7TE"
ADMIN_ID = 6535364725
# ===================================================

# Flask App for Web Hosting
app = Flask(__name__)

@app.route('/')
def home():
    return "SkillPro Bot is Running!"

# Telegram Bot Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! This is SkillPro Bot. Use /help to see commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Start the bot\n/help - Show this help\n/admin - Check admin access")

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text("✅ You are an admin!")
    else:
        await update.message.reply_text("❌ You are not an admin.")

# Run both Flask and Telegram Bot
if __name__ == '__main__':
    # Start Telegram Bot
    import threading

    def run_bot():
        app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
        app_bot.add_handler(CommandHandler("start", start))
        app_bot.add_handler(CommandHandler("help", help_command))
        app_bot.add_handler(CommandHandler("admin", admin_command))
        app_bot.run_polling()

    threading.Thread(target=run_bot).start()

    # Start Flask Web Server
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
