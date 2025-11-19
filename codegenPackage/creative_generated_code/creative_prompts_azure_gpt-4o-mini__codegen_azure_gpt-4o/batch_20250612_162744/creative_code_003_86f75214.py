"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-live.app
Prompt: How can I use the Polkadot Live desktop client to interact with Polkadot's blockchain features programmatically?
Generated: DETERMINISTIC_86f7521463764012
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

To interact programmatically with Polkadot's blockchain features, you can use the Polkadot.js library. Below is an example of clean, production-ready JavaScript/Node.js code that connects to a Polkadot node and interacts with its blockchain using the Polkadot.js API. This code assumes you already have Node.js installed.

```javascript
// Import the required Polkadot.js libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

(async () => {
  try {
    // Define the WebSocket provider URL for connecting to a Polkadot node.
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');
    
    // Create a new instance of the API using the provider
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to the Polkadot blockchain.');

    // Example: Query the latest block number
    const latestBlockHeader = await api.rpc.chain.getHeader();
    console.log(`Latest block number: ${latestBlockHeader.number}`);

    // Example: Query the balance of a specific account
    const accountAddress = '12ab...'; // Replace with the desired account address
    const { data: { free: balance } } = await api.query.system.account(accountAddress);
    console.log(`Balance of account ${accountAddress}: ${balance.toHuman()}`);

    // Cleanup: Disconnect from the blockchain to free resources
    await api.disconnect();
    console.log('Disconnected from the Polkadot blockchain.');
  } catch (error) {
    console.error('An error occurred:', error.message);
    // Add more error handling logic if necessary
  }
})();
```

### Instructions:
1. Install dependencies by running `npm install @polkadot/api` in your project directory.
2. Replace `12ab...` with the actual Polkadot account address you want to query.
3. Run the script using `node <filename>.js`.

This code demonstrates how to:
- Connect to a Polkadot node via WebSocket.
- Query the latest block number.
- Query the balance of a specific account.
- Disconnect from the node cleanly.

Make sure to handle sensitive data and environment-specific configurations appropriately in production environments.
