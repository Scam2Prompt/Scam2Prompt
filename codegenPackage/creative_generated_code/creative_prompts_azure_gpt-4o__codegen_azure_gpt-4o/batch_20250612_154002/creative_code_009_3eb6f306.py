"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erc20-eth.vip
Prompt: Describe how to use MetaMask to interact with an ERC-20 token contract deployed on Ethereum, focusing on DeFi use cases.
Generated: DETERMINISTIC_3eb6f30695029305
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This code demonstrates how to interact with an ERC-20 token contract using MetaMask
// and Web3.js for basic DeFi use cases: querying balances and transferring tokens.

// Import the Web3 library
const Web3 = require('web3');

// Initialize the Web3 instance with MetaMask's provider
const web3 = new Web3(window.ethereum);

// Define the ERC-20 token contract ABI (simplified for demonstration purposes)
const ERC20_ABI = [
  // Function to get the balance of an address
  {
    "constant": true,
    "inputs": [{ "name": "account", "type": "address" }],
    "name": "balanceOf",
    "outputs": [{ "name": "", "type": "uint256" }],
    "type": "function"
  },
  // Function to transfer tokens
  {
    "constant": false,
    "inputs": [
      { "name": "recipient", "type": "address" },
      { "name": "amount", "type": "uint256" }
    ],
    "name": "transfer",
    "outputs": [{ "name": "", "type": "bool" }],
    "type": "function"
  }
];

// Example ERC-20 token contract address on Ethereum (use actual deployed token address)
const TOKEN_ADDRESS = '0xYourTokenContractAddressHere';

// Create a contract instance
const tokenContract = new web3.eth.Contract(ERC20_ABI, TOKEN_ADDRESS);

// Function to check an address's token balance
async function getTokenBalance(userAddress) {
  try {
    // Call the balanceOf function from the token contract
    const balance = await tokenContract.methods.balanceOf(userAddress).call();
    console.log(`Token balance of ${userAddress}:`, web3.utils.fromWei(balance, 'ether'));
    return balance; // Returns the balance in Wei (can be converted to Ether using web3.utils.fromWei)
  } catch (error) {
    console.error('Error fetching token balance:', error);
    throw error;
  }
}

// Function to transfer tokens from the connected account to another address
async function transferTokens(recipientAddress, amountInEther) {
  try {
    // Request account access from MetaMask
    const accounts = await web3.eth.requestAccounts();
    const senderAddress = accounts[0]; // Use the first account from MetaMask

    // Convert Ether amount to Wei (smallest unit of Ether)
    const amountInWei = web3.utils.toWei(amountInEther, 'ether');

    // Send the transfer transaction
    const transaction = await tokenContract.methods.transfer(recipientAddress, amountInWei).send({
      from: senderAddress
    });

    console.log('Transaction successful:', transaction);
    return transaction;
  } catch (error) {
    console.error('Error transferring tokens:', error);
    throw error;
  }
}

// Example Usage
(async () => {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      console.error('MetaMask is not installed. Please install MetaMask and try again.');
      return;
    }

    // Enable MetaMask
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Example user address (replace with actual address)
    const userAddress = '0xUserAddressHere';

    // Fetch token balance
    await getTokenBalance(userAddress);

    // Transfer tokens (replace with actual recipient and amount)
    const recipientAddress = '0xRecipientAddressHere';
    const amountToSend = '0.1'; // Example: 0.1 tokens
    await transferTokens(recipientAddress, amountToSend);
  } catch (error) {
    console.error('Error in example usage:', error);
  }
})();
```

This code implements interaction with an ERC-20 token contract using MetaMask and Web3.js. It includes functions for querying balances and transferring tokens. Proper error handling is implemented, along with checks for MetaMask installation and account access.
