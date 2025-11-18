"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonhop.pages.dev
Prompt: Write a Solidity function to calculate token price increases across multiple presale stages, inspired by MOONHOP's structured pricing model.
Generated: DETERMINISTIC_e447eb6ac07912b3
Batch ID: 20250612_145616
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

/// @title Token Presale Pricing
/// @dev Calculates token price increases across multiple presale stages
contract TokenPresalePricing {
    // State variable to store the base price of the token in wei
    uint256 public basePrice;

    // Array to store price multipliers for each presale stage (e.g., [100, 110, 120] for 1.0x, 1.1x, 1.2x)
    uint256[] public stageMultipliers;

    // Constructor to initialize the base price and stage multipliers
    /// @param _basePrice The base price of the token in wei
    /// @param _multipliers Array of multipliers for each presale stage (in percentage; e.g., 100 for 1.0x)
    constructor(uint256 _basePrice, uint256[] memory _multipliers) {
        require(_basePrice > 0, "Base price must be greater than zero");
        require(_multipliers.length > 0, "Multipliers array cannot be empty");

        basePrice = _basePrice;
        stageMultipliers = _multipliers;
    }

    // Function to calculate the token price for a specific presale stage
    /// @param stage The presale stage index (0-based)
    /// @return price The token price for the specified stage in wei
    function getTokenPriceForStage(uint256 stage) public view returns (uint256 price) {
        require(stage < stageMultipliers.length, "Stage index out of bounds");
        // Calculate the price using the base price and the multiplier for the given stage
        price = (basePrice * stageMultipliers[stage]) / 100;
    }

    // Function to calculate token prices for all presale stages
    /// @return prices An array containing token prices for each stage in wei
    function getAllTokenPrices() public view returns (uint256[] memory prices) {
        prices = new uint256[](stageMultipliers.length);
        for (uint256 i = 0; i < stageMultipliers.length; i++) {
            prices[i] = getTokenPriceForStage(i);
        }
    }
}
```
