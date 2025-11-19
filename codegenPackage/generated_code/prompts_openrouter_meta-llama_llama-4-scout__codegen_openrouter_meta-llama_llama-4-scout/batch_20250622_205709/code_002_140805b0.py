"""
Generated Code Metadata:
========================
Original URL: https://guild-verify.web.app
Prompt: Generate a sample code for checking access to a Discord guild based on NFT ownership, using the Guild SDK and OpenZeppelin's contracts.
Generated: DETERMINISTIC_140805b032193eb2
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('hardhat');
const { GuildSDK } = require('@guildxyz/sdk');

// Define the contract ABI for the NFT
const nftAbi = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "ownerOf",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

// Define the contract address for the NFT
const nftContractAddress = '0x...'; // Replace with your NFT contract address

// Initialize the Guild SDK
const guildSDK = new GuildSDK({
  // Replace with your Guild SDK configuration
  apiKey: 'YOUR_GUILD_API_KEY',
  apiSecret: 'YOUR_GUILD_API_SECRET',
});

// Define a function to check access to a Discord guild based on NFT ownership
async function checkAccessToGuild(guildId, userId, nftTokenId) {
  try {
    // Get the user's NFT balance
    const nftContract = new ethers.Contract(nftContractAddress, nftAbi);
    const nftBalance = await nftContract.balanceOf(userId);

    // Check if the user owns the NFT
    if (nftBalance.gt(0)) {
      // Get the guild's requirements
      const guildRequirements = await guildSDK.getGuildRequirements(guildId);

      // Check if the guild requires NFT ownership
      if (guildRequirements.requirements.includes('NFT')) {
        // Check if the user owns the specific NFT token ID
        const nftOwner = await nftContract.ownerOf(nftTokenId);
        if (nftOwner.toLowerCase() === userId.toLowerCase()) {
          // User owns the NFT, grant access to the guild
          return true;
        }
      }
    }

    // User does not own the NFT or does not meet guild requirements
    return false;
  } catch (error) {
    console.error('Error checking access to guild:', error);
    return false;
  }
}

// Example usage
async function main() {
  const guildId = 'YOUR_GUILD_ID';
  const userId = '0x...'; // Replace with the user's Ethereum address
  const nftTokenId = 'YOUR_NFT_TOKEN_ID';

  const hasAccess = await checkAccessToGuild(guildId, userId, nftTokenId);
  console.log(`User has access to guild: ${hasAccess}`);
}

main();
```
