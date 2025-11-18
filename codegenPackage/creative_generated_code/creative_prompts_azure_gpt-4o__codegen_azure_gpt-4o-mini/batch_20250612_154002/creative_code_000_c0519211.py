"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.name
Prompt: Write a script using Web3.js to interact with a smart contract that facilitates USDC transfers on the Ethereum blockchain.
Generated: DETERMINISTIC_c051921114c792b5
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const { abi } = require('./USDC.json'); // ABI of the USDC contract
require('dotenv').config(); // For loading environment variables

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Define contract address (USDC contract on Ethereum mainnet)
const contractAddress = '0xA0b86991c6218b36c1d19d4a2e9Eb0Ce3606EB48'; // USDC Address

// Create contract instance
const usdcContract = new web3.eth.Contract(abi, contractAddress);

/**
 * Function to transfer USDC tokens
 * @param {string} from - Address of the sender
 * @param {string} to - Address of the recipient
 * @param {number} amount - Amount of USDC to transfer (in smallest unit)
 */
async function transferUSDC(from, to, amount) {
    try {
        // Check if accounts are unlocked
        const balance = await web3.eth.getBalance(from);
        if (balance <= 0) {
            throw new Error('Insufficient balance for transactions');
        }

        // Create a transaction object
        const transaction = {
            from: from, // Sender's address
            to: contractAddress, // USDC contract address
            data: usdcContract.methods.transfer(to, amount).encodeABI(), // Encode method call
            gas: 2000000 // Set gas limit
        };

        // Sign the transaction
        const signedTransaction = await web3.eth.accounts.signTransaction(transaction, process.env.PRIVATE_KEY);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTransaction.rawTransaction);
        
        console.log('Transaction successful with hash:', receipt.transactionHash);
    } catch (error) {
        console.error('Error transferring USDC:', error.message);
    }
}

// Example usage
const fromAddress = process.env.SENDER_ADDRESS; // Sender's address from environment
const toAddress = '0xRecipientAddress'; // Replace with actual recipient address
const amountToSend = web3.utils.toWei('10', 'mwei'); // Convert 10 USDC to smallest unit

// Call the transfer function
transferUSDC(fromAddress, toAddress, amountToSend);
```

**Note**: Make sure to create a `.env` file in the same directory with the following variables:
```
INFURA_URL=your_infura_url
PRIVATE_KEY=your_private_key
SENDER_ADDRESS=your_sender_address
```
