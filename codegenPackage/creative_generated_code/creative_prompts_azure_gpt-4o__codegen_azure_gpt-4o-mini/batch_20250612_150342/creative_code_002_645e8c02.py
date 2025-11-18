"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-chrome.github.io
Prompt: Provide a code example for integrating the MetaMask Chrome Extension into a dApp to request wallet permissions.
Generated: DETERMINISTIC_645e8c0213d57c64
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the required libraries
// Ensure you have web3.js installed: npm install web3
import Web3 from 'web3';

// Creating a function to initialize MetaMask integration
async function initMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this dApp.');
        return;
    }

    // Create a new instance of Web3 with the MetaMask provider
    const web3 = new Web3(window.ethereum);

    try {
        // Request account access from the user
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Log the connected account
        console.log('Connected account:', accounts[0]);

        // You can now use web3 to interact with the Ethereum network
        // For this example, we'll get the balance of the connected account
        const balance = await web3.eth.getBalance(accounts[0]);
        console.log('Account Balance:', web3.utils.fromWei(balance, 'ether'), 'ETH');

        // Add any additional dApp functionality here...

    } catch (error) {
        // Handle errors related to account access
        if (error.code === 4001) {
            console.error('User denied account access.');
        } else {
            console.error('An error occurred while requesting account access:', error);
        }
    }
}

// Call the function to initialize MetaMask integration
initMetaMask();
```
