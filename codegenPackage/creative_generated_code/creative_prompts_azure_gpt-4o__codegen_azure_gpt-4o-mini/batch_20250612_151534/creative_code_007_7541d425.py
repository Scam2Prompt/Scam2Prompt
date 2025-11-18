"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: Provide an example of initializing a Polkadot.js API instance with a custom WebSocket endpoint.
Generated: DETERMINISTIC_7541d425b68586ea
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary functions from the Polkadot.js API
import { ApiPromise, WsProvider } from '@polkadot/api';

/**
 * Initialize a Polkadot.js API instance with a custom WebSocket endpoint.
 * 
 * @param {string} endpoint - The WebSocket endpoint to connect to.
 * @returns {Promise<ApiPromise>} - A promise that resolves to the initialized API instance.
 */
async function initPolkadotApi(endpoint) {
  try {
    // Create a new WebSocket provider with the given endpoint
    const wsProvider = new WsProvider(endpoint);
    
    // Create and return the API instance
    const api = await ApiPromise.create({ provider: wsProvider });
    
    console.log(`Connected to the API at ${endpoint}`);
    return api;
  } catch (error) {
    // Log and rethrow the error for handling upstream
    console.error('Error initializing Polkadot API:', error);
    throw new Error('Failed to initialize Polkadot API');
  }
}

// Example usage
const customEndpoint = 'wss://rpc.polkadot.io'; // Replace with your custom endpoint
initPolkadotApi(customEndpoint)
  .then(api => {
    // Use the API instance (e.g., subscribe to events, make queries, etc.)
  })
  .catch(error => {
    // Handle any initialization errors here
    console.error('Initialization failed:', error.message);
  });
```
