"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoinvip.pages.dev
Prompt: Write a script to automate the process of connecting to Uniswap, pasting the $PEIPEI token address, and swapping ETH for $PEIPEI using Web3.js.
Generated: DETERMINISTIC_ba61043202637d83
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to automate swapping ETH for $PEIPEI on Uniswap using Web3.js
 * 
 * Requirements:
 * - Node.js environment
 * - Web3.js installed (`npm install web3`)
 * - dotenv installed for managing environment variables (`npm install dotenv`)
 * 
 * Make sure to create a `.env` file with the following variables:
 * - PRIVATE_KEY: Your wallet's private key
 * - INFURA_URL: Infura endpoint for Ethereum network
 * - PEIPEI_TOKEN_ADDRESS: The $PEIPEI token contract address
 */

// Load required libraries
require('dotenv').config();
const Web3 = require('web3');

// Environment variables
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const INFURA_URL = process.env.INFURA_URL;
const PEIPEI_TOKEN_ADDRESS = process.env.PEIPEI_TOKEN_ADDRESS;
const UNISWAP_ROUTER_ADDRESS = "0xE592427A0AEce92De3Edee1F18E0157C05861564"; // Uniswap V3 Router address

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Accounts and contract instances
const account = web3.eth.accounts.wallet.add(PRIVATE_KEY);
const routerAbi = require('./abi/UniswapV3Router.json'); // Load Uniswap V3 Router ABI
const routerContract = new web3.eth.Contract(routerAbi, UNISWAP_ROUTER_ADDRESS);

// Swap ETH for $PEIPEI
async function swapETHForPEIPEI(amountInETH, slippageTolerance, gasLimit) {
  try {
    console.log("Preparing swap...");

    // Convert ETH input amount to Wei
    const amountInWei = web3.utils.toWei(amountInETH.toString(), 'ether');

    // Get current gas price
    const gasPrice = await web3.eth.getGasPrice();

    // Define token path (ETH -> $PEIPEI)
    const path = [web3.utils.toChecksumAddress(PEIPEI_TOKEN_ADDRESS)];

    // Estimated amountOut (minimum amount of $PEIPEI)
    const deadline = Math.floor(Date.now() / 1000) + 60 * 10; // 10 minutes from now

    // Build transaction parameters
    const tx = {
      from: account.address,
      to: UNISWAP_ROUTER_ADDRESS,
      gas: gasLimit,
  
    }
  }
}

```
