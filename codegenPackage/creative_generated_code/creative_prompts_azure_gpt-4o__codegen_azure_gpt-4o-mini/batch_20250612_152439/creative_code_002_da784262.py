"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet.pages.dev
Prompt: Generate a JavaScript example using LavaSDK to query transaction data from the Cosmos Hub Mainnet RPC.
Generated: DETERMINISTIC_da784262e854e96e
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { Client } = require('@lava-sdk/client');

// Initialize the Lava SDK client
const client = new Client({
    chain: 'cosmoshub-4', // Specify the Cosmos Hub Mainnet
    network: 'mainnet',    // Define network as mainnet
});

// Function to query transaction data by transaction hash
async function queryTransaction(transactionHash) {
    try {
        // Validate the transaction hash format
        if (!/^[a-f0-9]{64}$/.test(transactionHash)) {
            throw new Error('Invalid transaction hash format.');
        }

        // Query the transaction data from the Cosmos Hub
        const transactionData = await client.tx.getTransaction(transactionHash);

        // Check if transaction data was found
        if (!transactionData) {
            console.error(`Transaction with hash ${transactionHash} not found.`);
            return;
        }

        // Log the transaction data
        console.log('Transaction Data:', transactionData);
    } catch (error) {
        // Handle errors gracefully
        console.error('Error querying transaction data:', error.message);
    }
}

// Example usage of the function
const exampleTransactionHash = 'YOUR_TRANSACTION_HASH_HERE'; // Replace with a valid transaction hash
queryTransaction(exampleTransactionHash);
```
