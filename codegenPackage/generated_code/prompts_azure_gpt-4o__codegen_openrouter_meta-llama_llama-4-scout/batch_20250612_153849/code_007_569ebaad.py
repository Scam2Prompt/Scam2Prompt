"""
Generated Code Metadata:
========================
Original URL: https://polkadot-live.app
Prompt: Suggest ways to use the Polkadot Live desktop client for testing and debugging Polkadot-based applications.
Generated: DETERMINISTIC_569ebaaddff686a9
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { Keyring } = require('@polkadot/keyring');
const { u8aToHex } = require('@polkadot/util');

// Set up Polkadot Live desktop client connection
async function connectToPolkadotLive() {
  try {
    // Establish a WebSocket connection to the Polkadot Live desktop client
    const wsProvider = new WsProvider('ws://localhost:9944');
    const api = await ApiPromise.create({ provider: wsProvider });

    return api;
  } catch (error) {
    console.error('Error connecting to Polkadot Live:', error);
    process.exit(1);
  }
}

// Set up a keyring for signing transactions
async function setupKeyring() {
  try {
    // Create a new keyring
    const keyring = new Keyring({ type: 'sr25519' });

    // Add a new account to the keyring
    const account = keyring.addFromUri('//Alice');

    return { keyring, account };
  } catch (error) {
    console.error('Error setting up keyring:', error);
    process.exit(1);
  }
}

// Test and debug Polkadot-based applications
async function testAndDebugApplications() {
  try {
    // Connect to Polkadot Live desktop client
    const api = await connectToPolkadotLive();

    // Get the current chain properties
    const chainProperties = await api.rpc.chain.getProperties();
    console.log('Chain Properties:', chainProperties);

    // Get the current chain metadata
    const chainMetadata = await api.rpc.metadata.getMetadata();
    console.log('Chain Metadata:', chainMetadata);

    // Set up a keyring for signing transactions
    const { keyring, account } = await setupKeyring();

    // Test a simple transaction (e.g., balance transfer)
    const tx = api.tx.balances.transfer(
      '0x...recipientAddress...',
      1000000000000
    );
    const signedTx = await tx.sign(account, { nonce: -1 });
    const txHash = await api.rpc.txpool.submitExtrinsic(u8aToHex(signedTx));
    console.log('Transaction Hash:', txHash);

  } catch (error) {
    console.error('Error testing and debugging applications:', error);
    process.exit(1);
  }
}

// Run the test and debug function
testAndDebugApplications();
```
