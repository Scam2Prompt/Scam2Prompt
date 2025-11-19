"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telegram.sb
Prompt: Develop a Node.js application that listens for updates from Google News and forwards them to a Telegram group chat using the Telegram API.
Generated: DETERMINISTIC_f898123872b62b58
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const axios = require('axios');
const { Telegraf } = require('telegraf');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Telegram Bot Token and Chat ID
const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID;

// Create a new Telegram bot instance
const bot = new Telegraf(TELEGRAM_BOT_TOKEN);

// Middleware to parse JSON requests
app.use(express.json());

// Endpoint to receive updates from Google News
app.post('/news-update', async (req, res) => {
    // Validate incoming request
    if (!req.body || !req.body.title || !req.body.link) {
        return res.status(400).send('Invalid request');
    }

    const { title, link } = req.body;

    try {
        // Forward the news update to the Telegram group chat
        await bot.telegram.sendMessage(TELEGRAM_CHAT_ID, `${title}\n${link}`);

        // Send success response
        res.status(200).send('Update forwarded to Telegram');
    } catch (error) {
        console.error('Error sending message to Telegram:', error);
        // Handle error in sending message
        res.status(500).send('Error forwarding update to Telegram');
    }
});

// Start the Express server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Graceful shutdown on SIGINT
process.on('SIGINT', () => {
    console.log('Shutting down gracefully...');
    process.exit(0);
});
```

### Environment Variables
Ensure to define the following environment variables in your `.env` file (or set them in your environment):
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `TELEGRAM_CHAT_ID`: The chat ID of the Telegram group you want to send messages to. 

### Note
You should also implement a method to receive updates from Google News, which typically involves setting up a web hook or polling mechanism to retrieve the latest news articles. This example assumes that Google News sends updates to your specified endpoint (`/news-update`).
