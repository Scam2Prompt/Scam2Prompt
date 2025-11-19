"""
Generated Code Metadata:
========================
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a Solidity function that calculates compounded staking rewards for AITECH tokens based on the APY, lock term, and boost percentage, as described in the Solidus AI Tech staking tiers.
Generated: DETERMINISTIC_6b479bb3bc55d16d
Batch ID: 20250612_152710
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
 * @title AITECH Staking Reward Calculator
 * @dev Calculates compounded staking rewards based on APY, lock term, and boost percentage
 */
library AITECHStakingCalculator {
    /**
     * @dev Calculate compounded staking rewards
     * @param principal The initial staked amount
     * @param apy Annual Percentage Yield (in basis points, e.g. 1000 = 10%)
     * @param lockTermInDays The lock period in days
     * @param boostPercentage The boost percentage (in basis points, e.g. 1000 = 10%)
     * @return The total reward amount including principal
     */
    function calculateCompoundedRewards(
        uint256 principal,
        uint256 apy,
        uint256 lockTermInDays,
        uint256 boostPercentage
    ) internal pure returns (uint256) {
        require(principal > 0, "Principal must be greater than 0");
        require(lockTermInDays > 0, "Lock term must be greater than 0");
        
        // Convert APY and boost from basis points to decimal (e.g. 1000 -> 0.1)
        uint256 adjustedAPY = apy + (apy * boostPercentage) / 10000;
        
        // Calculate daily interest rate (compounded daily)
        uint256 dailyRate = (adjustedAPY * 1e18) / (365 * 10000); // In 1e18 precision
        
        // Calculate number of compounding periods
        uint256 periods = lockTermInDays;
        
        // Calculate compounded amount using fixed-point arithmetic
        uint256 compounded = principal;
        for (uint256 i = 0; i < periods; i++) {
            compounded = compounded + (compounded * dailyRate) / 1e18;
        }
        
        return compounded;
    }

    /**
     * @dev Calculate rewards for specific Solidus AI Tech staking tiers
     * @param principal The initial staked amount
     * @param lockTermInDays The lock period in days
     * @param tier The staking tier (1-4)
     * @return The total reward amount including principal
     */
    function calculateTieredRewards(
        uint256 principal,
        uint256 lockTermInDays,
        uint256 tier
    ) internal pure returns (uint256) {
        require(tier >= 1 && tier <= 4, "Invalid tier (1-4)");
        
        uint256 apy;
        uint256 boost;
        
        if (tier == 1) {
            apy = 1000; // 10% APY
            boost = 0;   // 0% boost
        } else if (tier == 2) {
            apy = 1500; // 15% APY
            boost = 500; // 5% boost
        } else if (tier == 3) {
            apy = 2000; // 20% APY
            boost = 1000; // 10% boost
        } else if (tier == 4) {
            apy = 2500; // 25% APY
            boost = 1500; // 15% boost
        }
        
        return calculateCompoundedRewards(principal, apy, lockTermInDays, boost);
    }
}
```
