"""
Generated Code Metadata:
========================
Original URL: https://neotokyo-85y.pages.dev
Prompt: Design a smart contract to manage the minting and uploading of digital assets in the Neo Tokyo ecosystem.
Generated: DETERMINISTIC_9da884f3f7219178
Batch ID: 20250622_210243
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
 * @title NeoTokyoDigitalAssetManager
 * @dev A smart contract to manage the minting and uploading of digital assets in the Neo Tokyo ecosystem.
 */
contract NeoTokyoDigitalAssetManager {
    // Event emitted when a new asset is minted
    event AssetMinted(uint256 assetId, address indexed owner, string metadataURI);

    // Event emitted when an asset's metadata is updated
    event AssetMetadataUpdated(uint256 assetId, string oldMetadataURI, string newMetadataURI);

    // Struct to represent a digital asset
    struct DigitalAsset {
        uint256 id;
        address owner;
        string metadataURI;
    }

    // Mapping to store digital assets by their ID
    mapping(uint256 => DigitalAsset) private assets;

    // Counter to generate unique asset IDs
    uint256 private assetCounter;

    // Modifier to ensure only the owner of an asset can perform certain actions
    modifier onlyAssetOwner(uint256 assetId) {
        require(assets[assetId].owner == msg.sender, "Caller is not the asset owner");
        _;
    }

    /**
     * @dev Mint a new digital asset.
     * @param metadataURI The URI pointing to the asset's metadata.
     * @return The ID of the newly minted asset.
     */
    function mintAsset(string memory metadataURI) external returns (uint256) {
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");

        // Increment the asset counter to generate a new ID
        assetCounter++;

        // Create the new asset
        DigitalAsset memory newAsset = DigitalAsset({
            id: assetCounter,
            owner: msg.sender,
            metadataURI: metadataURI
        });

        // Store the asset in the mapping
        assets[assetCounter] = newAsset;

        // Emit the AssetMinted event
        emit AssetMinted(assetCounter, msg.sender, metadataURI);

        return assetCounter;
    }

    /**
     * @dev Update the metadata URI of an existing asset.
     * @param assetId The ID of the asset to update.
     * @param newMetadataURI The new metadata URI.
     */
    function updateAssetMetadata(uint256 assetId, string memory newMetadataURI) external onlyAssetOwner(assetId) {
        require(bytes(newMetadataURI).length > 0, "New metadata URI cannot be empty");

        // Get the asset
        DigitalAsset storage asset = assets[assetId];

        // Store the old metadata URI for the event
        string memory oldMetadataURI = asset.metadataURI;

        // Update the asset's metadata URI
        asset.metadataURI = newMetadataURI;

        // Emit the AssetMetadataUpdated event
        emit AssetMetadataUpdated(assetId, oldMetadataURI, newMetadataURI);
    }

    /**
     * @dev Get details of a digital asset.
     * @param assetId The ID of the asset to retrieve.
     * @return The asset's details (ID, owner, metadata URI).
     */
    function getAsset(uint256 assetId) external view returns (uint256, address, string memory) {
        require(assetId > 0 && assetId <= assetCounter, "Asset does not exist");

        DigitalAsset memory asset = assets[assetId];
        return (asset.id, asset.owner, asset.metadataURI);
    }

    /**
     * @dev Get the total number of assets minted.
     * @return The total number of assets.
     */
    function getTotalAssets() external view returns (uint256) {
        return assetCounter;
    }
}
```
