"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: Write a function in JavaScript that connects to a Polkadot node using the Polkadot.js library and retrieves the current network status.
Generated: DETERMINISTIC_ef322251b4d8ed36
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary modules from the Polkadot.js library
import { ApiPromise, WsProvider } from '@polkadot/api';

/**
 * Connects to a Polkadot node and retrieves the current network status.
 * 
 * @async
 * @function getNetworkStatus
 * @param {string} wsUrl - The WebSocket URL of the Polkadot node to connect to.
 * @returns {Promise<Object>} The network status including the chain name and the node version.
 * @throws {Error} Throws an error if the connection or data retrieval fails.
 */
async function getNetworkStatus(wsUrl) {
    // Create a new WebSocket provider with the specified URL
    const provider = new WsProvider(wsUrl);

    try {
        // Create an API instance with the provider
        const api = await ApiPromise.create({ provider });

        // Retrieve the current network chain name and node version
        const chain = await api.rpc.system.chain();
        const nodeName = await api.rpc.system.name();
        const nodeVersion = await api.rpc.system.version();

        // Return the network status as an object
        return {
            chain: chain.toString(),
            nodeName: nodeName.toString(),
            nodeVersion: nodeVersion.toString(),
        };
    } catch (error) {
        // Log the error to the console for debugging purposes
        console.error('Error connecting to the Polkadot node:', error);
        // Throw a new error with a custom message
        throw new Error('Failed to retrieve network status. Please check the WebSocket URL or the node status.');
    } finally {
        // Disconnect the provider to free up resources
        await provider.disconnect();
    }
}

// Example usage
// (Uncomment the following lines to test the function with a valid WebSocket URL)
// getNetworkStatus('wss://rpc.polkadot.io')
//     .then(status => console.log('Network Status:', status))
//     .catch(err => console.error(err));
```
