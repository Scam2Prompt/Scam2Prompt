"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Create a Solidity function to distribute staking rewards in a decentralized network, inspired by the "코인을 맡기면 이자가 나온다고?" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_2100f5765b146c7f
Batch ID: 20250612_154412
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
    // Mapping to store staked amounts for each user
    mapping(address => uint256) public stakedAmount;
    // Mapping to track accumulated rewards for each user
    mapping(address => uint256) public rewards;
    // Total staked amount in the contract
    uint256 public totalStaked;
    // Reward rate per block
    uint256 public rewardRate; 
    // Block number when rewards distribution starts
    uint256 public startBlock;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _rewardRate;
        startBlock = block.number; // Start rewards distribution from contract deployment
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        distributeRewards(msg.sender);

        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
    }

    // Internal function to distribute rewards
    function distributeRewards(address user) internal {
        uint256 reward = calculateRewards(user);
        rewards[user] += reward;

        // Emit rewards distributed event
        emit RewardsDistributed(user, reward);
    }

    // Function to calculate rewards based on staking duration and amount
    function calculateRewards(address user) public view returns (uint256) {
        uint256 userStake = stakedAmount[user];
        
        // Calculate blocks staked since the last reward distribution
        uint256 blocksStaked = block.number - startBlock;
        
        // Calculate total rewards based on the user's stake and the reward rate
        return (userStake * rewardRate * blocksStaked) / totalStaked;
    }

    // Function to claim rewards
    function claimRewards() external {
        distributeRewards(msg.sender);
        uint256 rewardToClaim = rewards[msg.sender];
        require(rewardToClaim > 0, "No rewards to claim");

        // Reset rewards after claiming
        rewards[msg.sender] = 0;

        // Here we would transfer the reward tokens to the user (implementation omitted)
        // token.transfer(msg.sender, rewardToClaim);
    }
}
```
