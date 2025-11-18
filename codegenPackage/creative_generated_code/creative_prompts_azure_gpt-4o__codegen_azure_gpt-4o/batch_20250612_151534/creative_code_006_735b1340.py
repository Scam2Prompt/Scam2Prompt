"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: Write a function using Polkadot.js to decode and display metadata from the Polkadot blockchain.
Generated: DETERMINISTIC_735b13400d5af0c8
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Polkadot.js library
const { ApiPromise, WsProvider } = require('@polkadot/api');

/**
 * Function to decode and display metadata from the Polkadot blockchain.
 * 
 * @param {string} wsEndpoint - The WebSocket endpoint of the Polkadot node.
 */
async function displayMetadata(wsEndpoint) {
  try {
    // Establish connection to the Polkadot node using WebSocket endpoint
    const provider = new WsProvider(wsEndpoint);
    const api = await ApiPromise.create({ provider });

    // Fetch metadata from the chain
    const metadata = await api.rpc.state.getMetadata();

    // Decode and display the metadata
    console.log('Chain Metadata:');
    console.log(metadata.toHuman());

    // Gracefully disconnect from the provider
    await api.disconnect();
  } catch (error) {
    // Error handling for any issues during connection or metadata retrieval
    console.error('Error while fetching metadata:', error.message);
  }
}

// Example usage:
// Replace 'wss://rpc.polkadot.io' with the WebSocket endpoint of your desired Polkadot node
displayMetadata('wss://rpc.polkadot.io');
```
