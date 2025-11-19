"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.network
Prompt: Write a code snippet that demonstrates how to connect to the Polkadot network using its JavaScript API.
Generated: DETERMINISTIC_75229885706b26dd
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Polkadot.js API
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Asynchronously connect to the Polkadot network
async function connectToPolkadot() {
  try {
    // Define the WebSocket endpoint for the Polkadot network
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');

    // Create an instance of the API
    const api = await ApiPromise.create({ provider: wsProvider });

    // Verify the connection by retrieving the chain information
    const chain = await api.rpc.system.chain();
    const lastHeader = await api.rpc.chain.getHeader();

    // Log chain information and latest block header
    console.log(`Connected to chain: ${chain}`);
    console.log(`Last block number: ${lastHeader.number}`);
    console.log(`Block hash: ${lastHeader.hash}`);

    // Return the API instance for further use
    return api;
  } catch (error) {
    // Handle connection errors
    console.error('Failed to connect to the Polkadot network:', error);
    throw error;
  }
}

// Example usage: Connect to Polkadot and execute some logic
(async () => {
  try {
    const api = await connectToPolkadot();
    console.log('Connection successful! You can now interact with the Polkadot network.');
    
    // Perform additional actions with the `api` object if needed

    // Disconnect the API instance when done
    await api.disconnect();
    console.log('Disconnected from the Polkadot network.');
  } catch (error) {
    console.error('An error occurred:', error);
  }
})();
```
