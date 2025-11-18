"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge2014sale.pages.dev
Prompt: Write a Solidity function for calculating staking rewards for Doge2014 tokens based on the staking allocation percentage (25%) and the user's staked amount. Include logic for secure reward distribution.
Generated: DETERMINISTIC_7bf14d0c23dd27d6
Batch ID: 20250612_152240
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

contract Doge2014Staking {
    // State variables
    mapping(address => uint256) private stakedAmounts; // Maps user addresses to staked amounts
    mapping(address => uint256) private rewards; // Maps user addresses to accumulated rewards
    uint256 private totalStaked; // Total amount of tokens staked in the contract
    uint256 private rewardPercentage = 25; // Fixed reward percentage (25%)

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Modifier to check if the user has staked tokens
    modifier hasStakedTokens() {
        require(stakedAmounts[msg.sender] > 0, "No staked tokens found");
        _;
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update the staked amount for the user
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        // Any token transfer logic should be implemented here
        // For example: transferTokensFrom(msg.sender, address(this), amount);
    }

    // Function to calculate rewards based on staked amount
    function calculateRewards(address user) internal view returns (uint256) {
        return (stakedAmounts[user] * rewardPercentage) / 100;
    }

    // Function to distribute rewards to the user
    function distributeRewards() external hasStakedTokens {
        uint256 rewardAmount = calculateRewards(msg.sender);
        
        // Ensure rewards are only distributed if there are funds available
        require(rewardAmount > 0, "No rewards to distribute");

        // Update rewards mapping
        rewards[msg.sender] += rewardAmount;

        // Emit the RewardsDistributed event
        emit RewardsDistributed(msg.sender, rewardAmount);
        
        // Transfer rewards to the user
        // For example: transferTokens(msg.sender, rewardAmount);
    }

    // Function to view the user's staked amount
    function getStakedAmount() external view returns (uint256) {
        return stakedAmounts[msg.sender];
    }

    // Function to view the user's accumulated rewards
    function getRewards() external view returns (uint256) {
        return rewards[msg.sender];
    }

    // Optional: Function to withdraw staked tokens and reset the user's state
    function withdrawTokens() external hasStakedTokens {
        uint256 stakedAmount = stakedAmounts[msg.sender];

        // Reset user's staked amount and rewards
        stakedAmounts[msg.sender] = 0;
        rewards[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer the staked tokens back to the user
        // For example: transferTokens(msg.sender, stakedAmount);
    }
}
```
