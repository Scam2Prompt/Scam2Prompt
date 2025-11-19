"""
Generated Code Metadata:
========================
Original URL: https://astar-portal.vercel.app
Prompt: What are the steps to implement a light client connection in the Astar Portal, and how can I handle cancellations?
Generated: DETERMINISTIC_035efb08b7054f2e
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Function to initialize a light client connection to the Astar Portal
async function initializeLightClient(endpoint, onCancel) {
  // Validate the endpoint
  if (!endpoint || typeof endpoint !== 'string') {
    throw new Error('Invalid endpoint provided.');
  }

  // Create a WebSocket provider
  const provider = new WsProvider(endpoint);

  // Create a cancellation flag
  let isCancelled = false;

  // Attach cancellation handler
  if (typeof onCancel === 'function') {
    onCancel(() => {
      isCancelled = true;
      provider.disconnect(); // Disconnect the provider on cancellation
    });
  }

  try {
    // Initialize the API connection
    const api = await ApiPromise.create({ provider });

    // Check for cancellation before proceeding
    if (isCancelled) {
      throw new Error('Connection initialization cancelled.');
    }

    console.log('Light client connected successfully to Astar Portal.');

    // Return the API instance for further use
    return api;
  } catch (error) {
    // Handle errors during connection initialization
    console.error('Error initializing light client connection:', error.message);
    throw error;
  }
}

// Example usage
(async () => {
  // Define the endpoint for the Astar Portal
  const endpoint = 'wss://rpc.astar.network';

  // Define a cancellation handler
  let cancelConnection;
  const onCancel = (cancelFn) => {
    cancelConnection = cancelFn;
  };

  try {
    // Initialize the light client connection
    const api = await initializeLightClient(endpoint, onCancel);

    // Perform operations with the API instance
    console.log('API is ready:', api.isReady);

    // Simulate cancellation (for demonstration purposes)
    setTimeout(() => {
      console.log('Cancelling connection...');
      cancelConnection();
    }, 5000);
  } catch (error) {
    console.error('Failed to connect:', error.message);
  }
})();
```
