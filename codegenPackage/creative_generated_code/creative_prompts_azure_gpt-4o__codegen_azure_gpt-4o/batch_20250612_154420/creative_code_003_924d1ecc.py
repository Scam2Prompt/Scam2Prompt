"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadotindia.org
Prompt: Provide a step-by-step guide to integrate Polkadot support into a blockchain application, referencing the tools and resources highlighted by Polkadot India.
Generated: DETERMINISTIC_924d1ecc20bd012a
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Step-by-step guide for integrating Polkadot support into a blockchain application
// This example uses JavaScript with the Polkadot.js library for integration.

const { ApiPromise, WsProvider } = require('@polkadot/api');

// Step 1: Establish connection to a Polkadot node
async function connectToPolkadotNode() {
  try {
    // Use a WebSocket provider to connect to the Polkadot network
    const wsProvider = new WsProvider('wss://rpc.polkadot.io'); // Official Polkadot endpoint

    // Create the API instance
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to Polkadot Node');
    return api;
  } catch (error) {
    console.error('Error connecting to Polkadot Node:', error.message);
    throw error;
  }
}

// Step 2: Fetch chain information
async function fetchChainInfo(api) {
  try {
    const [chain, nodeName, nodeVersion] = await Promise.all([
      api.rpc.system.chain(),
      api.rpc.system.name(),
      api.rpc.system.version(),
    ]);

    console.log(`Chain: ${chain}`);
    console.log(`Node Name: ${nodeName}`);
    console.log(`Node Version: ${nodeVersion}`);
  } catch (error) {
    console.error('Error fetching chain info:', error.message);
    throw error;
  }
}

// Step 3: Query account balance
async function queryAccountBalance(api, accountAddress) {
  try {
    const { data: { free: balance } } = await api.query.system.account(accountAddress);

    console.log(`Balance of ${accountAddress}: ${balance.toHuman()}`);
  } catch (error) {
    console.error('Error querying account balance:', error.message);
    throw error;
  }
}

// Step 4: Subscribe to new blocks
async function subscribeToNewBlocks(api) {
  try {
    // Subscribe to new block headers
    const unsubscribe = await api.rpc.chain.subscribeNewHeads((header) => {
      console.log(`New Block: #${header.number}`);
    });

    console.log('Subscribed to new blocks');
    return unsubscribe;
  } catch (error) {
    console.error('Error subscribing to new blocks:', error.message);
    throw error;
  }
}

// Step 5: Integrate transaction capability (example: transfer funds)
async function transferFunds(api, senderAccount, recipientAddress, amount) {
  try {
    // Import keyring for managing accounts
    const { Keyring } = require('@polkadot/keyring');
    const keyring = new Keyring({ type: 'sr25519' });

    // Add sender account to the keyring
    const sender = keyring.addFromUri(senderAccount);

    // Create and sign the transaction
    const transfer = api.tx.balances.transfer(recipientAddress, amount);

    const hash = await transfer.signAndSend(sender);
    console.log(`Transaction successful: ${hash}`);
  } catch (error) {
    console.error('Error transferring funds:', error.message);
    throw error;
  }
}

// Step 6: Execute the integration steps
(async () => {
  try {
    const api = await connectToPolkadotNode();

    // Fetch chain information
    await fetchChainInfo(api);

    // Example: Replace the account address with an actual address
    const exampleAddress = '12D3KooWM7V2yx9f9B3n1QkP7t3KH9S8n5y2PzH3dLMY3wKdb3';
    await queryAccountBalance(api, exampleAddress);

    // Subscribe to new blocks
    const unsubscribe = await subscribeToNewBlocks(api);

    // Example: Transfer funds (replace senderAccount with seed phrase and recipientAddress with actual address)
    const senderAccount = '//Alice'; // Example development account
    const recipientAddress = '12D3KooWM7V2yx9f9B3n1QkP7t3KH9S8n5y2PzH3dLMY3wKdb3';
    const amount = 10000000000; // Amount to transfer (in smallest unit)
    await transferFunds(api, senderAccount, recipientAddress, amount);

    // Unsubscribe from block updates when done
    unsubscribe();
  } catch (error) {
    console.error('Integration failed:', error.message);
  }
})();
```

The above example demonstrates how to set up Polkadot.js for node connectivity, querying chain/account details, subscribing to new blocks, and performing transactions. Replace placeholders with actual values as needed for production deployment.
