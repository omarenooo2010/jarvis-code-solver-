
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً! أنا JARVIS Code Solver 🤖\n\n"
        "أقدر أساعدك في:\n"
        "1- Java\n"
        "2- Python\n"
        "3- تحليل الأكواد\n"
        "4- اكتشاف الأخطاء\n\n"
        "ابعت سؤال التدريب أو الكود اللي محتاج تحليله."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text

    await update.message.reply_text(
        "استلمت سؤالك بنجاح ✅\n\n"
        "السؤال:\n"
        + question
        + "\n\nجارفيس جاهز لتحليله. سيتم ربط محرك الذكاء الاصطناعي في الخطوة التالية."
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("JARVIS is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
