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
// Import required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { isNotNull } = require('@polkadot/util');

// Set up the Polkadot network endpoint
const POLKADOT_ENDPOINT = 'wss://rpc.polkadot.io';

// Main function to connect to Polkadot network and retrieve information
async function getPolkadotInfo() {
  try {
    // Create a WebSocket provider
    const provider = new WsProvider(POLKADOT_ENDPOINT);

    // Create an API promise
    const api = await ApiPromise.create({ provider });

    // Retrieve and display chain information
    const chainInfo = await api.rpc.chain.getChain();
    console.log('Chain:', chainInfo.toString());

    // Retrieve and display node information
    const nodeInfo = await api.rpc.system.name();
    console.log('Node Name:', nodeInfo.toString());

    // Retrieve and display current block number
    const blockNumber = await api.rpc.chain.getBlockNumber();
    console.log('Current Block Number:', blockNumber.toString());

    // Close the API connection
    await api.disconnect();
  } catch (error) {
    console.error('Error connecting to Polkadot network:', error);
  }
}

// Run the main function
getPolkadotInfo();
```
