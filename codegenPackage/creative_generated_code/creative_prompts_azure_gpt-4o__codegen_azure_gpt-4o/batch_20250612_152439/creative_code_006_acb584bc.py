"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanetwork.pages.dev
Prompt: Create a Node.js application that uses Lava SDK to interact with the Arbitrum mainnet RPC and fetch the latest block number.
Generated: DETERMINISTIC_acb584bcd8918aff
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Lava SDK library
const { LavaSDK } = require("@lavanet/lava-sdk");

// Import the dotenv library to handle environment variables
require("dotenv").config();

// Function to fetch the latest block number from the Arbitrum mainnet RPC
async function fetchLatestBlockNumber() {
  // Ensure the Lava API key is loaded from environment variables
  const lavaApiKey = process.env.LAVA_API_KEY;
  if (!lavaApiKey) {
    console.error("Error: LAVA_API_KEY is not set in the environment variables.");
    process.exit(1);
  }

  try {
    // Initialize the Lava SDK with the Arbitrum mainnet RPC
    const lava = new LavaSDK({
      chainId: "arbitrum", // Specify the chain ID for Arbitrum
      rpcInterface: "eth", // Specify the RPC interface (Ethereum-like)
      privKey: lavaApiKey, // Use the Lava API key for authentication
    });

    // Call the 'eth_blockNumber' method to fetch the latest block number
    const latestBlockHex = await lava.request("eth_blockNumber");

    // Convert the block number from hexadecimal to decimal
    const latestBlockNumber = parseInt(latestBlockHex, 16);

    console.log(`Latest block number on Arbitrum mainnet: ${latestBlockNumber}`);
  } catch (error) {
    // Handle errors gracefully
    console.error("Error fetching the latest block number:", error.message);
  }
}

// Entry point of the application
(async function () {
  await fetchLatestBlockNumber();
})();
```

### Prerequisites
1. Install dependencies:
   ```bash
   npm install @lavanet/lava-sdk dotenv
   ```

2. Set up a `.env` file in the root directory with your Lava API key:
   ```env
   LAVA_API_KEY=your_lava_api_key_here
   ```

3. Ensure Node.js is installed. This code is compatible with Node.js v12 or higher.
