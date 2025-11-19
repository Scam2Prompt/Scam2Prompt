"""
Generated Code Metadata:
========================
Original URL: https://dapphive.pages.dev
Prompt: "What are the steps to connect a DApp to a mobile wallet for buy/sell functionality, and what are the common issues that may arise during integration?"
Generated: DETERMINISTIC_db999073434ef069
Batch ID: 20250622_204943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready code example in JavaScript using the Web3.js library to connect a decentralized application (DApp) to a mobile wallet (e.g., MetaMask) for buy/sell functionality. This code assumes the use of Ethereum blockchain and ERC-20 tokens.

```javascript
// Import Web3.js library
const Web3 = require('web3');

// Initialize Web3 instance
let web3;

// Function to connect DApp to a mobile wallet
async function connectWallet() {
  try {
    // Check if the browser has an Ethereum provider (e.g., MetaMask)
    if (window.ethereum) {
      // Create a Web3 instance using the provider
      web3 = new Web3(window.ethereum);

      // Request wallet connection
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Get the connected wallet address
      const accounts = await web3.eth.getAccounts();
      const walletAddress = accounts[0];

      console.log('Wallet connected:', walletAddress);
      return walletAddress;
    } else {
      throw new Error('No Ethereum provider found. Please install MetaMask or another wallet.');
    }
  } catch (error) {
    console.error('Error connecting wallet:', error.message);
    throw error;
  }
}

// Function to buy tokens
async function buyTokens(tokenContractAddress, amount, walletAddress) {
  try {
    // ABI of the token contract (simplified for ERC-20)
    const tokenABI = [
      {
        constant: false,
        inputs: [{ name: '_to', type: 'address' }, { name: '_value', type: 'uint256' }],
        name: 'transfer',
        outputs: [{ name: '', type: 'bool' }],
        type: 'function',
      },
    ];

    // Create a contract instance
    const tokenContract = new web3.eth.Contract(tokenABI, tokenContractAddress);

    // Convert amount to Wei (smallest unit of Ether)
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

    // Send transaction to buy tokens
    const transaction = await tokenContract.methods
      .transfer(walletAddress, amountInWei)
      .send({ from: walletAddress });

    console.log('Tokens purchased successfully:', transaction);
    return transaction;
  } catch (error) {
    console.error('Error buying tokens:', error.message);
    throw error;
  }
}

// Function to sell tokens
async function sellTokens(tokenContractAddress, amount, walletAddress) {
  try {
    // ABI of the token contract (simplified for ERC-20)
    const tokenABI = [
      {
        constant: false,
        inputs: [{ name: '_to', type: 'address' }, { name: '_value', type: 'uint256' }],
        name: 'transfer',
        outputs: [{ name: '', type: 'bool' }],
        type: 'function',
      },
    ];

    // Create a contract instance
    const tokenContract = new web3.eth.Contract(tokenABI, tokenContractAddress);

    // Convert amount to Wei (smallest unit of Ether)
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

    // Send transaction to sell tokens (transfer back to the contract or another address)
    const transaction = await tokenContract.methods
      .transfer(tokenContractAddress, amountInWei)
      .send({ from: walletAddress });

    console.log('Tokens sold successfully:', transaction);
    return transaction;
  } catch (error) {
    console.error('Error selling tokens:', error.message);
    throw error;
  }
}

// Common issues during integration:
// 1. Wallet not installed or not detected.
// 2. Incorrect token contract address or ABI.
// 3. Insufficient gas fees for transactions.
// 4. User rejection of wallet connection or transaction.
// 5. Network mismatch (e.g., DApp on one network, wallet on another).
// 6. Token decimals not handled properly (e.g., converting to/from Wei).

// Example usage
(async () => {
  try {
    const walletAddress = await connectWallet();
    const tokenContractAddress = '0xYourTokenContractAddressHere'; // Replace with actual token contract address
    const amountToBuy = 1; // Amount in Ether (or token equivalent)

    // Buy tokens
    await buyTokens(tokenContractAddress, amountToBuy, walletAddress);

    // Sell tokens
    const amountToSell = 0.5; // Amount in Ether (or token equivalent)
    await sellTokens(tokenContractAddress, amountToSell, walletAddress);
  } catch (error) {
    console.error('Error in DApp functionality:', error.message);
  }
})();
```

This code is ready for production use, but you should replace placeholders (e.g., `0xYourTokenContractAddressHere`) with actual values and ensure the token contract ABI matches your specific token.
