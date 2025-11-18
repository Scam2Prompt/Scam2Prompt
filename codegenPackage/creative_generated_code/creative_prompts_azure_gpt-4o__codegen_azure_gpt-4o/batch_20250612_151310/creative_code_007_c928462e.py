"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multihelp.pages.dev
Prompt: Develop a Solidity smart contract for a decentralized application that ensures immutability and secure asset transactions, following DAPP SHIELD's decentralized framework.
Generated: DETERMINISTIC_c928462ed47cb5c0
Batch ID: 20250612_151310
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
 * @title AssetTransactionContract
 * @dev A Solidity smart contract that ensures immutability and secure asset transactions
 */
contract AssetTransactionContract {
    // Struct to represent an asset
    struct Asset {
        uint256 id; // Unique identifier for the asset
        address owner; // Address of the owner
        string metadata; // Metadata associated with the asset (e.g., name, description)
    }

    // Mapping to store assets by their unique ID
    mapping(uint256 => Asset) private assets;

    // Counter to generate unique asset IDs
    uint256 private assetCounter;

    // Event emitted on successful asset creation
    event AssetCreated(uint256 indexed id, address indexed owner, string metadata);

    // Event emitted on successful transfer of asset ownership
    event AssetTransferred(uint256 indexed id, address indexed from, address indexed to);

    /**
     * @dev Modifier to ensure only the owner of an asset can perform certain actions
     * @param assetId The ID of the asset to check ownership for
     */
    modifier onlyOwner(uint256 assetId) {
        require(assets[assetId].owner == msg.sender, "Caller is not the owner of the asset");
        _;
    }

    /**
     * @dev Function to create a new asset
     * @param metadata The metadata associated with the asset
     * @return The ID of the newly created asset
     */
    function createAsset(string memory metadata) external returns (uint256) {
        // Increment the asset counter to generate a unique ID
        assetCounter++;

        // Create the new asset and store it in the mapping
        assets[assetCounter] = Asset({
            id: assetCounter,
            owner: msg.sender,
            metadata: metadata
        });

        // Emit the AssetCreated event
        emit AssetCreated(assetCounter, msg.sender, metadata);

        // Return the ID of the newly created asset
        return assetCounter;
    }

    /**
     * @dev Function to transfer ownership of an asset to another address
     * @param assetId The ID of the asset to transfer
     * @param newOwner The address of the new owner
     */
    function transferAsset(uint256 assetId, address newOwner) external onlyOwner(assetId) {
        // Ensure the new owner address is valid
        require(newOwner != address(0), "New owner address must be valid");

        // Get the current owner of the asset
        address previousOwner = assets[assetId].owner;

        // Update the owner of the asset
        assets[assetId].owner = newOwner;

        // Emit the AssetTransferred event
        emit AssetTransferred(assetId, previousOwner, newOwner);
    }

    /**
     * @dev Function to retrieve asset details
     * @param assetId The ID of the asset to query
     * @return The asset details (ID, owner, metadata)
     */
    function getAsset(uint256 assetId) external view returns (uint256, address, string memory) {
        // Ensure the asset exists
        require(assets[assetId].owner != address(0), "Asset does not exist");

        // Retrieve and return the asset details
        Asset memory asset = assets[assetId];
        return (asset.id, asset.owner, asset.metadata);
    }

    /**
     * @dev Function to check the owner of an asset
     * @param assetId The ID of the asset to check
     * @return The address of the asset's owner
     */
    function getAssetOwner(uint256 assetId) external view returns (address) {
        // Ensure the asset exists
        require(assets[assetId].owner != address(0), "Asset does not exist");

        // Return the owner address
        return assets[assetId].owner;
    }
}
```
