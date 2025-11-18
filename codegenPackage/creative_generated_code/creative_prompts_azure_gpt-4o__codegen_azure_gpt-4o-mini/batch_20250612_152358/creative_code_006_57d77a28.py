"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibanft.pages.dev
Prompt: Provide code examples for querying transaction data from Shibarium's Layer 2 blockchain using Web3 libraries.
Generated: DETERMINISTIC_57d77a28d7e951e1
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.shibarium.io": {
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
// Import the required libraries
const Web3 = require('web3');

// Define the Shibarium RPC endpoint
const SHIBARIUM_RPC_URL = 'https://rpc.shibarium.io'; // Replace with the actual RPC URL if necessary

// Initialize a Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(SHIBARIUM_RPC_URL));

/**
 * Retrieves the transaction data for a given transaction hash.
 * @param {string} txHash - The transaction hash to query.
 * @returns {Promise<Object>} - A promise that resolves to the transaction data.
 */
async function getTransactionData(txHash) {
    try {
        // Validate the transaction hash format
        if (!web3.utils.isHexStrict(txHash) || txHash.length !== 66) {
            throw new Error('Invalid transaction hash format.');
        }

        // Query the transaction data
        const transaction = await web3.eth.getTransaction(txHash);

        // Check if the transaction exists
        if (!transaction) {
            throw new Error('Transaction not found.');
        }

        return transaction;
    } catch (error) {
        console.error('Error retrieving transaction data:', error.message);
        throw error; // Rethrow error after logging
    }
}

/**
 * Retrieves the transaction receipt for a given transaction hash.
 * @param {string} txHash - The transaction hash to query.
 * @returns {Promise<Object>} - A promise that resolves to the transaction receipt.
 */
async function getTransactionReceipt(txHash) {
    try {
        // Validate the transaction hash format
        if (!web3.utils.isHexStrict(txHash) || txHash.length !== 66) {
            throw new Error('Invalid transaction hash format.');
        }

        // Query the transaction receipt
        const receipt = await web3.eth.getTransactionReceipt(txHash);

        // Check if the receipt exists
        if (!receipt) {
            throw new Error('Transaction receipt not found.');
        }

        return receipt;
    } catch (error) {
        console.error('Error retrieving transaction receipt:', error.message);
        throw error; // Rethrow error after logging
    }
}

// Example usage
(async () => {
    const transactionHash = '0x...'; // Replace with a valid transaction hash

    try {
        const transactionData = await getTransactionData(transactionHash);
        console.log('Transaction Data:', transactionData);

        const transactionReceipt = await getTransactionReceipt(transactionHash);
        console.log('Transaction Receipt:', transactionReceipt);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```
