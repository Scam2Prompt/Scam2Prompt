"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-france.fr
Prompt: Write a code snippet that demonstrates how to interact with the Polkadot blockchain using its API for transaction management.
Generated: DETERMINISTIC_6c200fb1848d985c
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const { ApiPromise, WsProvider, Keyring } = require('@polkadot/api');

// Configure the WebSocket endpoint for connection to the Polkadot blockchain
const WS_ENDPOINT = 'wss://rpc.polkadot.io'; // Replace with desired Polkadot endpoint

// Transaction management example: Sending DOT from one account to another
async function manageTransaction() {
  try {
    // Step 1: Establish connection to the Polkadot blockchain
    const provider = new WsProvider(WS_ENDPOINT);
    const api = await ApiPromise.create({ provider });

    console.log('Connected to the Polkadot blockchain.');

    // Step 2: Initialize keyring to manage accounts
    const keyring = new Keyring({ type: 'sr25519' });

    // Step 3: Add sender's account to the keyring
    const senderAccount = keyring.addFromUri('<SECRET_PHRASE_OF_SENDER>'); // Replace with sender's mnemonic or private key

    // Step 4: Specify receiver's account and transfer amount
    const receiverAddress = '<RECEIVER_ADDRESS>'; // Replace with receiver's Polkadot address
    const transferAmount = 10000000000; // Amount in Planck (1 DOT = 10^10 Planck)

    console.log(`Preparing to send ${transferAmount} Planck to ${receiverAddress}`);

    // Step 5: Create and submit the transaction
    const transfer = api.tx.balances.transfer(receiverAddress, transferAmount);

    // Sign and send the transaction
    const unsub = await transfer.signAndSend(senderAccount, ({ status, events, dispatchError }) => {
      console.log(`Transaction status: ${status.type}`);

      // Check for successful completion
      if (status.isFinalized) {
        console.log(`Transaction finalized in block: ${status.asFinalized}`);
        unsub(); // Unsubscribe from transaction updates
      }

      // Handle any errors that occur during execution
      if (dispatchError) {
        if (dispatchError.isModule) {
          const decoded = api.registry.findMetaError(dispatchError.asModule);
          const { documentation, name, section } = decoded;
          console.error(`Error: ${section}.${name} - ${documentation.join(' ')}`);
        } else {
          console.error(`Error: ${dispatchError.toString()}`);
        }
      }

      // Log successful events
      events.forEach(({ event: { data, method, section } }) => {
        console.log(`Event: ${section}.${method} - ${data.toString()}`);
      });
    });

  } catch (error) {
    // Handle connection and transaction errors
    console.error('An error occurred:', error.message);
  } finally {
    console.log('Transaction management example complete.');
  }
}

// Execute the transaction management function
manageTransaction();
```

### Notes:
- Replace `<SECRET_PHRASE_OF_SENDER>` and `<RECEIVER_ADDRESS>` with actual values.
- Install the required package: `npm install @polkadot/api`.
- Ensure that the sender's account has sufficient balance to cover the transfer and transaction fees.
- This code is production-ready but assumes you have valid credentials and are using a secure environment for secret management.
