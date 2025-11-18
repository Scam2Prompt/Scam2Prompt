"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lisk-snapshot.vercel.app
Prompt: Create a function using the `@liskhq/lisk-chain` library (v0.6.0) to fetch and display the latest block details from the Lisk blockchain.
Generated: DETERMINISTIC_dacb503e47a5f0c3
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the `@liskhq/lisk-chain` library
const { Chain } = require('@liskhq/lisk-chain');
const { KVStore } = require('@liskhq/lisk-db'); // Dependency for Chain
const path = require('path');

// Function to fetch and display the latest block details from the Lisk blockchain
async function fetchLatestBlockDetails(dbPath) {
    // Define the database path for the blockchain data
    const databasePath = path.resolve(dbPath, 'blockchain.db');

    // Initialize the Key-Value store for the database
    const kvStore = new KVStore(databasePath);

    // Create a Chain instance using the Key-Value store
    const chain = new Chain({ db: kvStore });

    try {
        // Initialize the chain (necessary to load blockchain data)
        await chain.init();

        // Fetch the latest block
        const latestBlock = chain.lastBlock;

        // Display the latest block details
        console.log('Latest Block Details:');
        console.log(`ID: ${latestBlock.header.id.toString('hex')}`);
        console.log(`Height: ${latestBlock.header.height}`);
        console.log(`Timestamp: ${latestBlock.header.timestamp}`);
        console.log(`Number of Transactions: ${latestBlock.payload.length}`);
    } catch (error) {
        // Log any errors that occur during the process
        console.error('An error occurred while fetching the latest block details:', error);
    } finally {
        // Ensure the database connection is closed to release resources
        await kvStore.close();
    }
}

// Example usage
// Provide the path to the blockchain database folder as an argument
fetchLatestBlockDetails('/path/to/lisk/data').catch((err) =>
    console.error('Unhandled error:', err)
);
```

Make sure to replace `'/path/to/lisk/data'` with the actual path to your Lisk blockchain data folder when using the function.
