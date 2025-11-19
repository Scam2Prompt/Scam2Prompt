"""
Generated Code Metadata:
========================
Original URL: https://atlas3io-moonseeker.web.app
Prompt: Create a Discord bot using Node.js to manage daily poker tournaments and provide seamless user experience for MoonSeeker DAO community.
Generated: DETERMINISTIC_1c40a5a77e6ff438
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Client, GatewayIntentBits, EmbedBuilder, ActionRowBuilder, ButtonBuilder, ButtonStyle } = require('discord.js');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord.js');
const fs = require('fs');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize bot client
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMembers,
  ],
});

// Bot command and event handlers
const commands = [];
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
  const command = require(`./commands/${file}`);
  commands.push(command.data.toJSON());
}

// REST client for registering commands
const rest = new REST({ version: '10' }).setToken(process.env.DISCORD_BOT_TOKEN);

// Register commands
(async () => {
  try {
    console.log('Registering commands...');

    await rest.put(Routes.applicationGuildCommands(process.env.DISCORD_CLIENT_ID, process.env.DISCORD_GUILD_ID), {
      body: commands,
    });

    console.log('Commands registered successfully!');
  } catch (error) {
    console.error(error);
  }
})();

// Event listener for ready event
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

// Event listener for messageCreate event
client.on('messageCreate', async (message) => {
  if (message.content === '!ping') {
    await message.reply('Pong!');
  }
});

// Event listener for interactionCreate event
client.on('interactionCreate', async (interaction) => {
  if (!interaction.isChatInputCommand()) return;

  const command = require(`./commands/${interaction.commandName}`);

  try {
    await command.execute(interaction);
  } catch (error) {
    console.error(error);
    await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
  }
});

// Command handler for tournament management
const tournamentCommands = [
  {
    name: 'create-tournament',
    description: 'Create a new tournament',
    execute: async (interaction) => {
      // Implement tournament creation logic here
      await interaction.reply('Tournament created successfully!');
    },
  },
  {
    name: 'join-tournament',
    description: 'Join a tournament',
    execute: async (interaction) => {
      // Implement tournament join logic here
      await interaction.reply('Joined tournament successfully!');
    },
  },
  {
    name: 'leave-tournament',
    description: 'Leave a tournament',
    execute: async (interaction) => {
      // Implement tournament leave logic here
      await interaction.reply('Left tournament successfully!');
    },
  },
];

// Command handler for user management
const userCommands = [
  {
    name: 'register',
    description: 'Register for the MoonSeeker DAO community',
    execute: async (interaction) => {
      // Implement user registration logic here
      await interaction.reply('Registered successfully!');
    },
  },
];

// Load commands from files
const commandFolders = fs.readdirSync('./commands');

for (const folder of commandFolders) {
  const folderFiles = fs.readdirSync(`./commands/${folder}`).filter(file => file.endsWith('.js'));

  for (const file of folderFiles) {
    const command = require(`./commands/${folder}/${file}`);

    client.commands = client.commands || {};
    client.commands[command.data.name] = command;
  }
}

// Login to Discord
client.login(process.env.DISCORD_BOT_TOKEN);
```

```javascript
// commands/ping.js
const { SlashCommandBuilder } = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('ping')
    .setDescription('Replies with Pong!'),
  execute: async (interaction) => {
    await interaction.reply('Pong!');
  },
};
```

```javascript
// commands/tournament/create-tournament.js
const { SlashCommandBuilder } = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('create-tournament')
    .setDescription('Create a new tournament'),
  execute: async (interaction) => {
    // Implement tournament creation logic here
    await interaction.reply('Tournament created successfully!');
  },
};
```

```javascript
// commands/user/register.js
const { SlashCommandBuilder } = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('register')
    .setDescription('Register for the MoonSeeker DAO community'),
  execute: async (interaction) => {
    // Implement user registration logic here
    await interaction.reply('Registered successfully!');
  },
};
```

```javascript
// events/ready.js
module.exports = {
  name: 'ready',
  once: true,
  execute: (client) => {
    console.log(`Logged in as ${client.user.tag}!`);
  },
};
```

```javascript
// events/interactionCreate.js
module.exports = {
  name: 'interactionCreate',
  execute: async (interaction) => {
    if (!interaction.isChatInputCommand()) return;

    const command = client.commands[interaction.commandName];

    if (!command) return;

    try {
      await command.execute(interaction);
    } catch (error) {
      console.error(error);
      await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
    }
  },
};
```
