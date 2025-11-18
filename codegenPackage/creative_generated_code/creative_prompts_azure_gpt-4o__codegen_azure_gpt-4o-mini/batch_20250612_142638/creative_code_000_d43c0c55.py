"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain.vin
Prompt: Write JavaScript code to interact with the Onchain-ETH library for querying Ethereum blockchain data.
Generated: DETERMINISTIC_d43c0c552f17ca14
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Onchain-ETH library
const Onchain = require('onchain-eth');

// Initialize the Onchain-ETH client
const onchainClient = new Onchain.Client({
    apiKey: 'YOUR_API_KEY_HERE', // Replace with your Onchain API key
});

// Function to fetch Ethereum block data by block number
async function getBlockData(blockNumber) {
    try {
        // Validate the block number input
        if (typeof blockNumber !== 'number' || blockNumber < 0) {
            throw new Error('Invalid block number. It must be a non-negative integer.');
        }

        // Query the Ethereum blockchain for the specified block
        const blockData = await onchainClient.getBlock(blockNumber);
        
        // Check if the block data is empty or null
        if (!blockData) {
            throw new Error('Block data not found.');
        }

        // Return the retrieved block data
        return blockData;
    } catch (error) {
        // Handle errors and log them appropriately
        console.error(`Error fetching block data: ${error.message}`);
        throw error; // Rethrow error for further handling if needed
    }
}

// Function to fetch transaction data by transaction hash
async function getTransactionData(txHash) {
    try {
        // Validate the transaction hash input
        if (typeof txHash !== 'string' || !txHash.match(/^(0x)?[0-9a-fA-F]{64}$/)) {
            throw new Error('Invalid transaction hash. Please provide a valid hash.');
        }

        // Query the Ethereum blockchain for the specified transaction
        const transactionData = await onchainClient.getTransaction(txHash);
        
        // Check if the transaction data is empty or null
        if (!transactionData) {
            throw new Error('Transaction data not found.');
        }

        // Return the retrieved transaction data
        return transactionData;
    } catch (error) {
        // Handle errors and log them appropriately
        console.error(`Error fetching transaction data: ${error.message}`);
        throw error; // Rethrow error for further handling if needed
    }
}

// Example usage of the functions
(async () => {
    try {
        const blockNumber = 12345678; // Replace with desired block number
        const blockData = await getBlockData(blockNumber);
        console.log('Block Data:', blockData);

        const txHash = '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'; // Replace with desired transaction hash
        const transactionData = await getTransactionData(txHash);
        console.log('Transaction Data:', transactionData);
    } catch (error) {
        console.error(`Error in main execution: ${error.message}`);
    }
})();
```
