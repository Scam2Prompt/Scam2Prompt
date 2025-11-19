"""
Generated Code Metadata:
========================
Original URL: https://marian-314.pages.dev
Prompt: Design a Discord bot with a custom message using Node.js.
Generated: DETERMINISTIC_54b4ab4e77c773ba
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the required libraries
const { Client, GatewayIntentBits } = require('discord.js');
require('dotenv').config(); // Load environment variables from .env file

// Create a new client instance
const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
    ],
});

// Event listener for when the bot is ready
client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

// Event listener for message creation
client.on('messageCreate', (message) => {
    // Ignore messages from the bot itself
    if (message.author.bot) return;

    // Check for a specific command
    if (message.content === '!hello') {
        // Send a custom message back to the channel
        message.channel.send('Hello! I am your friendly Discord bot!');
    }
});

// Error handling for the client
client.on('error', (error) => {
    console.error('An error occurred:', error);
});

// Log in to Discord with your app's token
client.login(process.env.DISCORD_TOKEN).catch((error) => {
    console.error('Failed to login:', error);
});
```

### .env file example
```
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
```

### Instructions
1. Create a new directory for your bot and navigate into it.
2. Run `npm init -y` to create a `package.json` file.
3. Install the required packages with `npm install discord.js dotenv`.
4. Create a `.env` file in the root of your project and add your Discord bot token.
5. Save the provided code in a file named `bot.js`.
6. Run the bot using `node bot.js`.
