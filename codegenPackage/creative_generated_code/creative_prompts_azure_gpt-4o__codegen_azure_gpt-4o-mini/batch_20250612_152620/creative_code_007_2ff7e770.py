"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-com.pages.dev
Prompt: Develop a function in Solidity that calculates monthly and daily reward rates for $POODL staking, as described on the Poodl Inu platform.
Generated: DETERMINISTIC_2ff7e770781a684e
Batch ID: 20250612_152620
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

/// @title Poodl Inu Staking Reward Calculator
/// @notice This contract calculates monthly and daily reward rates for $POODL staking.
contract PoodlStakingRewardCalculator {
    // Constants for reward calculation
    uint256 private constant SECONDS_IN_A_DAY = 86400; // 24 * 60 * 60
    uint256 private constant SECONDS_IN_A_MONTH = 2592000; // 30 * 24 * 60 * 60

    /// @notice Calculates the daily reward rate based on total staked amount and reward per block.
    /// @param totalStaked Amount of $POODL staked in the contract
    /// @param rewardPerBlock Reward amount given for each block mined
    /// @param blocksPerDay Average number of blocks mined per day
    /// @return dailyRewardRate The calculated daily reward rate
    function calculateDailyRewardRate(
        uint256 totalStaked,
        uint256 rewardPerBlock,
        uint256 blocksPerDay
    ) public pure returns (uint256 dailyRewardRate) {
        // Validate inputs
        require(totalStaked > 0, "Total staked must be greater than zero");
        require(rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(blocksPerDay > 0, "Blocks per day must be greater than zero");

        // Calculate daily reward rate
        dailyRewardRate = (rewardPerBlock * blocksPerDay * 1e18) / totalStaked;
    }

    /// @notice Calculates the monthly reward rate based on total staked amount and reward per block.
    /// @param totalStaked Amount of $POODL staked in the contract
    /// @param rewardPerBlock Reward amount given for each block mined
    /// @param blocksPerMonth Average number of blocks mined per month
    /// @return monthlyRewardRate The calculated monthly reward rate
    function calculateMonthlyRewardRate(
        uint256 totalStaked,
        uint256 rewardPerBlock,
        uint256 blocksPerMonth
    ) public pure returns (uint256 monthlyRewardRate) {
        // Validate inputs
        require(totalStaked > 0, "Total staked must be greater than zero");
        require(rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(blocksPerMonth > 0, "Blocks per month must be greater than zero");

        // Calculate monthly reward rate
        monthlyRewardRate = (rewardPerBlock * blocksPerMonth * 1e18) / totalStaked;
    }
}
```
