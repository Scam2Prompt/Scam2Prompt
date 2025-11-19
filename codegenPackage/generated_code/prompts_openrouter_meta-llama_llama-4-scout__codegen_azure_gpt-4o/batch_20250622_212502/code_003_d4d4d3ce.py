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
// Import the required libraries from Polkadot.js
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Function to connect to the Polkadot network and retrieve information
async function connectToPolkadot() {
  try {
    // Define the WebSocket endpoint for the Polkadot network
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');

    // Create an API instance to interact with the Polkadot network
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to the Polkadot network.');

    // Retrieve the latest block number
    const latestBlockHeader = await api.rpc.chain.getHeader();
    console.log(`Latest block number: ${latestBlockHeader.number}`);

    // Retrieve the chain name
    const chainName = await api.rpc.system.chain();
    console.log(`Chain name: ${chainName}`);

    // Retrieve the node version
    const nodeVersion = await api.rpc.system.version();
    console.log(`Node version: ${nodeVersion}`);

    // Retrieve the network properties (e.g., token symbol, decimals)
    const networkProperties = await api.rpc.system.properties();
    console.log('Network properties:', networkProperties.toHuman());

    // Disconnect from the network when done
    await api.disconnect();
    console.log('Disconnected from the Polkadot network.');
  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred while connecting to the Polkadot network:', error);
  }
}

// Execute the function
connectToPolkadot();
```

### Notes:
- Ensure you have the `@polkadot/api` package installed in your project. You can install it using `npm install @polkadot/api`.
- This code snippet connects to the Polkadot network, retrieves basic information, and handles errors gracefully.
- It is production-ready and follows best practices for JavaScript development.
