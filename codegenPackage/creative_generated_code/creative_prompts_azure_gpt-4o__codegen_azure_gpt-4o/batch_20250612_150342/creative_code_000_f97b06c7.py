"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby-io-git-feat-app-debanker.vercel.app
Prompt: Write JavaScript code to integrate Rabby Wallet into a web application for managing cryptocurrency transactions.
Generated: DETERMINISTIC_f97b06c7907c4a52
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';

/**
 * Initializes Rabby Wallet integration.
 * This function checks if Rabby Wallet is installed and connects to it.
 * @returns {Promise<object>} Returns the provider and signer objects.
 */
async function initializeRabbyWallet() {
  // Ensure Rabby Wallet is installed
  if (!window.ethereum || !window.ethereum.isRabby) {
    throw new Error('Rabby Wallet is not installed. Please install Rabby Wallet to continue.');
  }

  try {
    // Request account access
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Create a new provider using ethers.js
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer (used for sending transactions)
    const signer = provider.getSigner();

    console.log('Rabby Wallet successfully connected.');
    return { provider, signer };
  } catch (error) {
    console.error('Error connecting to Rabby Wallet:', error.message);
    throw error;
  }
}

/**
 * Sends cryptocurrency to a specified address.
 * This function requires a signer obtained from Rabby Wallet.
 * @param {object} signer - The signer object from Rabby Wallet.
 * @param {string} recipientAddress - The recipient wallet address.
 * @param {string} amount - The amount to send (in Ether).
 * @returns {Promise<object>} Returns the transaction response.
 */
async function sendCrypto(signer, recipientAddress, amount) {
  try {
    // Validate recipient address
    if (!ethers.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid recipient address.');
    }

    // Convert amount to Wei
    const amountInWei = ethers.utils.parseEther(amount);

    // Send the transaction
    const txResponse = await signer.sendTransaction({
      to: recipientAddress,
      value: amountInWei,
    });

    console.log('Transaction sent:', txResponse);
    return txResponse;
  } catch (error) {
    console.error('Error sending transaction:', error.message);
    throw error;
  }
}

/**
 * Gets the current account balance.
 * @param {object} provider - The provider object from Rabby Wallet.
 * @param {string} address - The wallet address to fetch balance for.
 * @returns {Promise<string>} Returns the balance in Ether as a string.
 */
async function getBalance(provider, address) {
  try {
    // Validate address
    if (!ethers.utils.isAddress(address)) {
      throw new Error('Invalid wallet address.');
    }

    // Fetch the balance
    const balanceInWei = await provider.getBalance(address);

    // Convert balance to Ether
    const balanceInEther = ethers.utils.formatEther(balanceInWei);

    console.log(`Balance for ${address}: ${balanceInEther} ETH`);
    return balanceInEther;
  } catch (error) {
    console.error('Error fetching balance:', error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Initialize Rabby Wallet
    const { provider, signer } = await initializeRabbyWallet();

    // Get wallet address from signer
    const walletAddress = await signer.getAddress();

    // Fetch the balance
    const balance = await getBalance(provider, walletAddress);
    console.log(`Your balance: ${balance} ETH`);

    // Send cryptocurrency (uncomment the following lines to test sending functionality)
    // const recipientAddress = '0xRecipientWalletAddressHere';
    // const amountToSend = '0.01'; // Amount in Ether
    // await sendCrypto(signer, recipientAddress, amountToSend);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```
