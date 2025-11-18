"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Develop a chatbot in Python using the Telegram API that helps users inquire about Grupo ProBolsa's eco-friendly promotional products and sustainability practices.
Generated: DETERMINISTIC_f38b2e243b001b58
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define bot token (replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token)
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Define start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command. Provides a greeting and basic instructions.
    """
    user = update.effective_user
    await update.message.reply_html(
        rf"Hello {user.mention_html()}! 👋\n"
        "I'm your friendly Grupo ProBolsa chatbot. 🌱\n"
        "You can ask me about:\n"
        "- Our eco-friendly promotional products 📦\n"
        "- Our sustainability practices 🌍\n"
        "Type your question below to get started!",
        reply_markup=ForceReply(selective=True)
    )

# Define help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /help command. Provides information on how to use the bot.
    """
    await update.message.reply_text(
        "Here's how you can interact with me:\n"
        "- Use /start to begin.\n"
        "- Ask me questions about Grupo ProBolsa's eco-friendly products or sustainability practices.\n"
        "- Type /help if you need assistance."
    )

# Define message handler for general queries
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles generic user messages and provides responses based on keywords.
    """
    user_message = update.message.text.lower()

    if "products" in user_message or "eco-friendly" in user_message or "promotional" in user_message:
        response = (
            "Grupo ProBolsa offers a wide range of eco-friendly promotional products, "
            "including biodegradable bags, reusable packaging, and more. 🌱\n"
            "Feel free to ask for more details about specific products!"
        )
    elif "sustainability" in user_message or "practices" in user_message:
        response = (
            "Our sustainability practices are centered around reducing waste, using eco-friendly materials, "
            "and promoting a green lifestyle. 🌍\n"
            "Let me know if you'd like more in-depth information!"
        )
    else:
        response = (
            "I'm here to help with questions related to Grupo ProBolsa's eco-friendly products and sustainability practices. "
            "Could you rephrase your query? 😊"
        )

    await update.message.reply_text(response)

# Define error handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Logs errors and informs the user of any issues.
    """
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    await update.message.reply_text(
        "Oops! Something went wrong. Please try again later. 🙁"
    )

# Main function to initialize and run the bot
def main() -> None:
    """
    Starts the Telegram bot and sets up command and message handlers.
    """
    # Create the application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)

    # Run the bot
    application.run_polling()

# Entry point for the script
if __name__ == "__main__":
    main()
```
