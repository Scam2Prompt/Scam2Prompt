"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: Provide an example of how to check the balance of an account using MetaMask in a DApp, based on the information from Wormhole.
Generated: DETERMINISTIC_10a5198d9ebc1ad4
Batch ID: 20250612_162502
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
import { ethers } from 'ethers';

// Function to check account balance using MetaMask
async function checkAccountBalance() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install it to use this DApp.');
        }

        // Create a new Web3 instance
        const web3 = new Web3(window.ethereum);

        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the accounts from MetaMask
        const accounts = await web3.eth.getAccounts();

        // Check if any accounts are available
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please ensure you have an account created in MetaMask.');
        }

        // Get the balance of the first account
        const account = accounts[0];
        const balanceWei = await web3.eth.getBalance(account);

        // Convert balance from Wei to Ether
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');

        // Log the balance to the console
        console.log(`Account: ${account}`);
        console.log(`Balance: ${balanceEther} ETH`);

        // Return the balance for further use if needed
        return {
            account,
            balance: balanceEther
        };

    } catch (error) {
        // Handle any errors
        console.error('Error checking account balance:', error.message);
    }
}

// Call the function to check the balance
checkAccountBalance();
```
