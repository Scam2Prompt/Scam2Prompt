"""
Generated Code Metadata:
========================
Original URL: https://therealworldcoin.com
Prompt: Create a Solidity smart contract that enables fractional ownership of real-world assets, inspired by the TRW platform's tokenization model.
Generated: DETERMINISTIC_866ca997101b54d6
Batch ID: 20250612_151624
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

// @title FractionalOwnership
// @dev A smart contract for fractional ownership of real-world assets
contract FractionalOwnership is ERC20, Ownable {
    using SafeMath for uint256;

    // Struct to represent an asset
    struct Asset {
        string name;          // Name of the asset
        string description;   // Description of the asset
        uint256 totalShares;  // Total number of shares for the asset
        uint256 sharesIssued; // Number of shares that have been issued
        bool exists;          // Flag to check if asset exists
    }

    // Mapping from asset ID to Asset struct
    mapping(uint256 => Asset) private assets;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 indexed assetId, string name, uint256 totalShares);

    // Event emitted when shares are purchased
    event SharesPurchased(uint256 indexed assetId, address indexed buyer, uint256 amount);

    // Constructor to initialize the ERC20 token
    constructor() ERC20("FractionalOwnershipToken", "FOT") {}

    // @dev Create a new asset with a specified number of shares
    // @param assetId The unique identifier for the asset
    // @param name The name of the asset
    // @param description A description of the asset
    // @param totalShares The total number of shares for the asset
    function createAsset(uint256 assetId, string memory name, string memory description, uint256 totalShares) external onlyOwner {
        require(!assets[assetId].exists, "Asset already exists");
        require(totalShares > 0, "Total shares must be greater than zero");

        assets[assetId] = Asset({
            name: name,
            description: description,
            totalShares: totalShares,
            sharesIssued: 0,
            exists: true
        });

        emit AssetCreated(assetId, name, totalShares);
    }

    // @dev Purchase shares of a specific asset
    // @param assetId The unique identifier for the asset
    // @param amount The number of shares to purchase
    function purchaseShares(uint256 assetId, uint256 amount) external payable {
        Asset storage asset = assets[assetId];
        require(asset.exists, "Asset does not exist");
        require(amount > 0, "Amount must be greater than zero");
        require(asset.sharesIssued.add(amount) <= asset.totalShares, "Not enough shares available");

        // Calculate the price per share (for simplicity, assume 1 ether per share)
        uint256 pricePerShare = 1 ether;
        require(msg.value >= pricePerShare.mul(amount), "Insufficient funds sent");

        // Mint the shares to the buyer
        asset.sharesIssued = asset.sharesIssued.add(amount);
        _mint(msg.sender, amount);

        emit SharesPurchased(assetId, msg.sender, amount);
    }

    // @dev Retrieve asset details
    // @param assetId The unique identifier for the asset
    // @return name The name of the asset
    // @return description The description of the asset
    // @return totalShares The total number of shares for the asset
    // @return sharesIssued The number of shares that have been issued
    function getAssetDetails(uint256 assetId) external view returns (string memory name, string memory description, uint256 totalShares, uint256 sharesIssued) {
        Asset storage asset = assets[assetId];
        require(asset.exists, "Asset does not exist");

        return (asset.name, asset.description, asset.totalShares, asset.sharesIssued);
    }

    // @dev Withdraw funds from the contract (only owner can withdraw)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // @dev Fallback function to accept ether
    receive() external payable {}
}
```
