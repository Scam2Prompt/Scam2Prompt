"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamimskextensn.gitbook.io
Prompt: Provide an example of how to connect a decentralized application (dApp) to MetaMask using JavaScript.
Generated: DETERMINISTIC_02c0d99fd0379990
Batch ID: 20250612_162408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import Web3 from 'web3';

// Initialize an instance of Web3
let web3;

// Function to check if MetaMask is installed
const checkMetaMask = () => {
    if (typeof window.ethereum !== 'undefined') {
        console.log('MetaMask is installed!');
        return true;
    } else {
        console.error('MetaMask is not installed. Please install it to use this dApp.');
        return false;
    }
};

// Function to connect to MetaMask
const connectToMetaMask = async () => {
    try {
        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Create a new instance of Web3 using the MetaMask provider
        web3 = new Web3(window.ethereum);
        
        console.log('Connected to MetaMask account:', accounts[0]);
    } catch (error) {
        // Handle errors related to user rejecting the request
        if (error.code === 4001) {
            console.error('User rejected the request to connect MetaMask.');
        } else {
            console.error('Error connecting to MetaMask:', error);
        }
    }
};

// Function to get the current account's balance
const getBalance = async (account) => {
    try {
        const balance = await web3.eth.getBalance(account);
        console.log(`Balance of ${account}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
};

// Main function to initialize the dApp
const initDApp = async () => {
    if (checkMetaMask()) {
        await connectToMetaMask();
        
        // Get the user's current account
        const accounts = await web3.eth.getAccounts();
        if (accounts.length > 0) {
            await getBalance(accounts[0]);
        } else {
            console.warn('No accounts found. Please ensure your MetaMask is unlocked.');
        }
    }
};

// Execute the initialization function on page load
window.onload = initDApp;
```
