"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: Provide a step-by-step example of building immersive NFT apps with Meta Blocks open-source tools, including code for handling upgrades and decay.
Generated: DETERMINISTIC_1a9b5e9767985249
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example code for building an immersive NFT app using Meta Blocks open-source tools, focusing on handling upgrades and decay. The code uses JavaScript with Node.js and assumes familiarity with blockchain development and integration with tools such as ethers.js.

```javascript
// Import required libraries
const { ethers } = require("ethers");
const MetaBlocks = require("meta-blocks"); // Assuming Meta Blocks SDK is installed
require("dotenv").config(); // For managing environment variables

// Setup configurations
const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL); // Blockchain provider
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider); // Wallet for signing transactions
const metaBlocksContractAddress = process.env.META_BLOCKS_CONTRACT_ADDRESS; // Address of the deployed Meta Blocks contract

// Initialize Meta Blocks SDK
const metaBlocks = new MetaBlocks({ provider, contractAddress: metaBlocksContractAddress });

// Helper function to fetch NFT metadata
async function fetchNFTMetadata(tokenId) {
  try {
    const metadata = await metaBlocks.getMetadata(tokenId);
    console.log("NFT Metadata:", metadata);
    return metadata;
  } catch (error) {
    console.error("Error fetching NFT metadata:", error);
    throw error;
  }
}

// Function to handle upgrades
async function upgradeNFT(tokenId, upgradeData) {
  try {
    console.log("Upgrading NFT...");

    // Perform the upgrade using Meta Blocks
    const tx = await metaBlocks.upgrade(tokenId, upgradeData, {
      from: wallet.address,
    });

    console.log("Upgrade transaction submitted:", tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log("Upgrade transaction mined:", receipt);
  } catch (error) {
    console.error("Error upgrading NFT:", error);
    throw error;
  }
}

// Function to handle decay logic
async function applyDecay(tokenId) {
  try {
    console.log("Applying decay to NFT...");

    // Fetch the current metadata
    const metadata = await fetchNFTMetadata(tokenId);

    // Apply decay logic (example: reduce durability or stats)
    const decayedData = { ...metadata, durability: metadata.durability - 1 };

    // Update metadata on-chain
    const tx = await metaBlocks.updateMetadata(tokenId, decayedData, {
      from: wallet.address,
    });

    console.log("Decay transaction submitted:", tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log("Decay transaction mined:", receipt);
  } catch (error) {
    console.error("Error applying decay to NFT:", error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const tokenId = 1; // Replace with your NFT token ID

    console.log("Fetching metadata for token ID:", tokenId);
    const metadata = await fetchNFTMetadata(tokenId);

    console.log("Upgrading NFT with new stats...");
    const upgradeData = { ...metadata, level: metadata.level + 1 }; // Example upgrade logic
    await upgradeNFT(tokenId, upgradeData);

    console.log("Applying decay logic...");
    await applyDecay(tokenId);

    console.log("All operations completed successfully.");
  } catch (error) {
    console.error("An error occurred during NFT operations:", error);
  }
})();
```

### Notes:
1. Install dependencies using `npm install ethers dotenv meta-blocks` before running the code.
2. Replace environment variables (`RPC_URL`, `PRIVATE_KEY`, `META_BLOCKS_CONTRACT_ADDRESS`) with appropriate values.
3. Ensure Meta Blocks SDK documentation is referenced for API details like `upgrade` and `updateMetadata`.
