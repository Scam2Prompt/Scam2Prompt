"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Create a Solidity function to distribute staking rewards in a decentralized network, inspired by the "코인을 맡기면 이자가 나온다고?" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_2100f5765b146c7f
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StakingRewards {
    // Mapping to track the staked amounts of each user
    mapping(address => uint256) public stakedAmounts;
    // Mapping to track the rewards of each user
    mapping(address => uint256) public rewards;
    // Total staked amount in the contract
    uint256 public totalStaked;
    // Reward rate per block
    uint256 public rewardRate;
    // Block number when rewards start
    uint256 public startBlock;

    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 reward);

    // Constructor to initialize the reward rate and start block
    constructor(uint256 _rewardRate) {
        rewardRate = _rewardRate;
        startBlock = block.number;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update the user's staked amount and total staked
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        // Emit an event for staking
        emit RewardsDistributed(msg.sender, 0);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 blocksStaked = block.number - startBlock;
        return (blocksStaked * rewardRate * stakedAmounts[user]) / totalStaked;
    }

    // Function to distribute rewards to stakers
    function distributeRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update the user's rewards
        rewards[msg.sender] += reward;

        // Emit an event for rewards distribution
        emit RewardsDistributed(msg.sender, reward);
    }

    // Function to withdraw staked tokens and rewards
    function withdraw() external {
        uint256 stakedAmount = stakedAmounts[msg.sender];
        uint256 reward = rewards[msg.sender];

        require(stakedAmount > 0 || reward > 0, "No funds to withdraw");

        // Reset the user's staked amount and rewards
        stakedAmounts[msg.sender] = 0;
        rewards[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer the staked amount and rewards to the user
        // Note: In a real contract, you would use a token transfer function here
        // For example: token.transfer(msg.sender, stakedAmount + reward);

        // Emit an event for withdrawal
        emit RewardsDistributed(msg.sender, reward);
    }
}
```
