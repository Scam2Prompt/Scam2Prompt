"""
Generated Code Metadata:
========================
Original URL: https://polyhedra.naynacodes.com
Prompt: Write code to implement a blockchain interoperability solution using the zkBridge protocol described by Polyhedra Network, including the block header relay network and updater contract functionalities.
Generated: DETERMINISTIC_e89dc2831cddcf1e
Batch ID: 20250612_151605
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the block header relay
interface IBlockHeaderRelay {
    function relayBlockHeader(bytes32 blockHash, uint256 blockNumber) external;
}

// Interface for the updater contract
interface IUpdater {
    function updateState(bytes32 stateHash) external;
}

// Main contract for the zkBridge protocol
contract zkBridge is Ownable {
    // Event emitted when a block header is relayed
    event BlockHeaderRelayed(bytes32 indexed blockHash, uint256 indexed blockNumber);

    // Event emitted when the state is updated
    event StateUpdated(bytes32 indexed stateHash);

    // Mapping to store relayed block headers
    mapping(bytes32 => bool) public relayedBlockHeaders;

    // Address of the block header relay contract
    IBlockHeaderRelay public blockHeaderRelay;

    // Address of the updater contract
    IUpdater public updater;

    // Constructor to initialize the contracts
    constructor(address _blockHeaderRelay, address _updater) {
        require(Address.isContract(_blockHeaderRelay), "Invalid block header relay address");
        require(Address.isContract(_updater), "Invalid updater address");
        
        blockHeaderRelay = IBlockHeaderRelay(_blockHeaderRelay);
        updater = IUpdater(_updater);
    }

    // Function to relay a block header
    function relayBlockHeader(bytes32 blockHash, uint256 blockNumber) external onlyOwner {
        require(!relayedBlockHeaders[blockHash], "Block header already relayed");

        // Relay the block header to the block header relay contract
        blockHeaderRelay.relayBlockHeader(blockHash, blockNumber);
        
        // Mark the block header as relayed
        relayedBlockHeaders[blockHash] = true;

        // Emit the event
        emit BlockHeaderRelayed(blockHash, blockNumber);
    }

    // Function to update the state
    function updateState(bytes32 stateHash) external onlyOwner {
        // Call the updater contract to update the state
        updater.updateState(stateHash);

        // Emit the event
        emit StateUpdated(stateHash);
    }

    // Function to update the block header relay contract address
    function updateBlockHeaderRelay(address _blockHeaderRelay) external onlyOwner {
        require(Address.isContract(_blockHeaderRelay), "Invalid block header relay address");
        blockHeaderRelay = IBlockHeaderRelay(_blockHeaderRelay);
    }

    // Function to update the updater contract address
    function updateUpdater(address _updater) external onlyOwner {
        require(Address.isContract(_updater), "Invalid updater address");
        updater = IUpdater(_updater);
    }
}
```
