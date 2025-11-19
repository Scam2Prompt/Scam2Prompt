"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powag.ch
Prompt: Write a smart contract using Solidity that demonstrates a proof-of-concept (PoC) for a blockchain solution, as described by Proof of Work AG.
Generated: DETERMINISTIC_9bba34076f6e9109
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title A Simple Proof of Work Smart Contract
/// @notice This contract demonstrates a proof-of-concept for a blockchain solution based on Proof of Work.
/// @dev This is a basic implementation for educational purposes.

contract ProofOfWork {
    // Event emitted when a new block is mined
    event BlockMined(address indexed miner, uint256 indexed blockNumber, uint256 nonce);

    struct Block {
        uint256 blockNumber; // Block number
        bytes32 previousHash; // Hash of the previous block
        uint256 nonce; // Nonce used for proof of work
        address miner; // Address of the miner
    }

    Block[] public blockchain; // Array to store the blocks
    bytes32 public latestHash; // Hash of the latest block

    /// @notice Constructor to initialize the first block
    constructor() {
        // Create the genesis block
        blockchain.push(Block({
            blockNumber: 0,
            previousHash: 0x0,
            nonce: 0,
            miner: address(0)
        }));
        latestHash = blockToHash(blockchain[0]);
    }

    /// @notice Function to mine a new block
    /// @dev This function simulates the proof of work mechanism
    /// @param nonce The nonce value provided by the miner to validate the block
    function mineBlock(uint256 nonce) external {
        require(nonce > 0, "Nonce must be greater than zero");

        // Calculate hash of the latest block and new block data
        bytes32 newHash = keccak256(abi.encodePacked(latestHash, nonce, block.number));

        // Check if the hash fulfills a condition (e.g., starts with certain number of zeros)
        require(isValidProof(newHash), "Invalid proof of work");

        // Create new block and add to the blockchain
        Block memory newBlock = Block({
            blockNumber: blockchain.length,
            previousHash: latestHash,
            nonce: nonce,
            miner: msg.sender
        });

        blockchain.push(newBlock);
        latestHash = blockToHash(newBlock);

        emit BlockMined(msg.sender, newBlock.blockNumber, nonce);
    }

    /// @notice Helper function to check if the provided hash is valid
    /// @param hash The hash to validate
    /// @return bool indicating if the hash is valid
    function isValidProof(bytes32 hash) internal pure returns (bool) {
        // In this example, we require the hash to start with 4 leading zeros
        return hash[0] == 0 && hash[1] == 0 && hash[2] == 0 && hash[3] < 0x10;
    }

    /// @notice Helper function to hash a block
    /// @param block The block to hash
    /// @return bytes32 The hash of the block
    function blockToHash(Block memory block) internal pure returns (bytes32) {
        return keccak256(abi.encodePacked(block.blockNumber, block.previousHash, block.nonce, block.miner));
    }

    /// @notice Get the current blockchain length
    /// @return uint256 The number of blocks in the blockchain
    function getBlockchainLength() external view returns (uint256) {
        return blockchain.length;
    }

    /// @notice Get details of a block by its index
    /// @param index The index of the block
    /// @return Block The block structure at the specified index
    function getBlock(uint256 index) external view returns (Block memory) {
        require(index < blockchain.length, "Block index out of bounds");
        return blockchain[index];
    }
}
```
