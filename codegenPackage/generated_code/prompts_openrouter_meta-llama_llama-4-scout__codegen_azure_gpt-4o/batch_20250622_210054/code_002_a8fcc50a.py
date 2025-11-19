"""
Generated Code Metadata:
========================
Original URL: https://sophon.pages.dev
Prompt: Generate code for a simple blockchain-based application using the Sui Move programming language, created by Mysten founders.
Generated: DETERMINISTIC_a8fcc50a71cf1e6b
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
module BlockchainApp::SimpleBlockchain {
    use std::string;
    use std::vector;
    use std::error;

    /// Struct representing a single block in the blockchain
    struct Block has key, store {
        id: u64, // Unique identifier for the block
        previous_hash: string::String, // Hash of the previous block
        data: string::String, // Data stored in the block
        hash: string::String, // Hash of the current block
    }

    /// Struct representing the blockchain
    struct Blockchain has key, store {
        blocks: vector::Vector<Block>, // Vector of blocks
    }

    /// Helper function to calculate a simple hash (for demonstration purposes)
    public fun calculate_hash(id: u64, previous_hash: &string::String, data: &string::String): string::String {
        let concatenated = string::concat(string::concat(string::from_u64(id), previous_hash), data);
        string::hash(concatenated) // Using a simple hash function
    }

    /// Function to create a new block
    public fun create_block(id: u64, previous_hash: string::String, data: string::String): Block {
        let hash = calculate_hash(id, &previous_hash, &data);
        Block { id, previous_hash, data, hash }
    }

    /// Function to initialize a new blockchain
    public fun initialize_blockchain(): Blockchain {
        let genesis_block = create_block(0, string::String::from_utf8(vector::empty()), string::String::from_utf8(vector::empty()));
        Blockchain { blocks: vector::singleton(genesis_block) }
    }

    /// Function to add a new block to the blockchain
    public fun add_block(blockchain: &mut Blockchain, data: string::String): Result<(), error::Error> {
        let last_block = vector::last(&blockchain.blocks);
        match last_block {
            Option::Some(block) => {
                let new_block = create_block(block.id + 1, block.hash, data);
                vector::push_back(&mut blockchain.blocks, new_block);
                Result::Ok(())
            },
            Option::None => Result::Err(error::new("Failed to retrieve the last block")),
        }
    }

    /// Function to retrieve the blockchain
    public fun get_blockchain(blockchain: &Blockchain): vector::Vector<Block> {
        blockchain.blocks
    }
}
```
