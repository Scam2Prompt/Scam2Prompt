"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: Write a guide for integrating off-chain NFT upgrades using Meta Blocks tools and updating the NFT on-chain. Include relevant code snippets.
Generated: DETERMINISTIC_975b9e4541e14ca9
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers'; // Ethereum library
import MetaBlocks from 'metablocks-sdk'; // Meta Blocks SDK

// Define the NFT contract address and ABI
const NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddress'; // Replace with your NFT contract address
const NFT_CONTRACT_ABI = [ /* ABI goes here */ ];

// Initialize provider and signer
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Initialize the Meta Blocks SDK
const metaBlocks = new MetaBlocks();

// Connect to the NFT contract
const nftContract = new ethers.Contract(NFT_CONTRACT_ADDRESS, NFT_CONTRACT_ABI, signer);

/**
 * Function to upgrade an NFT off-chain
 * @param {string} nftId - The ID of the NFT to upgrade
 * @param {object} upgradeData - The upgrade data to be sent off-chain
 */
async function upgradeNFTOffChain(nftId, upgradeData) {
    try {
        // Send upgrade request to Meta Blocks
        const response = await metaBlocks.sendUpgradeRequest(nftId, upgradeData);
        
        // Check if the request was successful
        if (response.success) {
            console.log('Off-chain upgrade successful:', response.data);
            return response.data;
        } else {
            throw new Error('Off-chain upgrade failed: ' + response.error);
        }
    } catch (error) {
        console.error('Error upgrading NFT off-chain:', error);
        throw error; // Rethrow error for further handling
    }
}

/**
 * Function to update the NFT on-chain after an upgrade
 * @param {string} nftId - The ID of the NFT to update
 * @param {object} newMetadata - The new metadata for the NFT
 */
async function updateNFTOnChain(nftId, newMetadata) {
    try {
        // Call the update function on the NFT contract
        const transaction = await nftContract.updateNFT(nftId, newMetadata);
        
        // Wait for the transaction to be mined
        const receipt = await transaction.wait();
        console.log('On-chain update successful, transaction receipt:', receipt);
        
        return receipt;
    } catch (error) {
        console.error('Error updating NFT on-chain:', error);
        throw error; // Rethrow error for further handling
    }
}

/**
 * Main function to handle NFT upgrade process
 * @param {string} nftId - The ID of the NFT to upgrade
 * @param {object} upgradeData - The upgrade data to be sent off-chain
 * @param {object} newMetadata - The new metadata to update on-chain
 */
async function handleNFTUpgrade(nftId, upgradeData, newMetadata) {
    try {
        // Step 1: Upgrade NFT off-chain
        const upgradeResponse = await upgradeNFTOffChain(nftId, upgradeData);

        // Step 2: Update the NFT on-chain with new metadata
        await updateNFTOnChain(nftId, { ...newMetadata, upgradeResponse });
    } catch (error) {
        console.error('NFT upgrade process failed:', error);
    }
}

// Example usage
const nftId = '1'; // Example NFT ID
const upgradeData = { newProperty: 'newValue' }; // Example upgrade data
const newMetadata = { name: 'Updated NFT', description: 'Upgraded NFT description' }; // New metadata

handleNFTUpgrade(nftId, upgradeData, newMetadata);
```
