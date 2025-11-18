"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai-claim.pages.dev
Prompt: Write a Solidity smart contract snippet to distribute $SCOTTY staking rewards dynamically based on the user's share of the staking pool and the current reward rate per ETH block.
Generated: DETERMINISTIC_801d1d2060d19c0c
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

contract StakingRewards {
    // Mapping from user address to staked amount
    mapping(address => uint256) public stakedAmount;

    // Total amount of staked tokens
    uint256 public totalStaked;

    // Reward rate per block (in wei)
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 reward);

    // Error declaration for insufficient funds
    error InsufficientRewards();

    // Constructor to initialize the reward rate
    constructor(uint256 _rewardRate) {
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update state variables
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
    }

    // Function to calculate rewards based on staked amount and total staked
    function calculateRewards(address user) public view returns (uint256) {
        if (totalStaked == 0) return 0; // Avoid division by zero

        // Calculate user's share of the pool
        uint256 userShare = (stakedAmount[user] * rewardRate) / totalStaked;
        return userShare;
    }

    // Function to distribute rewards to a user
    function distributeRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available for distribution");

        // Handle potential underflow
        if (totalRewards < reward) {
            revert InsufficientRewards();
        }

        // Update total rewards and emit event
        totalRewards -= reward;
        emit RewardsDistributed(msg.sender, reward);

        // Logic for transferring rewards to the user would go here
        // (e.g., transferring $SCOTTY tokens)
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external {
        // Implement access control for owner
        rewardRate = newRate;
    }
}
```
