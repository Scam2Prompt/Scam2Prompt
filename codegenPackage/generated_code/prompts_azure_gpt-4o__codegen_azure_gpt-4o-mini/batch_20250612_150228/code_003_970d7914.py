"""
Generated Code Metadata:
========================
Original URL: https://bafybeielizhnh2kfpdv2iivhqh4ttf4kqfecv2qyislghqacr6n5gzcfzm.ipfs.dweb.link
Prompt: Create a smart contract for managing data ownership within the Vana decentralized AI ecosystem.
Generated: DETERMINISTIC_970d7914c4a00bdd
Batch ID: 20250612_150228
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

/// @title Vana Data Ownership Smart Contract
/// @author Your Name
/// @notice This contract manages data ownership within the Vana decentralized AI ecosystem
/// @dev This contract allows users to register, transfer, and revoke ownership of data

contract VanaDataOwnership {
    // Struct to represent data ownership
    struct Data {
        address owner;
        string metadata; // Metadata associated with the data
        bool exists; // Flag to check if data is registered
    }

    // Mapping from data ID to Data struct
    mapping(bytes32 => Data) private dataRegistry;

    // Event emitted when data ownership is registered
    event DataRegistered(bytes32 indexed dataId, address indexed owner, string metadata);

    // Event emitted when data ownership is transferred
    event DataTransferred(bytes32 indexed dataId, address indexed from, address indexed to);

    // Event emitted when data ownership is revoked
    event DataRevoked(bytes32 indexed dataId, address indexed owner);

    /// @notice Registers new data ownership
    /// @param dataId Unique identifier for the data
    /// @param metadata Metadata associated with the data
    function registerData(bytes32 dataId, string memory metadata) external {
        require(!dataRegistry[dataId].exists, "Data already registered");
        
        // Register the data
        dataRegistry[dataId] = Data({
            owner: msg.sender,
            metadata: metadata,
            exists: true
        });

        emit DataRegistered(dataId, msg.sender, metadata);
    }

    /// @notice Transfers data ownership to a new owner
    /// @param dataId Unique identifier for the data
    /// @param newOwner Address of the new owner
    function transferData(bytes32 dataId, address newOwner) external {
        require(dataRegistry[dataId].exists, "Data not registered");
        require(dataRegistry[dataId].owner == msg.sender, "Only the owner can transfer data");
        require(newOwner != address(0), "New owner cannot be the zero address");

        // Transfer ownership
        address previousOwner = dataRegistry[dataId].owner;
        dataRegistry[dataId].owner = newOwner;

        emit DataTransferred(dataId, previousOwner, newOwner);
    }

    /// @notice Revokes data ownership
    /// @param dataId Unique identifier for the data
    function revokeData(bytes32 dataId) external {
        require(dataRegistry[dataId].exists, "Data not registered");
        require(dataRegistry[dataId].owner == msg.sender, "Only the owner can revoke data");

        // Revoke ownership
        delete dataRegistry[dataId];

        emit DataRevoked(dataId, msg.sender);
    }

    /// @notice Gets the owner of the data
    /// @param dataId Unique identifier for the data
    /// @return owner Address of the data owner
    function getDataOwner(bytes32 dataId) external view returns (address owner) {
        require(dataRegistry[dataId].exists, "Data not registered");
        return dataRegistry[dataId].owner;
    }

    /// @notice Gets the metadata of the data
    /// @param dataId Unique identifier for the data
    /// @return metadata Metadata associated with the data
    function getDataMetadata(bytes32 dataId) external view returns (string memory metadata) {
        require(dataRegistry[dataId].exists, "Data not registered");
        return dataRegistry[dataId].metadata;
    }
}
```
