"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-apps.web.app
Prompt: What are the steps to set up a light client for the Astar & Shiden Network in my application?
Generated: DETERMINISTIC_fe7533475d4f72bc
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code to set up a light client for the Astar & Shiden Network using JavaScript and the Polkadot.js library:

```javascript
// Import the required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

async function setupLightClient() {
  try {
    // Step 1: Define the WebSocket endpoint for the Astar or Shiden network
    const ASTAR_WS_ENDPOINT = 'wss://rpc.astar.network';
    const SHIDEN_WS_ENDPOINT = 'wss://rpc.shiden.astar.network';

    // Choose the appropriate endpoint (you can swap between Astar or Shiden)
    const wsProvider = new WsProvider(ASTAR_WS_ENDPOINT); // Change to SHIDEN_WS_ENDPOINT for Shiden

    // Step 2: Create an instance of the API
    const api = await ApiPromise.create({ provider: wsProvider });

    // Step 3: Verify that the connection is established successfully
    const chainInfo = await api.rpc.system.chain();
    const nodeVersion = await api.rpc.system.version();
    console.log(`Connected to ${chainInfo} using node version ${nodeVersion}`);

    // Now the light client is ready to interact with the network!
    return api;
  } catch (error) {
    // Handle errors gracefully
    console.error('Error during light client setup:', error);
    throw error; // Rethrow error to allow the caller to handle it
  }
}

// Example usage
(async () => {
  const api = await setupLightClient();

  // Perform network interactions (e.g., query balance, send transactions, etc.)
  // Example: Query the latest block number
  const latestBlockNumber = await api.rpc.chain.getHeader();
  console.log(`Latest block number: ${latestBlockNumber.number}`);

  // Disconnect the API when done
  await api.disconnect();
})();
```

### Key Notes:
- Replace `ASTAR_WS_ENDPOINT` with `SHIDEN_WS_ENDPOINT` if you wish to connect to the Shiden network.
- Ensure that the `@polkadot/api` package is installed in your project (`npm install @polkadot/api`).
- The code includes error handling for network connection issues.
