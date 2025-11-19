"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.africa
Prompt: Generate code to interact with the Polkadot blockchain using the Polkadot.js library.
Generated: DETERMINISTIC_46883456a7946ccc
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary modules from @polkadot/api
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define the main async function to interact with the Polkadot blockchain
async function main() {
  try {
    // Specify the WebSocket endpoint for the Polkadot network
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');

    // Create an API instance connected to the Polkadot network
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to the Polkadot blockchain.');

    // Fetch the latest block number
    const latestBlockHeader = await api.rpc.chain.getHeader();
    console.log(`Latest block number: ${latestBlockHeader.number}`);

    // Fetch and log the chain information
    const chainName = await api.rpc.system.chain();
    console.log(`Chain name: ${chainName}`);

    const nodeName = await api.rpc.system.name();
    console.log(`Node name: ${nodeName}`);

    const nodeVersion = await api.rpc.system.version();
    console.log(`Node version: ${nodeVersion}`);

    // Retrieve and log account balance for a specific address
    const address = 'YourPolkadotAddressHere'; // Replace with a valid Polkadot address
    const { data: balance } = await api.query.system.account(address);
    console.log(`Balance for address ${address}: ${balance.free.toHuman()}`);

    // Subscribing to new blocks
    console.log('Subscribing to new blocks...');
    const unsubscribe = await api.rpc.chain.subscribeNewHeads((header) => {
      console.log(`New block number: ${header.number}`);
    });

    // Gracefully handle termination signals like Ctrl+C
    process.on('SIGINT', async () => {
      console.log('Disconnecting...');
      unsubscribe(); // Unsubscribe from block updates
      await api.disconnect(); // Disconnect the API
      console.log('Disconnected.');
      process.exit(0);
    });
  } catch (error) {
    // Handle any errors that occur during the execution
    console.error('An error occurred:', error);
  }
}

// Execute the main function
main();
```

Make sure you replace `YourPolkadotAddressHere` with a valid Polkadot address to fetch balance information. Install the required dependencies (`@polkadot/api`) using `npm install @polkadot/api` before running this script.
