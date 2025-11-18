"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jackthegoat-bonus.web.app
Prompt: Build a Telegram bot that notifies users of updates related to $JACK, including price changes, new photos, and community announcements. Integrate Solana's web3.js library for blockchain data.
Generated: DETERMINISTIC_314be09a22131a5e
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { Telegraf } = require('telegraf');
const Web3 = require('@solana/web3.js');

// Telegram bot token (replace with your own)
const TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN';

// Create a new Telegram bot instance
const bot = new Telegraf(TELEGRAM_BOT_TOKEN);

// Solana connection setup
const connection = new Web3.Connection(Web3.clusterApiUrl('mainnet-beta'), 'confirmed');

// Track the previous price for comparison
let previousPrice = null;

// Function to get the current price of $JACK (dummy implementation)
async function getCurrentPrice() {
    // TODO: Replace with actual API call or logic to fetch current price of $JACK
    return Math.random() * 100; // Simulating price data
}

// Function to get announcements (dummy implementation)
async function getAnnouncements() {
    // TODO: Replace with actual logic to fetch community announcements
    return ['New feature released!', 'Join our community call this Saturday!'];
}

// Function to check for updates and notify users
async function checkUpdates(ctx) {
    try {
        const currentPrice = await getCurrentPrice();
        if (previousPrice !== currentPrice) {
            await ctx.reply(`Price Update: $JACK is now $${currentPrice.toFixed(2)}`);
            previousPrice = currentPrice;
        }

        const announcements = await getAnnouncements();
        if (announcements.length > 0) {
            for (const announcement of announcements) {
                await ctx.reply(`Announcement: ${announcement}`);
            }
        }
    } catch (error) {
        console.error('Error checking updates:', error);
        await ctx.reply('An error occurred while fetching updates. Please try again later.');
    }
}

// Command to start updates
bot.command('start', (ctx) => {
    ctx.reply('Welcome! You will receive updates about $JACK.');
    setInterval(() => checkUpdates(ctx), 60000); // Check for updates every minute
});

// Start the bot
bot.launch().then(() => {
    console.log('Telegram bot is running...');
}).catch(error => {
    console.error('Failed to start the bot:', error);
});
```
