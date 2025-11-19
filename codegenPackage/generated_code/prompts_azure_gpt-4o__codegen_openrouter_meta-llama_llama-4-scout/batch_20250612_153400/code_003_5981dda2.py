"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20ai.pages.dev
Prompt: Create a function in Solidity that calculates staking rewards for DOGE20 tokens based on a fixed supply and a two-year distribution period.
Generated: DETERMINISTIC_5981dda2bfc25cb9
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title StakingRewardsCalculator
 * @author [Your Name]
 * @notice Calculates staking rewards for DOGE20 tokens.
 */
contract StakingRewardsCalculator {
    // Fixed supply of DOGE20 tokens
    uint256 public constant TOTAL_SUPPLY = 1000000000e18; // 1 billion tokens with 18 decimals

    // Two-year distribution period in seconds
    uint256 public constant DISTRIBUTION_PERIOD = 2 years;

    // Daily reward rate (1% of total supply over 2 years)
    uint256 public constant DAILY_REWARD_RATE = (TOTAL_SUPPLY * 1e16) / (DISTRIBUTION_PERIOD / 1 days);

    /**
     * @notice Calculates staking rewards for a given number of days.
     * @param days Number of days to calculate rewards for.
     * @return rewards The total rewards for the given period.
     */
    function calculateRewards(uint256 days) public pure returns (uint256 rewards) {
        // Check for zero days to avoid unnecessary calculations
        if (days == 0) {
            return 0;
        }

        // Calculate rewards based on daily reward rate
        rewards = days * DAILY_REWARD_RATE;

        // Ensure rewards do not exceed total supply
        if (rewards > TOTAL_SUPPLY) {
            rewards = TOTAL_SUPPLY;
        }
    }

    /**
     * @notice Calculates staking rewards for a given staker based on their stake duration.
     * @param stakeDurationDays Number of days the staker has been staking.
     * @param stakeAmount The amount of DOGE20 tokens staked.
     * @param totalStaked The total amount of DOGE20 tokens staked by all users.
     * @return rewards The total rewards for the given staker.
     */
    function calculateStakerRewards(
        uint256 stakeDurationDays,
        uint256 stakeAmount,
        uint256 totalStaked
    ) public pure returns (uint256 rewards) {
        // Check for zero stake duration or total staked to avoid division by zero
        if (stakeDurationDays == 0 || totalStaked == 0) {
            return 0;
        }

        // Calculate total rewards for the stake duration
        uint256 totalRewards = calculateRewards(stakeDurationDays);

        // Calculate staker's share of rewards based on their stake amount
        rewards = (totalRewards * stakeAmount) / totalStaked;
    }
}
```
