"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaindapps.pages.dev
Prompt: Write code to implement a decentralized asset management system using blockchain, as described on Decentralised Connect.
Generated: DETERMINISTIC_81320cf926c0d83a
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation for a decentralized asset management system using blockchain technology. The code is written in Solidity (Ethereum smart contracts) and follows best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Decentralized Asset Management System
 * @dev Implements a system to manage and transfer assets on the Ethereum blockchain.
 */
contract AssetManagement {
    // Owner of the contract (admin)
    address public owner;

    // Struct for asset data
    struct Asset {
        string name;
        string assetType;
        uint256 value;
        address owner;
    }

    // Mapping to store assets by their unique ID
    mapping(uint256 => Asset) private assets;

    // Counter for unique asset IDs
    uint256 private assetCounter;

    // Event emitted when a new asset is created
    event AssetCreated(
        uint256 indexed assetId,
        string name,
        string assetType,
        uint256 value,
        address indexed owner
    );

    // Event emitted when asset ownership is transferred
    event OwnershipTransferred(
        uint256 indexed assetId,
        address indexed previousOwner,
        address indexed newOwner
    );

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can call this function");
        _;
    }

    // Modifier to restrict access to asset owner
    modifier onlyAssetOwner(uint256 assetId) {
        require(msg.sender == assets[assetId].owner, "Only asset owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Assign the contract deployer as the owner
    }

    /**
     * @dev Create a new asset and assign ownership to the caller.
     * @param name Name of the asset.
     * @param assetType Type/category of the asset.
     * @param value Monetary value of the asset.
     */
    function createAsset(string memory name, string memory assetType, uint256 value) external {
        require(value > 0, "Asset value must be greater than zero");

        assetCounter++; // Increment the asset counter
        assets[assetCounter] = Asset(name, assetType, value, msg.sender);

        emit AssetCreated(assetCounter, name, assetType, value, msg.sender);
    }

    /**
     * @dev Transfer ownership of an asset to a new owner.
     * @param assetId ID of the asset to transfer.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(uint256 assetId, address newOwner) external onlyAssetOwner(assetId) {
        require(newOwner != address(0), "New owner address must be valid");

        address previousOwner = assets[assetId].owner;
        assets[assetId].owner = newOwner;

        emit OwnershipTransferred(assetId, previousOwner, newOwner);
    }

    /**
     * @dev Get details of an asset by its ID.
     * @param assetId ID of the asset to retrieve.
     * @return name Name of the asset.
     * @return assetType Type/category of the asset.
     * @return value Monetary value of the asset.
     * @return owner Owner of the asset.
     */
    function getAsset(uint256 assetId) external view returns (string memory, string memory, uint256, address) {
        Asset memory asset = assets[assetId];
        return (asset.name, asset.assetType, asset.value, asset.owner);
    }

    /**
     * @dev Destroy the contract and transfer any remaining ether to the owner.
     * Only callable by the contract owner.
     */
    function terminateContract() external onlyOwner {
        selfdestruct(payable(owner));
    }
}
```

### Deployment Notes:
- Use an Ethereum development framework like Hardhat or Truffle to deploy this smart contract.
- Ensure proper testing and security audits before deploying to production.
- Gas optimization should be considered for large-scale applications.
