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
// Import necessary modules from LavaSDK
import { LavaSDK, PerformanceMetrics } from 'lava-sdk'; 

// Define the configuration for LavaSDK
const config = {
    network: 'mainnet',
    apiKey: 'YOUR_API_KEY', // Replace with your actual API key
};

// Initialize LavaSDK
const lava = new LavaSDK(config);

/**
 * Fetch performance metrics for node providers on the Lava blockchain.
 * @async
 * @returns {Promise<PerformanceMetrics[]>} Array of performance metrics for node providers.
 * @throws {Error} Throws an error if the API call fails.
 */
async function fetchNodeProviderMetrics(): Promise<PerformanceMetrics[]> {
    try {
        // Fetch performance metrics from the Lava blockchain
        const metrics = await lava.getPerformanceMetrics();
        return metrics;
    } catch (error) {
        // Handle errors during the API call
        console.error('Failed to fetch node provider metrics:', error);
        throw new Error('Unable to retrieve node provider metrics');
    }
}

// Example usage of the function
(async () => {
    try {
        const metrics = await fetchNodeProviderMetrics();
        console.log('Node Provider Performance Metrics:', metrics);
    } catch (error) {
        // Handle errors from the fetch function
        console.error('Error:', error.message);
    }
})();
```
