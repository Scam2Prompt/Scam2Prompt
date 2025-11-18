"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: Write JavaScript code using Polkadot.js to connect to a Polkadot blockchain node and retrieve the latest block information.
Generated: DETERMINISTIC_2eabba1938f8a3a0
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Polkadot.js API
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Function to connect to the Polkadot blockchain node and retrieve the latest block information
async function getLatestBlockInfo() {
  try {
    // Define the WebSocket endpoint of the blockchain node
    const wsProvider = new WsProvider('wss://rpc.polkadot.io'); // Replace with your specific node endpoint if needed

    // Create an instance of the API
    const api = await ApiPromise.create({ provider: wsProvider });

    // Retrieve the latest block information
    const latestHeader = await api.rpc.chain.getHeader();

    // Log the latest block information
    console.log('Latest Block Information:');
    console.log(`Block Number: ${latestHeader.number}`);
    console.log(`Block Hash: ${latestHeader.hash.toHex()}`);
    console.log(`Parent Hash: ${latestHeader.parentHash.toHex()}`);
    console.log(`State Root: ${latestHeader.stateRoot.toHex()}`);
    console.log(`Extrinsics Root: ${latestHeader.extrinsicsRoot.toHex()}`);

    // Disconnect the API (cleanup)
    await api.disconnect();
  } catch (error) {
    // Handle any errors that occur during connection or retrieval
    console.error('An error occurred while fetching the latest block information:', error);
  }
}

// Execute the function
getLatestBlockInfo();
```
