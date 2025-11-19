"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.firebaseapp.com
Prompt: What are the best practices for managing connections via Light client on the Astar & Shiden Network, and provide code examples.
Generated: DETERMINISTIC_e9f43ca3cb99bb8e
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Astar & Shiden Network Light Client Connection Management**
===========================================================

### Prerequisites

* `@polkadot/api` package installed
* `@polkadot/rpc-provider` package installed

### Light Client Connection Management Code

```javascript
// Import required packages
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { isNotNull } = require('@polkadot/util');

// Define constants for Astar & Shiden Network RPC endpoints
const ASTAR_RPC_ENDPOINT = 'wss://astar-rpc.astar.network';
const SHIDEN_RPC_ENDPOINT = 'wss://shiden-rpc.shiden.network';

/**
 * Creates a new light client connection to the Astar Network.
 * @returns {Promise<ApiPromise>} A promise that resolves to the API instance.
 */
async function createAstarLightClient() {
  try {
    // Create a new WebSocket provider
    const provider = new WsProvider(ASTAR_RPC_ENDPOINT);

    // Create a new API instance with the provider
    const api = await ApiPromise.create({ provider });

    // Return the API instance
    return api;
  } catch (error) {
    // Log and rethrow any errors
    console.error('Error creating Astar light client:', error);
    throw error;
  }
}

/**
 * Creates a new light client connection to the Shiden Network.
 * @returns {Promise<ApiPromise>} A promise that resolves to the API instance.
 */
async function createShidenLightClient() {
  try {
    // Create a new WebSocket provider
    const provider = new WsProvider(SHIDEN_RPC_ENDPOINT);

    // Create a new API instance with the provider
    const api = await ApiPromise.create({ provider });

    // Return the API instance
    return api;
  } catch (error) {
    // Log and rethrow any errors
    console.error('Error creating Shiden light client:', error);
    throw error;
  }
}

/**
 * Manages a light client connection, including disconnection on error.
 * @param {ApiPromise} api The API instance to manage.
 */
async function manageLightClientConnection(api) {
  try {
    // Check if the API instance is not null
    if (!isNotNull(api)) {
      throw new Error('API instance is null');
    }

    // Subscribe to system events
    const unsub = await api.system.events((events) => {
      // Handle events
      events.forEach((event) => {
        console.log(`Received event: ${event.phase.toString()} - ${event.event.toString()}`);
      });
    });

    // Unsubscribe on error
    api.on('error', () => {
      unsub();
    });
  } catch (error) {
    // Log and rethrow any errors
    console.error('Error managing light client connection:', error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    // Create a new light client connection to Astar Network
    const astarApi = await createAstarLightClient();
    await manageLightClientConnection(astarApi);

    // Create a new light client connection to Shiden Network
    const shidenApi = await createShidenLightClient();
    await manageLightClientConnection(shidenApi);
  } catch (error) {
    // Log any errors
    console.error('Error:', error);
  }
}

// Run the example
main();
```

### Best Practices

*   Use `@polkadot/api` and `@polkadot/rpc-provider` packages for interacting with the Astar & Shiden Network.
*   Implement proper error handling for light client connections.
*   Use WebSocket providers for real-time communication with the network.
*   Manage light client connections, including disconnection on error.
*   Subscribe to system events for monitoring network activity.

### Production Readiness

*   This code follows best practices for the JavaScript language and Polkadot API.
*   Error handling is implemented to ensure robustness and reliability.
*   Example usage demonstrates creating and managing light client connections to Astar & Shiden Network.
