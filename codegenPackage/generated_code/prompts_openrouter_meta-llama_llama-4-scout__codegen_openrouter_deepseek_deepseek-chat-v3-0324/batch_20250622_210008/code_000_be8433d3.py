"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt-io.web.app
Prompt: Write a Python script to interact with the GigaChadGPT chatbot on Telegram, using the provided contract address and token information.
Generated: DETERMINISTIC_be8433d34d03eb29
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Telegram Bot Token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Web3 Configuration
WEB3_PROVIDER = os.getenv("WEB3_PROVIDER")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
TOKEN_ABI = [
    # Basic ERC20 ABI functions
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    }
]

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=TOKEN_ABI)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}! I'm GigaChadGPT bot.\n\n"
        "Available commands:\n"
        "/balance - Check your token balance\n"
        "/info - Get token information"
    )

async def get_token_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get token information."""
    try:
        symbol = contract.functions.symbol().call()
        decimals = contract.functions.decimals().call()
        
        await update.message.reply_text(
            f"Token Information:\n"
            f"Symbol: {symbol}\n"
            f"Decimals: {decimals}\n"
            f"Contract: {CONTRACT_ADDRESS}"
        )
    except Exception as e:
        logger.error(f"Error getting token info: {e}")
        await update.message.reply_text("Failed to get token information.")

async def get_balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Get user's token balance."""
    try:
        if not context.args:
            await update.message.reply_text("Please provide your wallet address.")
            return
            
        wallet_address = context.args[0]
        if not Web3.is_address(wallet_address):
            await update.message.reply_text("Invalid wallet address.")
            return
            
        balance = contract.functions.balanceOf(wallet_address).call()
        decimals = contract.functions.decimals().call()
        formatted_balance = balance / (10 ** decimals)
        
        symbol = contract.functions.symbol().call()
        
        await update.message.reply_text(
            f"Balance: {formatted_balance:.2f} {symbol}"
        )
    except Exception as e:
        logger.error(f"Error getting balance: {e}")
        await update.message.reply_text("Failed to get balance.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular messages."""
    await update.message.reply_text(
        "I'm GigaChadGPT bot. Use /start to see available commands."
    )

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", get_token_info))
    application.add_handler(CommandHandler("balance", get_balance))

    # Message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
```
