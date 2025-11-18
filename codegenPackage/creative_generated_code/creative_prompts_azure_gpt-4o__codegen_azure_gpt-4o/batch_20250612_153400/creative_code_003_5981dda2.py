"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Create a function in Solidity that calculates staking rewards for DOGE20 tokens based on a fixed supply and a two-year distribution period.
Generated: DETERMINISTIC_5981dda2bfc25cb9
Batch ID: 20250612_153400
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
 * @dev This contract calculates staking rewards for DOGE20 tokens based on a fixed supply
 *      and a two-year distribution period.
 */
contract StakingRewardsCalculator {
    // Fixed supply of rewards to distribute over the two-year period
    uint256 public constant TOTAL_REWARD_SUPPLY = 1000000 ether; // 1 million tokens (adjust decimals as needed)
    uint256 public constant DISTRIBUTION_PERIOD = 730 days; // Two years in days

    // Event to log reward calculations
    event RewardCalculated(address indexed staker, uint256 stakedAmount, uint256 stakingDuration, uint256 reward);

    /**
     * @dev Calculates staking rewards based on staked amount and duration.
     * @param stakedAmount The amount of DOGE20 tokens staked by the user (in wei or token smallest unit).
     * @param stakingDuration The duration for which tokens are staked, in seconds.
     * @return reward The calculated staking reward for the given inputs.
     */
    function calculateStakingReward(uint256 stakedAmount, uint256 stakingDuration) 
        external 
        pure 
        returns (uint256 reward) 
    {
        // Validate inputs
        require(stakedAmount > 0, "Staked amount must be greater than zero.");
        require(stakingDuration > 0, "Staking duration must be greater than zero.");
        require(stakingDuration <= DISTRIBUTION_PERIOD, "Staking duration exceeds the distribution period.");

        // Calculate reward using proportional distribution
        reward = (stakedAmount * stakingDuration * TOTAL_REWARD_SUPPLY) / (DISTRIBUTION_PERIOD);

        // Emit reward calculation event
        emit RewardCalculated(msg.sender, stakedAmount, stakingDuration, reward);

        return reward;
    }
}
```
