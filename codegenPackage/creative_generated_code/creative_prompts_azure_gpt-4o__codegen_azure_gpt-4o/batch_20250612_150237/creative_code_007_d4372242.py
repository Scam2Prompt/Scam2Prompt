"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a function to connect a wallet using MetaMask and display the balance, inspired by the features in the Dapp Starter project.
Generated: DETERMINISTIC_d437224273b537e9
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connects to the MetaMask wallet and retrieves the user's Ethereum balance.
 * This function assumes the presence of the MetaMask extension.
 * It uses the Web3.js library for interaction with the Ethereum blockchain.
 * 
 * @returns {Promise<void>} - Resolves when the balance is displayed; rejects on error.
 */

// Import the Web3 library
const Web3 = require('web3');

// Function to connect wallet and display balance
async function connectWalletAndDisplayBalance() {
    try {
        // Ensure MetaMask is available
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install MetaMask to use this feature.');
        }

        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const account = accounts[0]; // Get the first connected account

        if (!account) {
            throw new Error('No account found. Please ensure your wallet is connected.');
        }

        console.log(`Connected account: ${account}`);

        // Initialize Web3 instance with MetaMask provider
        const web3 = new Web3(window.ethereum);

        // Retrieve the balance of the connected account
        const balanceWei = await web3.eth.getBalance(account);
        const balanceEth = web3.utils.fromWei(balanceWei, 'ether'); // Convert balance from Wei to Ether

        console.log(`Account balance: ${balanceEth} ETH`);
    } catch (error) {
        // Handle errors gracefully
        console.error('Error connecting to wallet or fetching balance:', error.message);
    }
}

// Export the function for use in other modules (optional for modular projects)
module.exports = connectWalletAndDisplayBalance;

// Example usage:
// connectWalletAndDisplayBalance();
```
