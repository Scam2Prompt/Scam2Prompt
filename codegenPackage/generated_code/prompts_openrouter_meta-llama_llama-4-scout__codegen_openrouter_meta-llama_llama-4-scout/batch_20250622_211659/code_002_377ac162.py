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
// Import required modules
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { Keyring } = require('@polkadot/keyring');
const { mnemonicGenerate } = require('@polkadot/util-crypto');

// Set up Polkadot API endpoint
const endpoint = 'ws://localhost:9944';

// Set up keyring for account management
const keyring = new Keyring({ type: 'sr25519' });

// Function to generate a new account
function generateAccount() {
  // Generate a new mnemonic phrase
  const mnemonic = mnemonicGenerate(12);

  // Create a new keyring pair from the mnemonic phrase
  const pair = keyring.addFromMnemonic(mnemonic);

  return { mnemonic, pair };
}

// Function to connect to Polkadot API
async function connectToApi(endpoint) {
  try {
    // Create a new WebSocket provider
    const provider = new WsProvider(endpoint);

    // Create a new Polkadot API instance
    const api = await ApiPromise.create({ provider });

    return api;
  } catch (error) {
    console.error('Error connecting to Polkadot API:', error);
    process.exit(1);
  }
}

// Function to create a new extrinsic
async function createExtrinsic(api, account, recipient, amount) {
  try {
    // Get the current block hash
    const blockHash = await api.rpc.chain.getBlockHash();

    // Create a new extrinsic
    const extrinsic = api.tx.balances.transfer(recipient, amount);

    // Sign the extrinsic with the account
    const signedExtrinsic = await extrinsic.sign(account, { blockHash });

    return signedExtrinsic;
  } catch (error) {
    console.error('Error creating extrinsic:', error);
    process.exit(1);
  }
}

// Main function
async function main() {
  // Connect to Polkadot API
  const api = await connectToApi(endpoint);

  // Generate a new account
  const { mnemonic, pair } = generateAccount();
  console.log('Generated account:', pair.address);
  console.log('Mnemonic phrase:', mnemonic);

  // Set recipient and transfer amount
  const recipient = '0x...recipient_address...';
  const amount = 1000000000000; // 1 DOT

  // Create a new extrinsic
  const extrinsic = await createExtrinsic(api, pair, recipient, amount);

  // Submit the extrinsic
  try {
    const result = await api.rpc.author.submitExtrinsic(extrinsic);
    console.log('Extrinsic submitted:', result.toString());
  } catch (error) {
    console.error('Error submitting extrinsic:', error);
    process.exit(1);
  }

  // Close the Polkadot API connection
  await api.disconnect();
}

// Run the main function
main().catch((error) => {
  console.error('Error:', error);
  process.exit(1);
});
```
