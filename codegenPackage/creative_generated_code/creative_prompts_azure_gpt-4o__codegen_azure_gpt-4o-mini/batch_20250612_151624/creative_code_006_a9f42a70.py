"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapv2-ui.vercel.app
Prompt: Create a function in JavaScript to check the status of a transaction initiated on Mantle Swap using Web3.js or ethers.js.
Generated: DETERMINISTIC_a9f42a70559cd134
Batch ID: 20250612_151624
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.rpc.url": {
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
// Import the necessary libraries
const { ethers } = require('ethers');

// Define the provider and the transaction hash to check
const provider = new ethers.providers.JsonRpcProvider('https://your.rpc.url'); // Replace with your RPC URL

/**
 * Checks the status of a transaction on Mantle Swap.
 * @param {string} txHash - The transaction hash of the transaction to check.
 * @returns {Promise<string>} - A promise that resolves to the transaction status.
 */
async function checkTransactionStatus(txHash) {
    try {
        // Validate the transaction hash format
        if (!ethers.utils.isHexString(txHash) || txHash.length !== 66) {
            throw new Error('Invalid transaction hash format.');
        }

        // Fetch the transaction receipt
        const receipt = await provider.getTransactionReceipt(txHash);

        // Check if the transaction receipt exists
        if (!receipt) {
            return 'Transaction is pending or does not exist.';
        }

        // Check the status of the transaction
        if (receipt.status === 1) {
            return 'Transaction was successful.';
        } else {
            return 'Transaction failed.';
        }
    } catch (error) {
        // Handle any errors that occur during the execution
        console.error('Error checking transaction status:', error);
        throw new Error('Unable to check transaction status. Please try again later.');
    }
}

// Example usage (uncomment to test):
// (async () => {
//     const txHash = '0xYourTransactionHashHere'; // Replace with a valid transaction hash
//     const status = await checkTransactionStatus(txHash);
//     console.log('Transaction Status:', status);
// })();
```
