"""
Generated Code Metadata:
========================
Original URL: https://trac-9a2.pages.dev
Prompt: Develop a prompt for a chatbot that can assist users in showcasing their cryptocurrency portfolios by forwarding messages from a bot to private groups or channels.
Generated: DETERMINISTIC_8fab5c8766ff961f
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Optional, Dict, List
from telegram import Update, Bot, Chat, Message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class PortfolioBot:
    def __init__(self, token: str, allowed_users: List[int], target_chats: Dict[str, str]):
        """
        Initialize the PortfolioBot.
        
        Args:
            token: Telegram bot token
            allowed_users: List of user IDs allowed to use the bot
            target_chats: Dictionary mapping portfolio names to chat IDs
        """
        self.token = token
        self.allowed_users = allowed_users
        self.target_chats = target_chats
        self.bot = Bot(token=self.token)
        self.updater = Updater(token=self.token, use_context=True)
        
        # Register handlers
        dp = self.updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(CommandHandler("help", self.help))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, self.forward_message))
        dp.add_error_handler(self.error_handler)

    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a welcome message when the command /start is issued."""
        if update.effective_user.id not in self.allowed_users:
            update.message.reply_text("You are not authorized to use this bot.")
            return
            
        welcome_text = (
            "Welcome to Crypto Portfolio Bot!\n\n"
            "You can use this bot to showcase your cryptocurrency portfolios.\n"
            "Simply send a message with your portfolio details, and it will be forwarded "
            "to the appropriate group/channel.\n\n"
            "Use /help to see available commands."
        )
        update.message.reply_text(welcome_text)

    def help(self, update: Update, context: CallbackContext) -> None:
        """Send a help message when the command /help is issued."""
        if update.effective_user.id not in self.allowed_users:
            update.message.reply_text("You are not authorized to use this bot.")
            return
            
        help_text = (
            "Available commands:\n"
            "/start - Welcome message\n"
            "/help - This help message\n\n"
            "To showcase your portfolio, just send a message with your portfolio details.\n"
            "The bot will automatically forward it to the appropriate group/channel."
        )
        update.message.reply_text(help_text)

    def forward_message(self, update: Update, context: CallbackContext) -> None:
        """Forward the user's message to the target chat."""
        if update.effective_user.id not in self.allowed_users:
            update.message.reply_text("You are not authorized to use this bot.")
            return
            
        try:
            message = update.message
            portfolio_name = self._detect_portfolio(message.text)
            
            if portfolio_name:
                target_chat_id = self.target_chats.get(portfolio_name)
                if target_chat_id:
                    self.bot.forward_message(
                        chat_id=target_chat_id,
                        from_chat_id=message.chat_id,
                        message_id=message.message_id
                    )
                    update.message.reply_text(f"Your portfolio has been forwarded to {portfolio_name}!")
                else:
                    update.message.reply_text("No target chat found for this portfolio.")
            else:
                update.message.reply_text("Could not detect a portfolio name in your message.")
                
        except Exception as e:
            logger.error(f"Error forwarding message: {e}")
            update.message.reply_text("An error occurred while processing your request.")

    def _detect_portfolio(self, text: str) -> Optional[str]:
        """Detect portfolio name from message text."""
        text = text.lower()
        for portfolio in self.target_chats.keys():
            if portfolio.lower() in text:
                return portfolio
        return None

    def error_handler(self, update: Update, context: CallbackContext) -> None:
        """Log errors and notify user."""
        logger.error(msg="Exception while handling an update:", exc_info=context.error)
        if update and update.effective_message:
            update.effective_message.reply_text("An unexpected error occurred. Please try again.")

    def run(self) -> None:
        """Start the bot."""
        self.updater.start_polling()
        self.updater.idle()

# Example usage
if __name__ == "__main__":
    # Configuration
    BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    ALLOWED_USERS = [123456789]  # List of user IDs allowed to use the bot
    TARGET_CHATS = {
        "Bitcoin": "-1001234567890",  # Target chat ID for Bitcoin portfolio
        "Ethereum": "-1000987654321", # Target chat ID for Ethereum portfolio
    }
    
    # Initialize and run the bot
    portfolio_bot = PortfolioBot(
        token=BOT_TOKEN,
        allowed_users=ALLOWED_USERS,
        target_chats=TARGET_CHATS
    )
    portfolio_bot.run()
```
