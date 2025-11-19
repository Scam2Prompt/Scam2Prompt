"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-puffer.com
Prompt: Provide an example of how to use the MetaMask API for securely managing user transactions in a decentralized application.
Generated: DETERMINISTIC_5b5b14ff47b9ef29
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// This function initializes the Web3 instance and connects to MetaMask
async function initMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Create a new instance of Web3
        const web3 = new Web3(window.ethereum);

        // Request account access if needed
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('MetaMask is connected');
            return web3;
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
            throw new Error('Failed to connect to MetaMask');
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this application.');
        throw new Error('MetaMask not detected');
    }
}

// This function sends a transaction using MetaMask
async function sendTransaction(web3, toAddress, amount) {
    // Get the current accounts of the connected wallet
    const accounts = await web3.eth.getAccounts();
    const fromAddress = accounts[0];

    // Create the transaction object
    const transactionParams = {
        from: fromAddress,
        to: toAddress,
        value: web3.utils.toWei(amount, 'ether'), // Convert amount to Wei
        gas: '21000', // Gas limit for standard transaction
    };

    // Send the transaction
    try {
        const txHash = await web3.eth.sendTransaction(transactionParams);
        console.log('Transaction successful with hash:', txHash.transactionHash);
        return txHash.transactionHash;
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Transaction could not be completed');
    }
}

// Main function to execute the example
async function main() {
    try {
        const web3 = await initMetaMask();
        const recipientAddress = '0xRecipientAddressHere'; // Replace with the actual recipient address
        const amountToSend = '0.01'; // Amount in Ether

        // Send the transaction
        const txHash = await sendTransaction(web3, recipientAddress, amountToSend);
        console.log('Transaction hash:', txHash);
    } catch (error) {
        console.error('An error occurred:', error);
    }
}

// Execute the main function
main();
```

Make sure to replace `'0xRecipientAddressHere'` with the actual Ethereum address you intend to send Ether to.
