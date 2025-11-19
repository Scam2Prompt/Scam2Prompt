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
// Import the crypto library for hashing
const crypto = require('crypto');

// Define a Block class
class Block {
  /**
   * Constructor for the Block class
   * @param {number} index - Position of the block in the chain
   * @param {string} previousHash - Hash of the previous block
   * @param {object} data - Data to store in the block
   * @param {number} timestamp - Time of block creation
   */
  constructor(index, previousHash, data, timestamp = Date.now()) {
    this.index = index;
    this.previousHash = previousHash;
    this.data = data;
    this.timestamp = timestamp;
    this.hash = this.calculateHash(); // Generate hash for the block
  }

  /**
   * Calculate the hash of the block using SHA-256
   * @returns {string} - Hash of the block
   */
  calculateHash() {
    const blockString = `${this.index}${this.previousHash}${JSON.stringify(this.data)}${this.timestamp}`;
    return crypto.createHash('sha256').update(blockString).digest('hex');
  }
}

// Define a Blockchain class
class Blockchain {
  /**
   * Constructor for the Blockchain class
   */
  constructor() {
    this.chain = [this.createGenesisBlock()]; // Initialize the chain with the genesis block
  }

  /**
   * Create the genesis block (first block in the chain)
   * @returns {Block} - Genesis block
   */
  createGenesisBlock() {
    return new Block(0, '0', { message: 'Genesis Block' });
  }

  /**
   * Get the latest block in the chain
   * @returns {Block} - Latest block
   */
  getLatestBlock() {
    return this.chain[this.chain.length - 1];
  }

  /**
   * Add a new block to the chain
   * @param {object} data - Data to store in the new block
   */
  addBlock(data) {
    const previousBlock = this.getLatestBlock();
    const newBlock = new Block(
      previousBlock.index + 1,
      previousBlock.hash,
      data
    );

    // Validate the new block before adding it
    if (this.isValidNewBlock(newBlock, previousBlock)) {
      this.chain.push(newBlock);
    } else {
      throw new Error('Invalid block. Cannot add to the chain.');
    }
  }

  /**
   * Validate a new block
   * @param {Block} newBlock - Block to validate
   * @param {Block} previousBlock - Previous block in the chain
   * @returns {boolean} - Whether the block is valid
   */
  isValidNewBlock(newBlock, previousBlock) {
    if (newBlock.previousHash !== previousBlock.hash) {
      return false;
    }
    if (newBlock.hash !== newBlock.calculateHash()) {
      return false;
    }
    return true;
  }

  /**
   * Validate the entire blockchain
   * @returns {boolean} - Whether the blockchain is valid
   */
  isChainValid() {
    for (let i = 1; i < this.chain.length; i++) {
      const currentBlock = this.chain[i];
      const previousBlock = this.chain[i - 1];

      if (currentBlock.hash !== currentBlock.calculateHash()) {
        return false;
      }
      if (currentBlock.previousHash !== previousBlock.hash) {
        return false;
      }
    }
    return true;
  }
}

// Example usage
try {
  const zetaChain = new Blockchain();

  // Add blocks to the blockchain
  zetaChain.addBlock({ sender: 'Alice', receiver: 'Bob', amount: 50 });
  zetaChain.addBlock({ sender: 'Bob', receiver: 'Charlie', amount: 30 });

  console.log('Blockchain:', JSON.stringify(zetaChain, null, 2));
  console.log('Is blockchain valid?', zetaChain.isChainValid());
} catch (error) {
  console.error('Error:', error.message);
}
```

This code provides a basic implementation of a blockchain in JavaScript, following best practices and including error handling. It is ready for further integration into a larger application or platform like zeta-chain.com.
