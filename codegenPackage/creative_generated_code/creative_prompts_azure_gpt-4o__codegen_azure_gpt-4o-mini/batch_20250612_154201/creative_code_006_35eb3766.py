"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain-frontend.vercel.app
Prompt: Provide a code example for integrating MetaMask with Berachain to enable wallet connection and block number retrieval.
Generated: DETERMINISTIC_35eb37662304e182
Batch ID: 20250612_154201
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

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask is not installed. Please install it to use this feature.");
}

// Create a web3 instance
const web3 = new Web3(window.ethereum);

// Function to connect to MetaMask and retrieve the block number
async function connectWalletAndFetchBlockNumber() {
    try {
        // Request account access if not already granted
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Log the connected account
        console.log("Connected account:", accounts[0]);

        // Retrieve the current block number
        const blockNumber = await web3.eth.getBlockNumber();
        
        // Log the current block number
        console.log("Current Block Number:", blockNumber);
    } catch (error) {
        // Handle errors
        if (error.code === 4001) {
            console.error("User rejected the request.");
        } else {
            console.error("An error occurred:", error);
        }
    }
}

// Function to initialize the app
function init() {
    // Check for Ethereum provider and MetaMask support
    if (window.ethereum) {
        // Add event listener for account or chain change
        window.ethereum.on('accountsChanged', (accounts) => {
            console.log("Accounts changed:", accounts);
            // You may want to refresh the page or update the UI
        });

        window.ethereum.on('chainChanged', (chainId) => {
            console.log("Chain changed to:", chainId);
            // You may want to refresh the page or update the UI
        });

        // Connect wallet and fetch block number on button click or automatically
        document.getElementById("connectButton").addEventListener("click", connectWalletAndFetchBlockNumber);
    } else {
        console.error("Please install MetaMask!");
    }
}

// Start the application
init();
```

Make sure to include a button with the ID `connectButton` in your HTML file to trigger the wallet connection.
