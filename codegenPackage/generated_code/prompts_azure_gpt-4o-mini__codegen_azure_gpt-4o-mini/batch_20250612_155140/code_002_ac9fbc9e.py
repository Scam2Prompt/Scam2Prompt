"""
Generated Code Metadata:
========================
Original URL: https://casinotg.pages.dev
Prompt: Create a Solidity contract that implements a basic staking mechanism for the $TGC token, allowing users to earn passive income.
Generated: DETERMINISTIC_ac9fbc9efb753c90
Batch ID: 20250612_155140
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

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for the $TGC token
contract Staking {
    // State variables
    IERC20 public tgcToken; // The $TGC token contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per second
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastStakedTime; // Last time the user staked tokens
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the token address and reward rate
    constructor(IERC20 _tgcToken, uint256 _rewardRate) {
        tgcToken = _tgcToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(tgcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        // Update the last staked time
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate and pay rewards before unstaking
        _updateRewards(msg.sender);

        // Update the user's staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the tokens back to the user
        require(tgcToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the user's rewards and transfer the reward
        rewards[msg.sender] = 0;
        require(tgcToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        if (stakedAmount[user] > 0) {
            uint256 timeStaked = block.timestamp - lastStakedTime[user];
            uint256 reward = timeStaked * rewardRate * stakedAmount[user];
            rewards[user] += reward;
            lastStakedTime[user] = block.timestamp; // Update last staked time
        }
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the total rewards of a user
    function getRewards(address user) external view returns (uint256) {
        return rewards[user] + (block.timestamp - lastStakedTime[user]) * rewardRate * stakedAmount[user];
    }
}
```
