
import os
import asyncio
import threading
from flask import Flask
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))

app = Flask(__name__)

@app.get("/")
def home():
    return "Code Solver Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Code Solver Bot! 🤖\n\n"
        "I support Java and Python practice.\n"
        "Send me a programming question or code to analyze."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text or ""

    await update.message.reply_text(
        "Received successfully! ✅\n\n"
        "Your question:\n" + question +
        "\n\nAI analysis will be connected next."
    )

async def run_bot():
    bot = ApplicationBuilder().token(TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    await bot.initialize()
    await bot.start()
    await bot.updater.start_polling()

    await asyncio.Event().wait()

def bot_thread():
    asyncio.run(run_bot())

if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing")

    threading.Thread(target=bot_thread, daemon=True).start()
    app.run(host="0.0.0.0", port=PORT)

