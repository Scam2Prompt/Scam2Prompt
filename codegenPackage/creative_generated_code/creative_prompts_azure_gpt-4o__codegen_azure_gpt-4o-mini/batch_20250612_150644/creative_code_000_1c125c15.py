"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-spark.com
Prompt: Write code to integrate MetaMask SDK into a web3 application, enabling wallet connection and transaction management.
Generated: DETERMINISTIC_1c125c15fb5b2775
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries for the web3 application
import Web3 from 'web3';
import { MetaMaskInpageProvider } from '@metamask/providers';

// Check if the MetaMask provider is available
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install it to use this app.');
}

// Create a new instance of the MetaMask provider
const provider = window.ethereum;

// Create a new instance of Web3 using the provider
const web3 = new Web3(provider);

/**
 * Connects to the user's MetaMask wallet.
 */
async function connectWallet() {
    try {
        // Request account access if needed
        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        
        // Set the selected account (could be enhanced to allow account switching)
        const selectedAccount = accounts[0];
        console.log('Connected account:', selectedAccount);
        
        return selectedAccount;
    } catch (error) {
        console.error('Failed to connect to MetaMask:', error);
        throw new Error('Wallet connection failed.');
    }
}

/**
 * Sends a transaction using the connected wallet.
 * @param {string} to - The recipient address.
 * @param {string} amount - The amount of Ether to send (in Wei).
 */
async function sendTransaction(to, amount) {
    try {
        const accounts = await web3.eth.getAccounts();
        const from = accounts[0];

        // Create the transaction object
        const transactionParameters = {
            to: to,
            from: from,
            value: web3.utils.toHex(amount), // Convert amount to hex
            gas: '2000000', // Set gas limit
        };

        // Send the transaction
        const txHash = await provider.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        console.log('Transaction successful with hash:', txHash);
        return txHash;
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Transaction failed.');
    }
}

/**
 * Main function to run the application.
 */
async function main() {
    try {
        const account = await connectWallet();
        
        // Example usage: sending 0.01 Ether to a specified address
        const recipient = '0xRecipientAddressHere'; // Replace with actual recipient address
        const amountInWei = web3.utils.toWei('0.01', 'ether'); // Convert to Wei

        await sendTransaction(recipient, amountInWei);
    } catch (error) {
        console.error('Error in main execution:', error);
    }
}

// Run the main function
main();
```
