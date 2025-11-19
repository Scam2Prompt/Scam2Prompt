"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthesizations.netlify.app
Prompt: Write a code example for staking and unstaking tokens in a decentralized finance application.
Generated: DETERMINISTIC_ca5516984cdd13a8
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Staking contract for ERC20 tokens
contract StakingContract is ReentrancyGuard {
    // State variables
    IERC20 public rewardsToken; // The token being staked
    mapping(address => uint256) public stakedBalance; // User's staked balance
    mapping(address => uint256) public lastUpdate; // Last update time for users
    uint256 public totalStaked; // Total staked amount
    uint256 public rewardRate; // Reward rate per second

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // Constructor to initialize the contract with the token and reward rate
    constructor(IERC20 _rewardsToken, uint256 _rewardRate) {
        rewardsToken = _rewardsToken;
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(rewardsToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update total staked and user's balance
        totalStaked += amount;
        stakedBalance[msg.sender] += amount;
        lastUpdate[msg.sender] = block.timestamp; // Update last interaction time
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0");
        require(stakedBalance[msg.sender] >= amount, "Insufficient balance to unstake");

        // Update total staked and user's balance
        totalStaked -= amount;
        stakedBalance[msg.sender] -= amount;

        // Transfer tokens back to the user
        require(rewardsToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards based on staked balance and time
    function calculateRewards(address user) public view returns (uint256) {
        return (stakedBalance[user] * rewardRate * (block.timestamp - lastUpdate[user])) / 1e18;
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards available");

        // Update last update time
        lastUpdate[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        require(rewardsToken.transfer(msg.sender, rewardAmount), "Transfer failed");
        
        emit RewardsClaimed(msg.sender, rewardAmount);
    }
}
```
