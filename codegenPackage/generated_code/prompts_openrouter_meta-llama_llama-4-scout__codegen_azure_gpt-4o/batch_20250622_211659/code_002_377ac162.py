"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Generate a code example for building a Polkadot-based blockchain application using the Polkadot SDK and JavaScript.
Generated: DETERMINISTIC_377ac16290e5fc5e
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules from Polkadot.js
const { ApiPromise, WsProvider, Keyring } = require('@polkadot/api');

// Define the WebSocket endpoint for connecting to a Polkadot node
const WS_ENDPOINT = 'wss://rpc.polkadot.io';

// Main function to initialize the Polkadot API and perform blockchain operations
async function main() {
  try {
    // Connect to the Polkadot node via WebSocket
    const provider = new WsProvider(WS_ENDPOINT);
    const api = await ApiPromise.create({ provider });

    console.log('Connected to Polkadot blockchain.');

    // Query the latest block number
    const latestBlock = await api.rpc.chain.getHeader();
    console.log(`Latest block number: ${latestBlock.number}`);

    // Create a keyring instance for managing accounts
    const keyring = new Keyring({ type: 'sr25519' });

    // Add an account to the keyring (example: Alice's account)
    const alice = keyring.addFromUri('//Alice');
    console.log(`Alice's address: ${alice.address}`);

    // Example: Transfer DOT tokens from Alice to another account
    const recipientAddress = '5F3sa2TJAWMqDhXG6jhV4N8ko9rE8V9Y2z1z2w7Z3z3z3z3z'; // Replace with a valid address
    const transferAmount = 10000000000; // Amount in Planck (1 DOT = 10^10 Planck)

    // Create and sign the transaction
    const transfer = api.tx.balances.transfer(recipientAddress, transferAmount);
    const hash = await transfer.signAndSend(alice);

    console.log(`Transfer successful. Transaction hash: ${hash}`);

    // Disconnect from the Polkadot node
    await api.disconnect();
    console.log('Disconnected from Polkadot blockchain.');
  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred:', error);
  }
}

// Execute the main function
main();
```
