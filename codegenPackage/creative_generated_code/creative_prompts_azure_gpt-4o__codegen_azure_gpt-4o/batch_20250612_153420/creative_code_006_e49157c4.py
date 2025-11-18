"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claim-akz.pages.dev
Prompt: Create a Solidity function for a rewards calculator that takes the amount of $DOGE20 staked and the total staking pool size as inputs and returns the projected rewards over two years.
Generated: DETERMINISTIC_e49157c4d56aebba
Batch ID: 20250612_153420
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
 * @title RewardsCalculator
 * @notice Provides functionality to calculate staking rewards for $DOGE20 token.
 */
contract RewardsCalculator {
    // Annual reward rate (percentage) expressed as a fraction (e.g., 0.10 for 10%)
    uint256 public constant ANNUAL_REWARD_RATE = 10; // Example: 10% annual reward rate
    uint256 public constant REWARD_PERIOD_YEARS = 2; // Number of years for reward calculation

    /**
     * @notice Calculate projected rewards for a staker over two years.
     * @param stakedAmount The amount of $DOGE20 tokens staked by the user.
     * @param totalPoolSize The total size of the staking pool.
     * @return projectedRewards The amount of rewards the user is projected to earn.
     */
    function calculateRewards(uint256 stakedAmount, uint256 totalPoolSize)
        external
        pure
        returns (uint256 projectedRewards)
    {
        // Input validation
        require(stakedAmount > 0, "Staked amount must be greater than zero.");
        require(totalPoolSize > 0, "Total pool size must be greater than zero.");
        require(stakedAmount <= totalPoolSize, "Staked amount cannot exceed total pool size.");

        // Calculate user's share in the staking pool as a fraction
        uint256 userShare = (stakedAmount * 1e18) / totalPoolSize; // Scaled to avoid precision loss

        // Calculate annual rewards for the entire pool
        uint256 annualPoolRewards = (totalPoolSize * ANNUAL_REWARD_RATE) / 100;

        // Calculate user's annual rewards based on their share
        uint256 userAnnualRewards = (annualPoolRewards * userShare) / 1e18;

        // Calculate projected rewards over the specified number of years
        projectedRewards = userAnnualRewards * REWARD_PERIOD_YEARS;

        return projectedRewards;
    }
}
```
