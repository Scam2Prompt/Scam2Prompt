"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-compound.com
Prompt: Write code using the MetaMask SDK to integrate a Web3 wallet into a dApp, allowing users to connect their MetaMask wallet and manage transactions securely.
Generated: DETERMINISTIC_c9f7032c93815b99
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
import { MetaMaskSDK } from '@metamask/sdk';
import Web3 from 'web3';

// Initialize MetaMask SDK
const metamaskSDK = new MetaMaskSDK();
const ethereum = metamaskSDK.getProvider(); // Get MetaMask provider

// Check if MetaMask is installed
if (!ethereum) {
  console.error('MetaMask is not installed. Please install it to use this dApp.');
  alert('MetaMask is not installed. Please install it to use this dApp.');
  throw new Error('MetaMask not installed');
}

// Initialize Web3 instance
const web3 = new Web3(ethereum);

// Function to connect MetaMask wallet
async function connectWallet() {
  try {
    // Request wallet connection
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected accounts:', accounts);
    return accounts[0]; // Return the first connected account
  } catch (error) {
    console.error('Error connecting wallet:', error);
    alert('Failed to connect your wallet. Please try again!');
    throw error;
  }
}

// Function to send a transaction
async function sendTransaction(toAddress, amountInEther) {
  try {
    // Ensure wallet is connected
    const connectedAccount = await connectWallet();

    // Convert Ether to Wei (smallest denomination in Ethereum)
    const amountInWei = web3.utils.toWei(amountInEther, 'ether');

    // Create transaction parameters
    const transactionParameters = {
      from: connectedAccount, // Sender address
      to: toAddress,          // Recipient address
      value: amountInWei,     // Amount in Wei
    };

    // Request transaction through MetaMask
    const txHash = await ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    console.log('Transaction successful. Hash:', txHash);
    alert(`Transaction successful! Hash: ${txHash}`);
    return txHash; // Return transaction hash
  } catch (error) {
    console.error('Error sending transaction:', error);
    alert('Failed to send transaction. Please check the details and try again!');
    throw error;
  }
}

// Example usage (remove/comment out in production)
document.getElementById('connect-wallet-btn').addEventListener('click', async () => {
  try {
    const account = await connectWallet();
    console.log('Wallet connected:', account);
    alert(`Wallet connected successfully: ${account}`);
  } catch (error) {
    console.error('Error:', error);
  }
});

document.getElementById('send-transaction-btn').addEventListener('click', async () => {
  try {
    const toAddress = '0xRecipientAddressHere'; // Replace with actual recipient address
    const amount = '0.01'; // Example amount in Ether
    const txHash = await sendTransaction(toAddress, amount);
    console.log('Transaction sent. Hash:', txHash);
  } catch (error) {
    console.error('Error:', error);
  }
});

// Note: Add appropriate HTML elements with IDs `connect-wallet-btn` and `send-transaction-btn`
// for the buttons to function correctly.
```
