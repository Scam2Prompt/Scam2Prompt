"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-ultra.org
Prompt: Create a script that connects MetaMask to a dapp for minting and trading NFTs, including wallet connection and transaction signing.
Generated: DETERMINISTIC_3079814b1df0906d
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to connect MetaMask to a dApp for minting and trading NFTs.
 * This script handles wallet connection, ensures MetaMask is installed, and facilitates transaction signing.
 * 
 * Dependencies:
 * - Web3.js (Ensure you have it installed: npm install web3)
 * 
 * Note:
 * Replace `CONTRACT_ADDRESS`, `ABI`, and appropriate transaction logic with values from your NFT smart contract.
 */

const Web3 = require('web3');

// Initialize Web3 instance
let web3;

// Variable to store the connected account
let userAccount = null;

// Replace with your contract's address and ABI
const CONTRACT_ADDRESS = "0xYourContractAddress";
const CONTRACT_ABI = []; // Add your contract's ABI here

// Initialize contract instance
let nftContract;

/**
 * Check if MetaMask is installed and connect the wallet.
 */
async function connectWallet() {
    if (typeof window.ethereum === 'undefined') {
        console.error("MetaMask is not installed. Please install MetaMask to use this dApp.");
        alert("MetaMask is not installed. Please install MetaMask to use this dApp.");
        return;
    }

    try {
        // Request connection to MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        userAccount = accounts[0];
        console.log(`Wallet connected: ${userAccount}`);

        // Initialize Web3 with MetaMask provider
        web3 = new Web3(window.ethereum);

        // Initialize contract instance
        nftContract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);

        alert(`Wallet connected successfully: ${userAccount}`);
    } catch (error) {
        console.error("Error connecting wallet:", error);
        alert("Failed to connect wallet. Check the console for more details.");
    }
}

/**
 * Mint a new NFT.
 * @param {string} tokenURI - Metadata URI for the NFT being minted.
 */
async function mintNFT(tokenURI) {
    if (!userAccount || !nftContract) {
        alert("Wallet is not connected or contract is not initialized.");
        return;
    }

    try {
        // Call mint function on the contract
        const result = await nftContract.methods.mintNFT(userAccount, tokenURI)
            .send({ from: userAccount });

        console.log("NFT minted successfully:", result);
        alert("NFT minted successfully!");
    } catch (error) {
        console.error("Error minting NFT:", error);
        alert("Failed to mint NFT. Check the console for more details.");
    }
}

/**
 * Trade an NFT.
 * @param {string} tokenId - ID of the NFT to trade.
 * @param {string} recipient - Address of the recipient.
 */
async function tradeNFT(tokenId, recipient) {
    if (!userAccount || !nftContract) {
        alert("Wallet is not connected or contract is not initialized.");
        return;
    }

    try {
        // Call transfer function on the contract
        const result = await nftContract.methods.safeTransferFrom(userAccount, recipient, tokenId)
            .send({ from: userAccount });

        console.log("NFT traded successfully:", result);
        alert("NFT traded successfully!");
    } catch (error) {
        console.error("Error trading NFT:", error);
        alert("Failed to trade NFT. Check the console for more details.");
    }
}

/**
 * Event listeners for MetaMask account changes or chain changes.
 */
function setupEventListeners() {
    if (window.ethereum) {
        // Listen for account changes
        window.ethereum.on('accountsChanged', (accounts) => {
            userAccount = accounts[0];
            console.log(`Account changed: ${userAccount}`);
        });

        // Listen for chain changes
        window.ethereum.on('chainChanged', (chainId) => {
            console.log(`Chain changed to: ${chainId}`);
        });
    }
}

// Example usage (replace with your actual dApp's logic):
document.getElementById("connectButton").addEventListener("click", connectWallet);
document.getElementById("mintButton").addEventListener("click", () => {
    const tokenURI = prompt("Enter token URI for the NFT:");
    mintNFT(tokenURI);
});
document.getElementById("tradeButton").addEventListener("click", () => {
    const tokenId = prompt("Enter NFT token ID:");
    const recipient = prompt("Enter recipient address:");
    tradeNFT(tokenId, recipient);
});

// Initialize event listeners
setupEventListeners();
```
