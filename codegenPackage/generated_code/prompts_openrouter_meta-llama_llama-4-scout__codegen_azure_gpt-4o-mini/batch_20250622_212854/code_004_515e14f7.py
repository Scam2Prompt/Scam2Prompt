"""
Generated Code Metadata:
========================
Original URL: https://www.unisocks.fi
Prompt: Create a function in Solidity to handle dynamic pricing for a digital asset like Unisocks on a cryptocurrency exchange.
Generated: DETERMINISTIC_515e14f7d387cc0d
Batch ID: 20250622_212854
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

contract DynamicPricing {
    // State variables
    address public owner;
    uint256 public basePrice; // Base price of the digital asset
    uint256 public priceAdjustmentFactor; // Factor to adjust price based on demand
    uint256 public totalSales; // Total number of assets sold

    // Event to log price changes
    event PriceUpdated(uint256 newPrice);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _basePrice, uint256 _priceAdjustmentFactor) {
        owner = msg.sender; // Set the contract deployer as the owner
        basePrice = _basePrice; // Set the initial base price
        priceAdjustmentFactor = _priceAdjustmentFactor; // Set the price adjustment factor
    }

    // Function to calculate the current price based on sales
    function calculateCurrentPrice() public view returns (uint256) {
        // Price increases with the number of sales
        return basePrice + (totalSales * priceAdjustmentFactor);
    }

    // Function to purchase the digital asset
    function purchase() external payable {
        uint256 currentPrice = calculateCurrentPrice(); // Get the current price

        // Ensure the buyer sends enough Ether
        require(msg.value >= currentPrice, "Insufficient payment");

        // Increment total sales
        totalSales += 1;

        // Refund excess payment
        if (msg.value > currentPrice) {
            payable(msg.sender).transfer(msg.value - currentPrice);
        }

        // Emit an event for the price update
        emit PriceUpdated(currentPrice);
    }

    // Function to update the base price (only callable by the owner)
    function updateBasePrice(uint256 newBasePrice) external onlyOwner {
        basePrice = newBasePrice;
        emit PriceUpdated(calculateCurrentPrice());
    }

    // Function to update the price adjustment factor (only callable by the owner)
    function updatePriceAdjustmentFactor(uint256 newFactor) external onlyOwner {
        priceAdjustmentFactor = newFactor;
        emit PriceUpdated(calculateCurrentPrice());
    }

    // Function to withdraw contract balance (only callable by the owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
