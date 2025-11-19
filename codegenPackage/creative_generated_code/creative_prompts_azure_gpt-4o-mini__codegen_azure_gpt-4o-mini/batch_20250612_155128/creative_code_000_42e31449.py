"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: Generate a JavaScript code snippet that utilizes the Polkadot.js library for interacting with the Polkadot blockchain.
Generated: DETERMINISTIC_42e31449f602be3b
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the necessary libraries from Polkadot.js
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Function to connect to the Polkadot blockchain and retrieve the latest block number
async function connectToPolkadot() {
    try {
        // Define the WebSocket provider to connect to a Polkadot node
        const wsProvider = new WsProvider('wss://rpc.polkadot.io');

        // Create an API instance using the provider
        const api = await ApiPromise.create({ provider: wsProvider });

        console.log('Connected to the Polkadot blockchain.');

        // Retrieve the latest block number
        const lastBlock = await api.rpc.chain.getHeader();
        console.log(`Latest block number: ${lastBlock.number.toNumber()}`);

        // Disconnect from the provider
        await api.disconnect();
        console.log('Disconnected from the Polkadot blockchain.');

    } catch (error) {
        // Handle errors that may occur during the connection or data retrieval
        console.error('Error connecting to the Polkadot blockchain:', error);
    }
}

// Execute the function to connect and fetch the block number
connectToPolkadot();
```
