"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memecoin-web.pages.dev
Prompt: Provide a step-by-step guide to integrate the MEME token into a decentralized application (dApp) using the details from the Memecoin webpage.
Generated: DETERMINISTIC_24a3b629dfc24869
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/*
 * Integration of MEME token into a decentralized application (dApp)
 * Prerequisites: 
 * - Access to the MEME token contract address and ABI from the Memecoin webpage.
 * - Installed dependencies: web3.js, dotenv (for managing environment variables securely).
 * - Ensure your dApp has access to a blockchain node (e.g., an Infura endpoint or local Ethereum node).
 */

require('dotenv').config(); // Load environment variables securely
const Web3 = require('web3');

// Load environment variables (ensure these are set in a .env file)
const INFURA_URL = process.env.INFURA_URL; // Infura or other Ethereum node URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key for signing transactions
const MEME_TOKEN_ADDRESS = process.env.MEME_TOKEN_ADDRESS; // MEME token contract address
const MEME_TOKEN_ABI = require('./MemeTokenABI.json'); // Import MEME token ABI from file

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Get account from private key
const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
web3.eth.accounts.wallet.add(account); // Add account to Web3 wallet
web3.eth.defaultAccount = account.address;

// Load MEME Token contract
const memeToken = new web3.eth.Contract(MEME_TOKEN_ABI, MEME_TOKEN_ADDRESS);

/**
 * Fetches the balance of MEME tokens for a given wallet address.
 * @param {string} walletAddress - Address of the wallet to check balance.
 * @returns {Promise<string>} - MEME token balance in string format.
 */
async function getMemeTokenBalance(walletAddress) {
  try {
    const balance = await memeToken.methods.balanceOf(walletAddress).call();
    return web3.utils.fromWei(balance, 'ether'); // Convert balance from Wei to Ether units
  } catch (error) {
    console.error('Error fetching MEME token balance:', error);
    throw error;
  }
}

/**
 * Transfers MEME tokens from the connected wallet to a given recipient.
 * @param {string} recipientAddress - Address of the recipient.
 * @param {string} amount - Amount of MEME tokens to transfer (in Ether units).
 * @returns {Promise<string>} - Transaction hash of the transfer.
 */
async function transferMemeTokens(recipientAddress, amount) {
  try {
    const amountInWei = web3.utils.toWei(amount, 'ether'); // Convert amount to Wei
    const tx = memeToken.methods.transfer(recipientAddress, amountInWei);
    const gas = await tx.estimateGas({ from: account.address });
    const gasPrice = await web3.eth.getGasPrice();

    const receipt = await tx.send({
      from: account.address,
      gas,
      gasPrice,
    });

    console.log('Transfer successful:', receipt.transactionHash);
    return receipt.transactionHash;
  } catch (error) {
    console.error('Error during MEME token transfer:', error);
    throw error;
  }
}

/**
 * Approves a given address to spend MEME tokens on behalf of the connected wallet.
 * @param {string} spenderAddress - Address to be approved for spending.
 * @param {string} amount - Amount of MEME tokens to approve (in Ether units).
 * @returns {Promise<string>} - Transaction hash of the approval.
 */
async function approveMemeTokens(spenderAddress, amount) {
  try {
    const amountInWei = web3.utils.toWei(amount, 'ether'); // Convert amount to Wei
    const tx = memeToken.methods.approve(spenderAddress, amountInWei);
    const gas = await tx.estimateGas({ from: account.address });
    const gasPrice = await web3.eth.getGasPrice();

    const receipt = await tx.send({
      from: account.address,
      gas,
      gasPrice,
    });

    console.log('Approval successful:', receipt.transactionHash);
    return receipt.transactionHash;
  } catch (error) {
    console.error('Error during MEME token approval:', error);
    throw error;
  }
}

/**
 * Example usage of the MEME token integration.
 */
(async function exampleUsage() {
  const recipient = '0xRecipientWalletAddressHere'; // Replace with recipient address
  const spender = '0xSpenderWalletAddressHere'; // Replace with spender address

  try {
    // Fetch MEME token balance
    const balance = await getMemeTokenBalance(account.address);
    console.log(`MEME Token Balance: ${balance} MEME`);

    // Transfer MEME tokens
    const transferTxHash = await transferMemeTokens(recipient, '10'); // Transfer 10 MEME tokens
    console.log(`Transfer Transaction Hash: ${transferTxHash}`);

    // Approve MEME tokens
    const approvalTxHash = await approveMemeTokens(spender, '5'); // Approve 5 MEME tokens for spending
    console.log(`Approval Transaction Hash: ${approvalTxHash}`);
  } catch (error) {
    console.error('Error during example usage:', error);
  }
})();
```

**Note**:  
- Replace placeholders such as `0xRecipientWalletAddressHere` and `0xSpenderWalletAddressHere` with actual addresses.  
- Ensure the `.env` file contains `INFURA_URL`, `PRIVATE_KEY`, and `MEME_TOKEN_ADDRESS`.  
- The `MemeTokenABI.json` file should contain the ABI of the MEME token contract, which can be obtained from the Memecoin webpage.
