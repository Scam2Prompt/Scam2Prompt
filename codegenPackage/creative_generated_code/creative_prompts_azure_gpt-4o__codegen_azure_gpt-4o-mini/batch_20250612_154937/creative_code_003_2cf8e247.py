"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.polkadotstaker.com
Prompt: Provide an example of using the Polkadot.js API to delegate DOT tokens to a validator, ensuring the validator supports network decentralization.
Generated: DETERMINISTIC_2cf8e2473df6117c
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries from the Polkadot.js API
const { ApiPromise, WsProvider, Keyring } = require('@polkadot/api');

// Define the main function to delegate DOT tokens to a validator
async function delegateTokens(validatorAddress, amountToDelegate, userMnemonic) {
    // Connect to the Polkadot network
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');
    const api = await ApiPromise.create({ provider: wsProvider });

    // Create a keyring instance to manage user accounts
    const keyring = new Keyring({ type: 'sr25519' });
    
    // Add the user's account using the provided mnemonic
    const userAccount = keyring.addFromMnemonic(userMnemonic);

    // Check the user's balance before delegating
    const { data: { free: initialBalance } } = await api.query.system.account(userAccount.address);
    console.log(`Initial balance of ${userAccount.address}: ${initialBalance.toString()} DOT`);

    // Ensure the user has enough DOT to delegate
    if (initialBalance.isLessThan(amountToDelegate)) {
        throw new Error('Insufficient balance to delegate the specified amount.');
    }

    // Create a transaction to delegate tokens to the specified validator
    const tx = api.tx.staking.delegate(validatorAddress, amountToDelegate);
    
    // Sign and send the transaction
    const unsub = await tx.signAndSend(userAccount, ({ status }) => {
        if (status.isInBlock) {
            console.log(`Transaction included in block: ${status.asInBlock}`);
            unsub(); // Unsubscribe from the transaction updates
        } else if (status.isFinalized) {
            console.log(`Transaction finalized in block: ${status.asFinalized}`);
            unsub(); // Unsubscribe from the transaction updates
        } else {
            console.log(`Current transaction status: ${status}`);
        }
    });
}

// Example usage
const validatorAddress = 'YOUR_VALIDATOR_ADDRESS_HERE'; // Replace with actual validator address
const amountToDelegate = 1_000_000_000_000; // Amount in Plancks (1 DOT = 10^10 Plancks)
const userMnemonic = 'YOUR_MNEMONIC_HERE'; // Replace with user's mnemonic

// Call the function to delegate tokens
delegateTokens(validatorAddress, amountToDelegate, userMnemonic)
    .catch((error) => {
        console.error(`Error occurred: ${error.message}`);
    });
```
