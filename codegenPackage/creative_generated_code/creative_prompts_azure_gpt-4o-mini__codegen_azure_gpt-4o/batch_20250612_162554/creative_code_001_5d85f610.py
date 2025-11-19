"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www6.polkadot.net
Prompt: How can I use the Polkadot API to create a decentralized application that interacts with multiple blockchains?
Generated: DETERMINISTIC_5d85f6100a548fcc
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is clean and production-ready code for using the Polkadot API to create a decentralized application that interacts with multiple blockchains. The example demonstrates connecting to Polkadot and fetching data from multiple parachains.

```javascript
// Import necessary dependencies
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define a helper function to initialize connections to multiple blockchains
async function initializeApi(endpoint) {
  try {
    // Connect to the blockchain's WebSocket endpoint
    const provider = new WsProvider(endpoint);
    const api = await ApiPromise.create({ provider });

    console.log(`Connected to ${endpoint}`);
    return api;
  } catch (error) {
    console.error(`Failed to connect to ${endpoint}:`, error.message);
    throw error;
  }
}

// Define a function to fetch and display chain name and block number
async function fetchChainData(api) {
  try {
    // Retrieve chain name
    const chainName = await api.rpc.system.chain();
    // Retrieve the latest block number
    const lastBlock = await api.rpc.chain.getHeader();

    console.log(`Chain: ${chainName}, Last Block Number: #${lastBlock.number}`);
  } catch (error) {
    console.error('Error fetching chain data:', error.message);
    throw error;
  }
}

// Main function to interact with multiple blockchains
async function main() {
  // Define endpoints of blockchains to connect to
  const endpoints = [
    'wss://rpc.polkadot.io', // Polkadot relay chain
    'wss://kusama-rpc.polkadot.io', // Kusama relay chain
    // Add more endpoints as needed
  ];

  const apis = [];

  try {
    // Initialize API connections for all endpoints
    for (const endpoint of endpoints) {
      const api = await initializeApi(endpoint);
      apis.push(api);
    }

    // Fetch and display data from each connected blockchain
    for (const api of apis) {
      await fetchChainData(api);
    }
  } catch (error) {
    console.error('Error during blockchain interaction:', error.message);
  } finally {
    // Disconnect from all APIs
    for (const api of apis) {
      await api.disconnect();
    }
    console.log('Disconnected from all blockchains');
  }
}

// Run the main function
main().catch((error) => {
  console.error('Unexpected error:', error.message);
  process.exit(1); // Exit the process with an error code
});
```

### Notes:
1. This code assumes that you have Node.js installed and the `@polkadot/api` package set up. Install it using: `npm install @polkadot/api`.
2. Add more endpoints to the `endpoints` array to interact with additional blockchains.
3. Ensure proper security practices when deploying in production, such as sanitizing inputs and handling sensitive data carefully.
