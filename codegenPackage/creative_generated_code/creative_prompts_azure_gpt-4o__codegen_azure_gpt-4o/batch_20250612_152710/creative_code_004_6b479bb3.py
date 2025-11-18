"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a Solidity function that calculates compounded staking rewards for AITECH tokens based on the APY, lock term, and boost percentage, as described in the Solidus AI Tech staking tiers.
Generated: DETERMINISTIC_6b479bb3bc55d16d
Batch ID: 20250612_152710
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
 * @title AITECH Staking Rewards Calculator
 * @notice This contract calculates compounded staking rewards for AITECH tokens based on APY,
 *         lock term, and boost percentage in Solidus AI Tech staking tiers.
 */
contract StakingRewardsCalculator {
    /**
     * @notice Calculates compounded staking rewards for AITECH tokens.
     * @param principal The initial amount of tokens staked (in wei).
     * @param apy The annual percentage yield (APY) in basis points (e.g., 5000 for 50% APY).
     * @param lockTerm The lock period in days.
     * @param boostPercentage The boost percentage in basis points (e.g., 2000 for 20% boost).
     * @return totalRewards Total rewards after the lock term including compounded growth.
     */
    function calculateRewards(
        uint256 principal,
        uint256 apy,
        uint256 lockTerm,
        uint256 boostPercentage
    ) external pure returns (uint256 totalRewards) {
        require(principal > 0, "Principal must be greater than zero");
        require(apy > 0, "APY must be greater than zero");
        require(lockTerm > 0, "Lock term must be greater than zero");

        // Convert lock term from days to years (365 days in a year)
        uint256 lockTermInYears = lockTerm * 1e18 / 365;

        // Annual interest rate including boost, converted to a percentage
        uint256 boostedRate = apy + boostPercentage;
        uint256 annualRate = boostedRate * 1e16 / 10000; // Convert basis points to decimal representation

        // Compound rewards calculation using formula: A = P * (1 + r)^t
        // In Solidity, we approximate (1 + r)^t using fixed-point arithmetic
        uint256 ratePerYear = 1e18 + annualRate; // 1 + annual rate
        uint256 compoundedRate = exp(ratePerYear, lockTermInYears);

        // Calculate total rewards
        totalRewards = (principal * compoundedRate) / 1e18;

        return totalRewards;
    }

    /**
     * @notice Helper function to calculate exponentiation (a ^ b) using fixed-point arithmetic.
     * @param base Base value in fixed-point (scaled by 1e18).
     * @param exponent Exponent value in fixed-point (scaled by 1e18).
     * @return result Result of exponentiation in fixed-point (scaled by 1e18).
     */
    function exp(uint256 base, uint256 exponent) internal pure returns (uint256 result) {
        result = 1e18; // Start with 1 in fixed-point
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = (result * base) / 1e18; // Apply scaling
            }
            base = (base * base) / 1e18; // Square the base and apply scaling
            exponent /= 2; // Halve the exponent
        }
    }
}
```
