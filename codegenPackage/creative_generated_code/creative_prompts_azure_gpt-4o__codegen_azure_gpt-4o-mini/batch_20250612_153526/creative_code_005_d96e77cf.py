"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-io-dashborad.pages.dev
Prompt: Create a function in Solidity that calculates staking rewards for DOGE20 tokens based on the percentage of the staking pool held by a user.
Generated: DETERMINISTIC_d96e77cfa1220692
Batch ID: 20250612_153526
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
    address public owner;
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward rate percentage (e.g., 5 for 5%)
    
    // Mapping to track the amount staked by each user
    mapping(address => uint256) private stakedAmounts;

    // Event to be emitted when rewards are calculated
    event RewardsCalculated(address indexed user, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update total staked amount and user's staked amount
        totalStaked += amount;
        stakedAmounts[msg.sender] += amount;
    }

    // Function to calculate staking rewards for a user
    function calculateRewards(address user) external view returns (uint256) {
        require(totalStaked > 0, "No tokens staked");

        // Get the amount staked by the user
        uint256 userStake = stakedAmounts[user];
        
        // Calculate the user's percentage of the total staked amount
        uint256 userPercentage = (userStake * 100) / totalStaked;

        // Calculate the rewards based on the user's percentage and the reward rate
        uint256 rewards = (userPercentage * rewardRate) / 100;

        return rewards;
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update total staked amount and user's staked amount
        totalStaked -= amount;
        stakedAmounts[msg.sender] -= amount;
    }
    
    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }
}
```
