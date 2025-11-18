"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-disperse.vercel.app
Prompt: Explain how to integrate Starknet Disperse functionality into a JavaScript-based web application.
Generated: DETERMINISTIC_00e84c5c8322aaaa
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
const ethers = require('ethers'); // For interacting with Ethereum-based networks
const starknet = require('starknet'); // For interacting with Starknet
require('dotenv').config(); // For managing environment variables

// Load environment variables
const PRIVATE_KEY = process.env.PRIVATE_KEY; // User's private key for signing transactions
const PROVIDER_URL = process.env.PROVIDER_URL; // URL of the Ethereum provider
const STARKNET_GATEWAY_URL = process.env.STARKNET_GATEWAY_URL; // URL of Starknet gateway

// Ensure required variables are set
if (!PRIVATE_KEY || !PROVIDER_URL || !STARKNET_GATEWAY_URL) {
  throw new Error('Environment variables are not correctly set. Check .env file.');
}

// Initialize Ethereum provider and wallet
const provider = new ethers.providers.JsonRpcProvider(PROVIDER_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Starknet Disperse contract address and ABI
const STARKNET_DISPERSE_CONTRACT_ADDRESS = '0x...'; // Replace with actual contract address
const STARKNET_DISPERSE_CONTRACT_ABI = [
  // Replace with the actual contract ABI
  {
    inputs: [
      { name: 'addresses', type: 'address[]' },
      { name: 'amounts', type: 'uint256[]' }
    ],
    name: 'disperseTokens',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function'
  }
];

// Initialize the Starknet Disperse contract
const starknetDisperseContract = new ethers.Contract(
  STARKNET_DISPERSE_CONTRACT_ADDRESS,
  STARKNET_DISPERSE_CONTRACT_ABI,
  wallet
);

// Utility function: Validate input addresses and amounts
function validateInputs(addresses, amounts) {
  if (!Array.isArray(addresses) || !Array.isArray(amounts)) {
    throw new Error('Invalid inputs: addresses and amounts must be arrays.');
  }
  if (addresses.length !== amounts.length) {
    throw new Error('Invalid inputs: addresses and amounts arrays must have the same length.');
  }
  addresses.forEach((address) => {
    if (!ethers.utils.isAddress(address)) {
      throw new Error(`Invalid Ethereum address: ${address}`);
    }
  });
  amounts.forEach((amount) => {
    if (!ethers.BigNumber.isBigNumber(ethers.BigNumber.from(amount))) {
      throw new Error(`Invalid amount: ${amount}`);
    }
  });
}

// Function: Disperse tokens to multiple recipients
async function disperseTokens(addresses, amounts) {
  try {
    // Validate the input data
    validateInputs(addresses, amounts);

    // Send the transaction to the Starknet Disperse contract
    const tx = await starknetDisperseContract.disperseTokens(addresses, amounts);
    console.log('Transaction sent:', tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log('Transaction mined successfully:', receipt);
  } catch (error) {
    console.error('Error in disperseTokens:', error);
    throw error; // Rethrow the error for higher-level handling
  }
}

// Example usage of the disperse functionality
// Replace with actual recipient addresses and amounts
const recipientAddresses = ['0x...', '0x...']; // Example addresses
const recipientAmounts = ['1000', '2000']; // Example amounts in wei

(async () => {
  try {
    console.log('Starting token disperse...');
    await disperseTokens(recipientAddresses, recipientAmounts);
    console.log('Token disperse completed.');
  } catch (error) {
    console.error('Error in main execution:', error);
  }
})();
```

Placeholders such as contract addresses, ABI, and example input values should be replaced with actual values for your application. Make sure to install required dependencies (`ethers`, `starknet`, `dotenv`) via `npm install ethers starknet dotenv` before running the script.
