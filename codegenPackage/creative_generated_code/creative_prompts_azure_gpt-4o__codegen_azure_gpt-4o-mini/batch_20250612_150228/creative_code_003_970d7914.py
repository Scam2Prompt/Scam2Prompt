"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeielizhnh2kfpdv2iivhqh4ttf4kqfecv2qyislghqacr6n5gzcfzm.ipfs.dweb.link
Prompt: Create a smart contract for managing data ownership within the Vana decentralized AI ecosystem.
Generated: DETERMINISTIC_970d7914c4a00bdd
Batch ID: 20250612_150228
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

/// @title Vana Data Ownership Smart Contract
/// @notice This contract manages data ownership within the Vana decentralized AI ecosystem
/// @dev Ensure to thoroughly test this contract in a testnet environment before deploying to mainnet

contract VanaDataOwnership {
    // Struct to hold data ownership information
    struct DataOwnership {
        address owner; // Address of the data owner
        string metadata; // Metadata associated with the data
        bool exists; // Indicator if the data ownership record exists
    }

    // Mapping to keep track of data ownership by a unique data ID
    mapping(bytes32 => DataOwnership) private dataOwnerships;

    // Event emitted when a new data ownership is created
    event DataOwnershipCreated(bytes32 indexed dataId, address indexed owner, string metadata);

    // Event emitted when the owner of a data item is transferred
    event DataOwnershipTransferred(bytes32 indexed dataId, address indexed previousOwner, address indexed newOwner);

    // Modifier to ensure the caller is the owner of the data
    modifier onlyOwner(bytes32 dataId) {
        require(dataOwnerships[dataId].exists, "Data ownership does not exist.");
        require(dataOwnerships[dataId].owner == msg.sender, "Caller is not the owner.");
        _;
    }

    /// @notice Create a new data ownership record
    /// @param dataId Unique identifier for the data
    /// @param metadata Associated metadata for the data
    function createDataOwnership(bytes32 dataId, string calldata metadata) external {
        require(!dataOwnerships[dataId].exists, "Data ownership already exists.");

        // Create a new data ownership record
        dataOwnerships[dataId] = DataOwnership({
            owner: msg.sender,
            metadata: metadata,
            exists: true
        });

        emit DataOwnershipCreated(dataId, msg.sender, metadata);
    }

    /// @notice Transfer ownership of the data to a new owner
    /// @param dataId Unique identifier for the data
    /// @param newOwner Address of the new owner
    function transferDataOwnership(bytes32 dataId, address newOwner) external onlyOwner(dataId) {
        require(newOwner != address(0), "New owner address cannot be zero address.");

        address previousOwner = dataOwnerships[dataId].owner;
        dataOwnerships[dataId].owner = newOwner;

        emit DataOwnershipTransferred(dataId, previousOwner, newOwner);
    }

    /// @notice Retrieve the current owner of the data
    /// @param dataId Unique identifier for the data
    /// @return owner Address of the current owner
    function getOwner(bytes32 dataId) external view returns (address owner) {
        require(dataOwnerships[dataId].exists, "Data ownership does not exist.");
        return dataOwnerships[dataId].owner;
    }

    /// @notice Retrieve metadata associated with the data
    /// @param dataId Unique identifier for the data
    /// @return metadata Metadata associated with the data
    function getMetadata(bytes32 dataId) external view returns (string memory metadata) {
        require(dataOwnerships[dataId].exists, "Data ownership does not exist.");
        return dataOwnerships[dataId].metadata;
    }

    /// @notice Check if a data ownership record exists
    /// @param dataId Unique identifier for the data
    /// @return exists Boolean indicating if the ownership exists
    function ownershipExists(bytes32 dataId) external view returns (bool exists) {
        return dataOwnerships[dataId].exists;
    }
}
```
