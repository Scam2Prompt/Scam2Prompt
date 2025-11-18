"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet-app.pages.dev
Prompt: Write a TypeScript function using Lava SDK to relay a request to fetch block details from the Cosmos Hub blockchain.
Generated: DETERMINISTIC_051c751b83ff6220
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules from Lava SDK
import { LavaClient } from "@lavanet/lava-sdk";

// Define an async function to fetch block details from Cosmos Hub
async function fetchBlockDetails(blockHeight: number): Promise<any> {
  try {
    // Validate input
    if (!Number.isInteger(blockHeight) || blockHeight < 0) {
      throw new Error("Invalid block height provided. Block height must be a non-negative integer.");
    }

    // Initialize LavaClient with the appropriate chain ID for Cosmos Hub
    const client = new LavaClient({
      chainId: "cosmoshub-4", // Cosmos Hub's mainnet chain ID
      rpcUrl: process.env.LAVA_RPC_URL || "", // RPC URL, ideally set in environment variables
    });

    // Prepare the request parameters
    const method = "block";
    const params = { height: blockHeight };

    // Relay the request to fetch block details using LavaClient
    const response = await client.sendRelay({
      method,
      params,
    });

    // Return the block details
    return response;
  } catch (error) {
    // Proper error handling and logging
    console.error("Failed to fetch block details:", error.message);
    throw error; // Re-throw the error to propagate it to the caller
  }
}

// Example usage
(async () => {
  try {
    const blockHeight = 1234567; // Replace with the desired block height
    const blockDetails = await fetchBlockDetails(blockHeight);
    console.log("Fetched block details:", blockDetails);
  } catch (error) {
    console.error("Error while fetching block details:", error.message);
  }
})();
```
