"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.tap.5ire.network
Prompt: How do I troubleshoot JavaScript issues when trying to use Metamask on 5ire Tap?
Generated: DETERMINISTIC_8f538a2431d3e647
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

async function connectToMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        throw new Error("MetaMask is not installed. Please install it to use this application.");
    }

    // Request account access if needed
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Connected account:", accounts[0]);
        return accounts[0]; // Return the connected account
    } catch (error) {
        console.error("User denied account access or error occurred:", error);
        throw new Error("Could not connect to MetaMask. Please check your MetaMask settings.");
    }
}

async function getBalance(account) {
    // Create an instance of the provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    try {
        // Get the balance of the connected account
        const balance = await provider.getBalance(account);
        console.log("Account balance (in ETH):", ethers.utils.formatEther(balance));
        return ethers.utils.formatEther(balance); // Return balance in ETH
    } catch (error) {
        console.error("Error getting balance:", error);
        throw new Error("Could not retrieve balance. Please check your network connection.");
    }
}

async function main() {
    try {
        const account = await connectToMetaMask(); // Connect to MetaMask
        const balance = await getBalance(account); // Get account balance
        console.log(`Balance of ${account}: ${balance} ETH`);
    } catch (error) {
        console.error("An error occurred during the operation:", error);
    }
}

// Run the main function
main();
```
