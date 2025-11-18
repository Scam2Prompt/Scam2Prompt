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
// Import required modules from the Polkadot.js API package
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define the WebSocket endpoint for connecting to the Polkadot network
const customWsEndpoint = 'wss://custom-polkadot-endpoint.example.com';

// Initialize the Polkadot.js API instance
async function initializePolkadotAPI() {
  try {
    // Create a WebSocket provider with the custom endpoint
    const wsProvider = new WsProvider(customWsEndpoint);

    // Create an instance of the API using the WebSocket provider
    const api = await ApiPromise.create({ provider: wsProvider });

    // Log a success message
    console.log('Polkadot.js API initialized successfully.');
    
    // Return the API instance for further use
    return api;
  } catch (error) {
    // Handle any errors that occur during initialization
    console.error('Error initializing Polkadot.js API:', error);
    throw error; // Re-throw the error to signal failure
  }
}

// Example usage of the function
initializePolkadotAPI()
  .then((api) => {
    console.log('API is ready for use.');
    // Add logic here to interact with the Polkadot API
  })
  .catch((error) => {
    console.error('Failed to initialize the API:', error);
  });
```
