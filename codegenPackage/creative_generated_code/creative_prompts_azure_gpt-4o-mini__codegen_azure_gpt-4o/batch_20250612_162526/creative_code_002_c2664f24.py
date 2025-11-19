"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-apps.firebaseapp.com
Prompt: What are the steps to connect and disconnect from the Astar & Shiden Network using the Astar Portal?
Generated: DETERMINISTIC_c2664f24554dbe04
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a JavaScript/TypeScript code snippet leveraging the Polkadot.js API to connect and disconnect from the Astar & Shiden Network using the Astar Portal. This code assumes you have Node.js installed and the `@polkadot/api` package available.

```typescript
// Import the Polkadot.js API library
import { ApiPromise, WsProvider } from '@polkadot/api';

async function connectAstarPortal() {
  // The WebSocket URL for Astar & Shiden Network's RPC endpoint
  const ASTAR_WS_URL = 'wss://rpc.astar.network';
  const SHIDEN_WS_URL = 'wss://rpc.shiden.astar.network';

  let api: ApiPromise;

  try {
    // Step 1: Initialize a WebSocket provider for the desired network
    const wsProvider = new WsProvider(ASTAR_WS_URL); // Use SHIDEN_WS_URL for Shiden Network

    // Step 2: Create an instance of the Polkadot.js API
    api = await ApiPromise.create({ provider: wsProvider });

    console.log('Successfully connected to Astar Portal.');

    // Step 3: Perform operations using the API instance
    // Example: Fetch chain information
    const chain = await api.rpc.system.chain();
    const lastHeader = await api.rpc.chain.getHeader();

    console.log(`Connected to chain: ${chain}`);
    console.log(`Last block number: ${lastHeader.number}`);

    return api; // Return the API instance for further usage
  } catch (error) {
    console.error('Failed to connect to Astar Portal:', error.message);

    // Gracefully handle connection errors
    throw new Error('Connection Error');
  }
}

async function disconnectAstarPortal(api: ApiPromise) {
  if (!api) {
    console.warn('API instance not provided for disconnection.');
    return;
  }

  try {
    // Step 4: Disconnect the API instance
    await api.disconnect();
    console.log('Successfully disconnected from Astar Portal.');
  } catch (error) {
    console.error('Error while disconnecting:', error.message);

    // Gracefully handle disconnection errors
    throw new Error('Disconnection Error');
  }
}

// Example usage
(async () => {
  let api: ApiPromise;

  try {
    // Connect to the Astar Network
    api = await connectAstarPortal();

    // Perform network operations or interactions here...

  } finally {
    // Disconnect to avoid resource leaks
    await disconnectAstarPortal(api);
  }
})();
```

### Notes:
1. Ensure you have installed the required dependencies before running:
   ```bash
   npm install @polkadot/api
   ```
2. Replace `ASTAR_WS_URL` with `SHIDEN_WS_URL` if you want to connect to Shiden Network.

This code handles connection and disconnection with proper error handling while adhering to best practices.
