"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.sbs
Prompt: How do I integrate USDC with a JavaScript application for decentralized finance?
Generated: DETERMINISTIC_de2602c486b0ed85
Batch ID: 20250612_155739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require('ethers');

// Define your Ethereum provider (using Infura in this example)
// Make sure to replace 'YOUR_INFURA_PROJECT_ID' with your actual Infura project ID
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');

// Define the USDC contract address on Ethereum mainnet
const USDC_ADDRESS = '0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48';

// Define the ABI for the USDC contract
const USDC_ABI = [
    // Only including the necessary functions for this example
    "function balanceOf(address owner) view returns (uint256)",
    "function transfer(address to, uint256 amount) returns (bool)"
];

// Create a new instance of the USDC contract
const usdcContract = new ethers.Contract(USDC_ADDRESS, USDC_ABI, provider);

// Function to get the USDC balance of a specific address
async function getUSDCBalance(address) {
    try {
        const balance = await usdcContract.balanceOf(address);
        console.log(`USDC Balance of ${address}: ${ethers.utils.formatUnits(balance, 6)} USDC`);
        return balance;
    } catch (error) {
        console.error(`Error fetching balance: ${error.message}`);
        throw error; // Rethrow the error after logging
    }
}

// Function to transfer USDC from one address to another
async function transferUSDC(senderPrivateKey, recipientAddress, amount) {
    // Create a wallet instance using sender's private key
    const wallet = new ethers.Wallet(senderPrivateKey, provider);
    
    // Create a new instance of the USDC contract connected to the wallet
    const usdcWithSigner = usdcContract.connect(wallet);

    try {
        // Convert amount to the correct format (USDC has 6 decimals)
        const amountInUnits = ethers.utils.parseUnits(amount.toString(), 6);
        
        // Perform the transfer
        const tx = await usdcWithSigner.transfer(recipientAddress, amountInUnits);
        
        console.log(`Transaction hash: ${tx.hash}`);
        
        // Wait for the transaction to be confirmed
        await tx.wait();
        console.log(`Successfully transferred ${amount} USDC to ${recipientAddress}`);
    } catch (error) {
        console.error(`Error during transfer: ${error.message}`);
        throw error; // Rethrow the error after logging
    }
}

// Example usage - replace with actual values
const addressToCheck = '0xYourWalletAddress';
const senderPrivateKey = '0xYourPrivateKey'; // WARNING: Keep this safe and do not expose it in production
const recipientAddress = '0xRecipientWalletAddress';
const transferAmount = 10; // Amount of USDC to transfer

// Run the methods
(async () => {
    await getUSDCBalance(addressToCheck);
    await transferUSDC(senderPrivateKey, recipientAddress, transferAmount);
})();
```
