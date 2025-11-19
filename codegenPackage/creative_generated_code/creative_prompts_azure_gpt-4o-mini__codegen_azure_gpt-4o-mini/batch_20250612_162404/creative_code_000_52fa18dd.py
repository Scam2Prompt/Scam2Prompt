"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappback.firebaseapp.com
Prompt: How can I enable JavaScript to run a DappBack application effectively?
Generated: DETERMINISTIC_52fa18dd8f4ab4a7
Batch ID: 20250612_162404
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

// Check if Web3 is injected by the browser (e.g., MetaMask)
if (typeof window.ethereum !== 'undefined') {
    // Create a new instance of Web3 using the injected provider
    const web3 = new Web3(window.ethereum);

    // Request account access if needed
    async function enableEthereum() {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Ethereum account access granted');
        } catch (error) {
            console.error('User denied account access:', error);
            return;
        }
    }

    // Call the function to enable Ethereum
    enableEthereum();

    // Example function to get the current account's balance
    async function getBalance(account) {
        try {
            const balance = await web3.eth.getBalance(account);
            console.log(`Balance of account ${account}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
        } catch (error) {
            console.error('Error fetching balance:', error);
        }
    }

    // Listen for account changes and update balance accordingly
    window.ethereum.on('accountsChanged', async (accounts) => {
        console.log('Accounts changed:', accounts);
        if (accounts.length > 0) {
            await getBalance(accounts[0]);
        } else {
            console.log('Please connect to MetaMask.');
        }
    });

    // Get the current accounts on initialization
    window.ethereum.request({ method: 'eth_accounts' })
        .then(accounts => {
            if (accounts.length > 0) {
                console.log('Connected account:', accounts[0]);
                getBalance(accounts[0]);
            } else {
                console.log('Please connect to MetaMask.');
            }
        })
        .catch(error => {
            console.error('Error getting accounts:', error);
        });

} else {
    console.error('Please install MetaMask or another Ethereum-compatible browser extension.');
}
```
