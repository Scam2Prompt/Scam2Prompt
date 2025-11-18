"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testuser.usdtddex.com
Prompt: Create a Solidity contract snippet to implement the staking functionality for USDTD tokens, including the ability to stake, unstake, and claim rewards based on the daily percentage rates described.
Generated: DETERMINISTIC_2e9ab7a46914cbc7
Batch ID: 20250612_150345
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

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    IERC20 public usdtToken;            // The USDT token contract
    uint256 public dailyRewardRate;     // Daily reward rate in basis points (1% = 100 basis points)
    mapping(address => uint256) public stakes;   // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public lastStakedTime; // Last time the user staked
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the USDT token address and daily reward rate
    constructor(IERC20 _usdtToken, uint256 _dailyRewardRate) {
        usdtToken = _usdtToken;
        dailyRewardRate = _dailyRewardRate;
    }

    // Function to stake USDT tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Must stake more than 0");
        require(usdtToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's rewards before staking
        updateRewards(msg.sender);
        
        stakes[msg.sender] += amount; // Increase the user's stake
        lastStakedTime[msg.sender] = block.timestamp; // Update the last staked time

        emit Staked(msg.sender, amount);
    }

    // Function to unstake USDT tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Must unstake more than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's rewards before unstaking
        updateRewards(msg.sender);
        
        stakes[msg.sender] -= amount; // Decrease the user's stake
        require(usdtToken.transfer(msg.sender, amount), "Transfer failed"); // Transfer tokens back

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim accumulated rewards
    function claimRewards() external {
        updateRewards(msg.sender); // Update rewards before claiming
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0; // Reset the user's rewards
        require(usdtToken.transfer(msg.sender, rewardAmount), "Transfer failed"); // Transfer rewards

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Internal function to update rewards based on time passed
    function updateRewards(address user) internal {
        if (stakes[user] > 0) {
            uint256 timeStaked = block.timestamp - lastStakedTime[user]; // Time since last stake
            uint256 reward = (stakes[user] * dailyRewardRate * timeStaked) / 1 days / 10000; // Calculate reward
            rewards[user] += reward; // Accumulate rewards
        }
        lastStakedTime[user] = block.timestamp; // Update last staked time
    }

    // View function to check the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    // View function to check the pending rewards of a user
    function getPendingRewards(address user) external view returns (uint256) {
        uint256 timeStaked = block.timestamp - lastStakedTime[user];
        uint256 reward = (stakes[user] * dailyRewardRate * timeStaked) / 1 days / 10000;
        return rewards[user] + reward;
    }
}
```
