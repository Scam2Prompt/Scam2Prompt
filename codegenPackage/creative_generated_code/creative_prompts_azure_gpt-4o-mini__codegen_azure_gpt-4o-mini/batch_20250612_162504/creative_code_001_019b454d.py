"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-i.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens that allows users to earn passive rewards based on their stake.
Generated: DETERMINISTIC_019b454d6d1bab46
Batch ID: 20250612_162504
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

// Interface for the DOGE20 token contract
interface IDOGE20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract to allow users to stake DOGE20 tokens and earn rewards
contract StakingDoge20 {
    IDOGE20 public doge20Token; // The DOGE20 token contract
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount staked
    uint256 public totalRewards; // Total rewards distributed
    mapping(address => uint256) public stakedAmount; // User staked amounts
    mapping(address => uint256) public rewards; // User rewards
    mapping(address => uint256) public lastUpdate; // Last block update for each user

    // Events for staking and reward distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the DOGE20 token contract and reward rate
    constructor(address _doge20Token, uint256 _rewardRate) {
        doge20Token = IDOGE20(_doge20Token);
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before staking or unstaking
    modifier updateRewards() {
        if (stakedAmount[msg.sender] > 0) {
            rewards[msg.sender] += calculateReward(msg.sender);
            lastUpdate[msg.sender] = block.number;
        }
        _;
    }

    // Function to calculate rewards based on staked amount and blocks
    function calculateReward(address user) internal view returns (uint256) {
        return (block.number - lastUpdate[user]) * rewardRate * stakedAmount[user];
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot stake 0");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot unstake 0");
        require(amount <= stakedAmount[msg.sender], "Insufficient staked amount");

        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        totalRewards += reward;
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to get the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the user's earned rewards
    function getRewards(address user) external view returns (uint256) {
        return rewards[user] + calculateReward(user);
    }
}
```
