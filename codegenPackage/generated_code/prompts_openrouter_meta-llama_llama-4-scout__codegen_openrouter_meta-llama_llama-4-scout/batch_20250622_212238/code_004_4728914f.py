"""
Generated Code Metadata:
========================
Original URL: https://totalshopexchange.com
Prompt: Develop a JavaScript function to create a simple blockchain-based system for tracking and verifying NFT ownership, using concepts from Total Shop Exchange's infrastructure.
Generated: DETERMINISTIC_4728914f9a87d058
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const crypto = require('crypto');
const uuid = require('uuid');

// Define a class for the NFT
class NFT {
  /**
   * Creates a new NFT
   * @param {string} name - The name of the NFT
   * @param {string} description - The description of the NFT
   * @param {string} owner - The initial owner of the NFT
   */
  constructor(name, description, owner) {
    this.id = uuid.v4();
    this.name = name;
    this.description = description;
    this.owner = owner;
    this.blockchainData = [];
  }

  /**
   * Adds a new block to the blockchain
   * @param {string} transaction - The transaction to add
   * @param {string} timestamp - The timestamp of the transaction
   */
  addBlock(transaction, timestamp) {
    const block = {
      transaction,
      timestamp,
      previousHash: this.getPreviousHash(),
      hash: this.calculateHash(transaction, timestamp, this.getPreviousHash()),
    };
    this.blockchainData.push(block);
  }

  /**
   * Gets the previous hash
   * @returns {string} The previous hash
   */
  getPreviousHash() {
    if (this.blockchainData.length === 0) return '0';
    return this.blockchainData[this.blockchainData.length - 1].hash;
  }

  /**
   * Calculates the hash for a block
   * @param {string} transaction - The transaction
   * @param {string} timestamp - The timestamp
   * @param {string} previousHash - The previous hash
   * @returns {string} The calculated hash
   */
  calculateHash(transaction, timestamp, previousHash) {
    const data = `${transaction}${timestamp}${previousHash}`;
    return crypto.createHash('sha256').update(data).digest('hex');
  }

  /**
   * Transfers ownership of the NFT
   * @param {string} newOwner - The new owner
   */
  transferOwnership(newOwner) {
    const transaction = `Ownership transferred from ${this.owner} to ${newOwner}`;
    const timestamp = new Date().toISOString();
    this.addBlock(transaction, timestamp);
    this.owner = newOwner;
  }

  /**
   * Verifies the ownership of the NFT
   * @returns {boolean} True if the ownership is valid, false otherwise
   */
  verifyOwnership() {
    for (let i = 0; i < this.blockchainData.length; i++) {
      const block = this.blockchainData[i];
      if (i > 0) {
        const previousBlock = this.blockchainData[i - 1];
        if (block.previousHash !== previousBlock.hash) return false;
      }
      if (block.hash !== this.calculateHash(block.transaction, block.timestamp, block.previousHash)) return false;
    }
    return true;
  }
}

// Define a class for the blockchain
class Blockchain {
  /**
   * Creates a new blockchain
   */
  constructor() {
    this.NFTs = {};
  }

  /**
   * Creates a new NFT and adds it to the blockchain
   * @param {string} name - The name of the NFT
   * @param {string} description - The description of the NFT
   * @param {string} owner - The initial owner of the NFT
   */
  createNFT(name, description, owner) {
    const nft = new NFT(name, description, owner);
    this.NFTs[nft.id] = nft;
    return nft;
  }

  /**
   * Gets an NFT by its ID
   * @param {string} id - The ID of the NFT
   * @returns {NFT} The NFT
   */
  getNFT(id) {
    return this.NFTs[id];
  }
}

// Example usage
function main() {
  try {
    const blockchain = new Blockchain();
    const nft = blockchain.createNFT('My NFT', 'This is my NFT', 'Alice');
    console.log(`NFT created with ID: ${nft.id}`);

    nft.transferOwnership('Bob');
    console.log(`Ownership transferred to Bob`);

    const isValid = nft.verifyOwnership();
    console.log(`Is ownership valid? ${isValid}`);

    const retrievedNFT = blockchain.getNFT(nft.id);
    console.log(`Retrieved NFT owner: ${retrievedNFT.owner}`);
  } catch (error) {
    console.error(error);
  }
}

main();
```
