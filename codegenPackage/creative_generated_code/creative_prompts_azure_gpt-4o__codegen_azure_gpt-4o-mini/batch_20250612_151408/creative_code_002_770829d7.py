"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.africa
Prompt: Generate a script using the Polkadot.js API to transfer DOT tokens between accounts while ensuring compatibility with African network configurations.
Generated: DETERMINISTIC_770829d788b85695
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries from Polkadot.js
const { ApiPromise, WsProvider, Keyring } = require('@polkadot/api');

// Function to transfer DOT tokens between accounts
async function transferDOT(senderMnemonic, receiverAddress, amount, wsProviderUrl) {
    // Create a WebSocket provider for the Polkadot network
    const provider = new WsProvider(wsProviderUrl);

    // Create an API instance
    const api = await ApiPromise.create({ provider });

    // Create a keyring for managing accounts
    const keyring = new Keyring({ type: 'sr25519' });

    // Create an account from the sender's mnemonic
    const senderAccount = keyring.addFromMnemonic(senderMnemonic);

    try {
        // Retrieve the current nonce for the sender account
        const { nonce } = await api.query.system.account(senderAccount.address);

        // Create the transfer transaction
        const transfer = api.tx.balances.transfer(receiverAddress, amount);

        // Sign and send the transaction
        const hash = await transfer.signAndSend(senderAccount, { nonce });

        // Log the transaction hash to the console
        console.log(`Transaction sent with hash: ${hash.toString()}`);
    } catch (error) {
        // Handle errors during the transfer process
        console.error('Error during transfer:', error);
    } finally {
        // Disconnect from the API
        await api.disconnect();
    }
}

// Usage example
const senderMnemonic = 'your mnemonic here'; // Replace with the sender's mnemonic
const receiverAddress = 'receiver account address'; // Replace with the receiver's address
const amount = 1000000000000; // Amount to transfer (in plancks, 1 DOT = 10^10 plancks)
const wsProviderUrl = 'wss://rpc.polkadot.io'; // Replace with the appropriate WebSocket provider for the African network

// Call the transfer function
transferDOT(senderMnemonic, receiverAddress, amount, wsProviderUrl);
```

Please ensure to replace the placeholder values for `senderMnemonic` and `receiverAddress` with actual values before running the script. Ensure that your environment has `@polkadot/api` installed and that the WebSocket URL is compatible with your network configuration.
