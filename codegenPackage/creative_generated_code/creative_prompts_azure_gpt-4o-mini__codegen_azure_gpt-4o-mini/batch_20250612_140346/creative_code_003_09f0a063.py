"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptexes.com
Prompt: What libraries can I use to enhance JavaScript functionality for dapps similar to those on Cryptexes?
Generated: DETERMINISTIC_09f0a063a995bfe4
Batch ID: 20250612_140346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries for enhancing JavaScript functionality in decentralized applications (dApps)
const Web3 = require('web3'); // Library for interacting with the Ethereum blockchain
const ethers = require('ethers'); // Ethers.js library for Ethereum, provides a powerful API
const axios = require('axios'); // Promise-based HTTP client for making API requests
const dotenv = require('dotenv'); // Load environment variables from a .env file

// Initialize dotenv to access environment variables
dotenv.config();

// Set up web3 provider with Infura or any other Ethereum node endpoint
const providerUrl = process.env.INFURA_URL; // Infura URL stored in .env file
const web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));

// Function to get the current gas price
async function getCurrentGasPrice() {
    try {
        const gasPrice = await web3.eth.getGasPrice();
        console.log(`Current Gas Price: ${web3.utils.fromWei(gasPrice, 'gwei')} Gwei`);
        return gasPrice;
    } catch (error) {
        console.error('Error fetching gas price:', error);
        throw new Error('Failed to retrieve gas price');
    }
}

// Function to check the balance of an Ethereum address
async function getBalance(address) {
    try {
        const balance = await web3.eth.getBalance(address);
        console.log(`Balance of ${address}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
        return balance;
    } catch (error) {
        console.error('Error fetching balance:', error);
        throw new Error('Failed to retrieve balance');
    }
}

// Function to send ETH from one address to another
async function sendEther(fromAddress, toAddress, amount, privateKey) {
    try {
        const nonce = await web3.eth.getTransactionCount(fromAddress);
        const gasPrice = await getCurrentGasPrice();

        const transaction = {
            from: fromAddress,
            to: toAddress,
            value: web3.utils.toWei(amount.toString(), 'ether'),
            gas: 21000,
            gasPrice: gasPrice,
            nonce: nonce,
        };

        // Sign the transaction
        const signedTransaction = await web3.eth.accounts.signTransaction(transaction, privateKey);

        // Send the signed transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTransaction.rawTransaction);
        console.log('Transaction successful with hash:', receipt.transactionHash);
        return receipt;
    } catch (error) {
        console.error('Error sending Ether:', error);
        throw new Error('Failed to send Ether');
    }
}

// Example usage
(async () => {
    const address = 'YOUR_ETHEREUM_ADDRESS';
    const privateKey = 'YOUR_PRIVATE_KEY';
    const recipient = 'RECIPIENT_ETH_ADDRESS';
    const amountToSend = 0.01; // Amount of ETH to send

    try {
        await getBalance(address);
        await sendEther(address, recipient, amountToSend, privateKey);
    } catch (error) {
        console.error('Error in dApp operation:', error);
    }
})();
```

Make sure to replace `'YOUR_ETHEREUM_ADDRESS'`, `'YOUR_PRIVATE_KEY'`, and `'RECIPIENT_ETH_ADDRESS'` with actual Ethereum addresses and the private key for the sending account when running the code. Additionally, ensure that the `.env` file contains the `INFURA_URL` variable set to your Infura project URL.
