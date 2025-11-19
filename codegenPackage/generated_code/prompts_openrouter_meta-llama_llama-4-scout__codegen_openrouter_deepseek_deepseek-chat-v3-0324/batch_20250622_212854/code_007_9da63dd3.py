"""
Generated Code Metadata:
========================
Original URL: https://www.unisocks.fi
Prompt: Implement a simple smart contract in Rust for managing the buying, selling, and redeeming of digital assets like Unisocks.
Generated: DETERMINISTIC_9da63dd3f0ebd244
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title DigitalAssetManager
/// @notice A smart contract for managing digital assets like Unisocks
contract DigitalAssetManager {
    // Struct to represent a digital asset
    struct Asset {
        uint256 id;
        string name;
        uint256 price;
        address owner;
        bool isRedeemed;
    }

    // Mapping from asset ID to Asset
    mapping(uint256 => Asset) public assets;
    
    // Counter for asset IDs
    uint256 private nextAssetId = 1;
    
    // Event emitted when an asset is bought
    event AssetBought(uint256 indexed assetId, address indexed buyer, uint256 price);
    
    // Event emitted when an asset is sold
    event AssetSold(uint256 indexed assetId, address indexed seller, uint256 price);
    
    // Event emitted when an asset is redeemed
    event AssetRedeemed(uint256 indexed assetId, address indexed owner);

    /// @notice Creates a new digital asset
    /// @param _name Name of the asset
    /// @param _price Initial price of the asset
    function createAsset(string memory _name, uint256 _price) external {
        uint256 assetId = nextAssetId++;
        assets[assetId] = Asset({
            id: assetId,
            name: _name,
            price: _price,
            owner: msg.sender,
            isRedeemed: false
        });
    }

    /// @notice Buys an existing digital asset
    /// @param _assetId ID of the asset to buy
    function buyAsset(uint256 _assetId) external payable {
        Asset storage asset = assets[_assetId];
        require(asset.id != 0, "Asset does not exist");
        require(msg.value >= asset.price, "Insufficient funds");
        require(asset.owner != msg.sender, "Cannot buy your own asset");
        require(!asset.isRedeemed, "Asset already redeemed");

        address previousOwner = asset.owner;
        asset.owner = msg.sender;
        asset.price = msg.value;

        payable(previousOwner).transfer(msg.value);
        
        emit AssetBought(_assetId, msg.sender, msg.value);
    }

    /// @notice Sells a digital asset you own
    /// @param _assetId ID of the asset to sell
    /// @param _price New price for the asset
    function sellAsset(uint256 _assetId, uint256 _price) external {
        Asset storage asset = assets[_assetId];
        require(asset.id != 0, "Asset does not exist");
        require(asset.owner == msg.sender, "Not the owner");
        require(!asset.isRedeemed, "Asset already redeemed");
        require(_price > 0, "Price must be greater than zero");

        asset.price = _price;
        
        emit AssetSold(_assetId, msg.sender, _price);
    }

    /// @notice Redeems a digital asset you own
    /// @param _assetId ID of the asset to redeem
    function redeemAsset(uint256 _assetId) external {
        Asset storage asset = assets[_assetId];
        require(asset.id != 0, "Asset does not exist");
        require(asset.owner == msg.sender, "Not the owner");
        require(!asset.isRedeemed, "Asset already redeemed");

        asset.isRedeemed = true;
        
        emit AssetRedeemed(_assetId, msg.sender);
    }

    /// @notice Gets details of an asset
    /// @param _assetId ID of the asset to query
    /// @return Asset details
    function getAsset(uint256 _assetId) external view returns (Asset memory) {
        require(assets[_assetId].id != 0, "Asset does not exist");
        return assets[_assetId];
    }
}
```
