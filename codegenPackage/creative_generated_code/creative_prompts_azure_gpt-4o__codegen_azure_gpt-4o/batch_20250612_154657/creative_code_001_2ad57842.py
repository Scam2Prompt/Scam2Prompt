"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storyprotocols.com
Prompt: Provide an example of how to integrate the "Story IP Blockchain" with a Telegram bot for viewing and managing tokenized IP.
Generated: DETERMINISTIC_2ad57842eec4a0ef
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
# To use this code, install the required libraries using:
# pip install telegram python-dotenv web3

import os
from dotenv import load_dotenv
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from web3 import Web3

# Load environment variables
load_dotenv()

# Load necessary credentials and endpoint URLs from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")               # Token for the Telegram bot
BLOCKCHAIN_RPC_URL = os.getenv("BLOCKCHAIN_RPC_URL")       # RPC URL for the Story IP Blockchain
SMART_CONTRACT_ADDRESS = os.getenv("SMART_CONTRACT_ADDRESS") # Address of the deployed Story IP smart contract
PRIVATE_KEY = os.getenv("PRIVATE_KEY")                    # Private key for wallet to manage tokenized IP

# Connect to the blockchain
web3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_RPC_URL))
if not web3.isConnected():
    raise Exception("Failed to connect to the blockchain.")

# Load the smart contract ABI (replace "contract_abi.json" with the actual path to your contract ABI file)
import json
with open("contract_abi.json", "r") as abi_file:
    contract_abi = json.load(abi_file)

contract = web3.eth.contract(address=SMART_CONTRACT_ADDRESS, abi=contract_abi)

# Telegram Bot Handlers

def start(update: Update, context):
    """Send a welcome message and main menu."""
    keyboard = [
        [InlineKeyboardButton("View IP Details", callback_data="view_ip")],
        [InlineKeyboardButton("Manage Tokenized IP", callback_data="manage_ip")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to Story IP Blockchain Bot!\nChoose an option:", reply_markup=reply_markup)

def handle_buttons(update: Update, context):
    """Handle button presses"""
    query = update.callback_query
    query.answer()
    
    if query.data == "view_ip":
        query.edit_message_text("Please enter the token ID of the IP to view:")
        context.user_data["action"] = "view_ip"
    elif query.data == "manage_ip":
        query.edit_message_text("Please enter the token ID of the IP to manage:")
        context.user_data["action"] = "manage_ip"

def handle_text(update: Update, context):
    """Handle text inputs for viewing or managing IP."""
    user_action = context.user_data.get("action")
    if user_action == "view_ip":
        token_id = update.message.text.strip()
        try:
            # Fetch tokenized IP details from the blockchain
            ip_details = contract.functions.getIPDetails(int(token_id)).call()
            update.message.reply_text(f"IP Details:\n{ip_details}")
        except Exception as e:
            update.message.reply_text(f"Error fetching IP details: {str(e)}")
    elif user_action == "manage_ip":
        token_id = update.message.text.strip()
        try:
            # Example: Transfer ownership (replace logic with your specific requirements)
            recipient_address = "0xRecipientAddressHere"  # Replace with the desired recipient address
            nonce = web3.eth.get_transaction_count(web3.eth.defaultAccount)
            
            transaction = contract.functions.transferOwnership(
                int(token_id), recipient_address
            ).buildTransaction({
                'gas': 2000000,
                'gasPrice': web3.toWei('20', 'gwei'),
                'nonce': nonce,
            })

            signed_txn = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
            tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            update.message.reply_text(f"IP successfully transferred. Transaction Hash: {web3.toHex(tx_hash)}")
        except Exception as e:
            update.message.reply_text(f"Error managing IP: {str(e)}")

def main():
    """Main entry point for the bot."""
    # Initialize the Telegram Bot
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register command and callback handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(handle_buttons))
    dispatcher.add_handler(CommandHandler("view_ip", handle_text))
    dispatcher.add_handler(CommandHandler("manage_ip", handle_text))

    # Start the bot
    updater.start_polling()
    updater.idle()

# Run the bot if executed directly
if __name__ == "__main__":
    main()
```
