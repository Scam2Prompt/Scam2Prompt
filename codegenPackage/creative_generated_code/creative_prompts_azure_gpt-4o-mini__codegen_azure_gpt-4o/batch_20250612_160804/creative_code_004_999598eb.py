"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guild-verify.web.app
Prompt: Explain how to integrate the Guild SDK with Discord to manage roles based on NFT ownership, specifically for Ubisoft Web3.
Generated: DETERMINISTIC_999598eb72e65d02
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is clean, production-ready JavaScript code for integrating the Guild SDK with Discord to manage roles based on NFT ownership for Ubisoft Web3. This example assumes the use of Node.js.

```javascript
// Import required dependencies
const { Client, GatewayIntentBits } = require('discord.js'); // Discord.js library for bot interaction
const GuildSDK = require('@guildxyz/sdk'); // Guild SDK for managing roles
require('dotenv').config(); // For securely loading environment variables

/**
 * Production-ready Discord bot integration with Guild SDK to manage roles
 * based on NFT ownership (specific to Ubisoft Web3).
 */

// Load environment variables
const DISCORD_TOKEN = process.env.DISCORD_TOKEN; // Discord bot token
const GUILD_API_KEY = process.env.GUILD_API_KEY; // Guild SDK API key
const GUILD_ID = process.env.GUILD_ID; // Guild ID for role management
const NFT_CONTRACT_ADDRESS = process.env.NFT_CONTRACT_ADDRESS; // Ubisoft Web3 NFT contract address

// Initialize Discord client with required intents
const discordClient = new Client({
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMembers]
});

// Initialize Guild SDK
const guildSDK = new GuildSDK(GUILD_API_KEY);

/**
 * Check NFT ownership for a Discord user using Guild SDK.
 * @param {string} discordId - The Discord user ID.
 * @returns {Promise<boolean>} - Returns true if the user owns the NFT, otherwise false.
 */
async function checkNFTOwnership(discordId) {
  try {
    // Query Guild SDK to check NFT ownership
    const result = await guildSDK.checkNFTOwnership({
      guildId: GUILD_ID,
      discordId,
      contractAddress: NFT_CONTRACT_ADDRESS
    });

    return result.hasAccess;
  } catch (error) {
    console.error('Error checking NFT ownership:', error.message);
    return false; // Assume no ownership in case of an error
  }
}

/**
 * Assign role to user if they own the NFT.
 * @param {GuildMember} member - The Discord guild member object.
 */
async function assignRoleBasedOnNFT(member) {
  try {
    // Check for NFT ownership
    const hasNFT = await checkNFTOwnership(member.user.id);

    // Define the role to assign
    const roleName = 'NFT Holder';
    const role = member.guild.roles.cache.find(r => r.name === roleName);

    if (!role) {
      console.error(`Role "${roleName}" not found in the guild.`);
      return;
    }

    // Assign role if NFT is owned, otherwise remove it
    if (hasNFT) {
      await member.roles.add(role);
      console.log(`Assigned role "${roleName}" to ${member.user.tag}.`);
    } else {
      await member.roles.remove(role);
      console.log(`Removed role "${roleName}" from ${member.user.tag}.`);
    }
  } catch (error) {
    console.error(`Error assigning role to ${member.user.tag}:`, error.message);
  }
}

// Event: Bot ready
discordClient.once('ready', () => {
  console.log(`Logged in as ${discordClient.user.tag}.`);
});

// Event: User joins the guild
discordClient.on('guildMemberAdd', async member => {
  console.log(`New member joined: ${member.user.tag}. Checking NFT ownership...`);
  await assignRoleBasedOnNFT(member);
});

// Event: Periodic check for all members (e.g., every hour)
setInterval(async () => {
  const guild = discordClient.guilds.cache.first(); // Get the first guild the bot is in
  if (!guild) {
    console.error('Bot is not part of any guild.');
    return;
  }

  console.log('Performing periodic check for all members...');
  guild.members.fetch().then(members => {
    members.forEach(async member => {
      await assignRoleBasedOnNFT(member);
    });
  }).catch(error => console.error('Error fetching guild members:', error.message));
}, 3600000); // 3600000 ms = 1 hour

// Login the bot to Discord
discordClient.login(DISCORD_TOKEN).catch(error => {
  console.error('Error logging into Discord:', error.message);
});
```

### Required Setup
1. Install dependencies: `npm install discord.js @guildxyz/sdk dotenv`.
2. Add a `.env` file with the following keys:
   ```plaintext
   DISCORD_TOKEN=your_discord_bot_token
   GUILD_API_KEY=your_guild_sdk_api_key
   GUILD_ID=your_guild_id
   NFT_CONTRACT_ADDRESS=ubisoft_nft_contract_address
   ```
3. Ensure the bot has the appropriate permissions in your Discord server to manage roles.

This code uses best practices such as error handling, environment variables for sensitive data, and modular functions. It periodically checks users for NFT ownership and assigns/removes roles accordingly.
