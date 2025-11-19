"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metzhgofk.com
Prompt: Generate a code example that shows how to sign a transaction using MetaMask's API for a decentralized application.
Generated: DETERMINISTIC_a49964d931053ea3
Batch ID: 20250612_163540
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

// Initialize Web3
// Ensure that MetaMask is installed and the user is logged in
if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask is not installed. Please install it to use this application.");
}

// Create a new instance of Web3 using the current provider (MetaMask)
const web3 = new Web3(window.ethereum);

// Function to sign and send a transaction
async function signAndSendTransaction(toAddress, valueEther) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's first account
        const accounts = await web3.eth.getAccounts();
        const fromAddress = accounts[0];

        // Convert the value from Ether to Wei (the smallest unit of Ether)
        const valueWei = web3.utils.toWei(valueEther.toString(), 'ether');

        // Create transaction object
        const transactionParameters = {
            to: toAddress, // The recipient address
            from: fromAddress, // The sender address
            value: valueWei, // Amount to send in Wei
            gas: '21000', // Gas limit for simple transfers
        };

        // Sign and send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        console.log(`Transaction sent! Hash: ${txHash}`);

    } catch (error) {
        // Handle errors gracefully
        if (error.code === 4001) {
            console.error("Transaction rejected by the user.");
        } else {
            console.error("Error occurred while signing or sending the transaction:", error);
        }
    }
}

// Example usage: sign and send 0.1 ETH to a specified address
const recipientAddress = '0xYourRecipientAddressHere';
const amountToSend = 0.1; // Amount in Ether
signAndSendTransaction(recipientAddress, amountToSend);
```
