"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dyno.pw
Prompt: Recommend a way to configure Dyno Bot for role management in a Discord server, referencing the bot's capabilities mentioned on the Dyno Bot site.
Generated: DETERMINISTIC_3bfb34e3d6a0eb68
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const { Client, Intents } = require('discord.js');

// Create a new client instance
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MEMBERS] });

// Your Discord bot token
const TOKEN = 'YOUR_BOT_TOKEN_HERE';

// Event listener for when the bot is ready
client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

// Function to assign a role to a user
async function assignRole(member, roleName) {
    try {
        // Fetch the role from the guild
        const role = member.guild.roles.cache.find(r => r.name === roleName);
        if (!role) {
            console.error(`Role "${roleName}" not found.`);
            return;
        }

        // Add the role to the member
        await member.roles.add(role);
        console.log(`Assigned role "${roleName}" to ${member.user.tag}`);
    } catch (error) {
        console.error(`Failed to assign role "${roleName}" to ${member.user.tag}:`, error);
    }
}

// Function to remove a role from a user
async function removeRole(member, roleName) {
    try {
        const role = member.guild.roles.cache.find(r => r.name === roleName);
        if (!role) {
            console.error(`Role "${roleName}" not found.`);
            return;
        }

        await member.roles.remove(role);
        console.log(`Removed role "${roleName}" from ${member.user.tag}`);
    } catch (error) {
        console.error(`Failed to remove role "${roleName}" from ${member.user.tag}:`, error);
    }
}

// Event listener for when a member joins a guild
client.on('guildMemberAdd', async member => {
    // Assign default role on member join
    await assignRole(member, 'DefaultRole'); // Change 'DefaultRole' to the desired role name
});

// Event listener for when a member leaves a guild
client.on('guildMemberRemove', async member => {
    // Optionally remove a specific role when the member leaves
    await removeRole(member, 'DefaultRole'); // Change 'DefaultRole' to the desired role name
});

// Log in to Discord with your app's token
client.login(TOKEN);
```

**Note: Make sure to replace `YOUR_BOT_TOKEN_HERE` with your actual Discord bot token and modify role names as necessary. Also, ensure your bot has the required permissions to manage roles in the Discord server.**
