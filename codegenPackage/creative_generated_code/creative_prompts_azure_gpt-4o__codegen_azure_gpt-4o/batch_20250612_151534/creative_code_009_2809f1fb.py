"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: How can Polkadot.js be used to query runtime constants from the Polkadot blockchain? Provide example code.
Generated: DETERMINISTIC_2809f1fba925ae5d
Batch ID: 20250612_151534
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

async function queryRuntimeConstants() {
  try {
    // Connect to a Polkadot node via WebSocket
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');
    const api = await ApiPromise.create({ provider: wsProvider });

    // Example: Query runtime constants from the Balances pallet
    // "existentialDeposit" is the minimum amount required to keep an account alive
    const existentialDeposit = api.consts.balances.existentialDeposit;

    // Log the runtime constant to the console
    console.log(`Existential Deposit: ${existentialDeposit.toHuman()}`);

    // Cleanup: Disconnect from the WebSocket provider
    await api.disconnect();
  } catch (error) {
    // Handle errors gracefully
    console.error('Error querying runtime constants:', error);
  }
}

// Execute the function
queryRuntimeConstants();
```
