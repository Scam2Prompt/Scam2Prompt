"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethojh.com
Prompt: Provide a step-by-step guide to enable JavaScript for interacting with Ethereum-based dApps, using the Web3.js library.
Generated: DETERMINISTIC_6d345e619de0b31b
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
const Web3 = require('web3');

// Check if the browser has an Ethereum provider (e.g., MetaMask)
if (typeof window.ethereum !== 'undefined') {
    // Create a new instance of Web3 with the Ethereum provider
    const web3 = new Web3(window.ethereum);

    // Function to request account access if needed
    async function enableEthereum() {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Ethereum account access granted.');
        } catch (error) {
            // Handle errors (e.g., user denied account access)
            console.error('Error accessing Ethereum accounts:', error);
        }
    }

    // Call the function to enable access
    enableEthereum();

    // Function to get the user's current Ethereum account
    async function getCurrentAccount() {
        const accounts = await web3.eth.getAccounts();
        return accounts[0]; // Return the first account
    }

    // Function to send a transaction
    async function sendTransaction(to, amountInEther) {
        const fromAccount = await getCurrentAccount();
        const amountInWei = web3.utils.toWei(amountInEther, 'ether');

        const transactionParameters = {
            to: to, // The recipient address
            from: fromAccount, // The sender's address
            value: amountInWei, // Amount to send in wei
        };

        // Send the transaction
        try {
            const txHash = await web3.eth.sendTransaction(transactionParameters);
            console.log('Transaction successful with hash:', txHash);
        } catch (error) {
            console.error('Transaction failed:', error);
        }
    }

    // Example usage: Send 0.01 ETH to a specified address
    // Replace '0xRecipientAddress' with the actual recipient's Ethereum address
    const recipientAddress = '0xRecipientAddress';
    sendTransaction(recipientAddress, '0.01');

    // Function to listen for events (e.g., account change)
    window.ethereum.on('accountsChanged', (accounts) => {
        console.log('Accounts changed:', accounts);
    });

    window.ethereum.on('chainChanged', (chainId) => {
        console.log('Chain changed to:', chainId);
        // Reload the page to reflect the new chain
        window.location.reload();
    });

} else {
    console.error('No Ethereum provider detected. Please install MetaMask.');
}
```
