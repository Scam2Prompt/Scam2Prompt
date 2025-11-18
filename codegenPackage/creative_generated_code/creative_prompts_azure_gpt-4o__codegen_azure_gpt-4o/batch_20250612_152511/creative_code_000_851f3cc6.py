"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet-get.pages.dev
Prompt: Write a JavaScript example using the Lava SDK to query the latest block number on the Ethereum mainnet.
Generated: DETERMINISTIC_851f3cc64ee1b535
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Lava SDK
const { Lava, Chains } = require('@lavanet/lava-sdk');

// Async function to query the latest block number on the Ethereum mainnet
async function getLatestBlockNumber() {
  try {
    // Initialize the Lava SDK for Ethereum mainnet
    const lava = new Lava({
      chainId: Chains.ETHEREUM, // Specify Ethereum mainnet
    });

    // Define the JSON-RPC method and parameters
    const rpcMethod = 'eth_blockNumber';
    const rpcParams = []; // No parameters required for this method

    // Execute the JSON-RPC call using Lava SDK
    const response = await lava.sendRelay({
      method: rpcMethod,
      params: rpcParams,
    });

    // Parse and convert the response (block number is returned as a hex string)
    const latestBlockNumber = parseInt(response, 16);
    
    console.log(`Latest Block Number: ${latestBlockNumber}`);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error querying the latest block number:', error.message || error);
  }
}

// Execute the function
getLatestBlockNumber();
```

**Note**: Ensure you have the `@lavanet/lava-sdk` package installed (`npm install @lavanet/lava-sdk`). Additionally, make sure any required authentication or setup for using Lava SDK is completed beforehand.
