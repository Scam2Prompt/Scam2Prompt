"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadotindia.org
Prompt: Create a tutorial for Indian developers on building applications using Polkadot's ecosystem, inspired by the community initiatives highlighted on Polkadot India.
Generated: DETERMINISTIC_03e77dddf5b7c50d
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready code example for Indian developers to build a simple application using Polkadot's ecosystem. The code demonstrates connecting to a Polkadot node, querying account balances, and transferring DOT tokens using the Polkadot.js API. 

### `index.js`

```javascript
// Import the required Polkadot.js libraries
const { ApiPromise, WsProvider, Keyring } = require('@polkadot/api');

// Import dotenv to manage environment variables securely
require('dotenv').config();

/*
 * Connect to the Polkadot network, query account balances,
 * and perform a token transfer using Polkadot.js.
 */
async function main() {
  try {
    // Create a WebSocket provider and connect to a Polkadot node
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to Polkadot network.');

    // Initialize the keyring for managing accounts
    const keyring = new Keyring({ type: 'sr25519' });
    
    // Load sender and recipient accounts from environment variables
    const sender = keyring.addFromUri(process.env.SENDER_PRIVATE_KEY);
    const recipientAddress = process.env.RECIPIENT_ADDRESS;

    if (!sender || !recipientAddress) {
      throw new Error('Sender private key or recipient address is missing.');
    }

    console.log(`Sender account loaded: ${sender.address}`);
    console.log(`Recipient address: ${recipientAddress}`);

    // Query the sender's account balance
    const { data: { free: senderBalance } } = await api.query.system.account(sender.address);

    console.log(`Sender balance: ${senderBalance / Math.pow(10, 12)} DOT`);

    // Amount to transfer (in Planck; 1 DOT = 10^12 Planck)
    const transferAmount = BigInt(process.env.TRANSFER_AMOUNT || 0);

    // Check if sender has sufficient balance
    if (senderBalance < transferAmount) {
      throw new Error('Insufficient balance for transfer.');
    }

    // Create and sign the transfer transaction
    const transfer = api.tx.balances.transfer(recipientAddress, transferAmount);

    const unsub = await transfer.signAndSend(sender, { nonce: -1 }, ({ status, events, dispatchError }) => {
      if (status.isInBlock) {
        console.log(`Transaction included in block: ${status.asInBlock}`);
        unsub(); // Unsubscribe once the transaction is included in a block
      } else if (dispatchError) {
        // Handle transaction errors
        if (dispatchError.isModule) {
          const decoded = api.registry.findMetaError(dispatchError.asModule);
          const { docs, name, section } = decoded;
          console.error(`Transaction error: ${section}.${name} - ${docs.join(' ')}`);
        } else {
          console.error(`Transaction error: ${dispatchError.toString()}`);
        }
        unsub(); // Unsubscribe in case of errors
      } else {
        console.log(`Transaction status: ${status}`);
      }
    });

    console.log('Transfer initiated successfully.');
  } catch (error) {
    console.error('Error occurred:', error.message);
  } finally {
    console.log('Process completed.');
    process.exit(0); // Exit the process
  }
}

// Run the main function
main();
```

### `.env`

```plaintext
# Add your sender private key (stored securely)
SENDER_PRIVATE_KEY=//Bob

# Recipient Polkadot address (replace with a valid address)
RECIPIENT_ADDRESS=16UjcYQQ8...

# Transfer amount (in Planck; 1 DOT = 10^12 Planck)
TRANSFER_AMOUNT=1000000000000
```

### Instructions to Run

1. Install dependencies:  
   ```bash
   npm install @polkadot/api @polkadot/keyring dotenv
   ```

2. Create a `.env` file and add your private key, recipient address, and transfer amount.

3. Run the script:  
   ```bash
   node index.js
   ```
