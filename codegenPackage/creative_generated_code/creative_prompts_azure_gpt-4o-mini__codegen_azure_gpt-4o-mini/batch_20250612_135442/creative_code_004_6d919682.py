"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://send-ethereum.webflow.io
Prompt: Explain how to implement error handling for sending ETH transactions using MetaMask.
Generated: DETERMINISTIC_6d91968211236aa5
Batch ID: 20250612_135442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';

// Function to send ETH using MetaMask
async function sendETH(recipient, amount) {
    // Validate the recipient address
    if (!Web3.utils.isAddress(recipient)) {
        throw new Error('Invalid recipient address');
    }

    // Convert amount to Wei
    const amountInWei = Web3.utils.toWei(amount.toString(), 'ether');

    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        throw new Error('MetaMask is not installed. Please install it to use this feature.');
    }

    // Create a new instance of Web3 using MetaMask's provider
    const web3 = new Web3(window.ethereum);
    
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the current user's account address
        const accounts = await web3.eth.getAccounts();
        const sender = accounts[0];

        // Prepare the transaction object
        const transactionParameters = {
            to: recipient, // Recipient address
            from: sender, // Sender address
            value: amountInWei, // Amount in Wei
            gas: '21000', // Gas limit
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(transactionParameters);

        // Log the transaction hash
        console.log('Transaction successful with hash:', txHash.transactionHash);
        return txHash.transactionHash; // Return the transaction hash for reference
    } catch (error) {
        // Handle specific errors
        if (error.code === 4001) { // User rejected the request
            console.error('Transaction rejected by the user.');
        } else {
            console.error('Transaction failed:', error.message);
        }
        throw new Error('Transaction failed. Please try again later.');
    }
}

// Example usage
// (Make sure to call sendETH within an async function or handle the promise)
(async () => {
    try {
        const recipientAddress = '0xRecipientAddressHere'; // Replace with actual recipient
        const amountToSend = 0.01; // Amount in ETH
        await sendETH(recipientAddress, amountToSend);
    } catch (error) {
        console.error('Error sending ETH:', error.message);
    }
})();
```
