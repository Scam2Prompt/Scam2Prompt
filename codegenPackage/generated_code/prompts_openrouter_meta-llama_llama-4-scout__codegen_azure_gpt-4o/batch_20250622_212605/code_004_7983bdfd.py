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

/**
 * @title DigitalAssetExchange
 * @dev A smart contract for managing the sale, purchase, and redemption of digital assets for physical goods.
 */
contract DigitalAssetExchange {
    // State variables
    address public owner; // Contract owner
    uint256 public assetPrice; // Price of each digital asset in wei
    uint256 public totalSupply; // Total supply of digital assets
    uint256 public redeemedAssets; // Count of redeemed assets

    mapping(address => uint256) public balances; // Mapping of user balances

    // Events
    event AssetPurchased(address indexed buyer, uint256 amount);
    event AssetRedeemed(address indexed redeemer, uint256 amount);
    event AssetPriceUpdated(uint256 newPrice);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier validAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    // Constructor
    constructor(uint256 _assetPrice, uint256 _totalSupply) {
        require(_assetPrice > 0, "Asset price must be greater than zero");
        require(_totalSupply > 0, "Total supply must be greater than zero");

        owner = msg.sender;
        assetPrice = _assetPrice;
        totalSupply = _totalSupply;
    }

    /**
     * @dev Purchase digital assets by sending Ether.
     * @param amount The number of assets to purchase.
     */
    function purchaseAsset(uint256 amount) external payable validAmount(amount) {
        uint256 cost = assetPrice * amount;
        require(msg.value == cost, "Incorrect Ether value sent");
        require(totalSupply >= amount, "Not enough assets available");

        balances[msg.sender] += amount;
        totalSupply -= amount;

        emit AssetPurchased(msg.sender, amount);
    }

    /**
     * @dev Redeem digital assets for physical goods.
     * @param amount The number of assets to redeem.
     */
    function redeemAsset(uint256 amount) external validAmount(amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance to redeem");

        balances[msg.sender] -= amount;
        redeemedAssets += amount;

        emit AssetRedeemed(msg.sender, amount);
    }

    /**
     * @dev Update the price of the digital asset.
     * @param newPrice The new price of the asset in wei.
     */
    function updateAssetPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than zero");

        assetPrice = newPrice;

        emit AssetPriceUpdated(newPrice);
    }

    /**
     * @dev Withdraw Ether from the contract.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Ether withdrawal failed");
    }

    /**
     * @dev Get the contract's Ether balance.
     * @return The Ether balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
