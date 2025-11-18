"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reliablenftmarketplace.com
Prompt: Create a function in Solidity to calculate the difference between the floor price and the estimated value of an NFT, as highlighted by Reliable NFT Marketplace.
Generated: DETERMINISTIC_a1b2dad20a17bd45
Batch ID: 20250612_154820
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

/**
 * @title NFTValueCalculator
 * @dev This contract calculates the difference between the floor price and the estimated value of an NFT.
 */
contract NFTValueCalculator {

    // Event to log the calculated difference
    event DifferenceCalculated(int256 difference);

    /**
     * @dev Calculates the difference between the floor price and the estimated value of an NFT.
     * @param floorPrice The current floor price of the NFT.
     * @param estimatedValue The estimated value of the NFT.
     * @return difference The difference between the estimated value and the floor price.
     */
    function calculateDifference(uint256 floorPrice, uint256 estimatedValue) 
        external 
        pure 
        returns (int256 difference) 
    {
        // Validate input values to ensure they are not negative (uint256 cannot be negative)
        require(floorPrice >= 0, "Floor price should be non-negative");
        require(estimatedValue >= 0, "Estimated value should be non-negative");

        // Calculate the difference
        difference = int256(estimatedValue) - int256(floorPrice);

        // Emit the calculated difference
        emit DifferenceCalculated(difference);
    }
}
```
