"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.network
Prompt: How can I use the Polkadot library to create a decentralized application that interacts with multiple blockchains?
Generated: DETERMINISTIC_1159c523973428cc
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules from the Polkadot.js library
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Function to create and connect to multiple blockchain nodes
async function createMultiChainConnection(nodes) {
  try {
    // Create Promises for each node's connection
    const connections = nodes.map(async (nodeUrl) => {
      const provider = new WsProvider(nodeUrl); // WebSocket provider to connect to node
      const api = await ApiPromise.create({ provider }); // Create API instance
      return api; // Return API instance for interaction
    });

    // Resolve all connections
    const apis = await Promise.all(connections);

    console.log('Connected to all nodes successfully.');
    return apis; // Return API objects for further interaction
  } catch (error) {
    console.error('Error connecting to nodes:', error);
    throw error; // Properly propagate errors
  }
}

// Example function to interact with multiple blockchains
async function fetchChainData(apis) {
  try {
    const results = await Promise.all(
      apis.map(async (api, index) => {
        // Fetch system name and chain information for each node
        const systemName = await api.rpc.system.name();
        const chain = await api.rpc.system.chain();
        const version = await api.rpc.system.version();
        return {
          nodeIndex: index,
          systemName,
          chain,
          version,
        };
      })
    );

    console.log('Fetched chain data:', results);
    return results;
  } catch (error) {
    console.error('Error fetching chain data:', error);
    throw error; // Propagate errors
  }
}

// Main function for the decentralized application
async function main() {
  // Define WebSocket URLs for the blockchain nodes
  const nodeUrls = [
    'wss://rpc.polkadot.io', // Example Polkadot node
    'wss://kusama-rpc.polkadot.io', // Example Kusama node
  ];

  try {
    // Step 1: Connect to multiple blockchain nodes
    const apis = await createMultiChainConnection(nodeUrls);

    // Step 2: Fetch and log chain data
    const chainData = await fetchChainData(apis);

    // Optional: Perform further actions or process chainData as needed
    console.log('Chain data successfully retrieved:', chainData);

    // Disconnect from nodes when finished
    apis.forEach(async (api) => await api.disconnect());
    console.log('Disconnected from all nodes.');
  } catch (error) {
    console.error('An error occurred during execution:', error);
  }
}

// Execute the main function
main();
```
