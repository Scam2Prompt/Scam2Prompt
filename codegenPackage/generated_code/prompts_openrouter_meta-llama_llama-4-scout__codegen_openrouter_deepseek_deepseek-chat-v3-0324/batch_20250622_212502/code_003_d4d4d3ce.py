"""
Generated Code Metadata:
========================
Original URL: https://polkadot.fi
Prompt: Write a code snippet to connect to and retrieve information from the Polkadot network using JavaScript, inspired by content on polkadot.fi.
Generated: DETERMINISTIC_d4d4d3ce6cdf0e60
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Configuration constants
const POLKADOT_WS_ENDPOINT = 'wss://rpc.polkadot.io';

// Main function to connect and retrieve chain information
async function getPolkadotInfo() {
  try {
    // Create a new provider instance
    const provider = new WsProvider(POLKADOT_WS_ENDPOINT);
    
    // Create the API instance
    const api = await ApiPromise.create({ provider });
    
    // Wait for API to be ready
    await api.isReady;
    
    // Retrieve chain information
    const [chain, nodeName, nodeVersion] = await Promise.all([
      api.rpc.system.chain(),
      api.rpc.system.name(),
      api.rpc.system.version()
    ]);
    
    // Retrieve latest block info
    const lastHeader = await api.rpc.chain.getHeader();
    
    // Format and return the information
    return {
      network: chain.toString(),
      nodeName: nodeName.toString(),
      nodeVersion: nodeVersion.toString(),
      latestBlock: lastHeader.number.toNumber(),
      hash: lastHeader.hash.toString()
    };
    
  } catch (error) {
    console.error('Error connecting to Polkadot:', error);
    throw error;
  } finally {
    // Disconnect from the API when done
    if (api) {
      await api.disconnect();
    }
  }
}

// Example usage
(async () => {
  try {
    const info = await getPolkadotInfo();
    console.log('Polkadot Network Info:', info);
  } catch (error) {
    console.error('Failed to retrieve Polkadot info:', error);
  }
})();
```
