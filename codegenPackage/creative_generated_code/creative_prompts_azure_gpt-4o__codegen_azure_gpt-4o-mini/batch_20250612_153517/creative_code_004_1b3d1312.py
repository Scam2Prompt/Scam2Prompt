"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-feat-bridge-sdk-b50625-offchain-labs.vercel.app
Prompt: Create a function to query the status of a token bridge transaction using the Arbitrum Bridge SDK on Arbitrum Sepolia.
Generated: DETERMINISTIC_1b3d131233741e06
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Arbitrum Bridge SDK
import { ArbSdk } from '@arbitrum/sdk';

// Function to query the status of a token bridge transaction
async function queryBridgeTransactionStatus(transactionHash) {
    // Validate the input transaction hash
    if (!transactionHash) {
        throw new Error('Transaction hash is required');
    }

    // Initialize the Arbitrum SDK with the Sepolia network configuration
    const arbSdk = new ArbSdk({ network: 'sepolia' });

    try {
        // Fetch transaction details using the transaction hash
        const transactionDetails = await arbSdk.getTransaction(transactionHash);

        // Check if transaction details were retrieved successfully
        if (!transactionDetails) {
            throw new Error('Transaction not found');
        }

        // Return the transaction status
        return {
            status: transactionDetails.status,
            blockNumber: transactionDetails.blockNumber,
            timestamp: transactionDetails.timestamp,
        };
    } catch (error) {
        // Handle errors and log them for debugging purposes
        console.error('Error querying transaction status:', error);
        throw new Error('Failed to query transaction status');
    }
}

// Example usage (uncomment to test)
// queryBridgeTransactionStatus('YOUR_TRANSACTION_HASH')
//     .then(status => console.log('Transaction Status:', status))
//     .catch(error => console.error('Error:', error));
```
