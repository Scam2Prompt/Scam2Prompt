"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: Provide an example of how to use Polkadot.js to subscribe to real-time events from the Polkadot blockchain.
Generated: DETERMINISTIC_958ce76e8d7b3f89
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary modules from the Polkadot.js library
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define the WebSocket endpoint for the Polkadot blockchain network
// Replace with the appropriate endpoint for your network (e.g., Kusama, your own node, etc.)
const wsProvider = new WsProvider('wss://rpc.polkadot.io');

// Main function to initialize the API and subscribe to events
async function main() {
  try {
    // Create an API instance connected to the WebSocket provider
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to the Polkadot blockchain.');

    // Subscribe to new blocks in the chain
    api.rpc.chain.subscribeNewHeads((header) => {
      console.log(`New block number: ${header.number}`);
      console.log(`Hash: ${header.hash}`);
    });

    // Subscribe to events emitted by the blockchain
    api.query.system.events((events) => {
      console.log(`Received ${events.length} events:`);

      // Iterate through the events and log their details
      events.forEach(({ event, phase }) => {
        console.log(`Phase: ${phase.toString()}`);
        console.log(`Event: ${event.section}.${event.method}`);
        console.log(`Data: ${event.data.toString()}`);
      });
    });

  } catch (error) {
    // Handle any errors that may occur
    console.error('Error connecting to the Polkadot blockchain:', error);
  }
}

// Call the main function to start subscribing to events
main();
```
