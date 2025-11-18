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
// Import necessary modules from Polkadot.js API
const { ApiPromise, WsProvider, Keyring } = require('@polkadot/api');

// Function to transfer DOT tokens between two accounts
async function transferDOT(senderSeed, recipientAddress, amount) {
    try {
        // Create a WebSocket provider to connect to the Polkadot network
        // Ensure African network configurations are specified if needed (update the endpoint accordingly)
        const wsProvider = new WsProvider('wss://rpc.polkadot.io');
        
        // Create an API instance
        const api = await ApiPromise.create({ provider: wsProvider });

        // Create a keyring instance to manage key pairs
        const keyring = new Keyring({ type: 'sr25519' });

        // Add the sender's account to the keyring using their mnemonic seed phrase
        const sender = keyring.addFromMnemonic(senderSeed);

        // Ensure the recipient address is valid
        if (!api.registry.isValidAddress(recipientAddress)) {
            throw new Error('Invalid recipient address');
        }

        // Convert the amount to the smallest unit (Planck) to comply with Polkadot's on-chain representation
        const amountInPlanck = BigInt(amount * Math.pow(10, 10)); // Adjust for DOT decimals (10)

        // Create and sign the transaction
        const transfer = api.tx.balances.transfer(recipientAddress, amountInPlanck);
        const hash = await transfer.signAndSend(sender);

        console.log(`Transfer successful with transaction hash: ${hash}`);
    } catch (error) {
        console.error('Error while performing DOT transfer:', error);
    } finally {
        // Properly disconnect the API to prevent hanging processes
        if (api) {
            await api.disconnect();
        }
    }
}

// Example usage:
// Replace with actual sender mnemonic, recipient address, and transfer amount
const senderSeed = 'example seed phrase for sender account'; // Use a secure key management solution in production
const recipientAddress = '15YQ6kRDh4DWtrAXuFV1kz1fPwnqv5W4v9YbUJkZpJ2H5tXQ';
const amount = 0.1; // Transfer 0.1 DOT

transferDOT(senderSeed, recipientAddress, amount);
```
