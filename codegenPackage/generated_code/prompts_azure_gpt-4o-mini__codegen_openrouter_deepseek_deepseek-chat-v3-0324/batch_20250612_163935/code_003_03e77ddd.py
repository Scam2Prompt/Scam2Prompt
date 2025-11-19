"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Create a tutorial for Indian developers on building applications using Polkadot's ecosystem, inspired by the community initiatives highlighted on Polkadot India.
Generated: DETERMINISTIC_03e77dddf5b7c50d
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, well-commented JavaScript tutorial for building a basic Polkadot application using the `@polkadot/api` library:

```javascript
// Import required Polkadot libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Configuration constants
const WS_PROVIDER_URL = 'wss://rpc.polkadot.io'; // Mainnet endpoint
// For testing: 'wss://westend-rpc.polkadot.io' (Westend testnet)

/**
 * Initialize Polkadot API connection
 * @returns {Promise<ApiPromise>} Initialized API instance
 */
async function initPolkadotApi() {
  try {
    // Create provider instance
    const provider = new WsProvider(WS_PROVIDER_URL);
    
    // Create the API instance
    const api = await ApiPromise.create({ 
      provider,
      throwOnConnect: true,
      throwOnUnknown: true
    });
    
    console.log('✅ Successfully connected to Polkadot network');
    return api;
  } catch (error) {
    console.error('❌ Failed to connect to Polkadot network:', error);
    throw error;
  }
}

/**
 * Query account balance
 * @param {ApiPromise} api Polkadot API instance
 * @param {string} address Account address
 */
async function getAccountBalance(api, address) {
  try {
    // Validate address format
    if (!api.isValidAddress(address)) {
      throw new Error('Invalid address format');
    }

    // Query the account balance
    const { data: { free: balance } } = await api.query.system.account(address);
    
    console.log(`💰 Account ${address} has a balance of ${balance.toHuman()}`);
    return balance;
  } catch (error) {
    console.error('❌ Failed to fetch account balance:', error);
    throw error;
  }
}

/**
 * Transfer DOT tokens between accounts
 * @param {ApiPromise} api Polkadot API instance
 * @param {object} keyringPair Keyring pair of sender
 * @param {string} recipientAddress Recipient address
 * @param {number} amount Amount in Planck (1 DOT = 10^10 Planck)
 */
async function transferDOT(api, keyringPair, recipientAddress, amount) {
  try {
    // Validate recipient address
    if (!api.isValidAddress(recipientAddress)) {
      throw new Error('Invalid recipient address');
    }

    // Create transfer transaction
    const transfer = api.tx.balances.transfer(recipientAddress, amount);
    
    // Sign and send transaction
    const hash = await transfer.signAndSend(keyringPair);
    
    console.log(`🔄 Transfer submitted with hash: ${hash}`);
    return hash;
  } catch (error) {
    console.error('❌ Transfer failed:', error);
    throw error;
  }
}

/**
 * Subscribe to new blocks
 * @param {ApiPromise} api Polkadot API instance
 */
async function subscribeToBlocks(api) {
  try {
    const unsubscribe = await api.rpc.chain.subscribeNewHeads((header) => {
      console.log(`⛓️ New block #${header.number}: ${header.hash}`);
    });
    
    console.log('🔔 Subscribed to new blocks');
    return unsubscribe;
  } catch (error) {
    console.error('❌ Failed to subscribe to blocks:', error);
    throw error;
  }
}

// Main execution function
(async () => {
  try {
    // 1. Initialize connection
    const api = await initPolkadotApi();
    
    // 2. Get current block number
    const lastBlock = await api.rpc.chain.getBlock();
    console.log(`📦 Current block: #${lastBlock.block.header.number}`);
    
    // 3. Example account (replace with actual account)
    const exampleAddress = '13xYZx4yCD3W5KXaXr15EiZspTULQEQX6akdY8J2LrqQJNpX';
    
    // 4. Query balance
    await getAccountBalance(api, exampleAddress);
    
    // 5. Subscribe to new blocks
    await subscribeToBlocks(api);
    
    // Note: For actual transfers, you would need:
    // const { Keyring } = require('@polkadot/keyring');
    // const keyring = new Keyring({ type: 'sr25519' });
    // const keyringPair = keyring.addFromUri('your seed phrase');
    
  } catch (error) {
    console.error('🚨 Application error:', error);
    process.exit(1);
  }
})();
```

And here's a corresponding `package.json`:

```json
{
  "name": "polkadot-india-tutorial",
  "version": "1.0.0",
  "description": "Polkadot tutorial for Indian developers",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "@polkadot/api": "^9.4.1",
    "@polkadot/keyring": "^10.4.1"
  },
  "engines": {
    "node": ">=16.0.0"
  },
  "license": "MIT"
}
```
