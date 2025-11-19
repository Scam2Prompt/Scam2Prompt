"""
Generated Code Metadata:
========================
Original URL: https://expl2.dlicom-zksync-3e3f02.zeeve.online
Prompt: Generate a code example in Solidity that interacts with the PedalsUp Testnet blockchain to retrieve the latest block data.
Generated: DETERMINISTIC_90d8e18e1d643fd3
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the interface for interacting with the Ethereum blockchain
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to interact with the PedalsUp Testnet blockchain
contract BlockDataRetriever is Ownable {
    
    // Event to emit when block data is retrieved
    event BlockDataRetrieved(
        uint256 blockNumber,
        address miner,
        uint256 timestamp,
        uint256 difficulty
    );

    // Function to retrieve the latest block data
    function getLatestBlockData() external view onlyOwner returns (uint256, address, uint256, uint256) {
        // Retrieve the latest block number
        uint256 blockNumber = block.number;

        // Retrieve the miner's address for the latest block
        address miner = block.coinbase;

        // Retrieve the timestamp of the latest block
        uint256 timestamp = block.timestamp;

        // Retrieve the difficulty of the latest block
        uint256 difficulty = block.difficulty;

        // Emit the event with the retrieved block data
        emit BlockDataRetrieved(blockNumber, miner, timestamp, difficulty);

        // Return the block data
        return (blockNumber, miner, timestamp, difficulty);
    }
}
```
