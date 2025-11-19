"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://982e0a97.web3-site.pages.dev
Prompt: What are the best practices for using Web3 libraries in a decentralized application?
Generated: DETERMINISTIC_1270085387aaac7c
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Best practices for using Web3 libraries in a decentralized application (DApp).
 * This example demonstrates connecting to an Ethereum blockchain, querying an account balance, 
 * and sending a transaction using the Web3.js library.
 */

// Import Web3.js
const Web3 = require('web3');

// Use environment variables to store sensitive information
require('dotenv').config();
const INFURA_URL = process.env.INFURA_URL; // Infura endpoint URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key of the sender
const RECEIVER_ADDRESS = process.env.RECEIVER_ADDRESS; // Receiver's wallet address

/**
 * Initialize Web3 instance connected to the Ethereum network.
 * Always prefer providers like Infura or Alchemy for production use.
 */
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

/**
 * Function to check the Ether balance of an account.
 * @param {string} address - Ethereum wallet address.
 * @returns {Promise<string>} - Returns the balance in Ether.
 */
async function getBalance(address) {
  try {
    // Query account balance (in Wei)
    const balanceWei = await web3.eth.getBalance(address);

    // Convert Wei to Ether
    return web3.utils.fromWei(balanceWei, 'ether');
  } catch (error) {
    console.error('Error fetching balance:', error.message);
    throw new Error('Failed to fetch account balance.');
  }
}

/**
 * Function to send a transaction.
 * @param {string} senderPrivateKey - Private key of the sender.
 * @param {string} receiverAddress - Ethereum wallet address of the receiver.
 * @param {string} amountEther - Amount to send (in Ether).
 * @returns {Promise<string>} - Returns the transaction hash.
 */
async function sendTransaction(senderPrivateKey, receiverAddress, amountEther) {
  try {
    // Get sender's account address from the private key
    const senderAccount = web3.eth.accounts.privateKeyToAccount(senderPrivateKey);
    const senderAddress = senderAccount.address;

    // Get the nonce for the sender's account
    const nonce = await web3.eth.getTransactionCount(senderAddress, 'latest');

    // Convert Ether to Wei
    const amountWei = web3.utils.toWei(amountEther, 'ether');

    // Create the transaction object
    const tx = {
      from: senderAddress,
      to: receiverAddress,
      value: amountWei,
      gas: 21000, // Base gas limit for standard transactions
      nonce: nonce,
    };

    // Sign the transaction using the sender's private key
    const signedTx = await web3.eth.accounts.signTransaction(tx, senderPrivateKey);

    // Send the signed transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    return receipt.transactionHash;
  } catch (error) {
    console.error('Error sending transaction:', error.message);
    throw new Error('Failed to send the transaction.');
  }
}

// Example usage
(async () => {
  try {
    const senderAddress = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY).address;

    // 1. Query the balance of the sender's account
    const senderBalance = await getBalance(senderAddress);
    console.log(`Sender's balance: ${senderBalance} ETH`);

    // 2. Send 0.01 ETH to the receiver
    const transactionHash = await sendTransaction(PRIVATE_KEY, RECEIVER_ADDRESS, '0.01');
    console.log(`Transaction successful! Hash: ${transactionHash}`);

    // 3. Query the updated balance of the sender's account
    const updatedBalance = await getBalance(senderAddress);
    console.log(`Updated Sender's balance: ${updatedBalance} ETH`);
  } catch (error) {
    console.error('Error in DApp operations:', error.message);
  }
})();

/**
 * Notes:
 * 1. Ensure private keys and sensitive information are stored securely (e.g., .env file).
 * 2. Always validate inputs, such as wallet addresses and amounts, before making calls.
 * 3. Use HTTPS endpoints for production to ensure secure communication with the blockchain.
 * 4. Handle errors gracefully to prevent disruption in the DApp.
 */
```
