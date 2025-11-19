"""
Generated Code Metadata:
========================
Original URL: https://clickhere.blog
Prompt: How can I use the Telegram Bot API to create a bot that shares updates with a group chat, and what libraries are recommended for this task in Node.js?
Generated: DETERMINISTIC_efb3958b57d26177
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const TelegramBot = require('node-telegram-bot-api');
const express = require('express');
require('dotenv').config();

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Load environment variables
const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const GROUP_CHAT_ID = process.env.GROUP_CHAT_ID;

// Validate required environment variables
if (!TELEGRAM_BOT_TOKEN || !GROUP_CHAT_ID) {
  console.error('Missing required environment variables');
  process.exit(1);
}

// Create bot instance
const bot = new TelegramBot(TELEGRAM_BOT_TOKEN, { polling: true });

// Middleware to parse JSON bodies
app.use(express.json());

// Health check endpoint
app.get('/', (req, res) => {
  res.status(200).json({ status: 'Bot is running' });
});

// Endpoint to receive updates and forward to Telegram group
app.post('/send-update', async (req, res) => {
  try {
    const { message } = req.body;

    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    // Send message to group chat
    await bot.sendMessage(GROUP_CHAT_ID, message);

    res.status(200).json({ success: true });
  } catch (error) {
    console.error('Error sending message:', error);
    res.status(500).json({ error: 'Failed to send message' });
  }
});

// Error handler for Telegram bot
bot.on('polling_error', (error) => {
  console.error('Polling error:', error);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Example of listening to messages in the group
bot.on('message', (msg) => {
  console.log('Received message:', msg.text);
});

// Example command handler
bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, 'Welcome to the group update bot!');
});
```
