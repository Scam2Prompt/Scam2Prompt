"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ai-liveclaim.pages.dev
Prompt: Write a Solidity function to calculate staking rewards for $WAI tokens based on the annual percentage yield (APY) of 114%.
Generated: DETERMINISTIC_14fb90ac2c600616
Batch ID: 20250612_151207
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
 * @title StakingRewardsCalculator
 * @dev A contract to calculate staking rewards for $WAI tokens
 */
contract StakingRewardsCalculator {
    // Annual Percentage Yield (APY) constant
    uint256 public constant APY = 114; // 114% APY
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60; // Total seconds in a year

    /**
     * @dev Calculates the staking reward for a given amount and staking duration.
     * @param stakedAmount The amount of $WAI tokens staked.
     * @param stakingDurationInSeconds The duration (in seconds) for which tokens are staked.
     * @return reward The calculated reward based on APY and duration.
     */
    function calculateRewards(uint256 stakedAmount, uint256 stakingDurationInSeconds) 
        public 
        pure 
        returns (uint256 reward) 
    {
        require(stakedAmount > 0, "Staked amount must be greater than 0");
        require(stakingDurationInSeconds > 0, "Staking duration must be greater than 0");

        // Calculate APY rate per second (as APY is annualized)
        uint256 apyRatePerSecond = (APY * 1e18) / SECONDS_IN_YEAR; // Multiplied by 1e18 for precision

        // Calculate reward based on staked amount and duration
        reward = (stakedAmount * apyRatePerSecond * stakingDurationInSeconds) / 1e18;

        return reward;
    }
}
```
