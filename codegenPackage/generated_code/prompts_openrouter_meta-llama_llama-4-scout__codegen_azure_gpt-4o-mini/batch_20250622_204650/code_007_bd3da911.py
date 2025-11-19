"""
Generated Code Metadata:
========================
Original URL: https://ondo-foundation.pages.dev
Prompt: Design a smart contract using Solidity that enables the tokenization of real-world assets (RWAs) on a blockchain, inspired by the Ondo Foundation's work.
Generated: DETERMINISTIC_bd3da9119d916700
Batch ID: 20250622_204650
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// @title RealWorldAssetToken
// @dev A smart contract for tokenizing real-world assets (RWAs) using ERC20 tokens
contract RealWorldAssetToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Struct to represent a real-world asset
    struct Asset {
        string name;          // Name of the asset
        string description;   // Description of the asset
        uint256 value;        // Value of the asset in smallest currency unit
        bool exists;          // Flag to check if asset exists
    }

    // Mapping from asset ID to Asset struct
    mapping(uint256 => Asset) private assets;

    // Event emitted when a new asset is tokenized
    event AssetTokenized(uint256 indexed assetId, string name, uint256 value);

    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 indexed assetId, address from, address to, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("RealWorldAssetToken", "RWAT") {}

    // @dev Function to tokenize a new real-world asset
    // @param assetId Unique identifier for the asset
    // @param name Name of the asset
    // @param description Description of the asset
    // @param value Value of the asset in smallest currency unit
    function tokenizeAsset(uint256 assetId, string memory name, string memory description, uint256 value) external onlyOwner {
        require(!assets[assetId].exists, "Asset already exists");

        // Create a new asset
        assets[assetId] = Asset({
            name: name,
            description: description,
            value: value,
            exists: true
        });

        // Mint tokens equivalent to the asset's value
        _mint(msg.sender, value);

        emit AssetTokenized(assetId, name, value);
    }

    // @dev Function to transfer tokens representing an asset
    // @param assetId Unique identifier for the asset
    // @param to Address to transfer tokens to
    // @param amount Amount of tokens to transfer
    function transferAsset(uint256 assetId, address to, uint256 amount) external {
        require(assets[assetId].exists, "Asset does not exist");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens
        _transfer(msg.sender, to, amount);

        emit AssetTransferred(assetId, msg.sender, to, amount);
    }

    // @dev Function to get asset details
    // @param assetId Unique identifier for the asset
    // @return name Name of the asset
    // @return description Description of the asset
    // @return value Value of the asset
    function getAsset(uint256 assetId) external view returns (string memory name, string memory description, uint256 value) {
        require(assets[assetId].exists, "Asset does not exist");

        Asset memory asset = assets[assetId];
        return (asset.name, asset.description, asset.value);
    }
}
```
