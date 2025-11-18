"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheaidapp.pages.dev
Prompt: Write a Solidity function to allow users to withdraw their staked $SCOTTY tokens while maintaining accurate tracking of their rewards and pool percentage.
Generated: DETERMINISTIC_001c6949eeedf382
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

contract StakingPool {
    // Mapping to track user stakes and rewards
    mapping(address => uint256) private stakes;
    mapping(address => uint256) private rewards;

    // Total staked amount in the pool
    uint256 public totalStaked;

    // Reward rate per staked token (e.g., per block)
    uint256 public rewardRate;

    // Event to log withdrawals
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Modifier to check if the user has staked tokens
    modifier hasStake() {
        require(stakes[msg.sender] > 0, "No tokens staked");
        _;
    }

    constructor(uint256 _rewardRate) {
        rewardRate = _rewardRate; // Set the reward rate during deployment
    }

    // Function to stake tokens (not requested, included for completeness)
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Update user's stake and the total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        // Assuming a transfer function to move tokens to the contract
        // token.transferFrom(msg.sender, address(this), amount);
    }

    // Function to withdraw staked tokens and rewards
    function withdraw() external hasStake {
        // Calculate rewards before resetting the user's stake
        uint256 reward = calculateRewards(msg.sender);
        
        // Get the amount to withdraw
        uint256 userStake = stakes[msg.sender];

        // Reset user's stakes and rewards
        stakes[msg.sender] = 0;
        rewards[msg.sender] = 0;
        totalStaked -= userStake;

        // Transfer the user's stake and rewards
        // Assuming a transfer function to move tokens to the user
        // token.transfer(msg.sender, userStake);
        // token.transfer(msg.sender, reward);

        // Emit withdrawal event
        emit Withdrawn(msg.sender, userStake, reward);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) private view returns (uint256) {
        // Simple reward calculation based on the staked amount and the reward rate
        return (stakes[user] * rewardRate);
    }

    // Function to view user stake
    function getStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to view user rewards
    function getRewards(address user) external view returns (uint256) {
        return calculateRewards(user);
    }
}
```
