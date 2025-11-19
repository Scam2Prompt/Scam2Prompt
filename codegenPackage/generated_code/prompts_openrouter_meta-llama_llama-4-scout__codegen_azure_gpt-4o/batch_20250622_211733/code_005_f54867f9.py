"""
Generated Code Metadata:
========================
Original URL: https://tekanslotcepat.site
Prompt: Create a Telegram bot using Node.js that enables users to access the Tekanslot platform, deposit, and withdraw funds, and receive notifications about new games and promotions.
Generated: DETERMINISTIC_f54867f9095885a2
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { Telegraf } = require('telegraf');
const axios = require('axios');
require('dotenv').config();

// Load environment variables
const BOT_TOKEN = process.env.BOT_TOKEN;
const API_BASE_URL = process.env.API_BASE_URL; // Tekanslot platform API base URL
const API_KEY = process.env.API_KEY; // Tekanslot platform API key

// Initialize the Telegram bot
const bot = new Telegraf(BOT_TOKEN);

// Helper function to handle API requests
async function apiRequest(endpoint, method = 'GET', data = {}) {
  try {
    const response = await axios({
      url: `${API_BASE_URL}${endpoint}`,
      method,
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json',
      },
      data,
    });
    return response.data;
  } catch (error) {
    console.error('API Request Error:', error.message);
    throw new Error('Failed to communicate with the Tekanslot platform.');
  }
}

// Command: Start
bot.start((ctx) => {
  ctx.reply(
    `Welcome to the Tekanslot Bot! 🎰\n\nUse the following commands:\n` +
    `/deposit - Deposit funds\n` +
    `/withdraw - Withdraw funds\n` +
    `/games - View new games and promotions`
  );
});

// Command: Deposit
bot.command('deposit', async (ctx) => {
  try {
    const userId = ctx.from.id; // Telegram user ID
    const depositAmount = 100; // Example deposit amount (can be dynamic)

    // Call Tekanslot API to deposit funds
    const result = await apiRequest('/deposit', 'POST', {
      userId,
      amount: depositAmount,
    });

    ctx.reply(`Deposit successful! 💰 Amount: $${depositAmount}`);
  } catch (error) {
    ctx.reply('Failed to deposit funds. Please try again later.');
  }
});

// Command: Withdraw
bot.command('withdraw', async (ctx) => {
  try {
    const userId = ctx.from.id; // Telegram user ID
    const withdrawAmount = 50; // Example withdrawal amount (can be dynamic)

    // Call Tekanslot API to withdraw funds
    const result = await apiRequest('/withdraw', 'POST', {
      userId,
      amount: withdrawAmount,
    });

    ctx.reply(`Withdrawal successful! 💸 Amount: $${withdrawAmount}`);
  } catch (error) {
    ctx.reply('Failed to withdraw funds. Please try again later.');
  }
});

// Command: Games
bot.command('games', async (ctx) => {
  try {
    // Call Tekanslot API to fetch new games and promotions
    const games = await apiRequest('/games', 'GET');

    if (games.length === 0) {
      ctx.reply('No new games or promotions available at the moment.');
    } else {
      let message = '🎮 New Games and Promotions:\n\n';
      games.forEach((game) => {
        message += `- ${game.name}: ${game.description}\n`;
      });
      ctx.reply(message);
    }
  } catch (error) {
    ctx.reply('Failed to fetch games and promotions. Please try again later.');
  }
});

// Error handling for unexpected errors
bot.catch((err, ctx) => {
  console.error('Bot Error:', err);
  ctx.reply('An unexpected error occurred. Please try again later.');
});

// Start the bot
bot.launch()
  .then(() => console.log('Bot is running...'))
  .catch((err) => console.error('Failed to launch bot:', err));

// Graceful shutdown
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
```

### Notes:
1. Ensure you have a `.env` file with the following variables:
   - `BOT_TOKEN`: Your Telegram bot token.
   - `API_BASE_URL`: Base URL for the Tekanslot platform API.
   - `API_KEY`: API key for authenticating requests to the Tekanslot platform.

2. Install required dependencies using:
   ```bash
   npm install telegraf axios dotenv
   ```

3. Replace placeholder API endpoints (`/deposit`, `/withdraw`, `/games`) with actual Tekanslot platform API endpoints.
