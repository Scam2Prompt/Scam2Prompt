"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.web.app
Prompt: What are the steps to set up a light client for the Astar & Shiden Network in my application?
Generated: DETERMINISTIC_fe7533475d4f72bc
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for setting up a light client for Astar and Shiden networks using Polkadot.js API:

```javascript
// Import required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Network configurations
const NETWORKS = {
  astar: {
    name: 'Astar',
    wsEndpoint: 'wss://rpc.astar.network',
    types: {
      Address: 'MultiAddress',
      LookupSource: 'MultiAddress'
    }
  },
  shiden: {
    name: 'Shiden',
    wsEndpoint: 'wss://rpc.shiden.astar.network',
    types: {
      Address: 'MultiAddress',
      LookupSource: 'MultiAddress'
    }
  }
};

/**
 * Initialize light client connection to Astar or Shiden network
 * @param {string} network - 'astar' or 'shiden'
 * @returns {Promise<ApiPromise>} Polkadot.js API instance
 */
async function initLightClient(network) {
  try {
    if (!NETWORKS[network]) {
      throw new Error(`Unsupported network: ${network}. Use 'astar' or 'shiden'`);
    }

    const config = NETWORKS[network];
    console.log(`Connecting to ${config.name} network...`);

    // Initialize the provider
    const provider = new WsProvider(config.wsEndpoint);

    // Create the API instance
    const api = await ApiPromise.create({
      provider,
      types: config.types,
      // Light client options
      noInitWarn: true,
      throwOnConnect: false,
      throwOnUnknown: false
    });

    // Wait for connection
    await api.isReady;
    console.log(`Successfully connected to ${config.name} network`);

    return api;
  } catch (error) {
    console.error(`Error connecting to ${network}:`, error);
    throw error;
  }
}

/**
 * Disconnect from the network
 * @param {ApiPromise} api - Polkadot.js API instance
 */
async function disconnect(api) {
  try {
    if (api) {
      await api.disconnect();
      console.log('Disconnected from network');
    }
  } catch (error) {
    console.error('Error disconnecting:', error);
    throw error;
  }
}

// Example usage
(async () => {
  let api;
  try {
    // Connect to Astar network
    api = await initLightClient('astar');
    
    // Get chain info
    const [chain, nodeName, nodeVersion] = await Promise.all([
      api.rpc.system.chain(),
      api.rpc.system.name(),
      api.rpc.system.version()
    ]);
    
    console.log(`Connected to chain: ${chain}`);
    console.log(`Node: ${nodeName} v${nodeVersion}`);
    
    // Your application logic here
    
  } catch (error) {
    console.error('Application error:', error);
  } finally {
    if (api) {
      await disconnect(api);
    }
  }
})();
```
