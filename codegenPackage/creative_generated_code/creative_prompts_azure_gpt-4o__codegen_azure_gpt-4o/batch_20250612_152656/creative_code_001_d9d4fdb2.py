"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testai-qhn.pages.dev
Prompt: Create a function in Solidity that calculates compounding rewards for staked AITECH tokens based on lock term durations (e.g., 90, 180, or 365 days) and tier boosts.
Generated: DETERMINISTIC_d9d4fdb29304ecf2
Batch ID: 20250612_152656
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
 * @title StakingRewards
 * @dev Contract to calculate compounding rewards for staked AITECH tokens based on lock durations and tier boosts.
 */
contract StakingRewards {

    // Struct to represent staking details
    struct Stake {
        uint256 amount; // Amount of staked tokens
        uint256 startTime; // Timestamp when staking started
        uint256 lockDuration; // Lock term duration in days (e.g., 90, 180, 365)
        uint256 tierBoost; // Boost percentage based on user tier (e.g., 10 for 10%)
    }

    // Constant for annual reward rate (percentage)
    uint256 constant annualRewardRate = 15; // 15% annual reward rate

    /**
     * @notice Calculates the compounding rewards for staked tokens.
     * @param stake The Stake struct containing staking details.
     * @return totalRewards The total compounded rewards for the stake.
     */
    function calculateRewards(Stake memory stake) public pure returns (uint256 totalRewards) {
        // Validate input
        require(stake.amount > 0, "Stake amount must be greater than zero.");
        require(stake.lockDuration == 90 || stake.lockDuration == 180 || stake.lockDuration == 365, "Invalid lock duration.");
        require(stake.tierBoost >= 0 && stake.tierBoost <= 100, "Tier boost must be between 0 and 100.");

        // Convert annual reward rate to daily rate for compounding
        uint256 dailyRate = annualRewardRate * 1e18 / 365;

        // Include tier boost in calculation
        uint256 boostedRate = dailyRate * (100 + stake.tierBoost) / 100;

        // Calculate total compounding periods
        uint256 compoundingPeriods = stake.lockDuration;

        // Initialize total rewards
        uint256 rewards = stake.amount;

        // Compound rewards
        for (uint256 i = 0; i < compoundingPeriods; i++) {
            rewards += rewards * boostedRate / 1e20; // Divided by 1e20 to account for precision
        }

        // Calculate final rewards
        totalRewards = rewards - stake.amount; // Subtract initial stake amount to get pure rewards
    }
}
```
