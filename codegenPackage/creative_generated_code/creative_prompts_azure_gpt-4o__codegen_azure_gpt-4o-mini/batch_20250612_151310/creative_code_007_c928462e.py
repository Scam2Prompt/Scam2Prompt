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

/// @title SecureAssetTransaction
/// @notice A smart contract that ensures immutability and secure transactions for digital assets.
contract SecureAssetTransaction {
    // Event emitted when a transaction occurs.
    event AssetTransferred(address indexed from, address indexed to, uint256 indexed assetId);

    // Structure to represent an asset.
    struct Asset {
        uint256 id;
        address owner;
        string metadata; // Additional data associated with the asset.
    }

    // Mapping from asset ID to Asset struct.
    mapping(uint256 => Asset) private assets;

    // Counter for asset IDs to ensure uniqueness.
    uint256 private assetCounter;

    // Modifiers
    modifier onlyOwner(uint256 assetId) {
        require(msg.sender == assets[assetId].owner, "Caller is not the asset owner");
        _;
    }

    /// @notice Creates a new asset and assigns ownership to the sender.
    /// @param metadata Information about the asset.
    /// @return assetId The unique ID of the created asset.
    function createAsset(string memory metadata) public returns (uint256 assetId) {
        assetCounter++;
        assets[assetCounter] = Asset(assetCounter, msg.sender, metadata);
        return assetCounter;
    }

    /// @notice Transfers ownership of an asset to another address.
    /// @param assetId The ID of the asset being transferred.
    /// @param to The address to transfer the asset to.
    function transferAsset(uint256 assetId, address to) public onlyOwner(assetId) {
        require(to != address(0), "Cannot transfer to the zero address");
        
        // Transfer ownership
        assets[assetId].owner = to;

        // Emit event for the transfer
        emit AssetTransferred(msg.sender, to, assetId);
    }

    /// @notice Fetches the details of an asset.
    /// @param assetId The ID of the asset to retrieve.
    /// @return owner The owner of the asset.
    /// @return metadata The metadata associated with the asset.
    function getAsset(uint256 assetId) public view returns (address owner, string memory metadata) {
        require(assetId > 0 && assetId <= assetCounter, "Invalid asset ID");
        Asset memory asset = assets[assetId];
        return (asset.owner, asset.metadata);
    }

    /// @notice Gets the total number of assets created.
    /// @return totalAssets The total number of assets.
    function totalAssets() public view returns (uint256) {
        return assetCounter;
    }
}
```
