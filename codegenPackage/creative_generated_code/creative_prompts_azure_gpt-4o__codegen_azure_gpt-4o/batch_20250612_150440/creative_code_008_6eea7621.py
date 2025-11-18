"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-svd.vercel.app
Prompt: Provide an example of a function in Solidity to calculate staking rewards for "FREE SHAVACADOO" tokens based on the duration of staking.
Generated: DETERMINISTIC_6eea7621131b2993
Batch ID: 20250612_150440
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

/// @title Staking Rewards Contract for FREE SHAVACADOO Tokens
/// @author Example
/// @notice This contract provides a function to calculate staking rewards based on duration
/// @dev Rewards are calculated at a fixed annual percentage yield (APY)

contract StakingRewards {
    // State variables
    uint256 public annualRate; // Annual Percentage Yield (APY) in basis points (e.g., 500 = 5%)
    uint256 constant BASIS_POINTS_DIVISOR = 10000; // Basis points divisor to calculate rates

    /// @notice Constructor to initialize the annual rate
    /// @param _annualRate APY in basis points (e.g., 500 means 5%)
    constructor(uint256 _annualRate) {
        require(_annualRate > 0, "Annual rate must be greater than zero");
        require(_annualRate <= BASIS_POINTS_DIVISOR, "Annual rate must not exceed 100%");
        annualRate = _annualRate;
    }

    /// @notice Calculates staking rewards for a given amount and duration
    /// @param stakedAmount The amount of tokens staked
    /// @param stakingDuration The duration of staking in seconds
    /// @return rewards The calculated staking rewards
    function calculateRewards(uint256 stakedAmount, uint256 stakingDuration) public view returns (uint256 rewards) {
        require(stakedAmount > 0, "Staked amount must be greater than zero");
        require(stakingDuration > 0, "Staking duration must be greater than zero");

        // Calculate rewards based on the formula:
        // Rewards = (stakedAmount * annualRate * stakingDuration) / (BASIS_POINTS_DIVISOR * 365 days)
        rewards = (stakedAmount * annualRate * stakingDuration) / (BASIS_POINTS_DIVISOR * 365 days);

        return rewards;
    }
}
```
