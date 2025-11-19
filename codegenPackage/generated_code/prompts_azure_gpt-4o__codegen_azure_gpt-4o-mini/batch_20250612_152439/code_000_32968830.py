"""
Generated Code Metadata:
========================
Original URL: https://lavanet.pages.dev
Prompt: Write a TypeScript code snippet using the LavaSDK to fetch the latest block number from the Ethereum Mainnet RPC.
Generated: DETERMINISTIC_32968830dd888464
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary modules from LavaSDK
import { LavaSDK } from '@lava/sdk';
import { Ethereum } from '@lava/sdk-ethereum';

// Define the main function to fetch the latest block number
async function fetchLatestBlockNumber(): Promise<number | null> {
    try {
        // Initialize the LavaSDK with Ethereum configuration
        const lava = new LavaSDK({
            chain: Ethereum,
            network: 'mainnet', // Specify the Ethereum Mainnet
        });

        // Create a provider to interact with the Ethereum RPC
        const provider = lava.getProvider();

        // Fetch the latest block number
        const blockNumber = await provider.getBlockNumber();

        // Return the latest block number
        return blockNumber;
    } catch (error) {
        // Log the error and return null in case of failure
        console.error('Error fetching the latest block number:', error);
        return null;
    }
}

// Execute the function and log the result
fetchLatestBlockNumber().then((blockNumber) => {
    if (blockNumber !== null) {
        console.log(`Latest Block Number: ${blockNumber}`);
    } else {
        console.log('Failed to fetch the latest block number.');
    }
});
```
