"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbbag.com
Prompt: Generate a code snippet that demonstrates how to securely connect a wallet for purchasing $MBAG tokens during the presale.
Generated: DETERMINISTIC_7d8bba33a9c2c7a6
Batch ID: 20250612_163630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';
import Web3Modal from 'web3modal';

// Define the contract address and ABI for the $MBAG token
const MBAG_TOKEN_ADDRESS = '0xYourTokenContractAddressHere';
const MBAG_TOKEN_ABI = [
    // Add the ABI of the token contract here
    "function buyTokens() payable"
];

// Initialize necessary variables
let provider;
let signer;
let contract;

// Function to connect wallet and initialize the contract
async function connectWallet() {
    try {
        // Create a new instance of Web3Modal
        const web3Modal = new Web3Modal({
            cacheProvider: false, // Do not cache provider
            providerOptions: {} // Add any provider options here if needed
        });

        // Connect to wallet
        const connection = await web3Modal.connect();
        provider = new ethers.providers.Web3Provider(connection);
        signer = provider.getSigner();

        // Initialize contract
        contract = new ethers.Contract(MBAG_TOKEN_ADDRESS, MBAG_TOKEN_ABI, signer);
        console.log('Wallet connected successfully.');
    } catch (error) {
        console.error('Failed to connect wallet:', error);
    }
}

// Function to purchase $MBAG tokens
async function purchaseMBAGTokens(amountInEther) {
    try {
        // Validate amount
        if (isNaN(amountInEther) || amountInEther <= 0) {
            throw new Error('Invalid amount. Must be a positive number.');
        }

        // Convert amount to wei
        const amountInWei = ethers.utils.parseEther(amountInEther.toString());

        // Send transaction to buy tokens
        const transaction = await contract.buyTokens({ value: amountInWei });
        console.log('Transaction submitted. Waiting for confirmation...');

        // Wait for transaction confirmation
        await transaction.wait();
        console.log('Tokens purchased successfully!');
    } catch (error) {
        console.error('Error purchasing $MBAG tokens:', error);
    }
}

// Example usage:
// Connect wallet
connectWallet().then(() => {
    // Purchase 0.1 ETH worth of $MBAG tokens
    purchaseMBAGTokens(0.1);
});
```
