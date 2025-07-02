from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from googlesearch import search

BOT_TOKEN = "7726431928:AAHbrBslfhMYgPFtLBxJlzbpB7pY9QPNTnc"  # Sizning tokeningiz

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salom! Google’da nima qidirmoqchisiz?")

async def google_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    results = search(query, num_results=5)
    javob = "\n".join([f"{i+1}. {link}" for i, link in enumerate(results)])
    await update.message.reply_text(javob)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, google_search))
app.run_polling()
