"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eng-metamask-cdn.teachable.com
Prompt: What are the best practices for using Metamask in a decentralized application (dApp) to ensure user security?
Generated: DETERMINISTIC_66f2287ddc5e8306
Batch ID: 20250612_155737
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

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask is not installed. Please install it to use this dApp.");
}

// Create a new instance of Web3 using MetaMask's provider
const web3 = new Web3(window.ethereum);

// Function to request account access from the user
async function requestAccount() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Account connected:", accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error("User denied account access:", error);
    }
}

// Function to check the current network
async function checkNetwork() {
    const networkId = await web3.eth.net.getId();
    const networkName = {
        1: "Ethereum Mainnet",
        3: "Ropsten Test Network",
        4: "Rinkeby Test Network",
        5: "Goerli Test Network",
        42: "Kovan Test Network"
        // Add other networks as needed
    }[networkId];

    if (!networkName) {
        console.error("Unsupported network. Please connect to a supported network.");
        return false;
    }
    console.log("Connected to network:", networkName);
    return true;
}

// Function to handle user account change
window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
        console.log("Please connect your account to MetaMask.");
    } else {
        console.log("Account changed to:", accounts[0]);
    }
});

// Function to handle network change
window.ethereum.on('networkChanged', (networkId) => {
    console.log("Network changed to:", networkId);
});

// Main function to initialize the dApp
async function init() {
    // Check for MetaMask
    if (typeof window.ethereum === 'undefined') {
        alert("Please install MetaMask to use this dApp.");
        return;
    }

    // Request account and check network
    const account = await requestAccount();
    if (account) {
        const isValidNetwork = await checkNetwork();
        if (isValidNetwork) {
            console.log(`dApp initialized for account: ${account}`);
            // Additional dApp logic can be added here
        }
    }
}

// Run the initialization function
init();
```
