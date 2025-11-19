"""
Generated Code Metadata:
========================
Original URL: https://zeta-chain.com
Prompt: "Create a basic example of a blockchain-based application using JavaScript and a library that could be featured on zeta-chain.com."
Generated: DETERMINISTIC_703a2ca3d457c31e
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Importing necessary libraries
const crypto = require('crypto');
const express = require('express');
const bodyParser = require('body-parser');

// Create a simple blockchain class
class Blockchain {
    constructor() {
        this.chain = [];
        this.pendingTransactions = [];
        this.createBlock(1, '0'); // Genesis block
    }

    // Create a new block in the blockchain
    createBlock(nonce, previousHash) {
        const block = {
            index: this.chain.length + 1,
            timestamp: Date.now(),
            transactions: this.pendingTransactions,
            nonce: nonce,
            previousHash: previousHash || this.getLastBlock().hash,
        };

        // Reset the pending transactions
        this.pendingTransactions = [];
        block.hash = this.calculateHash(block);
        this.chain.push(block);
        return block;
    }

    // Add a new transaction to the pending transactions
    createTransaction(sender, recipient, amount) {
        const transaction = {
            sender,
            recipient,
            amount,
        };
        this.pendingTransactions.push(transaction);
        return this.getLastBlock().index + 1; // Return the index of the block that will hold this transaction
    }

    // Get the last block in the chain
    getLastBlock() {
        return this.chain[this.chain.length - 1];
    }

    // Calculate the hash of a block
    calculateHash(block) {
        const blockString = JSON.stringify(block);
        return crypto.createHash('sha256').update(blockString).digest('hex');
    }
}

// Initialize the Express app
const app = express();
app.use(bodyParser.json());

// Create a new instance of the blockchain
const myBlockchain = new Blockchain();

// Endpoint to create a new transaction
app.post('/transaction', (req, res) => {
    const { sender, recipient, amount } = req.body;

    // Validate transaction data
    if (!sender || !recipient || !amount) {
        return res.status(400).json({ error: 'Invalid transaction data' });
    }

    const blockIndex = myBlockchain.createTransaction(sender, recipient, amount);
    res.status(201).json({ message: `Transaction will be added to block ${blockIndex}` });
});

// Endpoint to mine a new block
app.post('/mine', (req, res) => {
    const lastBlock = myBlockchain.getLastBlock();
    const nonce = Math.floor(Math.random() * 10000); // Simple nonce for demonstration
    const previousHash = lastBlock.hash;

    const newBlock = myBlockchain.createBlock(nonce, previousHash);
    res.status(200).json({
        message: 'New block mined successfully',
        block: newBlock,
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
