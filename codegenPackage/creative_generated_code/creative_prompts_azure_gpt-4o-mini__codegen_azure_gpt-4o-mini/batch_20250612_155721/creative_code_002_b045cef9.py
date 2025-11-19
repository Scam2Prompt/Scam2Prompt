"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mateimsklogi-usa.godaddysites.com
Prompt: Generate a code snippet that demonstrates how to connect a web application to MetaMask for Ethereum transactions.
Generated: DETERMINISTIC_b045cef9775a3230
Batch ID: 20250612_155721
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

// Function to connect to MetaMask and get the user's Ethereum account
async function connectToMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Create a new instance of Web3 using the provider from MetaMask
        const web3 = new Web3(window.ethereum);
        
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            // Get the user's Ethereum accounts
            const accounts = await web3.eth.getAccounts();
            console.log('Connected account:', accounts[0]);
            return { web3, accounts };
        } catch (error) {
            // Handle user rejection or other errors
            console.error('User denied account access or there was an error:', error);
            throw new Error('Could not connect to MetaMask. Please try again.');
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this feature.');
        throw new Error('MetaMask is not installed. Please install it to use this feature.');
    }
}

// Function to send a transaction using MetaMask
async function sendTransaction(web3, fromAddress, toAddress, amount) {
    try {
        // Convert amount to Wei (smallest unit of Ether)
        const valueInWei = web3.utils.toWei(amount.toString(), 'ether');
        
        // Create the transaction object
        const transactionParameters = {
            to: toAddress, // Required except during contract publications.
            from: fromAddress, // Must match user's active address.
            value: valueInWei, // Only required to send ether to the recipient from the sender.
            gas: '2000000', // Optional, but recommended.
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(transactionParameters);
        console.log('Transaction successful with hash:', txHash.transactionHash);
        return txHash;
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Transaction failed. Please check the console for details.');
    }
}

// Example usage
(async () => {
    try {
        const { web3, accounts } = await connectToMetaMask();
        const fromAddress = accounts[0];
        const toAddress = '0xRecipientAddressHere'; // Replace with actual recipient address
        const amount = 0.01; // Amount in Ether to send
        
        // Send transaction
        await sendTransaction(web3, fromAddress, toAddress, amount);
    } catch (error) {
        // Handle any errors that occurred during connection or transaction
        console.error('Error in example usage:', error);
    }
})();
```
