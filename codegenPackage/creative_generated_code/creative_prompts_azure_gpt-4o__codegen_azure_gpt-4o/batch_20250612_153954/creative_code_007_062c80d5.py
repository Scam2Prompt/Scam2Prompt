"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-buildon.top
Prompt: Write a Solidity function to calculate rewards for BUILD token holders based on their staking duration and contribution to construction projects.
Generated: DETERMINISTIC_062c80d56afa648f
Batch ID: 20250612_153954
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
 * @title BUILD Token Rewards Calculator
 * @dev This contract provides a function to calculate rewards for BUILD token holders 
 * based on their staking duration and contribution to construction projects.
 */
contract BuildTokenRewards {
    // State variables
    uint256 public constant REWARD_BASE_RATE = 100; // Base reward rate (in tokens per second)
    uint256 public constant CONTRIBUTION_MULTIPLIER = 10; // Multiplier for contributions

    // Struct to store information about a staker
    struct Staker {
        uint256 stakedAmount; // Amount of BUILD tokens staked
        uint256 stakingStartTime; // Timestamp when staking started
        uint256 contributionScore; // Contribution score to construction projects
    }

    // Mapping to store staker data
    mapping(address => Staker) public stakers;

    /**
     * @dev Calculate rewards for a given staker.
     * @param stakerAddress The address of the staker.
     * @return rewardAmount The calculated reward amount.
     */
    function calculateRewards(address stakerAddress) external view returns (uint256 rewardAmount) {
        // Retrieve staker data
        Staker memory staker = stakers[stakerAddress];

        // Ensure the staker has staked tokens
        require(staker.stakedAmount > 0, "No staked tokens");

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp - staker.stakingStartTime;

        // Ensure staking duration is valid
        require(stakingDuration > 0, "Invalid staking duration");

        // Calculate base reward from staking duration
        uint256 baseReward = stakingDuration * REWARD_BASE_RATE * staker.stakedAmount;

        // Calculate contribution-based bonus
        uint256 contributionBonus = staker.contributionScore * CONTRIBUTION_MULTIPLIER;

        // Total reward is base reward plus contribution bonus
        rewardAmount = baseReward + contributionBonus;

        return rewardAmount;
    }

    /**
     * @dev Allows a user to stake tokens and set initial contribution score.
     * @param amount The amount of BUILD tokens to stake.
     * @param contributionScore The initial contribution score to construction projects.
     */
    function stakeTokens(uint256 amount, uint256 contributionScore) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(contributionScore >= 0, "Invalid contribution score");

        // Update staker information
        stakers[msg.sender].stakedAmount += amount;
        stakers[msg.sender].stakingStartTime = block.timestamp;
        stakers[msg.sender].contributionScore = contributionScore;
    }
}
```
