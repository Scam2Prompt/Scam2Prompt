"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nimnetwork.pages.dev
Prompt: Write a smart contract for asset verification on the Nim Rolldrop AI Gaming Chain using Solidity.
Generated: DETERMINISTIC_31f666d171ad0234
Batch ID: 20250612_152620
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

/// @title Asset Verification Smart Contract
/// @notice This contract manages the verification of assets on the Nim Rolldrop AI Gaming Chain
/// @dev This contract allows users to register and verify assets securely
contract AssetVerification {
    
    // Structure to hold asset information
    struct Asset {
        uint256 id;               // Unique identifier for the asset
        string name;              // Name of the asset
        address owner;            // Owner of the asset
        bool verified;            // Verification status
    }

    // Mapping from asset ID to Asset struct
    mapping(uint256 => Asset) private assets;

    // Event emitted when an asset is registered
    event AssetRegistered(uint256 indexed assetId, string name, address indexed owner);

    // Event emitted when an asset is verified
    event AssetVerified(uint256 indexed assetId);

    // Error messages
    error AssetNotFound(uint256 assetId);
    error NotAssetOwner(address caller, address assetOwner);
    
    /// @notice Registers a new asset
    /// @param assetId The unique identifier for the asset
    /// @param name The name of the asset
    /// @dev The caller must be the current owner of the asset
    function registerAsset(uint256 assetId, string memory name) external {
        // Ensure the asset does not already exist
        require(assets[assetId].id == 0, "Asset already registered");

        // Create and store the new asset
        assets[assetId] = Asset({
            id: assetId,
            name: name,
            owner: msg.sender,
            verified: false
        });

        // Emit event for asset registration
        emit AssetRegistered(assetId, name, msg.sender);
    }

    /// @notice Verifies the specified asset
    /// @param assetId The unique identifier for the asset to verify
    /// @dev Only the owner of the asset can verify it
    function verifyAsset(uint256 assetId) external {
        Asset storage asset = assets[assetId];

        // Check if the asset exists
        if (asset.id == 0) {
            revert AssetNotFound(assetId);
        }

        // Ensure only the asset owner can verify
        if (msg.sender != asset.owner) {
            revert NotAssetOwner(msg.sender, asset.owner);
        }

        // Update the verification status
        asset.verified = true;

        // Emit event for asset verification
        emit AssetVerified(assetId);
    }

    /// @notice Gets the details of an asset
    /// @param assetId The unique identifier for the asset
    /// @return The asset details: id, name, owner, verified status
    function getAsset(uint256 assetId) external view returns (Asset memory) {
        Asset memory asset = assets[assetId];

        // Check if the asset exists
        if (asset.id == 0) {
            revert AssetNotFound(assetId);
        }

        return asset;
    }

    /// @notice Checks if an asset is verified
    /// @param assetId The unique identifier for the asset
    /// @return True if the asset is verified, false otherwise
    function isAssetVerified(uint256 assetId) external view returns (bool) {
        Asset memory asset = assets[assetId];

        // Asset must exist to check its verification status
        require(asset.id != 0, "Asset not found");
        
        return asset.verified;
    }
}
```
