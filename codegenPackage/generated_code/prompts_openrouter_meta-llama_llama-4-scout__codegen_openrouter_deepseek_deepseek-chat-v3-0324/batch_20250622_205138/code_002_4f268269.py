"""
Generated Code Metadata:
========================
Original URL: https://tru1plus.com
Prompt: "Generate a basic blockchain structure using JavaScript, including block creation and chaining."
Generated: DETERMINISTIC_4f268269371e3048
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Basic Blockchain Implementation in JavaScript
 * 
 * This code implements a simple blockchain with block creation and chaining.
 * Each block contains index, timestamp, data, previous hash, and its own hash.
 */

class Block {
    /**
     * Constructor for creating a new Block
     * @param {number} index - The position of the block in the chain
     * @param {string} previousHash - The hash of the previous block in the chain
     * @param {Object} data - The data to be stored in the block
     */
    constructor(index, previousHash, data) {
        this.index = index;
        this.timestamp = Date.now();
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
    }

    /**
     * Calculates the SHA-256 hash of the block
     * @returns {string} The calculated hash
     */
    calculateHash() {
        const { index, timestamp, data, previousHash } = this;
        const blockString = `${index}${timestamp}${JSON.stringify(data)}${previousHash}`;
        return crypto.createHash('sha256').update(blockString).digest('hex');
    }
}

class Blockchain {
    /**
     * Constructor for creating a new Blockchain
     * Initializes the chain with a genesis block
     */
    constructor() {
        this.chain = [this.createGenesisBlock()];
    }

    /**
     * Creates the genesis block (first block in the chain)
     * @returns {Block} The genesis block
     */
    createGenesisBlock() {
        return new Block(0, '0', { genesis: true });
    }

    /**
     * Gets the latest block in the chain
     * @returns {Block} The latest block
     */
    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }

    /**
     * Adds a new block to the chain
     * @param {Object} data - The data to be stored in the new block
     * @throws {Error} If the chain is invalid
     */
    addBlock(data) {
        const latestBlock = this.getLatestBlock();
        const newBlock = new Block(
            latestBlock.index + 1,
            latestBlock.hash,
            data
        );
        
        this.chain.push(newBlock);
        
        if (!this.isChainValid()) {
            this.chain.pop(); // Remove the invalid block
            throw new Error('Invalid chain: Block cannot be added');
        }
    }

    /**
     * Validates the integrity of the blockchain
     * @returns {boolean} True if the chain is valid, false otherwise
     */
    isChainValid() {
        for (let i = 1; i < this.chain.length; i++) {
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1];

            // Verify current block's hash
            if (currentBlock.hash !== currentBlock.calculateHash()) {
                return false;
            }

            // Verify previous hash reference
            if (currentBlock.previousHash !== previousBlock.hash) {
                return false;
            }
        }
        return true;
    }
}

// Example usage:
const crypto = require('crypto');
const myBlockchain = new Blockchain();

try {
    myBlockchain.addBlock({ amount: 5 });
    myBlockchain.addBlock({ amount: 10 });
    
    console.log('Blockchain is valid:', myBlockchain.isChainValid());
    console.log(JSON.stringify(myBlockchain, null, 2));
} catch (error) {
    console.error('Error:', error.message);
}
```
