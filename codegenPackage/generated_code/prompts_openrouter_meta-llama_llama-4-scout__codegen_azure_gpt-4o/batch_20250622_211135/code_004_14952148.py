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
// Import required modules
const { Client, GatewayIntentBits } = require('discord.js');
const fs = require('fs');
require('dotenv').config(); // Load environment variables from a .env file

// Create a new Discord client instance
const client = new Client({
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});

// File to store user stories
const STORIES_FILE = 'user_stories.json';

// Ensure the stories file exists
if (!fs.existsSync(STORIES_FILE)) {
  fs.writeFileSync(STORIES_FILE, JSON.stringify([]));
}

// Helper function to load stories from the file
function loadStories() {
  try {
    const data = fs.readFileSync(STORIES_FILE, 'utf8');
    return JSON.parse(data);
  } catch (error) {
    console.error('Error reading stories file:', error);
    return [];
  }
}

// Helper function to save stories to the file
function saveStories(stories) {
  try {
    fs.writeFileSync(STORIES_FILE, JSON.stringify(stories, null, 2));
  } catch (error) {
    console.error('Error writing to stories file:', error);
  }
}

// Event: Bot is ready
client.once('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

// Event: Message received
client.on('messageCreate', async (message) => {
  // Ignore messages from bots
  if (message.author.bot) return;

  // Command: Submit a story
  if (message.content.startsWith('!submit')) {
    const story = message.content.slice(8).trim(); // Extract the story text
    if (!story) {
      return message.reply('Please provide a story after the `!submit` command.');
    }

    // Load existing stories, add the new one, and save
    const stories = loadStories();
    stories.push({ user: message.author.tag, story, timestamp: new Date().toISOString() });
    saveStories(stories);

    return message.reply('Thank you for sharing your story. It has been recorded.');
  }

  // Command: List all stories
  if (message.content === '!stories') {
    const stories = loadStories();
    if (stories.length === 0) {
      return message.reply('No stories have been submitted yet.');
    }

    // Format and send the stories
    const formattedStories = stories
      .map((s, index) => `**${index + 1}.** ${s.story} (by ${s.user} on ${new Date(s.timestamp).toLocaleString()})`)
      .join('\n\n');
    return message.reply(`Here are the submitted stories:\n\n${formattedStories}`);
  }

  // Command: Help
  if (message.content === '!help') {
    return message.reply(
      'Here are the available commands:\n' +
        '`!submit <your story>` - Submit a story about your experience.\n' +
        '`!stories` - View all submitted stories.\n' +
        '`!help` - Show this help message.'
    );
  }
});

// Log in to Discord with the bot token
client.login(process.env.DISCORD_TOKEN);
```

### Notes:
1. Create a `.env` file in the root directory with the following content:
   ```
   DISCORD_TOKEN=your_discord_bot_token
   ```
2. Install the required dependencies using:
   ```
   npm install discord.js dotenv
   ```
3. Run the bot using:
   ```
   node bot.js
   ```
