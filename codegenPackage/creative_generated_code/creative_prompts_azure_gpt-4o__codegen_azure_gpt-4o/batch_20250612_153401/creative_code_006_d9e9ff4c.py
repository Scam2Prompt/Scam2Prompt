"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange-ethena.pages.dev
Prompt: Create a function using Solidity to interact with Ethena's staking mechanism and calculate rewards based on the provided APY of 24.04%.
Generated: DETERMINISTIC_d9e9ff4c0dbf243a
Batch ID: 20250612_153401
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
 * @title EthenaStakingRewards
 * @dev A contract to interact with Ethena's staking mechanism and calculate rewards
 * based on the provided APY of 24.04%.
 */
contract EthenaStakingRewards {
    // State variables
    uint256 public apy = 2404; // APY represented as 24.04% (scaled by 100 for precision)
    uint256 constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60; // Seconds in a year

    mapping(address => uint256) public stakedAmounts; // Tracks staked amounts for each user
    mapping(address => uint256) public stakingTimestamps; // Tracks staking start time for each user

    /**
     * @dev Event emitted when a user stakes tokens.
     * @param user The address of the user who staked.
     * @param amount The amount of tokens staked.
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user claims rewards.
     * @param user The address of the user who claimed rewards.
     * @param rewards The calculated rewards amount.
     */
    event RewardsClaimed(address indexed user, uint256 rewards);

    /**
     * @dev Function to stake tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero.");
        
        // Update staked amount and timestamp for the user
        stakedAmounts[msg.sender] += amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to calculate rewards for a user based on APY.
     * @param user The address of the user.
     * @return The calculated rewards based on APY and staking duration.
     */
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = stakedAmounts[user];
        require(stakedAmount > 0, "No staked amount found for this user.");
        
        uint256 stakingDuration = block.timestamp - stakingTimestamps[user];
        require(stakingDuration > 0, "Invalid staking duration.");

        // Formula: rewards = stakedAmount * (APY / 10000) * (stakingDuration / SECONDS_IN_YEAR)
        uint256 rewards = (stakedAmount * apy * stakingDuration) / (10000 * SECONDS_IN_YEAR);
        return rewards;
    }

    /**
     * @dev Function to claim rewards for the user.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim.");

        // Reset staking timestamp to prevent double reward claims
        stakingTimestamps[msg.sender] = block.timestamp;

        emit RewardsClaimed(msg.sender, rewards);

        // Here, the actual transfer of rewards should occur.
        // Example: Transfer rewards tokens to the user
        // Replace this comment with actual token transfer logic if required.
    }

    /**
     * @dev Function to check the staked amount of a user.
     * @param user The address of the user.
     * @return The staked amount.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }

    /**
     * @dev Function to check the staking start time of a user.
     * @param user The address of the user.
     * @return The staking start time.
     */
    function getStakingTimestamp(address user) external view returns (uint256) {
        return stakingTimestamps[user];
    }
}
```
