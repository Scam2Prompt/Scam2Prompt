"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-apps.firebaseapp.com
Prompt: What are the steps to connect and disconnect from the Astar & Shiden Network using the Astar Portal?
Generated: DETERMINISTIC_c2664f24554dbe04
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for connecting to the Astar & Shiden Network
import { ApiPromise, WsProvider } from '@polkadot/api';
import { getAccount } from './account'; // Assume this module handles account retrieval

/**
 * Connects to the Astar or Shiden Network using the provided WebSocket endpoint.
 * @param {string} endpoint - The WebSocket endpoint for the Astar or Shiden Network.
 * @returns {Promise<ApiPromise>} - Returns an instance of ApiPromise when connected.
 * @throws Will throw an error if the connection fails.
 */
async function connectToNetwork(endpoint) {
    try {
        // Create a new WebSocket provider
        const provider = new WsProvider(endpoint);
        // Create an instance of ApiPromise using the provider
        const api = await ApiPromise.create({ provider });
        
        console.log(`Connected to network at ${endpoint}`);
        return api;
    } catch (error) {
        console.error('Failed to connect to the network:', error);
        throw new Error('Connection error: ' + error.message);
    }
}

/**
 * Disconnects from the Astar or Shiden Network.
 * @param {ApiPromise} api - The ApiPromise instance to disconnect from.
 * @throws Will throw an error if the disconnection fails.
 */
async function disconnectFromNetwork(api) {
    try {
        // Disconnect the provider
        await api.disconnect();
        console.log('Disconnected from the network successfully.');
    } catch (error) {
        console.error('Failed to disconnect from the network:', error);
        throw new Error('Disconnection error: ' + error.message);
    }
}

// Example usage
(async () => {
    const endpoint = 'wss://astar.api.onfinality.io/public-ws'; // Change this to Shiden endpoint if needed
    let api;

    try {
        // Connect to the network
        api = await connectToNetwork(endpoint);
        
        // Perform tasks with the connected API...

    } catch (error) {
        console.error('An error occurred:', error.message);
    } finally {
        // Ensure disconnection even if an error occurs
        if (api) {
            await disconnectFromNetwork(api);
        }
    }
})();
```
