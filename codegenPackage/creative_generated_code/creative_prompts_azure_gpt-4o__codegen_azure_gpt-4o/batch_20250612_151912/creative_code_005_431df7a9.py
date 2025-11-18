"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orchidprotocols.com
Prompt: Write a JavaScript function to fund an Orchid account with ERC-20 tokens and send nanopayments for decentralized services.
Generated: DETERMINISTIC_431df7a9ffb84844
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
const Web3 = require('web3'); // Web3 library to interact with Ethereum blockchain
const abi = require('./erc20Abi.json'); // Import ERC-20 Token ABI

// Initialize Web3 instance (ensure `process.env.INFURA_URL` is configured properly)
const web3 = new Web3(process.env.INFURA_URL);

// Configure account details and contract address
const ORCHID_ACCOUNT_ADDRESS = process.env.ORCHID_ACCOUNT_ADDRESS; // Orchid account address
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key of the sender's wallet
const TOKEN_CONTRACT_ADDRESS = process.env.TOKEN_CONTRACT_ADDRESS; // ERC-20 Token contract address

/**
 * Fund Orchid account with ERC-20 tokens
 * @param {string} recipientAddress - The address of the Orchid account
 * @param {number} amount - The number of tokens to transfer (in smallest unit, e.g., Wei for ETH-based tokens)
 */
async function fundOrchidAccount(recipientAddress, amount) {
  try {
    // Validate input
    if (!web3.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid recipient address.');
    }
    if (amount <= 0) {
      throw new Error('Amount must be greater than zero.');
    }

    // Create contract instance for the ERC-20 token
    const tokenContract = new web3.eth.Contract(abi, TOKEN_CONTRACT_ADDRESS);

    // Get the sender's wallet address
    const senderAddress = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY).address;

    // Estimate gas for the transaction
    const gasEstimate = await tokenContract.methods.transfer(recipientAddress, amount).estimateGas({
      from: senderAddress,
    });

    // Create the transaction
    const tx = {
      from: senderAddress,
      to: TOKEN_CONTRACT_ADDRESS,
      gas: gasEstimate,
      data: tokenContract.methods.transfer(recipientAddress, amount).encodeABI(),
    };

    // Sign the transaction
    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

    // Send the transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log('Transaction successful:', receipt.transactionHash);
  } catch (error) {
    console.error('Failed to fund Orchid account:', error.message);
  }
}

/**
 * Send nanopayments for decentralized services
 * @param {string} recipientAddress - The address of the service provider
 * @param {number} amount - The nanopayment amount (smallest unit, e.g., Wei for ETH-based tokens)
 */
async function sendNanopayment(recipientAddress, amount) {
  try {
    // Validate input
    if (!web3.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid recipient address.');
    }
    if (amount <= 0) {
      throw new Error('Amount must be greater than zero.');
    }

    // Get the sender's wallet address
    const senderAddress = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY).address;

    // Create the transaction
    const tx = {
      from: senderAddress,
      to: recipientAddress,
      value: web3.utils.toWei(amount.toString(), 'gwei'), // Convert nanopayment to Wei
      gas: 21000, // Standard gas limit for ETH transfers
    };

    // Sign the transaction
    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

    // Send the transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log('Nanopayment successful:', receipt.transactionHash);
  } catch (error) {
    console.error('Failed to send nanopayment:', error.message);
  }
}

// Export the functions for external usage
module.exports = {
  fundOrchidAccount,
  sendNanopayment,
};
```
