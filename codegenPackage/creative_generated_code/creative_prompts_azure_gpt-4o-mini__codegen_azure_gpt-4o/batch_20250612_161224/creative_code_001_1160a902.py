"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet-get.pages.dev
Prompt: Write a JavaScript function using the Lava SDK to retrieve the latest block number from the Starknet chain.
Generated: DETERMINISTIC_1160a90252f78731
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Lava SDK
const LavaSDK = require("@lavanet/lava-sdk");

// Function to fetch the latest block number from the Starknet chain
async function getLatestBlockNumber() {
  try {
    // Initialize the Lava SDK client with the Starknet chain configuration
    const lavaClient = new LavaSDK({
      chainId: 'starknet-mainnet', // Use the appropriate chain ID
      privateKey: process.env.LAVA_PRIVATE_KEY, // Ensure the private key is stored securely as an environment variable
    });

    // Define the query to retrieve the latest block number
    const method = 'starknet_blockNumber'; // Starknet method for fetching the block number
    const params = []; // No parameters needed for this query

    // Fetch the latest block number using the Lava SDK
    const response = await lavaClient.sendRelay(method, params);

    // Parse and return the block number from the response
    const blockNumber = response.result;
    console.log(`Latest block number: ${blockNumber}`);
    return blockNumber;

  } catch (error) {
    // Handle any errors that occur during the process
    console.error('Error fetching the latest block number:', error.message);
    throw new Error('Failed to retrieve the latest block number. Please check the SDK configuration and your network connection.');
  }
}

// Example usage of the function
getLatestBlockNumber()
  .then((blockNumber) => {
    console.log(`Retrieved block number successfully: ${blockNumber}`);
  })
  .catch((err) => {
    console.error(`Error during execution: ${err.message}`);
  });

module.exports = { getLatestBlockNumber };
```
