"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: How can I implement a staking mechanism for the $ZUSHI token that aligns with Zushi's energy-efficient consensus model?
Generated: DETERMINISTIC_2c02cf0e0f2594b1
Batch ID: 20250612_160853
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $ZUSHI token
contract ZushiStaking is Ownable {
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Variables
    IERC20 public zushiToken; // Reference to the $ZUSHI token
    uint256 public totalStaked; // Total amount staked
    uint256 public rewardRate; // Reward rate per second
    mapping(address => uint256) public stakedBalance; // User's staked amount
    mapping(address => uint256) public rewards; // Rewards per user
    mapping(address => uint256) public lastUpdateTime; // Last update time for rewards

    // Constructor to initialize the staking contract
    constructor(IERC20 _zushiToken, uint256 _rewardRate) {
        zushiToken = _zushiToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards for a user
    modifier updateReward(address account) {
        rewards[account] += earned(account);
        lastUpdateTime[account] = block.timestamp;
        _;
    }

    // Function to stake $ZUSHI tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        require(zushiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedBalance[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $ZUSHI tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");

        stakedBalance[msg.sender] -= amount;
        totalStaked -= amount;

        require(zushiToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return (stakedBalance[account] * rewardRate * (block.timestamp - lastUpdateTime[account])) / 1e18;
    }

    // Function to withdraw rewards
    function withdrawRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to withdraw");

        rewards[msg.sender] = 0;
        require(zushiToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Function to set new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
