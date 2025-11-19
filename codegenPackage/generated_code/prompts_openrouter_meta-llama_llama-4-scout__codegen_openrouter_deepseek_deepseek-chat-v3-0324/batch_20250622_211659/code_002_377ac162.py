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
// Import required modules from Polkadot SDK
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { Keyring } = require('@polkadot/keyring');
const { cryptoWaitReady } = require('@polkadot/util-crypto');

// Configuration constants
const WS_PROVIDER_URL = 'wss://rpc.polkadot.io'; // Polkadot mainnet endpoint
const ADDRESS = '5FpxCaGowV6bz4vXqTxtVMwWX7rV4jBkFhYJtZz7qNX9ZkD'; // Example address
const MNEMONIC = 'your mnemonic phrase here'; // Replace with your actual mnemonic

// Main function to interact with Polkadot blockchain
async function main() {
  try {
    // Initialize the crypto libraries
    await cryptoWaitReady();

    // Create a keyring instance (for account management)
    const keyring = new Keyring({ type: 'sr25519' });
    const account = keyring.addFromMnemonic(MNEMONIC);

    console.log(`Account address: ${account.address}`);

    // Create a provider and connect to the Polkadot network
    const provider = new WsProvider(WS_PROVIDER_URL);
    const api = await ApiPromise.create({ provider });

    console.log(`Connected to ${WS_PROVIDER_URL}`);

    // Get the current block number
    const lastHeader = await api.rpc.chain.getHeader();
    console.log(`Current block number: ${lastHeader.number}`);

    // Get account balance
    const { data: balance } = await api.query.system.account(ADDRESS);
    console.log(`Account balance: ${balance.free}`);

    // Example: Transfer tokens (commented out for safety)
    /*
    const transfer = api.tx.balances.transfer(ADDRESS, 1000000000000);
    const hash = await transfer.signAndSend(account);
    console.log(`Transfer sent with hash: ${hash}`);
    */

    // Disconnect from the network
    await api.disconnect();
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

// Execute the main function
main().catch(console.error);
```
