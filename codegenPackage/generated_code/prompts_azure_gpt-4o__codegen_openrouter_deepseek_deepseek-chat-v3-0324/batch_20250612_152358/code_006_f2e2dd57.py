"""
Generated Code Metadata:
========================
Original URL: https://mewnbase.pages.dev
Prompt: Write a function in Solidity to calculate ETH reflections based on trading volume and bag size, as described in the Mewnbase tokenomics.
Generated: DETERMINISTIC_f2e2dd576add4813
Batch ID: 20250612_152358
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
 * @title ETH Reflections Calculator
 * @dev Calculates ETH reflections based on trading volume and bag size
 */
contract ETHReflectionsCalculator {
    // Reflection parameters
    uint256 public constant REFLECTION_PERCENTAGE = 5; // 5% of trading volume
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1B tokens
    
    /**
     * @dev Calculates ETH reflections for a holder
     * @param tradingVolume Total ETH trading volume
     * @param holderBalance Holder's token balance
     * @return reflectionAmount ETH reflection amount for the holder
     */
    function calculateReflections(
        uint256 tradingVolume,
        uint256 holderBalance
    ) external pure returns (uint256 reflectionAmount) {
        require(tradingVolume > 0, "Trading volume must be positive");
        require(holderBalance > 0, "Holder balance must be positive");
        require(holderBalance <= TOTAL_SUPPLY, "Holder balance exceeds total supply");
        
        // Calculate total reflections pool (5% of trading volume)
        uint256 totalReflections = (tradingVolume * REFLECTION_PERCENTAGE) / 100;
        
        // Calculate holder's share based on their bag size
        reflectionAmount = (totalReflections * holderBalance) / TOTAL_SUPPLY;
        
        return reflectionAmount;
    }
}
```
