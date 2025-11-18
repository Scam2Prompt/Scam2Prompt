"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Provide sample code for handling Ethereum transactions using Fortmatic in a JavaScript-based dApp.
Generated: DETERMINISTIC_b36f041a77b4ee31
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
const Web3 = require('web3');
const Fortmatic = require('fortmatic');

// Configuration constants
const FORTMATIC_API_KEY = 'YOUR_FORTMATIC_API_KEY'; // Replace with your actual API key
const NETWORK = 'mainnet'; // Use 'mainnet', 'rinkeby', or other supported networks

// Initialize Fortmatic provider
const fm = new Fortmatic(FORTMATIC_API_KEY, NETWORK);

// Initialize Web3 instance with Fortmatic provider
const web3 = new Web3(fm.getProvider());

// Function to fetch the user's Ethereum account
async function getUserAccount() {
  try {
    // Request Ethereum accounts from the provider
    const accounts = await web3.eth.getAccounts();

    // Ensure at least one account is returned
    if (accounts.length === 0) {
      throw new Error('No Ethereum accounts found.');
    }

    return accounts[0]; // Return the first account
  } catch (error) {
    console.error('Error fetching user account:', error.message);
    throw error; // Re-throw the error for upstream handling
  }
}

// Function to send an Ethereum transaction
async function sendTransaction(toAddress, amountInEther) {
  try {
    // Validate inputs
    if (!web3.utils.isAddress(toAddress)) {
      throw new Error('Invalid Ethereum address.');
    }
    if (isNaN(Number(amountInEther)) || Number(amountInEther) <= 0) {
      throw new Error('Invalid transaction amount.');
    }

    // Get the user's account
    const fromAddress = await getUserAccount();

    // Convert amount from Ether to Wei
    const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

    // Create transaction object
    const transaction = {
      from: fromAddress,
      to: toAddress,
      value: amountInWei,
      gas: 21000, // Set a standard gas limit for simple transfers
    };

    // Send the transaction
    const txReceipt = await web3.eth.sendTransaction(transaction);

    console.log('Transaction successful. Receipt:', txReceipt);
    return txReceipt; // Return the transaction receipt
  } catch (error) {
    console.error('Error sending transaction:', error.message);
    throw error; // Re-throw the error for upstream handling
  }
}

// Example usage
(async () => {
  try {
    const recipient = '0xRecipientEthereumAddress'; // Replace with actual recipient address
    const amount = '0.01'; // Amount in Ether to send

    console.log('Sending transaction...');
    const receipt = await sendTransaction(recipient, amount);
    console.log('Transaction completed:', receipt);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
})();
```
