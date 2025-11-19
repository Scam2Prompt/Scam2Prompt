"""
Generated Code Metadata:
========================
Original URL: https://polkadot-france.fr
Prompt: Suggest APIs or SDKs for monitoring Polkadot transactions in real-time, referencing the technical details provided on Polkadot France.
Generated: DETERMINISTIC_737eae4bebe2f4a3
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Polkadot Real-Time Transaction Monitoring

Below is an example of how you can monitor Polkadot transactions in real-time using the Polkadot API and the `polkadot-api` SDK.

#### Prerequisites

* Node.js (14 or higher)
* npm or yarn

#### Installation

```bash
npm install @polkadot/api
```

#### Code

```javascript
// Import required modules
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define constants
const POLKADOT_WS_PROVIDER = 'wss://rpc.polkadot.io'; // Polkadot WS provider

// Create a new instance of the Polkadot API
async function createPolkadotApi() {
  try {
    // Create a new WS provider
    const wsProvider = new WsProvider(POLKADOT_WS_PROVIDER);

    // Create a new Polkadot API instance
    const api = await ApiPromise.create({ provider: wsProvider });

    return api;
  } catch (error) {
    console.error('Error creating Polkadot API instance:', error);
    process.exit(1);
  }
}

// Monitor transactions in real-time
async function monitorTransactions() {
  try {
    // Create a new Polkadot API instance
    const api = await createPolkadotApi();

    // Subscribe to new transactions
    const unsub = await api.rpc.chain.subscribeNewHeads(async (header) => {
      try {
        // Get the block number and hash
        const blockNumber = header.number.toString();
        const blockHash = header.hash.toString();

        // Get the block transactions
        const block = await api.rpc.chain.getBlock(blockHash);
        const transactions = block.block.extrinsics;

        // Process each transaction
        transactions.forEach((transaction) => {
          const txHash = transaction.hash.toString();
          const txBytes = transaction.toHex();

          console.log(`New transaction detected:
            Block Number: ${blockNumber}
            Block Hash: ${blockHash}
            Transaction Hash: ${txHash}
            Transaction Bytes: ${txBytes}
          `);
        });
      } catch (error) {
        console.error('Error processing block:', error);
      }
    });

    // Unsubscribe from the subscription when the process exits
    process.on('exit', () => {
      unsub();
    });
  } catch (error) {
    console.error('Error monitoring transactions:', error);
    process.exit(1);
  }
}

// Run the transaction monitoring function
monitorTransactions();
```
