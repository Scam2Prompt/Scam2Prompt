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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title KnowledgeAssetManager
 * @dev A smart contract for managing knowledge assets and their ownership on blockchain
 */
contract KnowledgeAssetManager is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to represent a Knowledge Asset
    struct KnowledgeAsset {
        uint256 id;
        string uri; // URI pointing to the asset's metadata
        address owner;
        uint256 createdAt;
        uint256 updatedAt;
    }

    // Mapping from asset ID to KnowledgeAsset
    mapping(uint256 => KnowledgeAsset) private _assets;
    
    // Mapping from owner address to their owned asset IDs
    mapping(address => uint256[]) private _ownedAssets;
    
    // Counter for generating unique asset IDs
    Counters.Counter private _assetIdCounter;
    
    // Event emitted when a new asset is created
    event AssetCreated(
        uint256 indexed id,
        address indexed owner,
        string uri,
        uint256 createdAt
    );
    
    // Event emitted when asset ownership is transferred
    event AssetTransferred(
        uint256 indexed id,
        address indexed previousOwner,
        address indexed newOwner
    );
    
    // Event emitted when asset metadata is updated
    event AssetUpdated(
        uint256 indexed id,
        string newUri,
        uint256 updatedAt
    );

    /**
     * @dev Creates a new knowledge asset
     * @param uri The URI pointing to the asset's metadata
     * @return The ID of the newly created asset
     */
    function createAsset(string memory uri) external returns (uint256) {
        require(bytes(uri).length > 0, "URI cannot be empty");
        
        _assetIdCounter.increment();
        uint256 newAssetId = _assetIdCounter.current();
        
        KnowledgeAsset memory newAsset = KnowledgeAsset({
            id: newAssetId,
            uri: uri,
            owner: msg.sender,
            createdAt: block.timestamp,
            updatedAt: block.timestamp
        });
        
        _assets[newAssetId] = newAsset;
        _ownedAssets[msg.sender].push(newAssetId);
        
        emit AssetCreated(newAssetId, msg.sender, uri, block.timestamp);
        
        return newAssetId;
    }

    /**
     * @dev Transfers ownership of an asset
     * @param assetId The ID of the asset to transfer
     * @param newOwner The address of the new owner
     */
    function transferAsset(uint256 assetId, address newOwner) external {
        require(newOwner != address(0), "New owner cannot be zero address");
        require(_assets[assetId].owner == msg.sender, "Only owner can transfer");
        
        address previousOwner = _assets[assetId].owner;
        _assets[assetId].owner = newOwner;
        _assets[assetId].updatedAt = block.timestamp;
        
        // Remove from previous owner's list
        _removeAssetFromOwner(previousOwner, assetId);
        
        // Add to new owner's list
        _ownedAssets[newOwner].push(assetId);
        
        emit AssetTransferred(assetId, previousOwner, newOwner);
    }

    /**
     * @dev Updates the URI of an asset
     * @param assetId The ID of the asset to update
     * @param newUri The new URI for the asset
     */
    function updateAssetUri(uint256 assetId, string memory newUri) external {
        require(bytes(newUri).length > 0, "URI cannot be empty");
        require(_assets[assetId].owner == msg.sender, "Only owner can update");
        
        _assets[assetId].uri = newUri;
        _assets[assetId].updatedAt = block.timestamp;
        
        emit AssetUpdated(assetId, newUri, block.timestamp);
    }

    /**
     * @dev Gets an asset by ID
     * @param assetId The ID of the asset to retrieve
     * @return The KnowledgeAsset struct
     */
    function getAsset(uint256 assetId) external view returns (KnowledgeAsset memory) {
        require(_assets[assetId].id != 0, "Asset does not exist");
        return _assets[assetId];
    }

    /**
     * @dev Gets all asset IDs owned by an address
     * @param owner The address to query
     * @return An array of asset IDs
     */
    function getAssetsByOwner(address owner) external view returns (uint256[] memory) {
        return _ownedAssets[owner];
    }

    /**
     * @dev Internal function to remove an asset from an owner's list
     * @param owner The owner's address
     * @param assetId The ID of the asset to remove
     */
    function _removeAssetFromOwner(address owner, uint256 assetId) private {
        uint256[] storage ownerAssets = _ownedAssets[owner];
        for (uint256 i = 0; i < ownerAssets.length; i++) {
            if (ownerAssets[i] == assetId) {
                ownerAssets[i] = ownerAssets[ownerAssets.length - 1];
                ownerAssets.pop();
                break;
            }
        }
    }
}
```
