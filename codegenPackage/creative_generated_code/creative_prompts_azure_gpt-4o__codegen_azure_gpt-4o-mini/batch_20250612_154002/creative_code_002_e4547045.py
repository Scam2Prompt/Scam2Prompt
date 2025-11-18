"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqqk.com
Prompt: Generate code to enable JavaScript-based wallet integration for Ethereum transactions in a DeFi application.
Generated: DETERMINISTIC_e4547045d721ebf2
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3'; // Web3.js library for interacting with the Ethereum blockchain
import { ethers } from 'ethers'; // Ethers.js library for wallet integration and transaction handling

// Initialize Web3 provider
const provider = new ethers.providers.Web3Provider(window.ethereum);

// Function to request wallet connection
async function connectWallet() {
    try {
        // Request account access if needed
        await provider.send("eth_requestAccounts", []);
        console.log("Wallet connected successfully!");
    } catch (error) {
        console.error("Error connecting to wallet:", error);
    }
}

// Function to send Ethereum transaction
async function sendTransaction(to, amount) {
    try {
        // Get the signer (the user's wallet)
        const signer = provider.getSigner();
        
        // Prepare the transaction details
        const transaction = {
            to: to,
            value: ethers.utils.parseEther(amount), // Convert amount to wei
            gasLimit: 21000, // Set a gas limit for the transaction
            gasPrice: await provider.getGasPrice() // Get the current gas price
        };

        // Send the transaction
        const txResponse = await signer.sendTransaction(transaction);
        
        // Wait for the transaction to be mined
        const txReceipt = await txResponse.wait();
        console.log("Transaction successful:", txReceipt);
    } catch (error) {
        console.error("Error sending transaction:", error);
    }
}

// Function to get the user's Ethereum balance
async function getBalance() {
    try {
        // Get the signer and the address
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        
        // Fetch the balance
        const balance = await provider.getBalance(address);
        
        // Convert balance from wei to ether
        const formattedBalance = ethers.utils.formatEther(balance);
        console.log(`Your balance: ${formattedBalance} ETH`);
        
        return formattedBalance; // Return the balance
    } catch (error) {
        console.error("Error fetching balance:", error);
    }
}

// Event listener for window load to check if the wallet is already connected
window.addEventListener('load', async () => {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        await connectWallet();
        await getBalance(); // Fetch balance after wallet connection
    } else {
        console.error("Please install MetaMask!");
    }
});

// Example usage: Uncomment to send 0.01 ETH to a specified address
// sendTransaction('0xYourEthereumAddressHere', '0.01');
```
