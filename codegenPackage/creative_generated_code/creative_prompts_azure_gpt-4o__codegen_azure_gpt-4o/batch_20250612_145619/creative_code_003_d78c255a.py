"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imetobkbn.com
Prompt: Write a script to connect a web application to the Ethereum blockchain using Web3.js.
Generated: DETERMINISTIC_d78c255aee81e442
Batch ID: 20250612_145619
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
const Web3 = require('web3');

// Define a function to initialize and connect to the Ethereum blockchain
async function connectToEthereum() {
    try {
        // Check if Web3 is injected by a browser wallet (e.g., MetaMask)
        if (typeof window !== 'undefined' && window.ethereum) {
            // Use the browser's provider (e.g., MetaMask)
            const web3 = new Web3(window.ethereum);

            // Request account access from the user
            await window.ethereum.request({ method: 'eth_requestAccounts' });

            console.log('Connected to Ethereum via MetaMask');
            return web3;
        } 
        // Fallback to a local or remote node provider (e.g., Infura)
        else {
            // Replace with your Infura/WebSocket provider URL
            const providerUrl = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID';
            const web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));

            console.log('Connected to Ethereum via Infura');
            return web3;
        }
    } catch (error) {
        // Handle errors (e.g., user denied access, network issues)
        console.error('Failed to connect to Ethereum:', error.message);
        throw new Error('Unable to connect to Ethereum blockchain. See console for details.');
    }
}

// Example usage: Fetch and log the connected account's address
async function getAccountInfo() {
    try {
        const web3 = await connectToEthereum();

        // Fetch accounts accessible by the wallet or provider
        const accounts = await web3.eth.getAccounts();

        if (accounts.length === 0) {
            console.log('No accounts found. Please check your wallet connection.');
        } else {
            console.log('Connected account:', accounts[0]);
        }
    } catch (error) {
        console.error('Error fetching account info:', error.message);
    }
}

// Trigger the connection and account fetching process
getAccountInfo();
```
