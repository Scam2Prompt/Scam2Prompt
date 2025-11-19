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
const Discord = require('discord.js');
const { Client, Intents } = Discord;
const mongoose = require('mongoose');
require('dotenv').config();

// Define the UserStory schema
const userStorySchema = new mongoose.Schema({
    userId: { type: String, required: true },
    username: { type: String, required: true },
    story: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

const UserStory = mongoose.model('UserStory', userStorySchema);

// Initialize Discord client with necessary intents
const client = new Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.DIRECT_MESSAGES
    ]
});

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// Bot ready event
client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
});

// Handle incoming messages
client.on('messageCreate', async message => {
    // Ignore messages from bots
    if (message.author.bot) return;

    // Check if the message is a DM or in a specific channel
    const isDM = message.channel.type === 'DM';
    const isTargetChannel = message.channel.name === 'opensea-stories';

    if (isDM || isTargetChannel) {
        // Check if the message starts with the command prefix
        if (message.content.startsWith('!submitstory')) {
            const storyContent = message.content.replace('!submitstory', '').trim();

            if (!storyContent) {
                return message.reply('Please provide your story after the command. Example: `!submitstory My negative experience with OpenSea...`');
            }

            try {
                // Save the story to the database
                const newStory = new UserStory({
                    userId: message.author.id,
                    username: message.author.username,
                    story: storyContent
                });

                await newStory.save();

                // Respond to the user
                message.reply('Thank you for sharing your story. It has been recorded.');
            } catch (err) {
                console.error('Error saving story:', err);
                message.reply('There was an error saving your story. Please try again later.');
            }
        } else if (message.content.startsWith('!getstories')) {
            try {
                // Retrieve all stories from the database
                const stories = await UserStory.find().sort({ createdAt: -1 }).limit(10);

                if (stories.length === 0) {
                    return message.reply('No stories have been submitted yet.');
                }

                // Format the stories into an embed
                const embed = new Discord.MessageEmbed()
                    .setTitle('Recent Negative OpenSea Experiences')
                    .setColor('#FF0000')
                    .setDescription('Here are the most recent user-submitted stories about negative experiences with OpenSea:');

                stories.forEach(story => {
                    embed.addField(
                        `Submitted by ${story.username}`,
                        `${story.story}\n\n*Submitted on ${story.createdAt.toLocaleDateString()}*`
                    );
                });

                message.channel.send({ embeds: [embed] });
            } catch (err) {
                console.error('Error retrieving stories:', err);
                message.reply('There was an error retrieving stories. Please try again later.');
            }
        }
    }
});

// Error handling
client.on('error', error => {
    console.error('Discord client error:', error);
});

process.on('unhandledRejection', error => {
    console.error('Unhandled promise rejection:', error);
});

// Login to Discord
client.login(process.env.DISCORD_TOKEN);
```
