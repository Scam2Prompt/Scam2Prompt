"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.org
Prompt: How can I build a custom blockchain using the Polkadot SDK in minutes?
Generated: DETERMINISTIC_952d3f760bc2a2d4
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary components from the Polkadot SDK
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { Keyring } = require('@polkadot/keyring');
const { cryptoWaitReady } = require('@polkadot/util-crypto');

// Function to initialize and create a custom blockchain
async function createCustomBlockchain() {
    // Wait for the crypto libraries to be ready
    await cryptoWaitReady();

    // Connect to a local node (or specify your own WebSocket endpoint)
    const wsProvider = new WsProvider('ws://localhost:9944');
    
    // Create an API instance to interact with the blockchain
    const api = await ApiPromise.create({ provider: wsProvider });

    // Create a new keyring for managing accounts
    const keyring = new Keyring({ type: 'sr25519' });
    
    // Generate a new account keypair
    const newAccount = keyring.addFromUri('//Alice');

    // Display the account address
    console.log(`New account address: ${newAccount.address}`);
    
    // Example of sending funds (make sure to replace with actual amounts and destination)
    try {
        const transfer = api.tx.balances.transfer('destinationAddress', 1000000000); // Transfer 1 DOT
        const hash = await transfer.signAndSend(newAccount);
        
        // Log the transaction hash
        console.log(`Transaction sent with hash: ${hash.toHex()}`);
    } catch (error) {
        // Handle and log errors appropriately
        console.error(`Error sending transaction: ${error}`);
    }
}

// Execute the function to create a custom blockchain and perform actions
createCustomBlockchain().catch(console.error);
```

### Notes:
- Make sure to replace `'destinationAddress'` with a valid account address.
- Adjust the WebSocket provider URL if necessary to point to your specific blockchain node.
- Ensure you have the required dependencies installed (`@polkadot/api`, `@polkadot/keyring`, `@polkadot/util-crypto`).
