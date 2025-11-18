"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-yearn.com
Prompt: Create a script for swapping tokens using MetaMask's built-in swap functionality. Ensure the code adheres to the security features mentioned on the MetaMask website.
Generated: DETERMINISTIC_01021b440d6fe8a5
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required libraries
// Ensure you have a package manager like npm or yarn installed
const ethers = require('ethers'); // For interacting with Ethereum blockchain

// MetaMask Token Swapping Script
// This script assumes the user has MetaMask installed and connected to a wallet.

// Constants
const SWAP_CONTRACT_ADDRESS = '0xYourSwapContractAddress'; // Replace with the actual contract address for token swapping
const SWAP_ABI = [
  // Replace with the actual ABI of the swap contract
  // Example:
  {
    "inputs": [
      { "internalType": "address", "name": "tokenA", "type": "address" },
      { "internalType": "address", "name": "tokenB", "type": "address" },
      { "internalType": "uint256", "name": "amount", "type": "uint256" },
    ],
    "name": "swapTokens",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function",
  },
];

// Set up provider
// MetaMask injects `window.ethereum` into the browser
if (typeof window.ethereum === 'undefined') {
  throw new Error('MetaMask is not installed. Please install MetaMask to use this script.');
}

// Use ethers.js to get the provider and signer
const provider = new ethers.providers.Web3Provider(window.ethereum, 'any');
const signer = provider.getSigner();

// Function to swap tokens
async function swapTokens(tokenA, tokenB, amount) {
  try {
    // Request account access
    await provider.send('eth_requestAccounts', []);

    // Verify that MetaMask is connected to the user's wallet
    const userAddress = await signer.getAddress();
    console.log('Connected to wallet:', userAddress);

    // Create contract instance
    const swapContract = new ethers.Contract(SWAP_CONTRACT_ADDRESS, SWAP_ABI, signer);

    // Validate input parameters
    if (!ethers.utils.isAddress(tokenA) || !ethers.utils.isAddress(tokenB)) {
      throw new Error('Invalid token address.');
    }
    if (!ethers.BigNumber.isBigNumber(amount) && amount <= 0) {
      throw new Error('Invalid swap amount.');
    }

    // Initiate token swap
    console.log(`Swapping ${amount.toString()} of token ${tokenA} for token ${tokenB}`);
    const tx = await swapContract.swapTokens(tokenA, tokenB, ethers.BigNumber.from(amount));
    
    // Wait for transaction to be mined
    console.log('Transaction sent. Waiting for confirmation...');
    const receipt = await tx.wait();
    console.log('Token swap successful! Transaction receipt:', receipt);

    return receipt; // Return transaction receipt for further use

  } catch (error) {
    console.error('Error during token swap:', error.message);
    throw error; // Rethrow error for caller to handle
  }
}

// Example usage
// Replace with actual token addresses and amount
const tokenA = '0xTokenAAddress';
const tokenB = '0xTokenBAddress';
const amount = ethers.BigNumber.from('1000000000000000000'); // Example: 1 token (assuming 18 decimals)

// Call the swap function
swapTokens(tokenA, tokenB, amount)
  .then((receipt) => console.log('Swap completed:', receipt))
  .catch((error) => console.error('Swap failed:', error.message));

/*
Security Notes:
1. Ensure you understand MetaMask's security practices and permissions model before deploying this script.
2. Always validate user inputs and sanitize data to prevent malicious attacks.
3. Restrict contract addresses and tokens to those you trust.
4. Never store sensitive information like private keys in client-side code.
*/

```
