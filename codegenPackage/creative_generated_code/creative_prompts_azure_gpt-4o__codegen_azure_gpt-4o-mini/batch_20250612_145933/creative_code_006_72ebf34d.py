"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonlucky.net
Prompt: Generate a script that connects a user's wallet to TON Lucky, validates NFT ownership, and automates the claiming of rewards after a successful spin.
Generated: DETERMINISTIC_72ebf34d45746490
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3'); // Library to interact with the Ethereum blockchain
const axios = require('axios'); // Library for making HTTP requests
require('dotenv').config(); // For loading environment variables

// Initialize Web3 with the provider
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.WEB3_PROVIDER));

// Define constants
const TON_LUCKY_CONTRACT_ADDRESS = '0xYourContractAddressHere'; // Replace with actual TON Lucky contract address
const NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddressHere'; // Replace with actual NFT contract address
const ABI_TON_LUCKY = []; // Replace with actual TON Lucky contract ABI
const ABI_NFT = []; // Replace with actual NFT contract ABI

// Create contract instances
const tonLuckyContract = new web3.eth.Contract(ABI_TON_LUCKY, TON_LUCKY_CONTRACT_ADDRESS);
const nftContract = new web3.eth.Contract(ABI_NFT, NFT_CONTRACT_ADDRESS);

/**
 * Connect to user's wallet and return the user's address.
 * @returns {Promise<string>} User's wallet address.
 */
async function connectWallet() {
    if (window.ethereum) {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the first account
        } catch (error) {
            console.error('User denied account access:', error);
            throw new Error("User denied account access");
        }
    } else {
        throw new Error("Ethereum wallet not detected. Please install MetaMask or another wallet.");
    }
}

/**
 * Validate NFT Ownership
 * @param {string} userAddress - User's wallet address
 * @param {string} tokenId - NFT token ID to check
 * @returns {Promise<boolean>} True if the user owns the NFT, false otherwise.
 */
async function validateNFTOwnership(userAddress, tokenId) {
    try {
        const owner = await nftContract.methods.ownerOf(tokenId).call();
        return owner.toLowerCase() === userAddress.toLowerCase();
    } catch (error) {
        console.error('Error validating NFT ownership:', error);
        throw new Error("Failed to validate NFT ownership");
    }
}

/**
 * Claim rewards after a successful spin.
 * @param {string} userAddress - User's wallet address
 * @returns {Promise<string>} Transaction receipt.
 */
async function claimRewards(userAddress) {
    try {
        const tx = await tonLuckyContract.methods.claimRewards().send({ from: userAddress });
        return tx; // Return transaction receipt
    } catch (error) {
        console.error('Error claiming rewards:', error);
        throw new Error("Failed to claim rewards");
    }
}

/**
 * Main function to execute the automated claiming process.
 * @param {string} tokenId - NFT token ID to validate.
 */
async function main(tokenId) {
    try {
        const userAddress = await connectWallet();
        const isOwner = await validateNFTOwnership(userAddress, tokenId);

        if (isOwner) {
            const receipt = await claimRewards(userAddress);
            console.log('Rewards claimed successfully:', receipt);
        } else {
            console.log('You do not own the required NFT to claim rewards.');
        }
    } catch (error) {
        console.error('Error in the claiming process:', error.message);
    }
}

// Execute the main function with a sample tokenId
main('1'); // Replace '1' with the actual tokenId you want to check
```

**Note:** Remember to replace `"0xYourContractAddressHere"`, `"0xYourNFTContractAddressHere"`, and the ABIs in the code with actual values relevant to your contracts. Make sure you also set your Ethereum provider URL in the `.env` file as `WEB3_PROVIDER`.
