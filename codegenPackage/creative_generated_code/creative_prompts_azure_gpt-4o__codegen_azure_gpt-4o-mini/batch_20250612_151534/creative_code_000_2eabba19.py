"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: Write JavaScript code using Polkadot.js to connect to a Polkadot blockchain node and retrieve the latest block information.
Generated: DETERMINISTIC_2eabba1938f8a3a0
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary Polkadot.js libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

/**
 * Connects to a Polkadot blockchain node and retrieves the latest block information.
 */
async function fetchLatestBlock() {
    // Define the WebSocket endpoint for the Polkadot node
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');

    try {
        // Create an instance of the API with the WebSocket provider
        const api = await ApiPromise.create({ provider: wsProvider });

        // Retrieve the latest block number
        const lastHeader = await api.rpc.chain.getHeader();

        // Log the latest block information
        console.log(`Latest Block Number: ${lastHeader.number}`);
        console.log(`Block Hash: ${lastHeader.hash}`);
        console.log(`Parent Hash: ${lastHeader.parentHash}`);
        console.log(`State Root: ${lastHeader.stateRoot}`);
        console.log(`Extrinsics Root: ${lastHeader.extrinsicsRoot}`);
        console.log(`Author: ${lastHeader.author}`); // Note: Author field may vary based on node implementation
    } catch (error) {
        // Handle errors that may occur during connection or retrieval
        console.error('Error fetching the latest block:', error);
    } finally {
        // Clean up resources and disconnect from the provider
        await wsProvider.disconnect();
    }
}

// Execute the function to fetch the latest block information
fetchLatestBlock();
```
