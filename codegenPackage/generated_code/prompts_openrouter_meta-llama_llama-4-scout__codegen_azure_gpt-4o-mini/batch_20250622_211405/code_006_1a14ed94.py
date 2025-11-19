"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Create a smart contract using Solidity to manage data sharing, monetization, and incentivization for data owners and contributors on the PrivateAI platform.
Generated: DETERMINISTIC_1a14ed94ed1eb5c5
Batch ID: 20250622_211405
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

/// @title PrivateAI Data Sharing Smart Contract
/// @author Your Name
/// @notice This contract manages data sharing, monetization, and incentivization for data owners and contributors.
contract PrivateAI {
    // Struct to represent a data asset
    struct DataAsset {
        address owner; // Owner of the data
        string metadata; // Metadata about the data
        uint256 price; // Price for accessing the data
        bool isAvailable; // Availability status of the data
    }

    // Mapping to store data assets by their ID
    mapping(uint256 => DataAsset) public dataAssets;
    // Counter for data asset IDs
    uint256 public dataAssetCount;

    // Event emitted when a new data asset is created
    event DataAssetCreated(uint256 indexed assetId, address indexed owner, string metadata, uint256 price);
    // Event emitted when a data asset is purchased
    event DataAssetPurchased(uint256 indexed assetId, address indexed buyer);

    /// @notice Create a new data asset
    /// @param _metadata Metadata for the data asset
    /// @param _price Price for accessing the data asset
    function createDataAsset(string memory _metadata, uint256 _price) external {
        require(bytes(_metadata).length > 0, "Metadata cannot be empty");
        require(_price > 0, "Price must be greater than zero");

        dataAssetCount++;
        dataAssets[dataAssetCount] = DataAsset(msg.sender, _metadata, _price, true);

        emit DataAssetCreated(dataAssetCount, msg.sender, _metadata, _price);
    }

    /// @notice Purchase a data asset
    /// @param _assetId ID of the data asset to purchase
    function purchaseDataAsset(uint256 _assetId) external payable {
        DataAsset storage asset = dataAssets[_assetId];

        require(asset.isAvailable, "Data asset is not available");
        require(msg.value >= asset.price, "Insufficient payment");

        // Transfer payment to the owner
        payable(asset.owner).transfer(asset.price);

        // If the payment is more than the price, refund the excess
        if (msg.value > asset.price) {
            payable(msg.sender).transfer(msg.value - asset.price);
        }

        // Mark the asset as unavailable after purchase
        asset.isAvailable = false;

        emit DataAssetPurchased(_assetId, msg.sender);
    }

    /// @notice Get details of a data asset
    /// @param _assetId ID of the data asset
    /// @return owner Owner of the data asset
    /// @return metadata Metadata of the data asset
    /// @return price Price of the data asset
    /// @return isAvailable Availability status of the data asset
    function getDataAsset(uint256 _assetId) external view returns (address owner, string memory metadata, uint256 price, bool isAvailable) {
        DataAsset storage asset = dataAssets[_assetId];
        return (asset.owner, asset.metadata, asset.price, asset.isAvailable);
    }

    /// @notice Allow the owner to update the price of their data asset
    /// @param _assetId ID of the data asset
    /// @param _newPrice New price for the data asset
    function updateDataAssetPrice(uint256 _assetId, uint256 _newPrice) external {
        DataAsset storage asset = dataAssets[_assetId];

        require(msg.sender == asset.owner, "Only the owner can update the price");
        require(_newPrice > 0, "Price must be greater than zero");

        asset.price = _newPrice;
    }

    /// @notice Allow the owner to mark their data asset as available or unavailable
    /// @param _assetId ID of the data asset
    /// @param _isAvailable New availability status
    function setDataAssetAvailability(uint256 _assetId, bool _isAvailable) external {
        DataAsset storage asset = dataAssets[_assetId];

        require(msg.sender == asset.owner, "Only the owner can change availability");
        
        asset.isAvailable = _isAvailable;
    }
}
```
