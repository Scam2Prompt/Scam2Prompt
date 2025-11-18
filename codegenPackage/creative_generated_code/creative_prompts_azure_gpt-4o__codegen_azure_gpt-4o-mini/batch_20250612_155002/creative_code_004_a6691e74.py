"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet.de6k46fqs3775.amplifyapp.com
Prompt: Write a function using Router Nitro to check the status of a cross-chain transaction and handle errors.
Generated: DETERMINISTIC_a6691e7463493ad6
Batch ID: 20250612_155002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { NitroRouter } from 'router-nitro'; // Assumed library for cross-chain transactions
import axios from 'axios'; // For making HTTP requests

/**
 * Check the status of a cross-chain transaction.
 *
 * @param {string} transactionId - The ID of the transaction to check.
 * @returns {Promise<Object>} - A promise that resolves to the transaction status.
 * @throws {Error} - Throws an error if the transaction ID is invalid or if an HTTP error occurs.
 */
async function checkCrossChainTransactionStatus(transactionId) {
    // Validate the input
    if (!transactionId || typeof transactionId !== 'string') {
        throw new Error('Invalid transaction ID. It must be a non-empty string.');
    }

    try {
        // Create an instance of the NitroRouter
        const router = new NitroRouter();

        // Fetch the transaction status using NitroRouter
        const status = await router.getTransactionStatus(transactionId);

        // If the status is not found, throw an error
        if (!status) {
            throw new Error('Transaction status not found.');
        }

        return status; // Return the transaction status

    } catch (error) {
        // Handle specific NitroRouter errors
        if (error instanceof NitroRouter.Error) {
            throw new Error(`Router error: ${error.message}`);
        }
        
        // Handle HTTP errors
        if (axios.isAxiosError(error)) {
            throw new Error(`HTTP error: ${error.response?.status} - ${error.message}`);
        }
        
        // Re-throw other unexpected errors
        throw new Error(`Unexpected error: ${error.message}`);
    }
}

// Example usage:
// (Uncomment the following lines to test the function)
// checkCrossChainTransactionStatus('your-transaction-id')
//     .then(status => console.log('Transaction Status:', status))
//     .catch(error => console.error('Error checking transaction status:', error.message));
```
