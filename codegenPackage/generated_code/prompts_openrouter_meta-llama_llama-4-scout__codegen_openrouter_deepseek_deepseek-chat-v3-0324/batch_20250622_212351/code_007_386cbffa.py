"""
Generated Code Metadata:
========================
Original URL: https://wallstreet-pepe.vercel.app
Prompt: Develop a staking system for $WEPE Token holders to claim and stake their tokens, considering the provided token address and supply.
Generated: DETERMINISTIC_386cbffab26992c7
Batch ID: 20250622_212351
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WEPEStaking is ReentrancyGuard, Ownable {
    IERC20 public wepeToken;
    
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }
    
    uint256 public constant REWARD_RATE = 10; // 10% APY
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public totalStaked;
    
    mapping(address => Stake) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    
    constructor(address _wepeTokenAddress) {
        require(_wepeTokenAddress != address(0), "Invalid token address");
        wepeToken = IERC20(_wepeTokenAddress);
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(wepeToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Transfer tokens from user to contract
        require(wepeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Calculate pending rewards before updating stake
        uint256 pendingRewards = calculateRewards(msg.sender);
        
        // Update existing stake or create new one
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            userStake.rewardDebt += pendingRewards;
        } else {
            userStake.startTime = block.timestamp;
        }
        
        userStake.amount += amount;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        // Calculate and transfer rewards
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            require(wepeToken.transfer(msg.sender, rewards), "Reward transfer failed");
            emit RewardClaimed(msg.sender, rewards);
        }
        
        // Update stake
        userStake.amount -= amount;
        totalStaked -= amount;
        userStake.rewardDebt = 0;
        userStake.startTime = block.timestamp;
        
        // Transfer staked tokens back to user
        require(wepeToken.transfer(msg.sender, amount), "Unstake transfer failed");
        
        emit Unstaked(msg.sender, amount);
    }
    
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");
        
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");
        
        userStake.rewardDebt = 0;
        userStake.startTime = block.timestamp;
        
        require(wepeToken.transfer(msg.sender, rewards), "Reward transfer failed");
        emit RewardClaimed(msg.sender, rewards);
    }
    
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 rewards = (userStake.amount * REWARD_RATE * stakingDuration) / (REWARD_INTERVAL * 100);
        return rewards + userStake.rewardDebt;
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = wepeToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(wepeToken.transfer(owner(), balance), "Withdrawal failed");
    }
    
    function getUserStake(address user) external view returns (uint256 amount, uint256 startTime, uint256 pendingRewards) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.startTime, calculateRewards(user));
    }
}
```
