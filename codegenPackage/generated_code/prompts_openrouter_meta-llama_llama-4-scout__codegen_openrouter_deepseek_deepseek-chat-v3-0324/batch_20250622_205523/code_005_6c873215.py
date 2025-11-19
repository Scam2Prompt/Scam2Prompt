"""
Generated Code Metadata:
========================
Original URL: https://infinivi.io
Prompt: Create a JavaScript code for a Telegram bot that provides updates on IVI Token sales, roadmaps, and partnerships with sports clubs.
Generated: DETERMINISTIC_6c873215fa3eb68a
Batch ID: 20250622_205523
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/ivi/token-sales": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/ivi/roadmap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/ivi/partnerships": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Telegram bot with API token from environment variables
const bot = new TelegramBot(process.env.TELEGRAM_BOT_TOKEN, { polling: true });

// Cache for storing frequently accessed data
const cache = {
    tokenSales: null,
    roadmap: null,
    partnerships: null,
    lastUpdated: null
};

// API endpoints (replace with actual endpoints)
const API_ENDPOINTS = {
    TOKEN_SALES: 'https://api.example.com/ivi/token-sales',
    ROADMAP: 'https://api.example.com/ivi/roadmap',
    PARTNERSHIPS: 'https://api.example.com/ivi/partnerships'
};

// Function to fetch data from API with error handling
async function fetchData(endpoint) {
    try {
        const response = await axios.get(endpoint);
        return response.data;
    } catch (error) {
        console.error(`Error fetching data from ${endpoint}:`, error.message);
        return null;
    }
}

// Function to update cache
async function updateCache() {
    try {
        const [tokenSales, roadmap, partnerships] = await Promise.all([
            fetchData(API_ENDPOINTS.TOKEN_SALES),
            fetchData(API_ENDPOINTS.ROADMAP),
            fetchData(API_ENDPOINTS.PARTNERSHIPS)
        ]);

        if (tokenSales && roadmap && partnerships) {
            cache.tokenSales = tokenSales;
            cache.roadmap = roadmap;
            cache.partnerships = partnerships;
            cache.lastUpdated = new Date();
            console.log('Cache updated successfully');
        }
    } catch (error) {
        console.error('Error updating cache:', error.message);
    }
}

// Update cache every 30 minutes
setInterval(updateCache, 30 * 60 * 1000);
updateCache(); // Initial cache update

// Command handlers
bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    const welcomeMessage = `
Welcome to the IVI Token Bot! 🚀

Here's what I can do:
- /token_sales - Get latest IVI Token sales updates
- /roadmap - View the IVI project roadmap
- /partnerships - See current sports club partnerships
- /help - Show this help message

Use the commands above to get started!
    `;
    bot.sendMessage(chatId, welcomeMessage);
});

bot.onText(/\/help/, (msg) => {
    const chatId = msg.chat.id;
    const helpMessage = `
Available commands:
- /token_sales - Get latest IVI Token sales updates
- /roadmap - View the IVI project roadmap
- /partnerships - See current sports club partnerships
- /help - Show this help message
    `;
    bot.sendMessage(chatId, helpMessage);
});

bot.onText(/\/token_sales/, async (msg) => {
    const chatId = msg.chat.id;
    
    if (!cache.tokenSales) {
        await updateCache();
    }

    if (cache.tokenSales) {
        const message = `
🔹 IVI Token Sales Update 🔹

Current Price: ${cache.tokenSales.currentPrice || 'N/A'}
Total Sold: ${cache.tokenSales.totalSold || 'N/A'}
Remaining: ${cache.tokenSales.remaining || 'N/A'}
Last Updated: ${cache.lastUpdated.toLocaleString()}

${cache.tokenSales.additionalInfo || ''}
        `;
        bot.sendMessage(chatId, message);
    } else {
        bot.sendMessage(chatId, '⚠️ Unable to fetch token sales data at the moment. Please try again later.');
    }
});

bot.onText(/\/roadmap/, async (msg) => {
    const chatId = msg.chat.id;
    
    if (!cache.roadmap) {
        await updateCache();
    }

    if (cache.roadmap) {
        let message = '🚀 IVI Project Roadmap 🚀\n\n';
        cache.roadmap.forEach((item, index) => {
            message += `🔸 ${item.quarter}: ${item.description}\n`;
            if (item.completed) message += '✅ Completed\n\n';
            else message += '🟡 In Progress\n\n';
        });
        message += `Last Updated: ${cache.lastUpdated.toLocaleString()}`;
        bot.sendMessage(chatId, message);
    } else {
        bot.sendMessage(chatId, '⚠️ Unable to fetch roadmap data at the moment. Please try again later.');
    }
});

bot.onText(/\/partnerships/, async (msg) => {
    const chatId = msg.chat.id;
    
    if (!cache.partnerships) {
        await updateCache();
    }

    if (cache.partnerships) {
        let message = '⚽ IVI Sports Club Partnerships ⚽\n\n';
        cache.partnerships.forEach((club) => {
            message += `🏆 ${club.name}\n`;
            message += `📍 ${club.country}\n`;
            message += `🔗 ${club.website || 'No website available'}\n\n`;
        });
        message += `Last Updated: ${cache.lastUpdated.toLocaleString()}`;
        bot.sendMessage(chatId, message);
    } else {
        bot.sendMessage(chatId, '⚠️ Unable to fetch partnerships data at the moment. Please try again later.');
    }
});

// Error handling
bot.on('polling_error', (error) => {
    console.error('Polling error:', error);
});

// Log when bot is ready
console.log('IVI Token Bot is running...');
```
