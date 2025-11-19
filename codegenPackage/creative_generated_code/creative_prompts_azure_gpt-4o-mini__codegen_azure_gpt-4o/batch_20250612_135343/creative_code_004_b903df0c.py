"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyotamsoolin.github.io
Prompt: What features make MetaMask suitable for crypto gamers, and how can they utilize it for games like Axie Infinity?
Generated: DETERMINISTIC_b903df0c13f42b2c
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script demonstrates how crypto gamers can use MetaMask for games like Axie Infinity.
 * It includes features such as wallet setup, connecting to the Ethereum blockchain,
 * checking wallet balance, and signing transactions for in-game purchases.
 *
 * Prerequisites:
 * - MetaMask must be installed as a browser extension.
 * - Axie Infinity or similar game must support Ethereum-based transactions.
 */

// Import dependencies (in a real project, this would use npm or a bundler)
import Web3 from 'web3';

// Initialize Web3 instance using MetaMask's provider
const web3 = new Web3(window.ethereum);

/**
 * Function to check if MetaMask is installed and connected properly
 */
async function initializeMetaMask() {
  if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install MetaMask to use this feature.');
    return;
  }
  
  try {
    // Request account access
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected account:', accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error('Error connecting to MetaMask:', error.message);
  }
}

/**
 * Function to check wallet balance in Ether
 * @param {string} walletAddress - The user's Ethereum wallet address
 */
async function checkWalletBalance(walletAddress) {
  try {
    const balance = await web3.eth.getBalance(walletAddress);
    const formattedBalance = web3.utils.fromWei(balance, 'ether');
    console.log(`Wallet Balance: ${formattedBalance} ETH`);
    return formattedBalance;
  } catch (error) {
    console.error('Error fetching wallet balance:', error.message);
  }
}

/**
 * Function to sign and send a transaction for in-game purchases
 * @param {string} walletAddress - The user's Ethereum wallet address
 * @param {string} recipientAddress - The recipient address for the transaction (e.g., game wallet)
 * @param {string} amountInEther - The amount of Ether to send
 */
async function sendTransaction(walletAddress, recipientAddress, amountInEther) {
  try {
    // Convert Ether amount to Wei (smallest unit of Ether)
    const amountInWei = web3.utils.toWei(amountInEther, 'ether');
    
    // Create the transaction object
    const transaction = {
      from: walletAddress,
      to: recipientAddress,
      value: amountInWei,
      gas: 21000, // Standard gas limit for most transactions
    };

    // Send transaction using MetaMask
    const txHash = await web3.eth.sendTransaction(transaction);
    console.log('Transaction successful, hash:', txHash.transactionHash);
    return txHash.transactionHash;
  } catch (error) {
    console.error('Error sending transaction:', error.message);
  }
}

/**
 * Example usage of the above functions.
 * Replace `recipientAddress` and `amountInEther` with actual values for Axie Infinity or similar games.
 */
(async function startCryptoGaming() {
  const userWallet = await initializeMetaMask();
  if (!userWallet) return;

  // Check wallet balance
  await checkWalletBalance(userWallet);

  // Example recipient address and amount for Axie Infinity (replace with actual values)
  const recipientAddress = '0xRecipientAddressHere';
  const amountInEther = '0.05'; // Example purchase amount

  // Send a transaction for in-game purchases
  await sendTransaction(userWallet, recipientAddress, amountInEther);
})();
```
