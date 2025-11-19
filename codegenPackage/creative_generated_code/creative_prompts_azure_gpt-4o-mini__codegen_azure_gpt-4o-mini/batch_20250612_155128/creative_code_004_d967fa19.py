"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: What are the key features of the Polkadot.js library that make it suitable for blockchain development?
Generated: DETERMINISTIC_d967fa19cb393ea3
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script demonstrates the key features of the Polkadot.js library 
 * that make it suitable for blockchain development.
 * It establishes a connection to a Polkadot node and retrieves the latest block number.
 */

const { ApiPromise, WsProvider } = require('@polkadot/api');

async function main() {
    // Define the WebSocket provider URL (adjust as necessary)
    const wsProviderUrl = 'wss://rpc.polkadot.io';

    // Initialize the WebSocket provider
    const provider = new WsProvider(wsProviderUrl);

    try {
        // Create the API promise instance
        const api = await ApiPromise.create({ provider });

        // Output the connection status
        console.log('Connected to Polkadot node.');

        // Retrieve the latest block number
        const blockNumber = await api.rpc.chain.getHeader();
        console.log(`Latest block number: ${blockNumber.number}`);

        // Clean up and disconnect
        await api.disconnect();
        console.log('Disconnected from the node.');
    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred:', error);
    }
}

// Execute the main function
main().catch(error => {
    console.error('Execution failed:', error);
});
```
