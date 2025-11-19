"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.africa
Prompt: Generate code to interact with the Polkadot blockchain using the Polkadot.js library.
Generated: DETERMINISTIC_46883456a7946ccc
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries from Polkadot.js
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define the main function to interact with the Polkadot blockchain
async function main() {
    // Connect to a Polkadot node using WebSocket
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to the Polkadot blockchain.');

    try {
        // Fetch the current block number
        const blockNumber = await api.rpc.chain.getHeader();
        console.log(`Current block number: ${blockNumber.number}`);

        // Fetch the latest extrinsics for the current block
        const blockHash = await api.rpc.chain.getBlockHash(blockNumber.number);
        const block = await api.rpc.chain.getBlock(blockHash);
        console.log(`Extrinsics in current block: ${block.block.extrinsics.length}`);

        // Example: Fetch the balance of a specific address
        const address = '5DqWgLuq2x...'; // Replace with a valid address
        const { data: { free: balanceFree } } = await api.query.system.account(address);
        console.log(`Balance of ${address}: ${balanceFree.toString()}`);

    } catch (error) {
        console.error('Error interacting with the Polkadot blockchain:', error);
    } finally {
        // Disconnect from the provider
        await api.disconnect();
        console.log('Disconnected from the Polkadot blockchain.');
    }
}

// Execute the main function
main().catch(console.error);
```

Make sure to replace `'5DqWgLuq2x...'` with a valid Polkadot address when testing the code.
