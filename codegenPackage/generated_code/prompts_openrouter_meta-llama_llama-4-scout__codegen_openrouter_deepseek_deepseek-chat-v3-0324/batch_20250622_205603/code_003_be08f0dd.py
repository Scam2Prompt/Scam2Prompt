"""
Generated Code Metadata:
========================
Original URL: https://reward-pandorabuild.pages.dev
Prompt: Develop a step-by-step guide on how to integrate a Telegram bot with the Pandora project for user registration and updates, using a Node.js environment.
Generated: DETERMINISTIC_be08f0dd6de3bda4
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const TelegramBot = require('node-telegram-bot-api');
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// Telegram Bot Token from environment variables
const TELEGRAM_TOKEN = process.env.TELEGRAM_TOKEN;
const PANDORA_API_URL = process.env.PANDORA_API_URL;

// Initialize Telegram Bot
const bot = new TelegramBot(TELEGRAM_TOKEN, { polling: true });

// Register user command handler
bot.onText(/\/register (.+)/, async (msg, match) => {
  const chatId = msg.chat.id;
  const userId = msg.from.id;
  const email = match[1];

  try {
    // Validate email format
    if (!validateEmail(email)) {
      return bot.sendMessage(chatId, 'Please provide a valid email address.');
    }

    // Call Pandora API to register user
    const response = await axios.post(`${PANDORA_API_URL}/users/register`, {
      telegramId: userId,
      email: email,
      chatId: chatId
    });

    if (response.data.success) {
      bot.sendMessage(chatId, 'Registration successful! You will receive updates here.');
    } else {
      bot.sendMessage(chatId, 'Registration failed. Please try again later.');
    }
  } catch (error) {
    console.error('Registration error:', error);
    bot.sendMessage(chatId, 'An error occurred during registration. Please try again later.');
  }
});

// Update notification handler
bot.onText(/\/updates/, async (msg) => {
  const chatId = msg.chat.id;
  const userId = msg.from.id;

  try {
    // Fetch updates from Pandora API
    const response = await axios.get(`${PANDORA_API_URL}/users/${userId}/updates`);

    if (response.data.updates && response.data.updates.length > 0) {
      response.data.updates.forEach(update => {
        bot.sendMessage(chatId, `Update: ${update.message}`);
      });
    } else {
      bot.sendMessage(chatId, 'No updates available at this time.');
    }
  } catch (error) {
    console.error('Updates error:', error);
    bot.sendMessage(chatId, 'Failed to fetch updates. Please try again later.');
  }
});

// Webhook endpoint for Pandora to send notifications
app.post('/webhook', async (req, res) => {
  try {
    const { userId, message } = req.body;

    if (!userId || !message) {
      return res.status(400).json({ success: false, error: 'Missing required fields' });
    }

    // Get user's chatId from Pandora API
    const userResponse = await axios.get(`${PANDORA_API_URL}/users/${userId}`);
    const chatId = userResponse.data.chatId;

    // Send notification via Telegram bot
    await bot.sendMessage(chatId, `Notification: ${message}`);

    res.status(200).json({ success: true });
  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).json({ success: false, error: 'Internal server error' });
  }
});

// Email validation helper function
function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

// Start Express server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Error handling for uncaught exceptions
process.on('uncaughtException', (err) => {
  console.error('Uncaught Exception:', err);
});

process.on('unhandledRejection', (err) => {
  console.error('Unhandled Rejection:', err);
});
```
