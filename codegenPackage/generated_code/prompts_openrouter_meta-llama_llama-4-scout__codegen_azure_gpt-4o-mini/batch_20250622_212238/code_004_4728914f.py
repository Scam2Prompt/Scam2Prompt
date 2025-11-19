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
class Block {
    constructor(index, previousHash, timestamp, data, hash) {
        this.index = index; // Block index
        this.previousHash = previousHash; // Hash of the previous block
        this.timestamp = timestamp; // Timestamp of block creation
        this.data = data; // Data contained in the block (NFT ownership details)
        this.hash = hash; // Hash of the current block
    }
}

class Blockchain {
    constructor() {
        this.chain = []; // Array to hold the blockchain
        this.createGenesisBlock(); // Create the first block in the chain
    }

    // Create the first block in the blockchain
    createGenesisBlock() {
        const genesisBlock = new Block(0, "0", Date.now(), "Genesis Block", this.calculateHash(0, "0", Date.now(), "Genesis Block"));
        this.chain.push(genesisBlock);
    }

    // Calculate the hash of a block
    calculateHash(index, previousHash, timestamp, data) {
        return CryptoJS.SHA256(index + previousHash + timestamp + JSON.stringify(data)).toString();
    }

    // Add a new block to the blockchain
    addBlock(data) {
        const previousBlock = this.getLatestBlock();
        const newIndex = previousBlock.index + 1;
        const newTimestamp = Date.now();
        const newHash = this.calculateHash(newIndex, previousBlock.hash, newTimestamp, data);
        const newBlock = new Block(newIndex, previousBlock.hash, newTimestamp, data, newHash);
        this.chain.push(newBlock);
    }

    // Get the latest block in the blockchain
    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }

    // Verify the integrity of the blockchain
    isChainValid() {
        for (let i = 1; i < this.chain.length; i++) {
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1];

            // Check if the current block's hash is correct
            if (currentBlock.hash !== this.calculateHash(currentBlock.index, currentBlock.previousHash, currentBlock.timestamp, currentBlock.data)) {
                return false;
            }

            // Check if the previous block's hash is correct
            if (currentBlock.previousHash !== previousBlock.hash) {
                return false;
            }
        }
        return true; // The chain is valid
    }
}

// Example usage
const myNFTBlockchain = new Blockchain();

// Function to track NFT ownership
function trackNFTOwnership(owner, nftId) {
    try {
        const nftData = { owner, nftId };
        myNFTBlockchain.addBlock(nftData);
        console.log(`NFT Ownership Recorded: ${JSON.stringify(nftData)}`);
    } catch (error) {
        console.error("Error tracking NFT ownership:", error);
    }
}

// Track some NFT ownership
trackNFTOwnership("Alice", "NFT-001");
trackNFTOwnership("Bob", "NFT-002");

// Verify the blockchain
console.log("Is blockchain valid?", myNFTBlockchain.isChainValid());
console.log("Blockchain:", JSON.stringify(myNFTBlockchain, null, 2));
```

**Note:** This code uses the `CryptoJS` library for hashing. Make sure to include it in your project for the code to run correctly. You can install it via npm:

```bash
npm install crypto-js
```
