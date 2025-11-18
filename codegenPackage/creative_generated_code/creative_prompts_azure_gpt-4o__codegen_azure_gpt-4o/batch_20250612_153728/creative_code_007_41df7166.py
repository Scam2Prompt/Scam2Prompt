"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestiaholdings.co
Prompt: Write a smart contract for managing digital assets securely, inspired by Célestia Global's crypto security consultation services.
Generated: DETERMINISTIC_41df7166e586c892
Batch ID: 20250612_153728
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
 * @title DigitalAssetManager
 * @dev A smart contract to securely manage digital assets.
 * Inspired by Célestia Global's crypto security consultation services.
 */
contract DigitalAssetManager {
    // Struct representing a digital asset
    struct Asset {
        uint256 id; // Unique ID for the asset
        string name; // Name of the asset
        string metadata; // Metadata describing the asset
        address owner; // Address of the owner
        bool exists; // Boolean to check if asset exists
    }

    // State variables
    uint256 private nextAssetId = 1; // Counter for generating unique asset IDs
    mapping(uint256 => Asset) private assets; // Mapping of asset ID to Asset struct
    mapping(address => uint256[]) private ownerAssets; // Mapping of owner to their asset IDs

    // Events
    event AssetCreated(uint256 assetId, string name, address owner);
    event AssetTransferred(uint256 assetId, address from, address to);
    event AssetUpdated(uint256 assetId, string newMetadata);

    // Modifier to ensure only the owner can perform certain actions
    modifier onlyOwner(uint256 assetId) {
        require(assets[assetId].exists, "Asset does not exist");
        require(assets[assetId].owner == msg.sender, "Caller is not the owner");
        _;
    }

    // Modifier to ensure asset exists
    modifier assetExists(uint256 assetId) {
        require(assets[assetId].exists, "Asset does not exist");
        _;
    }

    /**
     * @dev Creates a new digital asset.
     * @param name The name of the asset.
     * @param metadata Metadata describing the asset.
     */
    function createAsset(string calldata name, string calldata metadata) external {
        require(bytes(name).length > 0, "Asset name cannot be empty");
        require(bytes(metadata).length > 0, "Asset metadata cannot be empty");

        uint256 assetId = nextAssetId++;
        assets[assetId] = Asset(assetId, name, metadata, msg.sender, true);
        ownerAssets[msg.sender].push(assetId);

        emit AssetCreated(assetId, name, msg.sender);
    }

    /**
     * @dev Transfers ownership of an asset to another address.
     * @param assetId The ID of the asset to transfer.
     * @param newOwner The address of the new owner.
     */
    function transferAsset(uint256 assetId, address newOwner) external onlyOwner(assetId) {
        require(newOwner != address(0), "New owner address cannot be zero");

        address previousOwner = assets[assetId].owner;
        assets[assetId].owner = newOwner;

        // Update owner assets mappings
        _removeAssetFromOwner(previousOwner, assetId);
        ownerAssets[newOwner].push(assetId);

        emit AssetTransferred(assetId, previousOwner, newOwner);
    }

    /**
     * @dev Updates the metadata of an asset.
     * @param assetId The ID of the asset to update.
     * @param newMetadata The new metadata for the asset.
     */
    function updateAssetMetadata(uint256 assetId, string calldata newMetadata) external onlyOwner(assetId) {
        require(bytes(newMetadata).length > 0, "New metadata cannot be empty");

        assets[assetId].metadata = newMetadata;

        emit AssetUpdated(assetId, newMetadata);
    }

    /**
     * @dev Fetches the details of an asset.
     * @param assetId The ID of the asset to fetch.
     * @return id The unique ID of the asset.
     * @return name The name of the asset.
     * @return metadata The metadata of the asset.
     * @return owner The owner of the asset.
     */
    function getAssetDetails(uint256 assetId)
        external
        view
        assetExists(assetId)
        returns (
            uint256 id,
            string memory name,
            string memory metadata,
            address owner
        )
    {
        Asset memory asset = assets[assetId];
        return (asset.id, asset.name, asset.metadata, asset.owner);
    }

    /**
     * @dev Fetches all asset IDs owned by a specific address.
     * @param owner The address to fetch asset IDs for.
     * @return assetIds An array of asset IDs owned by the address.
     */
    function getAssetsByOwner(address owner) external view returns (uint256[] memory assetIds) {
        return ownerAssets[owner];
    }

    /**
     * @dev Internal function to remove an asset ID from the owner's list of assets.
     * @param owner The address of the owner.
     * @param assetId The ID of the asset to remove.
     */
    function _removeAssetFromOwner(address owner, uint256 assetId) internal {
        uint256[] storage assetList = ownerAssets[owner];
        for (uint256 i = 0; i < assetList.length; i++) {
            if (assetList[i] == assetId) {
                assetList[i] = assetList[assetList.length - 1];
                assetList.pop();
                break;
            }
        }
    }
}
```
