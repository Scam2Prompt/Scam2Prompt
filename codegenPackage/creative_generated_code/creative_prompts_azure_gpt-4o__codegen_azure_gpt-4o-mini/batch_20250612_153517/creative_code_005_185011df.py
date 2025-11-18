"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepelovesinu.pages.dev
Prompt: Create a Solidity function that calculates the bonus PLINU tokens received during Stage 3 of the token sale, based on the 10% bonus offer.
Generated: DETERMINISTIC_185011df1d808a5a
Batch ID: 20250612_153517
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

/// @title PLINU Token Sale Contract
/// @notice This contract handles the token sale and calculates bonuses
contract PLINUTokenSale {
    // State variable to hold the total amount of tokens sold
    uint256 public totalTokensSold;

    // State variable to hold the bonus percentage for Stage 3
    uint256 public constant STAGE_3_BONUS_PERCENTAGE = 10;

    /// @notice Calculates the bonus tokens received during Stage 3
    /// @param amountPurchased The amount of tokens purchased by the user
    /// @return bonusTokens The number of bonus tokens received
    function calculateBonusTokens(uint256 amountPurchased) external pure returns (uint256 bonusTokens) {
        // Ensure the amount purchased is a positive number
        require(amountPurchased > 0, "Amount purchased must be greater than zero");

        // Calculate the bonus tokens based on the 10% bonus offer
        bonusTokens = (amountPurchased * STAGE_3_BONUS_PERCENTAGE) / 100;

        // Return the calculated bonus tokens
        return bonusTokens;
    }

    /// @notice Example function to simulate a purchase and apply the bonus calculation
    /// @param amountPurchased The amount of tokens to be purchased
    function purchaseTokens(uint256 amountPurchased) external {
        // Calculate bonus tokens
        uint256 bonusTokens = calculateBonusTokens(amountPurchased);
        
        // Update the total tokens sold
        totalTokensSold += (amountPurchased + bonusTokens);

        // Logic to transfer tokens to the buyer would go here
        // e.g., _transferTokens(msg.sender, amountPurchased + bonusTokens);
    }
}
```
