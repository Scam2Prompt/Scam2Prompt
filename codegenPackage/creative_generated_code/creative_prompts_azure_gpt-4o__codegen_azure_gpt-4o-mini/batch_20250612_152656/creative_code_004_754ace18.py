"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-d.web.app
Prompt: Write a function in Solidity to calculate staking rewards for DOGE20 tokens based on the percentage of the staking pool owned by a user.
Generated: DETERMINISTIC_754ace18dc14db09
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

contract StakingRewards {

    // State variables
    mapping(address => uint256) public stakedAmounts; // Amount of DOGE20 tokens staked by each user
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked in the pool
    uint256 public rewardRate; // Reward rate in percentage (e.g., 10 represents 10%)

    // Event to emit when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event to emit when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be positive");
        rewardRate = _rewardRate;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update state
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        // Emit the stake event
        emit Staked(msg.sender, amount);
    }

    // Function to calculate staking rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        // Check if the user has staked any tokens
        require(stakedAmounts[user] > 0, "User has not staked any tokens");

        // Calculate the percentage of the staking pool owned by the user
        uint256 userPercentage = (stakedAmounts[user] * 100) / totalStaked;

        // Calculate and return the rewards based on the user's percentage and reward rate
        uint256 rewards = (userPercentage * rewardRate) / 100;
        return rewards;
    }

    // Function to withdraw staked DOGE20 tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked balance");

        // Update state
        stakedAmounts[msg.sender] -= amount;
        totalStaked -= amount;

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }
}
```
