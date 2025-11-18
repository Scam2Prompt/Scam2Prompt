"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metumasikliogginn.godaddysites.com
Prompt: Create a step-by-step guide for setting up Metamask login integration in a web application using Web3.js.
Generated: DETERMINISTIC_d86fa8d9abfbe7d1
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Initialize Web3 instance
let web3;

// Function to initialize Web3 and check for MetaMask
async function initWeb3() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Initialize Web3 with the MetaMask provider
        web3 = new Web3(window.ethereum);
        console.log("MetaMask is installed!");
    } else {
        console.error("Please install MetaMask to use this app.");
        throw new Error("MetaMask not found");
    }
}

// Function to connect MetaMask
async function connectMetaMask() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Connected account:", accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error("Error connecting to MetaMask:", error);
        throw new Error("Failed to connect to MetaMask");
    }
}

// Function to get the current account balance
async function getAccountBalance(account) {
    try {
        const balance = await web3.eth.getBalance(account);
        console.log("Account balance:", web3.utils.fromWei(balance, 'ether'), "ETH");
        return balance;
    } catch (error) {
        console.error("Error fetching balance:", error);
        throw new Error("Failed to fetch account balance");
    }
}

// Main function to run the setup
async function runApp() {
    try {
        await initWeb3(); // Initialize Web3
        const account = await connectMetaMask(); // Connect MetaMask
        await getAccountBalance(account); // Get account balance
    } catch (error) {
        console.error("Error in application:", error);
    }
}

// Execute the application
runApp();
```
