"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet.pages.dev
Prompt: Write a TypeScript example using LavaSDK to interact with the StarkNet blockchain and retrieve the latest block number.
Generated: DETERMINISTIC_a1f73db48b2e9b90
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
/**
 * Example script to interact with the StarkNet blockchain using LavaSDK
 * and retrieve the latest block number.
 */

import { LavaSDK } from "@lavanet/lava-sdk";

// Define the LavaSDK configuration
const LAVA_NETWORK = "starknet-mainnet"; // Use the desired StarkNet network
const LAVA_API_KEY = "<YOUR_LAVA_API_KEY>"; // Replace with your Lava API key

async function getLatestBlockNumber(): Promise<void> {
  try {
    // Initialize LavaSDK instance
    const lavaSdk = new LavaSDK({
      network: LAVA_NETWORK,
      apiKey: LAVA_API_KEY,
    });

    console.log("Connecting to StarkNet blockchain...");

    // Query the latest block information from the StarkNet blockchain
    const response = await lavaSdk.sendRelay({
      method: "starknet_blockNumber",
      params: [],
    });

    if (response && typeof response === "number") {
      console.log(`Latest block number: ${response}`);
    } else {
      console.error("Unexpected response format:", response);
    }
  } catch (error) {
    // Handle errors gracefully
    console.error("An error occurred while fetching the latest block number:", error);
  }
}

// Execute the script
getLatestBlockNumber();
```

**Note:**
- Replace `<YOUR_LAVA_API_KEY>` with your valid Lava API key.
- Ensure the `@lavanet/lava-sdk` package is installed by running `npm install @lavanet/lava-sdk`.
- This code assumes that StarkNet supports the `starknet_blockNumber` method via LavaSDK. Adjust the method name if required by LavaSDK or StarkNet.
