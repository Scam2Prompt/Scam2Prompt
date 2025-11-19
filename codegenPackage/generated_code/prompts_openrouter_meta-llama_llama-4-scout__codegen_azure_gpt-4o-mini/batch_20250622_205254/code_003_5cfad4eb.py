"""
Generated Code Metadata:
========================
Original URL: https://polyhedra.naynacodes.com
Prompt: "Implement a block header relay network and updater contract using Expander, a fast ZK proof system, for a blockchain interoperability application."
Generated: DETERMINISTIC_5cfad4eb4d80ccb6
Batch ID: 20250622_205254
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

// Importing necessary libraries and interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the Expander ZK proof system
interface IExpander {
    function verifyProof(bytes calldata proof, bytes calldata input) external returns (bool);
}

// Contract for Block Header Relay Network
contract BlockHeaderRelay is Ownable {
    // Event emitted when a new block header is relayed
    event BlockHeaderRelayed(bytes32 indexed blockHash, bytes blockHeader);

    // Mapping to store block headers by their hash
    mapping(bytes32 => bytes) private blockHeaders;

    // Instance of the Expander ZK proof system
    IExpander public expander;

    // Constructor to set the Expander contract address
    constructor(address _expanderAddress) {
        require(Address.isContract(_expanderAddress), "Invalid Expander contract address");
        expander = IExpander(_expanderAddress);
    }

    // Function to relay a block header with a ZK proof
    function relayBlockHeader(bytes32 blockHash, bytes calldata blockHeader, bytes calldata proof, bytes calldata input) external onlyOwner {
        // Verify the ZK proof
        require(expander.verifyProof(proof, input), "Invalid ZK proof");

        // Store the block header
        blockHeaders[blockHash] = blockHeader;

        // Emit event for the relayed block header
        emit BlockHeaderRelayed(blockHash, blockHeader);
    }

    // Function to retrieve a block header by its hash
    function getBlockHeader(bytes32 blockHash) external view returns (bytes memory) {
        // Check if the block header exists
        require(blockHeaders[blockHash].length > 0, "Block header not found");
        return blockHeaders[blockHash];
    }

    // Function to update the Expander contract address
    function updateExpanderAddress(address newExpanderAddress) external onlyOwner {
        require(Address.isContract(newExpanderAddress), "Invalid Expander contract address");
        expander = IExpander(newExpanderAddress);
    }
}
```
