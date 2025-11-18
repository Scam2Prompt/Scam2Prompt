"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-france.fr
Prompt: Provide a code snippet to interact with Kusama's blockchain using the Polkadot.js library, focusing on querying active accounts and transactions as discussed on Polkadot France.
Generated: DETERMINISTIC_b687b0b8d8c2ec32
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries from Polkadot.js
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Async function to interact with the Kusama blockchain
async function main() {
  // Define the WebSocket provider (Kusama endpoint)
  const wsProvider = new WsProvider('wss://kusama-rpc.polkadot.io');

  try {
    // Create an API instance and connect to the blockchain
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to Kusama blockchain.');

    // Fetch the current block number (best finalized block)
    const blockHeader = await api.rpc.chain.getHeader();
    console.log(`Current block number: ${blockHeader.number}`);

    // Query system information to get all active accounts
    const activeAccounts = await api.query.system.account.entries();
    console.log(`Total active accounts: ${activeAccounts.length}`);

    // Loop through and display active account addresses (limited to first 10 for brevity)
    activeAccounts.slice(0, 10).forEach(([key, value], index) => {
      const accountAddress = key.args[0].toString();
      const accountInfo = value.toHuman();
      console.log(`Account ${index + 1}: ${accountAddress}`);
      console.log(`Account Info: ${JSON.stringify(accountInfo)}`);
    });

    // Query the current transaction pool
    const txPool = await api.rpc.author.pendingExtrinsics();
    console.log(`Number of pending transactions: ${txPool.length}`);

    // Display details of pending transactions (limited to first 5 for brevity)
    txPool.slice(0, 5).forEach((tx, index) => {
      console.log(`Transaction ${index + 1}: ${tx.toHuman()}`);
    });

    // Close the connection to free resources
    await api.disconnect();
    console.log('Disconnected from Kusama blockchain.');
  } catch (error) {
    // Handle any errors that occur
    console.error('An error occurred:', error);
  }
}

// Run the main function
main();
```
