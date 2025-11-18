"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scottytheai.web.app
Prompt: Write a Solidity function for calculating staking rewards based on lock duration and multipliers, as described in Scotty AI's staking system.
Generated: DETERMINISTIC_d06ca9395efa7fa7
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

/// @title Staking Rewards Calculator
/// @dev Calculates staking rewards based on lock duration and multiplier factors.

contract StakingRewards {
    // Struct to define staking tier multipliers
    struct StakingTier {
        uint256 lockDuration; // Lock duration in seconds
        uint256 multiplier;   // Multiplier in percentage (e.g., 120 for 1.2x)
    }

    // Array to hold predefined staking tiers
    StakingTier[] public stakingTiers;

    /// @notice Constructor to initialize staking tiers
    /// @param durations Array of lock durations in seconds
    /// @param multipliers Array of multipliers corresponding to lock durations
    constructor(uint256[] memory durations, uint256[] memory multipliers) {
        require(durations.length == multipliers.length, "Durations and multipliers must match in length");

        for (uint256 i = 0; i < durations.length; i++) {
            stakingTiers.push(StakingTier(durations[i], multipliers[i]));
        }
    }

    /// @notice Calculates staking rewards
    /// @param principal The principal amount staked by the user
    /// @param lockDuration The lock duration chosen by the user in seconds
    /// @return rewards The calculated rewards for the given principal and lock duration
    function calculateRewards(uint256 principal, uint256 lockDuration) external view returns (uint256 rewards) {
        require(principal > 0, "Principal amount must be greater than zero");
        require(lockDuration > 0, "Lock duration must be greater than zero");

        // Find the appropriate multiplier for the given lock duration
        uint256 applicableMultiplier = 100; // Default multiplier is 1x (100%)
        for (uint256 i = 0; i < stakingTiers.length; i++) {
            if (lockDuration >= stakingTiers[i].lockDuration) {
                applicableMultiplier = stakingTiers[i].multiplier;
            }
        }

        // Calculate rewards
        rewards = (principal * applicableMultiplier) / 100;

        return rewards;
    }

    /// @notice Retrieves the staking tiers
    /// @return tiers Array of staking tiers with lock durations and multipliers
    function getStakingTiers() external view returns (StakingTier[] memory tiers) {
        return stakingTiers;
    }
}
```
