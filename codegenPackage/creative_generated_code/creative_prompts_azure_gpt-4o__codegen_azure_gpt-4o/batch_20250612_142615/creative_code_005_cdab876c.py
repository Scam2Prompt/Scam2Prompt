"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasnft.org
Prompt: Develop a smart contract for managing Cornucopias digital assets, ensuring ownership verification and compatibility with the in-game economy.
Generated: DETERMINISTIC_cdab876cf5eadb67
Batch ID: 20250612_142615
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
 * @title CornucopiasAssetManager
 * @dev A smart contract for managing Cornucopias digital assets, ensuring ownership verification
 * and compatibility with the in-game economy.
 */
contract CornucopiasAssetManager {
    // Struct to define an asset in the game
    struct Asset {
        uint256 assetId;       // Unique identifier for the asset
        string name;           // Name of the asset
        string assetType;      // Type of asset (e.g., item, vehicle, land)
        uint256 value;         // Value of the asset in in-game currency
        address owner;         // Current owner of the asset
    }

    // Mapping of asset IDs to Asset structs
    mapping(uint256 => Asset) private assets;

    // Mapping to track all owned assets of an address
    mapping(address => uint256[]) private ownedAssets;

    // Event emitted when an asset is created
    event AssetCreated(uint256 indexed assetId, string name, string assetType, uint256 value, address indexed owner);

    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 indexed assetId, address indexed from, address indexed to);

    // Modifier to ensure the caller is the owner of the asset
    modifier onlyOwner(uint256 assetId) {
        require(assets[assetId].owner == msg.sender, "Caller is not the owner of the asset");
        _;
    }

    /**
     * @dev Create an asset and assign ownership to the caller.
     * @param assetId Unique ID for the asset.
     * @param name Name of the asset.
     * @param assetType Type of the asset (e.g., item, vehicle, land).
     * @param value Value of the asset in in-game currency.
     */
    function createAsset(uint256 assetId, string memory name, string memory assetType, uint256 value) external {
        require(assets[assetId].owner == address(0), "Asset ID already exists");

        // Create the asset
        Asset memory newAsset = Asset({
            assetId: assetId,
            name: name,
            assetType: assetType,
            value: value,
            owner: msg.sender
        });

        // Save the asset in mapping
        assets[assetId] = newAsset;

        // Track ownership
        ownedAssets[msg.sender].push(assetId);

        // Emit event
        emit AssetCreated(assetId, name, assetType, value, msg.sender);
    }

    /**
     * @dev Transfer ownership of an asset to another address.
     * @param assetId ID of the asset to transfer.
     * @param to Address of the new owner.
     */
    function transferAsset(uint256 assetId, address to) external onlyOwner(assetId) {
        require(to != address(0), "Cannot transfer to the zero address");

        // Remove asset from current owner's collection
        uint256[] storage senderAssets = ownedAssets[msg.sender];
        for (uint256 i = 0; i < senderAssets.length; i++) {
            if (senderAssets[i] == assetId) {
                senderAssets[i] = senderAssets[senderAssets.length - 1];
                senderAssets.pop();
                break;
            }
        }

        // Update ownership
        assets[assetId].owner = to;
        ownedAssets[to].push(assetId);

        // Emit event
        emit AssetTransferred(assetId, msg.sender, to);
    }

    /**
     * @dev Get details of an asset.
     * @param assetId ID of the asset.
     * @return Asset details.
     */
    function getAsset(uint256 assetId) external view returns (Asset memory) {
        require(assets[assetId].owner != address(0), "Asset does not exist");
        return assets[assetId];
    }

    /**
     * @dev Get all asset IDs owned by a specific address.
     * @param owner Address to query.
     * @return Array of asset IDs owned by the address.
     */
    function getOwnedAssets(address owner) external view returns (uint256[] memory) {
        return ownedAssets[owner];
    }
}
```
