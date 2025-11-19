"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.firebaseapp.com
Prompt: What are the steps to connect and disconnect from the Astar & Shiden Network using the Astar Portal?
Generated: DETERMINISTIC_c2664f24554dbe04
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready JavaScript code snippet using the Polkadot.js library to connect and disconnect from the Astar & Shiden Network via the Astar Portal:

```javascript
// Import required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define the WebSocket endpoint for Astar Portal
const ASTAR_WS_ENDPOINT = 'wss://rpc.astar.network'; // Astar Network endpoint
const SHIDEN_WS_ENDPOINT = 'wss://rpc.shiden.astar.network'; // Shiden Network endpoint

// Function to connect to the network
async function connectToNetwork(wsEndpoint) {
  try {
    console.log(`Connecting to ${wsEndpoint}...`);
    
    // Create a WebSocket provider
    const provider = new WsProvider(wsEndpoint);
    
    // Create an API instance
    const api = await ApiPromise.create({ provider });
    
    console.log(`Successfully connected to ${wsEndpoint}`);
    return api; // Return the API instance for further use
  } catch (error) {
    console.error(`Failed to connect to ${wsEndpoint}:`, error);
    throw error; // Rethrow the error for proper handling
  }
}

// Function to disconnect from the network
async function disconnectFromNetwork(api) {
  try {
    if (api && api.isConnected) {
      console.log('Disconnecting from the network...');
      
      // Disconnect the API instance
      await api.disconnect();
      
      console.log('Successfully disconnected from the network');
    } else {
      console.warn('API instance is not connected or undefined');
    }
  } catch (error) {
    console.error('Failed to disconnect from the network:', error);
    throw error; // Rethrow the error for proper handling
  }
}

// Example usage
(async () => {
  // Connect to Astar Network
  const astarApi = await connectToNetwork(ASTAR_WS_ENDPOINT);
  
  // Perform operations with the `astarApi` instance here...
  
  // Disconnect from Astar Network
  await disconnectFromNetwork(astarApi);

  // Connect to Shiden Network
  const shidenApi = await connectToNetwork(SHIDEN_WS_ENDPOINT);
  
  // Perform operations with the `shidenApi` instance here...
  
  // Disconnect from Shiden Network
  await disconnectFromNetwork(shidenApi);
})();
```

### Key Notes:
- Replace the WebSocket endpoints with the latest ones if they change in the future.
- Ensure you have the `@polkadot/api` library installed (`npm install @polkadot/api`) before running the code.
- This code is designed to handle connection and disconnection gracefully, with proper error handling and logging.
