"""
Generated Code Metadata:
========================
Original URL: https://fortnite3003.pages.dev
Prompt: "Develop a smart contract to manage knowledge assets and their ownership on a blockchain platform compatible with OriginTrail's multichain vision."
Generated: DETERMINISTIC_5ccfa37bdc3c72a3
Batch ID: 20250622_205948
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

/// @title KnowledgeAssetManager
/// @dev A smart contract to manage knowledge assets and their ownership
contract KnowledgeAssetManager {
    // Struct to represent a knowledge asset
    struct KnowledgeAsset {
        uint256 id;                // Unique identifier for the asset
        string name;               // Name of the knowledge asset
        string description;        // Description of the knowledge asset
        address owner;             // Current owner of the asset
        bool exists;               // Flag to check if asset exists
    }

    // Mapping from asset ID to KnowledgeAsset
    mapping(uint256 => KnowledgeAsset) private assets;
    // Counter for asset IDs
    uint256 private assetCounter;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 indexed assetId, string name, address indexed owner);
    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 indexed assetId, address indexed from, address indexed to);

    /// @dev Creates a new knowledge asset
    /// @param _name The name of the knowledge asset
    /// @param _description The description of the knowledge asset
    function createAsset(string memory _name, string memory _description) public {
        require(bytes(_name).length > 0, "Asset name cannot be empty");
        require(bytes(_description).length > 0, "Asset description cannot be empty");

        assetCounter++;
        assets[assetCounter] = KnowledgeAsset(assetCounter, _name, _description, msg.sender, true);

        emit AssetCreated(assetCounter, _name, msg.sender);
    }

    /// @dev Transfers ownership of a knowledge asset
    /// @param _assetId The ID of the asset to transfer
    /// @param _newOwner The address of the new owner
    function transferAsset(uint256 _assetId, address _newOwner) public {
        require(assets[_assetId].exists, "Asset does not exist");
        require(assets[_assetId].owner == msg.sender, "Only the owner can transfer the asset");
        require(_newOwner != address(0), "New owner cannot be the zero address");

        address previousOwner = assets[_assetId].owner;
        assets[_assetId].owner = _newOwner;

        emit AssetTransferred(_assetId, previousOwner, _newOwner);
    }

    /// @dev Retrieves the details of a knowledge asset
    /// @param _assetId The ID of the asset to retrieve
    /// @return The details of the knowledge asset
    function getAsset(uint256 _assetId) public view returns (KnowledgeAsset memory) {
        require(assets[_assetId].exists, "Asset does not exist");
        return assets[_assetId];
    }

    /// @dev Checks if an asset exists
    /// @param _assetId The ID of the asset to check
    /// @return True if the asset exists, false otherwise
    function assetExists(uint256 _assetId) public view returns (bool) {
        return assets[_assetId].exists;
    }
}
```
