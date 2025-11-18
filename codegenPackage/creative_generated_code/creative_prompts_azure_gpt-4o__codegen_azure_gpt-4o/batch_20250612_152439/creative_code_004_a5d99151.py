"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet-app.pages.dev
Prompt: Provide example code for routing multi-chain requests to Ethereum and Arbitrum using Lava SDK's chain abstraction feature.
Generated: DETERMINISTIC_a5d9915161047d0d
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Lava SDK
const { LavaRpcClient, createProvider } = require("@lavanet/lava-sdk");

// Configure Lava SDK clients for Ethereum and Arbitrum chains
async function initializeClients() {
  try {
    // Create Lava client for Ethereum chain
    const ethereumClient = await createProvider({
      chainId: "ethereum", // Specify the chain ID for Ethereum
      geolocation: "1",    // Geolocation is optional, set to default ("1")
    });

    // Create Lava client for Arbitrum chain
    const arbitrumClient = await createProvider({
      chainId: "arbitrum", // Specify the chain ID for Arbitrum
      geolocation: "1",    // Geolocation is optional, set to default ("1")
    });

    return { ethereumClient, arbitrumClient };
  } catch (error) {
    console.error("Error initializing Lava SDK clients:", error);
    throw error; // Rethrow error for higher-level handling
  }
}

// Function to route requests based on chain type
async function routeRequest(chain, method, params) {
  try {
    // Initialize clients for Ethereum and Arbitrum
    const { ethereumClient, arbitrumClient } = await initializeClients();

    // Determine which client to use based on the chain parameter
    let client;
    switch (chain.toLowerCase()) {
      case "ethereum":
        client = ethereumClient;
        break;
      case "arbitrum":
        client = arbitrumClient;
        break;
      default:
        throw new Error(`Unsupported chain: ${chain}`);
    }

    // Execute RPC method with the selected client
    const response = await client.sendRelay(method, params);
    return response; // Return the response from the RPC call

  } catch (error) {
    console.error(`Error routing request to ${chain}:`, error);
    throw error; // Rethrow error for higher-level handling
  }
}

// Example usage
async function main() {
  try {
    // Example: Query Ethereum chain for the latest block number
    const ethereumResponse = await routeRequest("ethereum", "eth_blockNumber", []);
    console.log("Ethereum Block Number:", ethereumResponse);

    // Example: Query Arbitrum chain for gas price
    const arbitrumResponse = await routeRequest("arbitrum", "eth_gasPrice", []);
    console.log("Arbitrum Gas Price:", arbitrumResponse);

  } catch (error) {
    console.error("Error in main function:", error);
  }
}

// Execute the main function
main();

```
