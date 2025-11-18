"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-ai.web.app
Prompt: Create a smart contract in Solidity that mimics the staking functionality described on the Scotty AI platform, including reward multipliers based on lock periods.
Generated: DETERMINISTIC_13f4f7ab008f3f0f
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

contract Staking {
    // Event to emit when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    
    // Event to emit when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Structure to hold staking details
    struct Staker {
        uint256 amount; // Amount staked
        uint256 lockPeriod; // Lock period in seconds
        uint256 startTime; // Time when staking started
    }

    // Mapping to keep track of stakers
    mapping(address => Staker) public stakers;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward multiplier based on lock period (lock period in seconds)
    mapping(uint256 => uint256) public rewardMultipliers;

    // Constructor to initialize reward multipliers
    constructor() {
        // Initialize reward multipliers for different lock periods
        rewardMultipliers[30 days] = 10; // 10% for 30 days
        rewardMultipliers[60 days] = 20; // 20% for 60 days
        rewardMultipliers[90 days] = 30; // 30% for 90 days
    }

    // Function to stake tokens
    function stake(uint256 amount, uint256 lockPeriod) external {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardMultipliers[lockPeriod] > 0, "Invalid lock period");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.lockPeriod = lockPeriod;
        staker.startTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount, lockPeriod);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No tokens to unstake");
        require(block.timestamp >= staker.startTime + staker.lockPeriod, "Lock period not yet ended");

        // Calculate reward based on amount staked and reward multiplier
        uint256 reward = (staker.amount * rewardMultipliers[staker.lockPeriod]) / 100;

        // Reset staker information
        totalStaked -= staker.amount;
        delete stakers[msg.sender];

        // Transfer staked amount and reward to user (implementation of transfer not shown)
        _transfer(msg.sender, staker.amount + reward);

        // Emit unstaking event
        emit Unstaked(msg.sender, staker.amount, reward);
    }

    // Internal function to handle token transfer (mock function)
    // In a real contract, you would implement ERC20 token transfer logic here
    function _transfer(address to, uint256 amount) internal {
        // Placeholder for actual token transfer logic
        // Use an ERC20 token contract to transfer the amount to the 'to' address
    }
}
```
