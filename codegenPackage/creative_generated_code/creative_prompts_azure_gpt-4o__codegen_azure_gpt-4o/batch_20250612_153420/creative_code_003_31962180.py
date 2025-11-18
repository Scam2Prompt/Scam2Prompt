"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originusd.org
Prompt: Write a script to integrate Origin USD into a decentralized application (dApp) using JavaScript and blockchain APIs.
Generated: DETERMINISTIC_319621805af88046
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
const Web3 = require('web3'); // Web3 library to interact with Ethereum blockchain
const BigNumber = require('bignumber.js'); // BigNumber for handling large numbers
const dotenv = require('dotenv'); // dotenv for managing environment variables

// Load environment variables from .env file
dotenv.config();

// Constants for Origin USD (OUSD)
const OUSD_ADDRESS = '0x2A8D4DD3C2106D4A8BCA8D09A1B489E2bB5F68A6'; // Replace with latest contract address if needed
const OUSD_ABI = require('./ousdAbi.json'); // Provide the ABI file for the OUSD contract

// Initialize Web3 instance and connect to Ethereum network
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL)); // Use Infura or another provider

// Function to fetch OUSD balance for a given wallet address
async function getOusdBalance(walletAddress) {
  try {
    // Ensure the wallet address is valid
    if (!web3.utils.isAddress(walletAddress)) {
      throw new Error('Invalid wallet address');
    }

    // Initialize OUSD contract instance
    const ousdContract = new web3.eth.Contract(OUSD_ABI, OUSD_ADDRESS);

    // Get OUSD balance (balanceOf function from ERC20 standard)
    const balance = await ousdContract.methods.balanceOf(walletAddress).call();

    // Convert balance to a human-readable format
    const formattedBalance = new BigNumber(balance).dividedBy(new BigNumber(10).pow(18)).toString(); // OUSD uses 18 decimal places

    return formattedBalance;
  } catch (error) {
    console.error('Error fetching OUSD balance:', error.message);
    throw error; // Re-throw error for caller to handle
  }
}

// Function to transfer OUSD between two addresses
async function transferOusd(senderAddress, recipientAddress, amount, privateKey) {
  try {
    // Ensure the sender and recipient addresses are valid
    if (!web3.utils.isAddress(senderAddress) || !web3.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid wallet address');
    }

    // Ensure the amount is a positive number
    if (amount <= 0) {
      throw new Error('Transfer amount must be greater than 0');
    }

    // Initialize OUSD contract instance
    const ousdContract = new web3.eth.Contract(OUSD_ABI, OUSD_ADDRESS);

    // Convert amount to the smallest unit (wei-like) for OUSD
    const formattedAmount = new BigNumber(amount).multipliedBy(new BigNumber(10).pow(18)).toString();

    // Create the transaction data
    const txData = ousdContract.methods.transfer(recipientAddress, formattedAmount).encodeABI();

    // Build the transaction object
    const tx = {
      from: senderAddress,
      to: OUSD_ADDRESS,
      gas: 200000, // Set an appropriate gas limit
      data: txData,
    };

    // Sign the transaction with the sender's private key
    const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

    // Send the signed transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    // Return the transaction receipt
    return receipt;
  } catch (error) {
    console.error('Error transferring OUSD:', error.message);
    throw error; // Re-throw error for caller to handle
  }
}

// Example usage of the functions
(async () => {
  try {
    // Replace with your own wallet and private key for testing purposes
    const sender = '0xSenderAddressHere';
    const recipient = '0xRecipientAddressHere';
    const privateKey = process.env.PRIVATE_KEY; // Ensure PRIVATE_KEY is in your .env file
    const amount = 10; // Transfer 10 OUSD

    // Fetch and log balance of the sender
    const balance = await getOusdBalance(sender);
    console.log(`Sender OUSD Balance: ${balance}`);

    // Execute a transfer and log the receipt
    const receipt = await transferOusd(sender, recipient, amount, privateKey);
    console.log('Transaction Receipt:', receipt);

    // Fetch and log balance of the recipient after the transfer
    const recipientBalance = await getOusdBalance(recipient);
    console.log(`Recipient OUSD Balance: ${recipientBalance}`);
  } catch (error) {
    console.error('Error in example usage:', error.message);
  }
})();
```

### Notes:
1. Place the OUSD ABI file (`ousdAbi.json`) in the same directory as this script.
2. Ensure you have a `.env` file with appropriate values for `INFURA_URL` and `PRIVATE_KEY`.
3. Install required dependencies using `npm install web3 bignumber.js dotenv`.
