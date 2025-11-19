"""
Generated Code Metadata:
========================
Original URL: https://unisocks.fi
Prompt: Design a basic smart contract for managing the sale, purchase, and redemption of digital assets for physical goods, inspired by the Unisocks platform.
Generated: DETERMINISTIC_7983bdfd9b45d931
Batch ID: 20250622_212605
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for managing the sale, purchase, and redemption of digital assets for physical goods
contract DigitalAssetMarketplace is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a digital asset
    struct DigitalAsset {
        uint256 id;
        string name;
        uint256 price; // Price in wei
        address owner;
        bool isRedeemed;
    }

    // Mapping to store digital assets by their ID
    mapping(uint256 => DigitalAsset) public digitalAssets;
    Counters.Counter private assetIdCounter;

    // Event emitted when a new digital asset is created
    event DigitalAssetCreated(uint256 indexed id, string name, uint256 price, address indexed owner);
    
    // Event emitted when a digital asset is purchased
    event DigitalAssetPurchased(uint256 indexed id, address indexed buyer);
    
    // Event emitted when a digital asset is redeemed
    event DigitalAssetRedeemed(uint256 indexed id, address indexed owner);

    // Function to create a new digital asset
    function createDigitalAsset(string memory _name, uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than zero");

        assetIdCounter.increment();
        uint256 newAssetId = assetIdCounter.current();

        digitalAssets[newAssetId] = DigitalAsset({
            id: newAssetId,
            name: _name,
            price: _price,
            owner: msg.sender,
            isRedeemed: false
        });

        emit DigitalAssetCreated(newAssetId, _name, _price, msg.sender);
    }

    // Function to purchase a digital asset
    function purchaseDigitalAsset(uint256 _assetId) external payable {
        DigitalAsset storage asset = digitalAssets[_assetId];

        require(asset.id != 0, "Digital asset does not exist");
        require(msg.value == asset.price, "Incorrect payment amount");
        require(asset.owner != msg.sender, "Owner cannot purchase their own asset");
        require(!asset.isRedeemed, "Asset has already been redeemed");

        // Transfer ownership of the asset
        asset.owner = msg.sender;

        emit DigitalAssetPurchased(_assetId, msg.sender);
    }

    // Function to redeem a digital asset for physical goods
    function redeemDigitalAsset(uint256 _assetId) external {
        DigitalAsset storage asset = digitalAssets[_assetId];

        require(asset.id != 0, "Digital asset does not exist");
        require(asset.owner == msg.sender, "Only the owner can redeem the asset");
        require(!asset.isRedeemed, "Asset has already been redeemed");

        // Mark the asset as redeemed
        asset.isRedeemed = true;

        emit DigitalAssetRedeemed(_assetId, msg.sender);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner()).transfer(balance);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
