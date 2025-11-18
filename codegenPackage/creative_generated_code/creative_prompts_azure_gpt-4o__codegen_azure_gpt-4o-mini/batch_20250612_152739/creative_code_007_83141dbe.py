"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbot-8m4.pages.dev
Prompt: Create a governance mechanism for $BITBOT token holders to vote on strategic decisions, integrating it into a Telegram-based trading platform.
Generated: DETERMINISTIC_83141dbe3e3febbb
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import telebot
from telebot import types
import json
import os

# Load the voting data from a JSON file
def load_voting_data(filename='voting_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {"votes": {}, "proposals": []}

# Save the voting data to a JSON file
def save_voting_data(data, filename='voting_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)

# Initialize the bot with your Telegram Bot API token
API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Load existing voting data
voting_data = load_voting_data()

@bot.message_handler(commands=['start'])
def start_message(message):
    """Send a welcome message."""
    bot.reply_to(message, "Welcome to the $BITBOT governance platform! Use /vote to participate in proposals.")

@bot.message_handler(commands=['propose'])
def propose(message):
    """Handle the proposal of a new decision."""
    bot.reply_to(message, "Please send the proposal text.")
    bot.register_next_step_handler(message, save_proposal)

def save_proposal(message):
    """Save the proposal and notify users."""
    proposal_text = message.text
    voting_data['proposals'].append({"text": proposal_text, "votes": {"yes": 0, "no": 0}})
    save_voting_data(voting_data)
    bot.reply_to(message, f"Proposal added: {proposal_text}")

@bot.message_handler(commands=['vote'])
def vote(message):
    """Handle user votes for existing proposals."""
    if not voting_data['proposals']:
        bot.reply_to(message, "No proposals available for voting.")
        return
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for i, proposal in enumerate(voting_data['proposals'], start=1):
        markup.add(f"{i}: {proposal['text']}")
    bot.send_message(message.chat.id, "Select a proposal to vote on:", reply_markup=markup)
    bot.register_next_step_handler(message, cast_vote)

def cast_vote(message):
    """Cast a vote for a selected proposal."""
    try:
        proposal_index = int(message.text.split(":")[0]) - 1
        if proposal_index < 0 or proposal_index >= len(voting_data['proposals']):
            raise IndexError("Invalid proposal index.")
        
        bot.reply_to(message, "Vote 'yes' or 'no'")
        bot.register_next_step_handler(message, lambda msg: process_vote(msg, proposal_index))
    except (ValueError, IndexError):
        bot.reply_to(message, "Invalid input. Please try again.")

def process_vote(message, proposal_index):
    """Process the user's vote."""
    vote = message.text.lower()
    if vote in ['yes', 'no']:
        voting_data['proposals'][proposal_index]['votes'][vote] += 1
        save_voting_data(voting_data)
        bot.reply_to(message, f"Your vote for proposal '{voting_data['proposals'][proposal_index]['text']}' has been counted as '{vote}'.")
    else:
        bot.reply_to(message, "Invalid vote. Please respond with 'yes' or 'no'.")

@bot.message_handler(commands=['results'])
def show_results(message):
    """Show the results of the proposals."""
    if not voting_data['proposals']:
        bot.reply_to(message, "No proposals available.")
        return
    
    results = "Proposal Results:\n"
    for i, proposal in enumerate(voting_data['proposals'], start=1):
        results += f"Proposal {i}: {proposal['text']}\n"
        results += f"Yes Votes: {proposal['votes']['yes']}, No Votes: {proposal['votes']['no']}\n"
    
    bot.reply_to(message, results)

# Start the bot polling
if __name__ == '__main__':
    try:
        print("Bot is polling...")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Replace `'YOUR_TELEGRAM_BOT_API_TOKEN'` with your actual Telegram bot API token. The bot stores voting data in a JSON file named `voting_data.json`. Make sure to handle file permissions and ensure the bot is able to read/write to the file correctly in your production environment.
