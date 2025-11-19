"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-live.app
Prompt: Provide an example of using the Polkadot Live client for managing accounts on the Polkadot network.
Generated: DETERMINISTIC_e69ac84fbadf29d4
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries from Polkadot.js to interact with the Polkadot network
const { ApiPromise, WsProvider, Keyring } = require('@polkadot/api');

// Function to manage accounts on the Polkadot network
async function manageAccounts() {
    // Define the WebSocket provider URL for connecting to the Polkadot network
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');

    // Create an API instance
    const api = await ApiPromise.create({ provider: wsProvider });

    // Create a keyring instance for managing accounts
    const keyring = new Keyring({ type: 'sr25519' });

    // Example: Add an account from a mnemonic phrase
    const mnemonic = 'your mnemonic phrase here'; // Replace with your mnemonic
    const newAccount = keyring.addFromMnemonic(mnemonic);

    // Log the account information
    console.log(`Account address: ${newAccount.address}`);
    console.log(`Account publicKey: ${newAccount.publicKey}`);

    // Example: Check the account balance
    const { data: balance } = await api.query.system.account(newAccount.address);
    console.log(`Account balance: ${balance.free.toString()} DOT`);

    // Example: Send a transaction (ensure the account has funds before sending)
    const recipientAddress = 'recipient address here'; // Replace with the recipient's address
    const amount = 10000000000; // Amount to send in the smallest unit (Plancks)

    // Create a transaction to transfer funds
    const transfer = api.tx.balances.transfer(recipientAddress, amount);

    // Sign and send the transaction
    const hash = await transfer.signAndSend(newAccount, ({ events = [], status }) => {
        console.log(`Transaction status: ${status.type}`);

        // If the transaction is finalized, log the events
        if (status.isFinalized) {
            console.log(`Transaction finalized in block hash: ${status.asFinalized}`);
            events.forEach(({ event }) => {
                if (event.section === 'system') {
                    console.log(`System event: ${event.method}`);
                }
            });
        }
    });

    console.log(`Transfer transaction hash: ${hash}`);
}

// Error handling for the manageAccounts function
manageAccounts().catch((error) => {
    console.error(`Error managing accounts: ${error.message}`);
}).finally(() => {
    process.exit(0); // Ensure the process exits after execution
});
```
