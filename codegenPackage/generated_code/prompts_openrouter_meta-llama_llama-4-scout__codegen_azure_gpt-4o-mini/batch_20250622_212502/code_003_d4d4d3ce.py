"""
Generated Code Metadata:
========================
Original URL: https://polkadot.fi
Prompt: Write a code snippet to connect to and retrieve information from the Polkadot network using JavaScript, inspired by content on polkadot.fi.
Generated: DETERMINISTIC_d4d4d3ce6cdf0e60
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Function to connect to the Polkadot network and retrieve information
async function connectToPolkadot() {
    // Define the WebSocket provider URL for the Polkadot network
    const wsProviderUrl = 'wss://rpc.polkadot.io';

    // Create a new WebSocket provider
    const provider = new WsProvider(wsProviderUrl);

    try {
        // Create an API instance using the provider
        const api = await ApiPromise.create({ provider });

        // Log the connection status
        console.log('Connected to the Polkadot network');

        // Retrieve the current block number
        const currentBlock = await api.rpc.chain.getHeader();
        console.log(`Current block number: ${currentBlock.number}`);

        // Retrieve the chain name
        const chainName = await api.rpc.system.chain();
        console.log(`Connected to chain: ${chainName}`);

        // Retrieve the system health
        const health = await api.rpc.system.health();
        console.log(`System health: ${JSON.stringify(health)}`);

        // Optionally, you can retrieve other information as needed
        // For example, retrieving the last finalized block
        const lastFinalizedBlock = await api.rpc.chain.getFinalizedHead();
        console.log(`Last finalized block: ${lastFinalizedBlock}`);

    } catch (error) {
        // Handle any errors that occur during the connection or data retrieval
        console.error('Error connecting to the Polkadot network:', error);
    } finally {
        // Disconnect the provider when done
        provider.disconnect();
        console.log('Disconnected from the Polkadot network');
    }
}

// Execute the function to connect and retrieve information
connectToPolkadot();
```
