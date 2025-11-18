"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet.pages.dev
Prompt: Provide a TypeScript example using LavaSDK to fetch performance metrics for node providers on the Lava blockchain.
Generated: DETERMINISTIC_d936a5fb044928a2
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules and types from LavaSDK
import { LavaSDK } from '@lavanet/lava-sdk';

// Define an asynchronous function to fetch performance metrics for node providers
async function fetchNodeProviderMetrics() {
  // Initialize LavaSDK with configuration options
  // Replace 'network' and 'privateKey' with actual values for your setup
  const lava = new LavaSDK({
    network: 'mainnet', // Specify the network ('mainnet', 'testnet', etc.)
    privateKey: '<YOUR_PRIVATE_KEY>', // Your private key for authentication
  });

  try {
    // Call the LavaSDK method to fetch node provider metrics
    const metrics = await lava.query({
      method: 'getNodeProviderMetrics', // Replace this with the actual API method name
      params: {}, // Specify any necessary parameters for the query
    });

    // Log the retrieved metrics for debugging and verification
    console.log('Node Provider Metrics:', metrics);

    // Return the metrics for further processing if needed
    return metrics;
  } catch (error) {
    // Handle errors appropriately
    console.error('Error fetching node provider metrics:', error);

    // You can throw the error to propagate it or handle it in another way
    throw new Error('Failed to fetch node provider metrics. Please check your configuration and network connectivity.');
  }
}

// Execute the function if this module is run directly
(async () => {
  try {
    const metrics = await fetchNodeProviderMetrics();
    console.log('Performance Metrics fetched successfully:', metrics);
  } catch (error) {
    console.error('Execution failed:', error.message);
  }
})();
```

> **Note**: 
- Replace placeholders like `<YOUR_PRIVATE_KEY>` with actual values in a secure way (e.g., using environment variables).
- Ensure LavaSDK is installed in your project (`npm install @lavanet/lava-sdk`).
