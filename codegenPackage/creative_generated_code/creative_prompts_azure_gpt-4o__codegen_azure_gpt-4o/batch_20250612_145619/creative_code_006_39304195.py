"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaimin-io.pages.dev
Prompt: Create a smart contract for GAIMIN's L2 gaming blockchain that supports 150k TPS and enables low-latency transactions for in-game assets.
Generated: DETERMINISTIC_39304195c1b65726
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/// @title GAIMIN L2 Gaming Blockchain Smart Contract
/// @notice This contract is designed to handle in-game asset transactions with high throughput and low latency.
/// @dev Leveraging Solidity 0.8.x for its built-in overflow/underflow protection and gas optimizations.
contract GaiminL2Gaming {

    // Events
    event AssetTransferred(address indexed from, address indexed to, uint256 assetId, uint256 amount);
    event AssetMinted(uint256 indexed assetId, address indexed owner, uint256 amount);
    event AssetBurned(uint256 indexed assetId, address indexed owner, uint256 amount);

    // Struct to represent an asset
    struct Asset {
        string name; // Asset name
        address creator; // Address that created the asset
        uint256 totalSupply; // Total supply of the asset
    }

    // Asset storage
    mapping(uint256 => Asset) private assets; // Maps asset ID to Asset details
    mapping(address => mapping(uint256 => uint256)) private balances; // Tracks balances per user per asset

    // Admin address
    address public admin;

    // Next asset ID
    uint256 private nextAssetId = 1;

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    // Constructor to set admin
    constructor() {
        admin = msg.sender;
    }

    // Function to mint a new asset
    /// @param name Name of the new asset
    /// @param initialSupply Initial supply of the asset
    /// @param owner Owner of the newly minted asset
    /// @return assetId ID of the newly minted asset
    function mintAsset(string memory name, uint256 initialSupply, address owner) external onlyAdmin returns (uint256 assetId) {
        require(bytes(name).length > 0, "Asset name must not be empty");
        require(owner != address(0), "Owner address must not be zero");

        assetId = nextAssetId++;
        assets[assetId] = Asset({ name: name, creator: msg.sender, totalSupply: initialSupply });
        balances[owner][assetId] = initialSupply;

        emit AssetMinted(assetId, owner, initialSupply);
    }

    // Function to transfer an asset
    /// @param to Recipient address
    /// @param assetId ID of the asset to transfer
    /// @param amount Amount of the asset to transfer
    function transferAsset(address to, uint256 assetId, uint256 amount) external {
        require(to != address(0), "Recipient address must not be zero");
        require(assets[assetId].creator != address(0), "Asset does not exist");
        require(balances[msg.sender][assetId] >= amount, "Insufficient balance");

        balances[msg.sender][assetId] -= amount;
        balances[to][assetId] += amount;

        emit AssetTransferred(msg.sender, to, assetId, amount);
    }

    // Function to burn an asset
    /// @param assetId ID of the asset to burn
    /// @param amount Amount of the asset to burn
    function burnAsset(uint256 assetId, uint256 amount) external {
        require(assets[assetId].creator != address(0), "Asset does not exist");
        require(balances[msg.sender][assetId] >= amount, "Insufficient balance");

        balances[msg.sender][assetId] -= amount;
        assets[assetId].totalSupply -= amount;

        emit AssetBurned(assetId, msg.sender, amount);
    }

    // Function to get the details of an asset
    /// @param assetId ID of the asset
    /// @return name Name of the asset
    /// @return creator Creator of the asset
    /// @return totalSupply Total supply of the asset
    function getAssetDetails(uint256 assetId) external view returns (string memory name, address creator, uint256 totalSupply) {
        Asset memory asset = assets[assetId];
        require(asset.creator != address(0), "Asset does not exist");

        return (asset.name, asset.creator, asset.totalSupply);
    }

    // Function to get the balance of an asset for a user
    /// @param owner Address of the owner
    /// @param assetId ID of the asset
    /// @return balance Balance of the asset
    function getAssetBalance(address owner, uint256 assetId) external view returns (uint256 balance) {
        return balances[owner][assetId];
    }

    // Function to change admin
    /// @param newAdmin Address of the new admin
    function changeAdmin(address newAdmin) external onlyAdmin {
        require(newAdmin != address(0), "New admin address must not be zero");
        admin = newAdmin;
    }
}
```
