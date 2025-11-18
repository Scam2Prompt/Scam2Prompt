"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-spark.com
Prompt: Write code using the MetaMask SDK to connect a dapp to a user's MetaMask wallet and retrieve their Ethereum account balance.
Generated: DETERMINISTIC_edbfb269231e2af9
Batch ID: 20250612_150658
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

// Define async function to connect to MetaMask and retrieve account balance
async function connectAndFetchBalance() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this dApp.');
        return;
    }

    // Create a new instance of Web3 with the provider from MetaMask
    const web3 = new Web3(window.ethereum);

    try {
        // Request account access from the user
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's accounts (Ethereum addresses)
        const accounts = await web3.eth.getAccounts();

        // Check if accounts were retrieved
        if (accounts.length === 0) {
            console.error('No accounts found. Make sure you are logged into MetaMask.');
            return;
        }

        // Get the first account
        const userAccount = accounts[0];

        // Fetch the balance of the user's account in Wei (smallest unit of Ether)
        const balanceWei = await web3.eth.getBalance(userAccount);
        
        // Convert balance from Wei to Ether
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');

        // Log the account and balance
        console.log(`Account: ${userAccount}`);
        console.log(`Balance: ${balanceEther} ETH`);

    } catch (error) {
        // Handle any errors that may occur
        console.error('Error connecting to MetaMask:', error.message);
    }
}

// Call the function to connect and fetch balance
connectAndFetchBalance();
```
