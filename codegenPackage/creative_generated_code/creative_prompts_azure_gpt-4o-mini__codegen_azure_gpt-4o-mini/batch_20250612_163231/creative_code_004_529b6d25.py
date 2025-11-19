"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: Explain how MetaMask integrates with popular web browsers and the benefits of using it for decentralized finance activities.
Generated: DETERMINISTIC_529b6d25c36a2612
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMask Integration Example with Web3.js
// This example demonstrates how to integrate MetaMask with a web application
// and how to perform basic decentralized finance (DeFi) activities.

// Import Web3 library
import Web3 from 'web3';

// Function to check if MetaMask is installed
async function checkMetaMask() {
    if (typeof window.ethereum !== 'undefined') {
        console.log('MetaMask is installed!');
        return true;
    } else {
        console.error('MetaMask is not installed. Please install it to use this app.');
        return false;
    }
}

// Function to connect to MetaMask
async function connectMetaMask() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);

        // Initialize Web3 with MetaMask's provider
        const web3 = new Web3(window.ethereum);
        return web3;
    } catch (error) {
        console.error('User rejected the request:', error);
        return null;
    }
}

// Function to get the account balance
async function getBalance(web3, account) {
    try {
        const balance = await web3.eth.getBalance(account);
        console.log(`Account balance for ${account}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
}

// Main function to handle MetaMask integration
async function main() {
    // Check for MetaMask installation
    if (await checkMetaMask()) {
        // Connect to MetaMask
        const web3 = await connectMetaMask();
        if (web3) {
            // Get the user's accounts
            const accounts = await web3.eth.getAccounts();
            // Fetch and display account balance
            await getBalance(web3, accounts[0]);
        }
    }
}

// Execute the main function
main();
```
