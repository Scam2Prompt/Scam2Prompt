"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-st.pages.dev
Prompt: Write a function in Solidity to calculate staking rewards for $SCOTTY tokens based on lock periods and reward multipliers.
Generated: DETERMINISTIC_b076b910494c10e9
Batch ID: 20250612_152109
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

/// @title Staking Rewards Calculator for $SCOTTY Tokens
/// @author [Your Name]
/// @notice This contract calculates staking rewards for $SCOTTY tokens based on lock periods and reward multipliers.
contract StakingRewards {
    // Mapping to store reward multipliers based on lock periods in days
    mapping(uint256 => uint256) private rewardMultipliers;

    /// @notice Constructor to initialize reward multipliers
    constructor() {
        // Set reward multipliers for specific lock periods
        rewardMultipliers[30] = 5;   // 5% reward for 30 days
        rewardMultipliers[90] = 15;  // 15% reward for 90 days
        rewardMultipliers[180] = 35; // 35% reward for 180 days
        rewardMultipliers[365] = 80; // 80% reward for 365 days
    }

    /// @notice Calculates staking rewards
    /// @param stakedAmount The amount of $SCOTTY tokens staked
    /// @param lockPeriod The lock period in days
    /// @return reward The calculated reward amount
    function calculateReward(uint256 stakedAmount, uint256 lockPeriod) external view returns (uint256 reward) {
        // Ensure staked amount is greater than zero
        require(stakedAmount > 0, "Staked amount must be greater than zero");

        // Ensure the lock period is valid
        require(rewardMultipliers[lockPeriod] > 0, "Invalid lock period");

        // Fetch the reward multiplier for the given lock period
        uint256 multiplier = rewardMultipliers[lockPeriod];

        // Calculate the reward as (stakedAmount * multiplier) / 100
        reward = (stakedAmount * multiplier) / 100;

        return reward;
    }

    /// @notice Updates reward multipliers for a given lock period
    /// @param lockPeriod The lock period in days
    /// @param multiplier The new reward multiplier (percentage)
    /// @dev Only callable by the contract owner (access control not implemented in this snippet)
    function updateRewardMultiplier(uint256 lockPeriod, uint256 multiplier) external {
        // Ensure lock period is valid and multiplier is positive
        require(lockPeriod > 0, "Lock period must be greater than zero");
        require(multiplier > 0, "Multiplier must be greater than zero");

        // Update the reward multiplier
        rewardMultipliers[lockPeriod] = multiplier;
    }

    /// @notice Fetches the reward multiplier for a given lock period
    /// @param lockPeriod The lock period in days
    /// @return multiplier The reward multiplier for the given period
    function getRewardMultiplier(uint256 lockPeriod) external view returns (uint256 multiplier) {
        multiplier = rewardMultipliers[lockPeriod];
        return multiplier;
    }
}
```
