"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.de
Prompt: Explain how to use the Arbitrum SDK to monitor gas fees and transaction finality on the layer-2 network.
Generated: DETERMINISTIC_37b0a1bfc16565aa
Batch ID: 20250612_150342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arb1.arbitrum.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries from the Arbitrum SDK and ethers.js
const { L2TransactionReceipt, L2Provider } = require('@arbitrum/sdk');
const { ethers } = require('ethers');

// Configuration: Replace with your own RPC endpoint and contract address if needed
const ARBITRUM_RPC_URL = 'https://arb1.arbitrum.io/rpc'; // Arbitrum mainnet RPC URL
const WALLET_PRIVATE_KEY = 'YOUR_PRIVATE_KEY_HERE'; // Replace with your wallet's private key

// Set up an ethers provider connected to the Arbitrum network
async function initializeProvider() {
  try {
    const provider = new L2Provider(ARBITRUM_RPC_URL);
    return provider;
  } catch (error) {
    console.error('Error initializing provider:', error.message);
    throw error; // Throw error for external handling
  }
}

// Function to monitor gas fees on the Arbitrum network
async function monitorGasFees(provider) {
  try {
    // Fetch current gas price
    const gasPrice = await provider.getGasPrice();
    console.log(`Current gas price: ${ethers.utils.formatUnits(gasPrice, 'gwei')} gwei`);
  } catch (error) {
    console.error('Error fetching gas fees:', error.message);
    throw error;
  }
}

// Function to monitor transaction finality
async function monitorTransactionFinality(provider, txHash) {
  try {
    console.log(`Monitoring finality for transaction: ${txHash}`);

    // Wait for the transaction receipt
    const receipt = await provider.waitForTransaction(txHash);
    console.log('Transaction Receipt:', receipt);

    // Wrap receipt with Arbitrum SDK to check finality
    const arbReceipt = new L2TransactionReceipt(receipt);

    // Check if the transaction is finalized
    const isFinalized = await arbReceipt.isFinalized();
    console.log(`Transaction finalized: ${isFinalized}`);
  } catch (error) {
    console.error('Error monitoring transaction finality:', error.message);
    throw error;
  }
}

// Main function to initialize monitoring
async function main() {
  try {
    const provider = await initializeProvider();

    // Monitor gas fees
    await monitorGasFees(provider);

    // Replace with a valid transaction hash to monitor finality
    const transactionHash = 'YOUR_TRANSACTION_HASH_HERE';
    await monitorTransactionFinality(provider, transactionHash);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

// Run the main function
main();
```
