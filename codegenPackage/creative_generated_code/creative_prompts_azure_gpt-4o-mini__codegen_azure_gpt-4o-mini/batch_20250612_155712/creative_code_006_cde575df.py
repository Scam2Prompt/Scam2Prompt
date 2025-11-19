"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-home-extension.godaddysites.com
Prompt: How does the MetaMask extension help users manage their identities with private keys and local wallets?
Generated: DETERMINISTIC_cde575dfbbc5cdd1
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Function to check if MetaMask is installed
function isMetaMaskInstalled() {
    return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask === true;
}

// Initialize Web3 instance
let web3;
if (isMetaMaskInstalled()) {
    web3 = new Web3(window.ethereum);
} else {
    console.error("MetaMask is not installed. Please install it to use this application.");
}

// Function to connect to MetaMask and request account access
async function connectMetaMask() {
    if (!isMetaMaskInstalled()) {
        throw new Error("MetaMask is not installed.");
    }

    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log(`Connected account: ${accounts[0]}`);
        return accounts[0];
    } catch (error) {
        console.error("Error connecting to MetaMask:", error);
        throw new Error("User denied account access or error occurred.");
    }
}

// Function to get the account balance
async function getAccountBalance(account) {
    try {
        const balance = await web3.eth.getBalance(account);
        console.log(`Balance for ${account}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
        return balance;
    } catch (error) {
        console.error("Error fetching balance:", error);
        throw new Error("Could not fetch balance.");
    }
}

// Function to sign a message
async function signMessage(account, message) {
    try {
        const signature = await web3.eth.personal.sign(message, account);
        console.log(`Signature for message "${message}": ${signature}`);
        return signature;
    } catch (error) {
        console.error("Error signing message:", error);
        throw new Error("Could not sign the message.");
    }
}

// Main function to demonstrate MetaMask capabilities
async function main() {
    try {
        const account = await connectMetaMask();
        await getAccountBalance(account);
        
        const message = "Hello, this is a test message!";
        await signMessage(account, message);
    } catch (error) {
        console.error("Error in main function:", error);
    }
}

// Execute the main function
main();
```
