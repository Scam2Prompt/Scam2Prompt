"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethojh.com
Prompt: Generate code to enable JavaScript functionality for a website that interacts with Ethereum wallets, ensuring compatibility with MetaMask.
Generated: DETERMINISTIC_09567c710004d0bd
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Enable strict mode for better error checking
'use strict';

// Check if MetaMask is installed and connected
async function checkMetaMask() {
    if (typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask) {
        console.log('MetaMask is installed!');
        return true;
    } else {
        console.error('MetaMask is not installed. Please install it to interact with the Ethereum blockchain.');
        return false;
    }
}

// Request account access from MetaMask
async function requestAccountAccess() {
    try {
        // Requesting MetaMask to enable accounts
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0]; // Return the first account
    } catch (error) {
        console.error('User denied account access or there was an error:', error.message);
        throw new Error('Failed to connect to MetaMask');
    }
}

// Get the current connected account
async function getConnectedAccount() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        if (accounts.length === 0) {
            console.warn('No accounts connected to MetaMask.');
            return null;
        }
        console.log('Currently connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Error fetching connected accounts:', error.message);
        throw new Error('Failed to fetch connected accounts');
    }
}

// Send a transaction
async function sendTransaction(toAddress, amountInEther) {
    try {
        const fromAddress = await getConnectedAccount();
        if (!fromAddress) {
            throw new Error('No connected account found.');
        }

        const transactionParams = {
            from: fromAddress,
            to: toAddress,
            value: window.ethereum.utils.toHex(window.ethereum.utils.toWei(amountInEther, 'ether')), // Convert Ether to Wei
        };

        const txHash = await window.ethereum.request({ method: 'eth_sendTransaction', params: [transactionParams] });
        console.log('Transaction sent with hash:', txHash);
        return txHash;
    } catch (error) {
        console.error('Error sending transaction:', error.message);
        throw new Error('Transaction failed');
    }
}

// Listen for account changes
function listenForAccountChanges(onAccountChangedCallback) {
    if (window.ethereum) {
        window.ethereum.on('accountsChanged', (accounts) => {
            console.log('Accounts changed:', accounts);
            onAccountChangedCallback(accounts);
        });
    } else {
        console.warn('MetaMask is not installed. Cannot listen for account changes.');
    }
}

// Example initialization for MetaMask interaction
async function initMetaMask() {
    if (await checkMetaMask()) {
        const account = await requestAccountAccess();
        console.log('MetaMask initialized with account:', account);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initMetaMask();

    // Example: Listen for account changes and log to the console
    listenForAccountChanges((accounts) => {
        if (accounts.length > 0) {
            console.log('New connected account:', accounts[0]);
        } else {
            console.warn('No accounts connected.');
        }
    });
});
```
