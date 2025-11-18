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
 * @title NFTPriceCalculator
 * @dev A contract to calculate the difference between the floor price and estimated value of an NFT.
 */
contract NFTPriceCalculator {
    // Event emitted when the price difference is calculated
    event PriceDifferenceCalculated(address indexed caller, uint256 floorPrice, uint256 estimatedValue, int256 difference);

    /**
     * @dev Calculates the difference between the floor price and the estimated value of an NFT.
     * @param floorPrice The floor price of the NFT in wei.
     * @param estimatedValue The estimated value of the NFT in wei.
     * @return difference The difference as a signed integer (can be positive or negative).
     */
    function calculatePriceDifference(uint256 floorPrice, uint256 estimatedValue) 
        external 
        pure 
        returns (int256 difference) 
    {
        // Ensure inputs are non-negative (implicitly enforced with uint256 type)
        require(floorPrice >= 0, "Floor price must be non-negative.");
        require(estimatedValue >= 0, "Estimated value must be non-negative.");

        // Calculate the difference safely
        difference = int256(estimatedValue) - int256(floorPrice);

        // Emit an event with the calculated data
        emit PriceDifferenceCalculated(msg.sender, floorPrice, estimatedValue, difference);

        return difference; // Return the calculated difference
    }
}
```
