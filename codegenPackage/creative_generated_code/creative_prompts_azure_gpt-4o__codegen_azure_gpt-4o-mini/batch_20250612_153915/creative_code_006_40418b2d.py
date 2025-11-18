"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin.pages.dev
Prompt: Develop a feature in a blockchain application that allows users to purchase multiple NFT boxes at a discount and calculate rewards for each box, referencing the Swapbox reward structure.
Generated: DETERMINISTIC_40418b2d27b18148
Batch ID: 20250612_153915
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTBoxPurchase is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public rewardToken; // ERC20 token used for rewards
    uint256 public boxPrice; // Regular price for a single NFT box
    uint256 public discountRate; // Discount rate in basis points (100 basis points = 1%)
    uint256 public rewardPerBox; // Rewards given for each box purchased

    event BoxesPurchased(address indexed buyer, uint256 quantity, uint256 totalCost, uint256 rewards);
    
    // Constructor to initialize contract parameters
    constructor(IERC20 _rewardToken, uint256 _boxPrice, uint256 _discountRate, uint256 _rewardPerBox) {
        rewardToken = _rewardToken;
        boxPrice = _boxPrice;
        discountRate = _discountRate;
        rewardPerBox = _rewardPerBox;
    }

    // Function to purchase NFT boxes with discount
    function purchaseBoxes(uint256 quantity) external {
        require(quantity > 0, "Quantity must be greater than zero");
        
        // Calculate total cost and rewards
        uint256 totalCost = calculateTotalCost(quantity);
        uint256 rewards = quantity.mul(rewardPerBox);
        
        // Transfer tokens for payment
        require(rewardToken.balanceOf(msg.sender) >= totalCost, "Insufficient balance");
        require(rewardToken.allowance(msg.sender, address(this)) >= totalCost, "Insufficient allowance");

        // Transfer the payment
        rewardToken.transferFrom(msg.sender, address(this), totalCost);
        
        // Emit event for purchase
        emit BoxesPurchased(msg.sender, quantity, totalCost, rewards);
    }

    // Function to calculate the total cost considering discount
    function calculateTotalCost(uint256 quantity) public view returns (uint256) {
        uint256 totalPrice = boxPrice.mul(quantity);
        uint256 discount = totalPrice.mul(discountRate).div(10000); // Convert basis points to percentage
        return totalPrice.sub(discount);
    }

    // Function for the owner to withdraw the funds collected from sales
    function withdrawFunds() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        rewardToken.transfer(msg.sender, balance);
    }

    // Function to update the box price by the contract owner
    function updateBoxPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "New price must be greater than zero");
        boxPrice = newPrice;
    }

    // Function to update the discount rate by the contract owner
    function updateDiscountRate(uint256 newDiscountRate) external onlyOwner {
        require(newDiscountRate <= 10000, "Discount rate must be less than or equal to 10000 basis points");
        discountRate = newDiscountRate;
    }

    // Function to update the reward per box
    function updateRewardPerBox(uint256 newReward) external onlyOwner {
        require(newReward > 0, "Reward must be greater than zero");
        rewardPerBox = newReward;
    }
}
```
