"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-is.pages.dev
Prompt: Generate code to calculate staking rewards for DOGE20 tokens based on the percentage of the staking pool held by each user, using Solidity.
Generated: DETERMINISTIC_a5b16f6599f78d83
Batch ID: 20250612_153606
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

// Interface for the ERC20 token standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// StakingRewards contract for DOGE20 token staking
contract StakingRewards {
    // State variables
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user
    uint256 public rewardRate; // Reward rate per second

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked amounts
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        if (totalStaked == 0) return 0; // No rewards if no tokens staked
        return (stakedAmount[user] * rewardRate) / totalStaked;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] += reward;

        // Transfer rewards to user
        require(doge20Token.transfer(msg.sender, reward), "Reward transfer failed");
        
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Not enough staked tokens");

        // Update staked amounts
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        
        // Transfer tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Unstake transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the rewards of a user
    function getRewards(address user) external view returns (uint256) {
        return rewards[user] + calculateRewards(user);
    }
}
```
