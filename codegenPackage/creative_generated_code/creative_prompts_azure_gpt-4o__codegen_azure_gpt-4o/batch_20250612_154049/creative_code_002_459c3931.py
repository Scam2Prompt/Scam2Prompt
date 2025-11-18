"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://horizondapp.com
Prompt: Generate code to enable JavaScript-based functionality for a web application that interacts with blockchain networks, similar to CoinHorizon.
Generated: DETERMINISTIC_459c39314954d5f6
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: blockchainInteraction.js

// Description: This script provides functionality to interact with blockchain networks.
// It includes methods to connect to a blockchain network, retrieve account information,
// send transactions, and fetch blockchain data.
// Dependencies: Web3.js library

// Import Web3.js for blockchain interaction
const Web3 = require('web3');

// Ensure the script handles runtime errors gracefully
try {
  // Initialize web3 instance
  let web3;

  /**
   * Connects to a blockchain network.
   * @param {string} providerURL - The URL of the JSON-RPC provider.
   */
  const connectToBlockchain = async (providerURL) => {
    try {
      // Create a Web3 instance with the given provider URL
      web3 = new Web3(new Web3.providers.HttpProvider(providerURL));

      // Check if the connection is established
      const isConnected = await web3.eth.net.isListening();
      console.log(`Connected to blockchain network: ${isConnected}`);
    } catch (error) {
      console.error("Failed to connect to the blockchain network:", error.message);
    }
  };

  /**
   * Retrieves the account balance for a given wallet address.
   * @param {string} walletAddress - The wallet address.
   * @returns {Promise<string>} - The account balance in Ether.
   */
  const getAccountBalance = async (walletAddress) => {
    try {
      // Ensure a valid Web3 instance exists
      if (!web3) throw new Error("Web3 is not initialized. Call connectToBlockchain first.");

      // Retrieve balance in Wei and convert to Ether
      const balanceWei = await web3.eth.getBalance(walletAddress);
      const balanceEther = web3.utils.fromWei(balanceWei, "ether");
      return balanceEther;
    } catch (error) {
      console.error("Failed to retrieve account balance:", error.message);
      throw error; // Rethrow error for the caller to handle
    }
  };

  /**
   * Sends a transaction from one wallet to another.
   * @param {string} from - The sender's address.
   * @param {string} to - The recipient's address.
   * @param {string} amount - The amount to send in Ether.
   * @param {string} privateKey - The sender's private key.
   * @returns {Promise<string>} - The transaction hash.
   */
  const sendTransaction = async (from, to, amount, privateKey) => {
    try {
      // Ensure a valid Web3 instance exists
      if (!web3) throw new Error("Web3 is not initialized. Call connectToBlockchain first.");

      // Convert Ether amount to Wei
      const amountWei = web3.utils.toWei(amount.toString(), "ether");

      // Create a transaction object
      const tx = {
        from,
        to,
        value: amountWei,
        gas: 21000, // Default gas for simple Ether transfers
      };

      // Sign the transaction
      const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

      // Send the signed transaction
      const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
      console.log("Transaction sent successfully:", receipt.transactionHash);
      return receipt.transactionHash;
    } catch (error) {
      console.error("Failed to send transaction:", error.message);
      throw error; // Rethrow error for the caller to handle
    }
  };

  /**
   * Fetches the latest block information from the blockchain.
   * @returns {Promise<object>} - The latest block object.
   */
  const getLatestBlock = async () => {
    try {
      // Ensure a valid Web3 instance exists
      if (!web3) throw new Error("Web3 is not initialized. Call connectToBlockchain first.");

      // Retrieve the latest block
      const latestBlock = await web3.eth.getBlock("latest");
      return latestBlock;
    } catch (error) {
      console.error("Failed to fetch the latest block:", error.message);
      throw error; // Rethrow error for the caller to handle
    }
  };

  // Export the functions for use in other parts of the application
  module.exports = {
    connectToBlockchain,
    getAccountBalance,
    sendTransaction,
    getLatestBlock,
  };
} catch (error) {
  console.error("Unexpected error occurred:", error.message);
  process.exit(1); // Exit the process in case of a fatal error
}
```
