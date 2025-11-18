"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxouyigo.com
Prompt: Write a smart contract in Solidity for managing rare digital assets, inspired by OKX's discussion of scarcity and value in Web3.0.
Generated: DETERMINISTIC_2af80e9723bece47
Batch ID: 20250612_145832
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

/**
 * @title RareDigitalAsset
 * @dev A smart contract for managing rare digital assets. Inspired by the concepts of scarcity and value in Web3.0.
 * This contract allows the creation, transfer, and tracking of unique digital assets.
 */
contract RareDigitalAsset {
    // State Variables
    address public owner; // Contract owner
    uint256 public totalSupply; // Total number of assets created

    // Struct to represent a unique digital asset
    struct Asset {
        uint256 id; // Unique ID
        string name; // Name of the asset
        string metadata; // Metadata associated with the asset
        address currentOwner; // Current owner of the asset
    }

    // Mapping to store assets by ID
    mapping(uint256 => Asset) public assets;

    // Mapping to track asset ownership
    mapping(address => uint256[]) public ownerAssets;

    // Events
    event AssetCreated(uint256 indexed id, string name, address indexed creator);
    event AssetTransferred(uint256 indexed id, address indexed from, address indexed to);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    modifier assetExists(uint256 assetId) {
        require(assets[assetId].id != 0, "Asset does not exist.");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Create a new digital asset.
     * @param name The name of the asset.
     * @param metadata Metadata for the asset.
     * Emits an AssetCreated event.
     */
    function createAsset(string memory name, string memory metadata) external onlyOwner {
        totalSupply++;
        uint256 assetId = totalSupply;

        // Create and store the asset
        assets[assetId] = Asset({
            id: assetId,
            name: name,
            metadata: metadata,
            currentOwner: owner
        });

        // Assign asset to the contract owner
        ownerAssets[owner].push(assetId);

        emit AssetCreated(assetId, name, msg.sender);
    }

    /**
     * @dev Transfer a digital asset to another address.
     * @param assetId The ID of the asset to transfer.
     * @param newOwner The address of the new owner.
     * Emits an AssetTransferred event.
     */
    function transferAsset(uint256 assetId, address newOwner) external assetExists(assetId) {
        // Check if the sender owns the asset
        require(assets[assetId].currentOwner == msg.sender, "You do not own this asset.");

        // Update the asset ownership
        assets[assetId].currentOwner = newOwner;

        // Update the owner's asset list
        _removeAssetFromOwner(msg.sender, assetId);
        ownerAssets[newOwner].push(assetId);

        emit AssetTransferred(assetId, msg.sender, newOwner);
    }

    /**
     * @dev Get the list of asset IDs owned by a specific address.
     * @param ownerAddress The address of the owner.
     * @return An array of asset IDs.
     */
    function getAssetsByOwner(address ownerAddress) external view returns (uint256[] memory) {
        return ownerAssets[ownerAddress];
    }

    /**
     * @dev Internal function to remove an asset from an owner's list.
     * @param ownerAddress The address of the owner.
     * @param assetId The ID of the asset to remove.
     */
    function _removeAssetFromOwner(address ownerAddress, uint256 assetId) internal {
        uint256[] storage assetsOwned = ownerAssets[ownerAddress];
        for (uint256 i = 0; i < assetsOwned.length; i++) {
            if (assetsOwned[i] == assetId) {
                assetsOwned[i] = assetsOwned[assetsOwned.length - 1];
                assetsOwned.pop();
                break;
            }
        }
    }
}
```
