"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io
Prompt: Write a code snippet that demonstrates how to connect a dapp to MetaMask for Ethereum transactions.
Generated: DETERMINISTIC_bac5d0530c35ef92
Batch ID: 20250612_135046
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

// Function to initialize Web3 and connect to MetaMask
async function connectToMetaMask() {
    try {
        // Check if MetaMask is installed
        if (window.ethereum) {
            // Create a new instance of Web3 with the provider from MetaMask
            const web3 = new Web3(window.ethereum);

            // Request account access from the user
            await window.ethereum.request({ method: 'eth_requestAccounts' });

            // Get the user's accounts
            const accounts = await web3.eth.getAccounts();

            // Log the connected account
            console.log('Connected account:', accounts[0]);

            return web3; // Return the web3 instance for further use
        } else {
            throw new Error('MetaMask is not installed. Please install it to use this dApp.');
        }
    } catch (error) {
        // Handle errors during the connection process
        console.error('Error connecting to MetaMask:', error.message);
    }
}

// Function to send a transaction using the connected account
async function sendTransaction(web3, to, value) {
    try {
        const accounts = await web3.eth.getAccounts();

        // Define transaction parameters
        const transactionParameters = {
            to: to, // Recipient address
            value: web3.utils.toHex(web3.utils.toWei(value, 'ether')), // Amount to send in Wei
            from: accounts[0], // The account sending the transaction
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(transactionParameters);

        // Log the transaction hash
        console.log('Transaction successful with hash:', txHash);
    } catch (error) {
        // Handle errors during the transaction process
        console.error('Error sending transaction:', error.message);
    }
}

// Main function to execute the dApp logic
async function main() {
    const web3 = await connectToMetaMask();
    if (web3) {
        // Example usage: Send 0.01 Ether to a specific address
        const recipientAddress = '0xYourRecipientAddressHere'; // Replace with the recipient address
        const etherAmount = '0.01'; // Amount in Ether to send

        await sendTransaction(web3, recipientAddress, etherAmount);
    }
}

// Execute the main function
main();
```
