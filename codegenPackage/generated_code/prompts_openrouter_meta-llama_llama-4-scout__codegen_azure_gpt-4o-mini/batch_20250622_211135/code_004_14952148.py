"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Create a Discord bot using Node.js that collects and shares user stories about negative experiences with OpenSea, similar to the "Holder's Rewards" section on the Fuck OpenSea website.
Generated: DETERMINISTIC_14952148376823a5
Batch ID: 20250622_211135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Client, Intents } = require('discord.js');
const fs = require('fs');
const path = require('path');

// Load environment variables from .env file
require('dotenv').config();

// Create a new Discord client instance
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

// Define the path for storing user stories
const storiesFilePath = path.join(__dirname, 'stories.json');

// Function to load stories from the JSON file
const loadStories = () => {
    if (fs.existsSync(storiesFilePath)) {
        const data = fs.readFileSync(storiesFilePath);
        return JSON.parse(data);
    }
    return [];
};

// Function to save stories to the JSON file
const saveStories = (stories) => {
    fs.writeFileSync(storiesFilePath, JSON.stringify(stories, null, 2));
};

// Event listener for when the bot is ready
client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

// Event listener for messages
client.on('messageCreate', (message) => {
    // Ignore messages from the bot itself
    if (message.author.bot) return;

    // Command to collect user stories
    if (message.content.startsWith('!story')) {
        const userStory = message.content.slice(7).trim(); // Extract the story from the message

        // Validate the user story
        if (!userStory) {
            return message.reply('Please provide a story after the command. Usage: !story <your story>');
        }

        // Load existing stories
        const stories = loadStories();

        // Add the new story to the list
        stories.push({ user: message.author.username, story: userStory });

        // Save the updated stories
        saveStories(stories);

        // Acknowledge the user
        message.reply('Thank you for sharing your story!');
    }

    // Command to share all user stories
    if (message.content === '!stories') {
        const stories = loadStories();

        // Check if there are any stories to share
        if (stories.length === 0) {
            return message.reply('No stories have been shared yet.');
        }

        // Format stories for display
        const storyMessages = stories.map((s, index) => `${index + 1}. **${s.user}**: ${s.story}`).join('\n');
        message.channel.send(`Here are the shared stories:\n${storyMessages}`);
    }
});

// Error handling for uncaught exceptions
process.on('uncaughtException', (error) => {
    console.error('Uncaught Exception:', error);
});

// Log in to Discord with your app's token
client.login(process.env.DISCORD_TOKEN).catch((error) => {
    console.error('Failed to login:', error);
});
```

### Instructions:
1. Create a `.env` file in the same directory as your script and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_token_here
   ```
2. Ensure you have the required packages installed:
   ```bash
   npm install discord.js dotenv
   ```
3. Run the bot using Node.js:
   ```bash
   node your_script_name.js
   ```
