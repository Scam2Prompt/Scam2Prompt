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
// Import the required modules from the Polkadot.js library
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Async function to connect to the Polkadot blockchain and query the latest block
async function main() {
  try {
    // Define the WebSocket endpoint for the Polkadot network
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');

    // Create an API instance connected to the network
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to the Polkadot blockchain.');

    // Query the latest block header
    const latestBlockHeader = await api.rpc.chain.getHeader();

    console.log('Latest block header:', latestBlockHeader.toHuman());

    // Example: Query a specific chain state (e.g., total issuance)
    const totalIssuance = await api.query.balances.totalIssuance();

    console.log('Total issuance:', totalIssuance.toString());

    // Disconnect the API when done
    await api.disconnect();
    console.log('Disconnected from the Polkadot blockchain.');
  } catch (error) {
    // Handle connection errors or other issues
    console.error('Error interacting with the Polkadot blockchain:', error);
  }
}

// Execute the main function
main();
```
