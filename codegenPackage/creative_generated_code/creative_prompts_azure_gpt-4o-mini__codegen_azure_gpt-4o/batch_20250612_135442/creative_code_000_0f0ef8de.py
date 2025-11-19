"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-snap-polkadot.pages.dev
Prompt: How can I create a Polkadot wallet Snap using MetaMask?
Generated: DETERMINISTIC_0f0ef8de174591ca
Batch ID: 20250612_135442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is clean, well-documented, production-ready code for creating a Polkadot wallet Snap using MetaMask. This assumes you have basic knowledge of MetaMask Snaps development and Polkadot's API. It is written in JavaScript and relies on the Polkadot.js library.

```javascript
// Import required dependencies
const { ApiPromise, WsProvider, Keyring } = require('@polkadot/api'); // Polkadot.js API for interacting with the Polkadot blockchain
const { SnapRPC } = require('@metamask/snaps-rpc'); // MetaMask Snaps RPC utility

// Define the Polkadot Snap
module.exports.onRpcRequest = async ({ origin, request }) => {
  try {
    switch (request.method) {
      // Handle wallet creation
      case 'polkadot_createWallet': {
        // Generate a new keypair using Polkadot.js
        const keyring = new Keyring({ type: 'sr25519' }); // Use sr25519 key type for Polkadot
        const newWallet = keyring.addFromUri(); // Generate a new wallet with a random mnemonic

        // Return wallet details (public key and address)
        return {
          publicKey: newWallet.publicKey.toString('hex'),
          address: newWallet.address,
        };
      }

      // Handle fetching Polkadot account balance
      case 'polkadot_getBalance': {
        const { address } = request.params; // Extract address from request parameters

        // Connect to Polkadot blockchain node
        const wsProvider = new WsProvider('wss://rpc.polkadot.io'); // Official Polkadot WebSocket endpoint
        const api = await ApiPromise.create({ provider: wsProvider });

        // Fetch balance for the given address
        const { data: balance } = await api.query.system.account(address);

        // Return balance in human-readable format
        return {
          free: balance.free.toString(),
          reserved: balance.reserved.toString(),
          miscFrozen: balance.miscFrozen.toString(),
          feeFrozen: balance.feeFrozen.toString(),
        };
      }

      // Handle signing a transaction
      case 'polkadot_signTransaction': {
        const { transaction, mnemonic } = request.params; // Extract transaction and mnemonic from request parameters

        // Generate keypair using mnemonic
        const keyring = new Keyring({ type: 'sr25519' });
        const wallet = keyring.addFromUri(mnemonic);

        // Sign the transaction
        const signedTransaction = wallet.sign(transaction);

        // Return the signed transaction
        return { signedTransaction };
      }

      default:
        throw new Error(`Method ${request.method} not supported.`);
    }
  } catch (error) {
    // Error handling: Log and return detailed error message
    console.error('Error occurred in Polkadot Snap:', error.message);
    throw new Error(`An error occurred: ${error.message}`);
  }
};
```

### Notes:
1. To use this code, ensure you have installed the required dependencies (`@polkadot/api` and `@metamask/snaps-rpc`).
2. Place this script in the MetaMask Snap project setup (`index.js` or equivalent).
3. Ensure the Snap manifest is configured correctly to expose these RPC methods.
4. Test thoroughly before deploying to production.
