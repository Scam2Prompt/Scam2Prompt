"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet.pages.dev
Prompt: Write a TypeScript code snippet using the LavaSDK to fetch the latest block number from the Ethereum Mainnet RPC.
Generated: DETERMINISTIC_32968830dd888464
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import required modules from LavaSDK
import { LavaSDK } from "@lavanet/lava-sdk";

// Define an asynchronous function to fetch the latest block number
async function fetchLatestBlockNumber() {
  try {
    // Initialize the LavaSDK instance for Ethereum Mainnet RPC
    const lava = new LavaSDK({
      chainId: "eth-mainnet", // Specify the chain ID for Ethereum Mainnet
      privateKey: "<YOUR_PRIVATE_KEY>" // Replace with your Lava API private key
    });

    // Call the 'eth_blockNumber' method to get the latest block number
    const response = await lava.sendRelay({
      method: "eth_blockNumber",
      params: [] // No parameters required for this method
    });

    // Parse the block number returned in hex format to a decimal number
    const latestBlockNumber = parseInt(response, 16);

    // Log the latest block number to the console
    console.log("Latest Ethereum block number:", latestBlockNumber);

    return latestBlockNumber; // Return the block number for further use
  } catch (error) {
    // Handle any errors that occur during the API request
    console.error("Error fetching the latest block number:", error.message);
  }
}

// Execute the function
fetchLatestBlockNumber();
```

**Note:** Replace `<YOUR_PRIVATE_KEY>` with the actual private key provided by LavaSDK for authentication. Ensure you have installed the `@lavanet/lava-sdk` package in your project (`npm install @lavanet/lava-sdk`).
