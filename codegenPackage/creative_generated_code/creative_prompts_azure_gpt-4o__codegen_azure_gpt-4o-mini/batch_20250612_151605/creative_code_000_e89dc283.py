"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra.naynacodes.com
Prompt: Write code to implement a blockchain interoperability solution using the zkBridge protocol described by Polyhedra Network, including the block header relay network and updater contract functionalities.
Generated: DETERMINISTIC_e89dc2831cddcf1e
Batch ID: 20250612_151605
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

// Import necessary libraries and interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the zkBridge protocol
interface IBlockHeaderRelay {
    function relayBlockHeader(bytes memory blockHeader) external returns (bool);
}

// Updater contract for handling block header updates
contract BlockHeaderUpdater is Ownable {
    using SafeMath for uint256;

    // Event emitted when a block header is updated
    event BlockHeaderUpdated(bytes indexed blockHeader);

    // Address of the block header relay contract
    IBlockHeaderRelay public blockHeaderRelay;

    // Mapping to store block headers by their hash
    mapping(bytes32 => bool) public blockHeaderExists;

    // Constructor to initialize the relay contract address
    constructor(address _blockHeaderRelay) {
        require(_blockHeaderRelay != address(0), "Invalid relay contract address");
        blockHeaderRelay = IBlockHeaderRelay(_blockHeaderRelay);
    }

    // Function to update the block header
    function updateBlockHeader(bytes memory blockHeader) external onlyOwner {
        // Calculate the block header hash
        bytes32 blockHeaderHash = keccak256(blockHeader);

        // Check if the block header already exists
        require(!blockHeaderExists[blockHeaderHash], "Block header already exists");

        // Relay the block header using the relay contract
        bool success = blockHeaderRelay.relayBlockHeader(blockHeader);
        require(success, "Failed to relay block header");

        // Mark the block header as existing
        blockHeaderExists[blockHeaderHash] = true;

        // Emit an event for the updated block header
        emit BlockHeaderUpdated(blockHeader);
    }
}

// Contract to manage the block header relay functionality
contract BlockHeaderRelay is IBlockHeaderRelay {
    // Event to log the reception of a block header
    event BlockHeaderRelayed(bytes indexed blockHeader);

    // Function to relay block headers
    function relayBlockHeader(bytes memory blockHeader) external override returns (bool) {
        // Here you would implement the logic to handle the block header
        // For example, verifying the block header and storing it
        
        // Emit an event to signify that the block header was relayed
        emit BlockHeaderRelayed(blockHeader);
        
        // Returning true to indicate successful relay (placeholder for actual logic)
        return true;
    }
}
```
