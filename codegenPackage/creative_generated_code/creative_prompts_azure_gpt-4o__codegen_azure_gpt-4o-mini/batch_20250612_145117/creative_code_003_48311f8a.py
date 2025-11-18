"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://detto.finance
Prompt: Provide a code example for detecting wallet connection status in a DeFi app using Ethers.js, similar to Detto Finance's "Connect Wallet" feature.
Generated: DETERMINISTIC_48311f8a6daea3f2
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import { ethers } from 'ethers';

// Define a function to detect wallet connection status
async function detectWalletConnection() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this application.');
        return false;
    }

    // Create a provider using ethers.js
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    try {
        // Request account access if needed
        await provider.send("eth_requestAccounts", []);
        
        // Get the list of accounts
        const accounts = await provider.listAccounts();

        // Check if any accounts are connected
        if (accounts.length > 0) {
            console.log('Wallet is connected:', accounts[0]);
            return true;
        } else {
            console.log('No wallet connected');
            return false;
        }
    } catch (error) {
        // Handle errors (console log and return false)
        console.error('Error detecting wallet connection:', error);
        return false;
    }
}

// Example usage
async function init() {
    const isConnected = await detectWalletConnection();
    if (isConnected) {
        // Proceed with the application logic for connected wallet
    } else {
        // Prompt user to connect their wallet
    }
}

// Call the init function when the script is run
init();
```
