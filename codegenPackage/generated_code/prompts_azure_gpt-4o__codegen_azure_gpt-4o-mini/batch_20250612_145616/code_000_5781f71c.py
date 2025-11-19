"""
Generated Code Metadata:
========================
Original URL: https://somnial.pages.dev
Prompt: Write a smart contract using Somnia's EVM Layer 1 blockchain to enable interoperability between two metaverses, ensuring seamless asset transfer and user interaction.
Generated: DETERMINISTIC_5781f71c55144d2a
Batch ID: 20250612_145616
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

/// @title Interoperability Smart Contract for Metaverses
/// @author Your Name
/// @notice This contract enables seamless asset transfer and user interaction between two metaverses
/// @dev This contract is designed to be deployed on Somnia's EVM Layer 1 blockchain

contract MetaverseInteroperability {
    // Event emitted when an asset is transferred between metaverses
    event AssetTransferred(
        address indexed from,
        address indexed to,
        uint256 assetId,
        string metaverseFrom,
        string metaverseTo
    );

    // Mapping to track asset ownership
    mapping(uint256 => address) private assetOwners;

    // Modifier to check if the caller is the owner of the asset
    modifier onlyAssetOwner(uint256 assetId) {
        require(assetOwners[assetId] == msg.sender, "Caller is not the asset owner");
        _;
    }

    /// @notice Transfer an asset from one metaverse to another
    /// @param assetId The ID of the asset being transferred
    /// @param to The address of the recipient in the target metaverse
    /// @param metaverseFrom The name of the source metaverse
    /// @param metaverseTo The name of the target metaverse
    function transferAsset(
        uint256 assetId,
        address to,
        string memory metaverseFrom,
        string memory metaverseTo
    ) external onlyAssetOwner(assetId) {
        // Ensure the recipient address is valid
        require(to != address(0), "Invalid recipient address");

        // Transfer the asset ownership
        assetOwners[assetId] = to;

        // Emit the asset transfer event
        emit AssetTransferred(msg.sender, to, assetId, metaverseFrom, metaverseTo);
    }

    /// @notice Get the owner of a specific asset
    /// @param assetId The ID of the asset
    /// @return The address of the asset owner
    function getAssetOwner(uint256 assetId) external view returns (address) {
        return assetOwners[assetId];
    }

    /// @notice Register an asset to an owner
    /// @param assetId The ID of the asset to register
    function registerAsset(uint256 assetId) external {
        // Ensure the asset is not already registered
        require(assetOwners[assetId] == address(0), "Asset already registered");

        // Register the asset to the caller
        assetOwners[assetId] = msg.sender;
    }

    /// @notice Unregister an asset from the owner
    /// @param assetId The ID of the asset to unregister
    /// @dev Only the asset owner can unregister the asset
    function unregisterAsset(uint256 assetId) external onlyAssetOwner(assetId) {
        // Unregister the asset by setting its owner to the zero address
        assetOwners[assetId] = address(0);
    }
}
```
