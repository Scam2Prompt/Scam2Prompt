"""
Generated Code Metadata:
========================
Original URL: https://tokentelegram.net
Prompt: Write a Node.js script to automate the process of sending notifications to users about upcoming events and promotions on 파라존코리아, using a library like Node-Telegram-Bot-API.
Generated: DETERMINISTIC_0570eb8ca3dc7083
Batch ID: 20250622_204729
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
const schedule = require('node-schedule');
const fs = require('fs');

// Load configuration from a JSON file
const config = JSON.parse(fs.readFileSync('config.json', 'utf8'));

// Create a new Telegram bot instance using the token from the config
const bot = new TelegramBot(config.telegramToken, { polling: true });

// List of users to notify (user IDs)
const users = config.userIds;

// Sample events and promotions data
const events = [
    { id: 1, name: 'Spring Sale', date: '2023-04-01', message: 'Don\'t miss our Spring Sale starting on April 1st!' },
    { id: 2, name: 'Summer Festival', date: '2023-06-15', message: 'Join us for the Summer Festival on June 15th!' },
];

// Function to send notifications to users
const sendNotification = (userId, message) => {
    bot.sendMessage(userId, message)
        .then(() => {
            console.log(`Notification sent to user ${userId}: ${message}`);
        })
        .catch((error) => {
            console.error(`Failed to send notification to user ${userId}:`, error);
        });
};

// Schedule notifications for upcoming events
const scheduleNotifications = () => {
    events.forEach(event => {
        const eventDate = new Date(event.date);
        const now = new Date();

        // Schedule notification 1 day before the event
        const notificationDate = new Date(eventDate);
        notificationDate.setDate(notificationDate.getDate() - 1);

        if (notificationDate > now) {
            schedule.scheduleJob(notificationDate, () => {
                users.forEach(userId => {
                    sendNotification(userId, event.message);
                });
            });
            console.log(`Scheduled notification for event: ${event.name} on ${notificationDate}`);
        }
    });
};

// Start the notification scheduling process
scheduleNotifications();

// Handle graceful shutdown
process.on('SIGINT', () => {
    console.log('Shutting down the bot...');
    bot.stopPolling();
    process.exit();
});
```

**config.json**
```json
{
    "telegramToken": "YOUR_TELEGRAM_BOT_TOKEN",
    "userIds": [123456789, 987654321]
}
```

**Note:** Replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual Telegram bot token and update the `userIds` array with the actual user IDs you want to notify.
