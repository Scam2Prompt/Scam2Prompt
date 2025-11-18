"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-metis.net
Prompt: Write a script to retrieve and display account balances and transaction history using MetaMask's Web3 Services API.
Generated: DETERMINISTIC_5e93dcdf2eb6f51a
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const Web3 = require('web3');

// Initialize Web3 instance connected to MetaMask's provider
if (typeof window.ethereum !== 'undefined') {
    var web3 = new Web3(window.ethereum);
} else {
    console.error('MetaMask is not installed. Please install it to use this script.');
    throw new Error('MetaMask is required');
}

// Async function to retrieve account balance and transaction history
(async () => {
    try {
        // Request account access via MetaMask
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user accounts
        const accounts = await web3.eth.getAccounts();

        if (accounts.length === 0) {
            console.error('No accounts found. Please ensure MetaMask is connected.');
            return;
        }

        const account = accounts[0]; // Using the first account
        console.log(`Connected account: ${account}`);

        // Fetch and display the account balance
        const balanceWei = await web3.eth.getBalance(account);
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
        console.log(`Account balance: ${balanceEther} ETH`);

        // Fetch and display the transaction history
        // Note: Web3.js does not support fetching transaction history directly. 
        // You need to use a third-party service like Etherscan API or Alchemy for this purpose.
        console.log('Transaction history cannot be fetched with Web3.js alone.');
        console.log('Consider integrating a third-party API for transaction history.');

    } catch (error) {
        // Handle potential errors from MetaMask or Web3.js
        console.error('An error occurred:', error.message);
    }
})();
```
