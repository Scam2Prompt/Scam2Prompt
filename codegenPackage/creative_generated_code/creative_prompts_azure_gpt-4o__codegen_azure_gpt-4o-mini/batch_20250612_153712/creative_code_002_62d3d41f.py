"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmsetumsklogi.webflow.io
Prompt: Provide a step-by-step guide in code to programmatically check the balance of an Ethereum wallet using the Metamask extension and the Web3.js library.
Generated: DETERMINISTIC_62d3d41f9502060c
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
import Web3 from 'web3';

// Function to check the balance of an Ethereum wallet
async function checkWalletBalance() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install it to use this feature.');
        }

        // Create a Web3 instance and set the provider to MetaMask
        const web3 = new Web3(window.ethereum);

        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's accounts
        const accounts = await web3.eth.getAccounts();

        // Check if accounts are available
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please ensure MetaMask is unlocked and has an account.');
        }

        // Get the first account (default account)
        const account = accounts[0];

        // Fetch the balance of the selected account
        const balanceWei = await web3.eth.getBalance(account);

        // Convert the balance from Wei to Ether
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');

        // Log the balance to the console
        console.log(`The balance of account ${account} is: ${balanceEther} ETH`);
    } catch (error) {
        // Handle errors and log them
        console.error('An error occurred:', error.message);
    }
}

// Call the function to check wallet balance
checkWalletBalance();
```

Make sure to include this code in an environment where MetaMask is available, such as a browser-based application.
