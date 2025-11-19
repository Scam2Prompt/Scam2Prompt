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

/**
 * @title KnowledgeAssetManager
 * @dev A smart contract to manage knowledge assets and their ownership on a blockchain platform.
 * Compatible with OriginTrail's multichain vision.
 */
contract KnowledgeAssetManager {
    // Struct to represent a knowledge asset
    struct KnowledgeAsset {
        string assetId; // Unique identifier for the asset
        string metadata; // Metadata describing the asset
        address owner; // Current owner of the asset
    }

    // Mapping to store knowledge assets by their unique ID
    mapping(string => KnowledgeAsset) private assets;

    // Event emitted when a new asset is registered
    event AssetRegistered(string assetId, string metadata, address indexed owner);

    // Event emitted when ownership of an asset is transferred
    event OwnershipTransferred(string assetId, address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Registers a new knowledge asset.
     * @param assetId The unique identifier for the asset.
     * @param metadata Metadata describing the asset.
     */
    function registerAsset(string memory assetId, string memory metadata) external {
        require(bytes(assetId).length > 0, "Asset ID cannot be empty");
        require(bytes(metadata).length > 0, "Metadata cannot be empty");
        require(assets[assetId].owner == address(0), "Asset already exists");

        // Create a new knowledge asset
        assets[assetId] = KnowledgeAsset({
            assetId: assetId,
            metadata: metadata,
            owner: msg.sender
        });

        emit AssetRegistered(assetId, metadata, msg.sender);
    }

    /**
     * @dev Transfers ownership of a knowledge asset to a new owner.
     * @param assetId The unique identifier for the asset.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(string memory assetId, address newOwner) external {
        require(bytes(assetId).length > 0, "Asset ID cannot be empty");
        require(newOwner != address(0), "New owner address cannot be zero");
        require(assets[assetId].owner == msg.sender, "Caller is not the owner of the asset");

        address previousOwner = assets[assetId].owner;

        // Update the owner of the asset
        assets[assetId].owner = newOwner;

        emit OwnershipTransferred(assetId, previousOwner, newOwner);
    }

    /**
     * @dev Retrieves the details of a knowledge asset.
     * @param assetId The unique identifier for the asset.
     * @return metadata Metadata describing the asset.
     * @return owner The current owner of the asset.
     */
    function getAssetDetails(string memory assetId) external view returns (string memory metadata, address owner) {
        require(bytes(assetId).length > 0, "Asset ID cannot be empty");
        require(assets[assetId].owner != address(0), "Asset does not exist");

        KnowledgeAsset memory asset = assets[assetId];
        return (asset.metadata, asset.owner);
    }
}
```
