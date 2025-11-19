"""
Generated Code Metadata:
========================
Original URL: https://levei.money
Prompt: Generate code to integrate lvlUSD into a decentralized application (dApp) for tracking deposits and earning stackable yields.
Generated: DETERMINISTIC_9b7e43906b6c6571
Batch ID: 20250612_154632
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface ILvlUSD {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract LvlUSDYieldTracker is Ownable, ReentrancyGuard {
    ILvlUSD public lvlUSDToken;
    
    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 pendingRewards;
    }
    
    uint256 public totalDeposits;
    uint256 public accRewardsPerShare;
    uint256 public lastRewardUpdate;
    uint256 public rewardPerSecond;
    
    mapping(address => UserInfo) public userInfo;
    
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Claim(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    
    constructor(address _lvlUSDToken, uint256 _rewardPerSecond) {
        require(_lvlUSDToken != address(0), "Invalid token address");
        lvlUSDToken = ILvlUSD(_lvlUSDToken);
        rewardPerSecond = _rewardPerSecond;
        lastRewardUpdate = block.timestamp;
    }
    
    function updateReward() internal {
        if (block.timestamp <= lastRewardUpdate || totalDeposits == 0) {
            lastRewardUpdate = block.timestamp;
            return;
        }
        
        uint256 timeElapsed = block.timestamp - lastRewardUpdate;
        uint256 rewards = timeElapsed * rewardPerSecond;
        accRewardsPerShare += (rewards * 1e12) / totalDeposits;
        lastRewardUpdate = block.timestamp;
    }
    
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        updateReward();
        
        UserInfo storage user = userInfo[msg.sender];
        
        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardsPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                user.pendingRewards += pending;
            }
        }
        
        require(lvlUSDToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardsPerShare) / 1e12;
        totalDeposits += _amount;
        
        emit Deposit(msg.sender, _amount);
    }
    
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient balance");
        
        updateReward();
        
        uint256 pending = (user.amount * accRewardsPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            user.pendingRewards += pending;
        }
        
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardsPerShare) / 1e12;
        totalDeposits -= _amount;
        
        require(lvlUSDToken.transfer(msg.sender, _amount), "Transfer failed");
        
        emit Withdraw(msg.sender, _amount);
    }
    
    function claim() external nonReentrant {
        updateReward();
        
        UserInfo storage user = userInfo[msg.sender];
        uint256 pending = (user.amount * accRewardsPerShare) / 1e12 - user.rewardDebt + user.pendingRewards;
        
        require(pending > 0, "No rewards to claim");
        
        user.pendingRewards = 0;
        user.rewardDebt = (user.amount * accRewardsPerShare) / 1e12;
        
        require(lvlUSDToken.transfer(msg.sender, pending), "Transfer failed");
        
        emit Claim(msg.sender, pending);
    }
    
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardsPerShare = accRewardsPerShare;
        
        if (block.timestamp > lastRewardUpdate && totalDeposits != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardUpdate;
            uint256 rewards = timeElapsed * rewardPerSecond;
            currentAccRewardsPerShare += (rewards * 1e12) / totalDeposits;
        }
        
        return user.pendingRewards + ((user.amount * currentAccRewardsPerShare) / 1e12 - user.rewardDebt);
    }
    
    function setRewardRate(uint256 _rewardPerSecond) external onlyOwner {
        updateReward();
        rewardPerSecond = _rewardPerSecond;
        emit RewardRateUpdated(_rewardPerSecond);
    }
    
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        
        require(amount > 0, "No deposits to withdraw");
        
        totalDeposits -= amount;
        user.amount = 0;
        user.rewardDebt = 0;
        user.pendingRewards = 0;
        
        require(lvlUSDToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdraw(msg.sender, amount);
    }
    
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(lvlUSDToken), "Cannot recover lvlUSD");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
