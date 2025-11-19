"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-s.pages.dev
Prompt: Write a code snippet to connect a decentralized wallet for purchasing DOGE20 tokens during the presale.
Generated: DETERMINISTIC_6905633ab982e9ee
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Setting up the provider and web3 instance
const provider = new ethers.providers.Web3Provider(window.ethereum);
let web3;

// Function to connect the wallet
async function connectWallet() {
    try {
        // Request account access from the user
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        // Initialize web3 instance with the current provider
        web3 = new Web3(window.ethereum);
        console.log("Wallet connected successfully!");
    } catch (error) {
        console.error("Failed to connect wallet:", error);
    }
}

// Function to purchase DOGE20 tokens
async function purchaseTokens(amountInEther) {
    const tokenContractAddress = '0xYourTokenContractAddress'; // Replace with the actual token contract address
    const presaleContractAddress = '0xYourPresaleContractAddress'; // Replace with the actual presale contract address
    
    // Replace with the actual ABI of the token contract
    const tokenABI = [
        // Add the necessary ABI methods here
    ];
    
    const presaleABI = [
        // Add the necessary ABI methods here
    ];

    const tokenContract = new web3.eth.Contract(tokenABI, tokenContractAddress);
    const presaleContract = new web3.eth.Contract(presaleABI, presaleContractAddress);
    
    const accounts = await web3.eth.getAccounts();
    const senderAddress = accounts[0];

    try {
        // Convert ETH amount to Wei
        const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

        // Sending transaction to purchase DOGE20 tokens
        const transaction = await presaleContract.methods.purchaseTokens(amountInWei).send({ from: senderAddress });
        
        console.log("Tokens purchased successfully!", transaction);
    } catch (error) {
        console.error("Failed to purchase tokens:", error);
    }
}

// Example usage
(async () => {
    await connectWallet();
    const amountToPurchase = 0.1; // Example amount in Ether
    await purchaseTokens(amountToPurchase);
})();
```

**Note:** Be sure to replace `'0xYourTokenContractAddress'`, `'0xYourPresaleContractAddress'`, and the corresponding ABI definitions with the actual values for your token and presale contracts.
