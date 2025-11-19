"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Generate a code example for building a Polkadot-based blockchain application using the Polkadot SDK and JavaScript.
Generated: DETERMINISTIC_377ac16290e5fc5e
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from the Polkadot SDK
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define the main function to run the application
async function main() {
    // Connect to a Polkadot node using WebSocket
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');
    
    // Create an API instance
    const api = await ApiPromise.create({ provider: wsProvider });

    // Log the chain name
    const chain = await api.rpc.system.chain();
    console.log(`Connected to chain: ${chain}`);

    // Fetch the latest block number
    const lastHeader = await api.rpc.chain.getHeader();
    console.log(`Last block number: ${lastHeader.number}`);

    // Subscribe to new blocks
    const unsubscribe = await api.rpc.chain.subscribeNewHeads((header) => {
        console.log(`New block number: ${header.number}`);
    });

    // Error handling for connection issues
    wsProvider.on('error', (error) => {
        console.error('WebSocket error:', error);
    });

    // Graceful shutdown on process exit
    process.on('SIGINT', async () => {
        console.log('Disconnecting...');
        await unsubscribe();
        await api.disconnect();
        process.exit(0);
    });
}

// Execute the main function and handle any errors
main().catch((error) => {
    console.error('Error in main execution:', error);
    process.exit(1);
});
```
