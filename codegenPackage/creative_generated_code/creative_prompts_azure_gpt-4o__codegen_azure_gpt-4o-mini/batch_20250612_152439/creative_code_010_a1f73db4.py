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
// Import necessary modules from LavaSDK
import { LavaSDK, StarkNet } from '@lava-labs/sdk';

// Define async function to retrieve the latest block number from StarkNet
async function getLatestBlockNumber(): Promise<number | null> {
    try {
        // Initialize LavaSDK with your API key (replace 'YOUR_API_KEY' with your actual API key)
        const lava = new LavaSDK({
            apiKey: 'YOUR_API_KEY',
            network: 'starknet', // Specify the network
        });

        // Create an instance of StarkNet using the LavaSDK
        const starkNet = lava.getStarkNet();

        // Retrieve the latest block number
        const latestBlock = await starkNet.getBlock();

        // Check if latestBlock is defined and return the block number
        if (latestBlock && latestBlock.number) {
            console.log(`Latest Block Number: ${latestBlock.number}`);
            return latestBlock.number;
        } else {
            console.error('Failed to retrieve the latest block number.');
            return null;
        }
    } catch (error) {
        // Handle errors that occur during the API call
        console.error('Error fetching the latest block number:', error);
        return null;
    }
}

// Call the function and log the result
getLatestBlockNumber().then(blockNumber => {
    if (blockNumber !== null) {
        console.log(`Block Number Retrieved: ${blockNumber}`);
    } else {
        console.log('No block number retrieved.');
    }
});
```
