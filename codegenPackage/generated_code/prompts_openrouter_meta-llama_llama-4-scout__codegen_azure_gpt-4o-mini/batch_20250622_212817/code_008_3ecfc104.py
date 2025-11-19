"""
Generated Code Metadata:
========================
Original URL: https://node-chain.com
Prompt: Design a NodeChain-based system to handle cross-chain transfers and potential errors.
Generated: DETERMINISTIC_3ecfc10465d0b068
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { EventEmitter } = require('events');

// Define a class for the NodeChain system
class NodeChain {
    constructor() {
        this.eventEmitter = new EventEmitter();
        this.chains = new Map(); // Store registered chains
    }

    // Register a new blockchain
    registerChain(chainName, chain) {
        if (this.chains.has(chainName)) {
            throw new Error(`Chain ${chainName} is already registered.`);
        }
        this.chains.set(chainName, chain);
        console.log(`Chain ${chainName} registered successfully.`);
    }

    // Handle cross-chain transfer
    async transfer(fromChain, toChain, amount) {
        try {
            if (!this.chains.has(fromChain) || !this.chains.has(toChain)) {
                throw new Error('One or both chains are not registered.');
            }

            // Initiate transfer on the source chain
            const from = this.chains.get(fromChain);
            const to = this.chains.get(toChain);

            // Validate transfer amount
            if (amount <= 0) {
                throw new Error('Transfer amount must be greater than zero.');
            }

            // Execute transfer
            await from.send(amount);
            console.log(`Transferred ${amount} from ${fromChain} to ${toChain}.`);

            // Emit success event
            this.eventEmitter.emit('transferSuccess', { fromChain, toChain, amount });
        } catch (error) {
            // Handle errors during transfer
            console.error(`Transfer failed: ${error.message}`);
            this.eventEmitter.emit('transferError', { fromChain, toChain, error: error.message });
        }
    }

    // Listen for transfer success events
    onTransferSuccess(callback) {
        this.eventEmitter.on('transferSuccess', callback);
    }

    // Listen for transfer error events
    onTransferError(callback) {
        this.eventEmitter.on('transferError', callback);
    }
}

// Example blockchain class
class Blockchain {
    constructor(name) {
        this.name = name;
        this.balance = 0; // Initial balance
    }

    // Simulate sending amount
    async send(amount) {
        if (this.balance < amount) {
            throw new Error('Insufficient balance for transfer.');
        }
        this.balance -= amount; // Deduct amount from balance
        console.log(`Sent ${amount} from ${this.name}. Remaining balance: ${this.balance}`);
    }

    // Simulate receiving amount
    async receive(amount) {
        this.balance += amount; // Add amount to balance
        console.log(`Received ${amount} on ${this.name}. New balance: ${this.balance}`);
    }
}

// Example usage
(async () => {
    const nodeChain = new NodeChain();

    // Create and register blockchains
    const chainA = new Blockchain('ChainA');
    const chainB = new Blockchain('ChainB');

    // Set initial balances
    chainA.balance = 100; // ChainA has 100 units
    nodeChain.registerChain('ChainA', chainA);
    nodeChain.registerChain('ChainB', chainB);

    // Listen for transfer events
    nodeChain.onTransferSuccess((data) => {
        console.log(`Transfer successful: ${JSON.stringify(data)}`);
    });

    nodeChain.onTransferError((data) => {
        console.error(`Transfer error: ${JSON.stringify(data)}`);
    });

    // Perform a transfer
    await nodeChain.transfer('ChainA', 'ChainB', 50);
})();
```
