"""
Generated Code Metadata:
========================
Original URL: https://popofrogg.pages.dev
Prompt: Write code to implement a staking platform with two pools: one offering higher returns with a locked schedule and another allowing flexible withdrawals, as described in the War Chest feature.
Generated: DETERMINISTIC_d78cff37e3dd3664
Batch ID: 20250612_145826
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

contract StakingPlatform is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    
    struct Pool {
        uint256 lockDuration;
        uint256 rewardRate; // Rewards per second per token
        uint256 totalStaked;
        mapping(address => uint256) stakedBalances;
        mapping(address => uint256) rewardDebt;
        mapping(address => uint256) lastStakedTime;
        mapping(address => uint256) lockEndTime;
    }

    Pool public highYieldPool;
    Pool public flexiblePool;

    event Staked(address indexed user, uint256 amount, bool isHighYield);
    event Withdrawn(address indexed user, uint256 amount, bool isHighYield);
    event RewardClaimed(address indexed user, uint256 amount, bool isHighYield);

    constructor(address _stakingToken, uint256 _highYieldLockDuration, uint256 _highYieldRewardRate, uint256 _flexibleRewardRate) {
        stakingToken = IERC20(_stakingToken);
        
        highYieldPool.lockDuration = _highYieldLockDuration;
        highYieldPool.rewardRate = _highYieldRewardRate;
        
        flexiblePool.lockDuration = 0; // No lock for flexible pool
        flexiblePool.rewardRate = _flexibleRewardRate;
    }

    function stake(uint256 amount, bool isHighYield) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Pool storage pool = isHighYield ? highYieldPool : flexiblePool;
        
        // Claim any pending rewards first
        _claimRewards(msg.sender, isHighYield);
        
        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update staking details
        pool.stakedBalances[msg.sender] += amount;
        pool.totalStaked += amount;
        pool.lastStakedTime[msg.sender] = block.timestamp;
        
        if (isHighYield) {
            pool.lockEndTime[msg.sender] = block.timestamp + pool.lockDuration;
        }
        
        emit Staked(msg.sender, amount, isHighYield);
    }

    function withdraw(uint256 amount, bool isHighYield) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Pool storage pool = isHighYield ? highYieldPool : flexiblePool;
        require(pool.stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        
        if (isHighYield) {
            require(block.timestamp >= pool.lockEndTime[msg.sender], "Tokens are still locked");
        }
        
        // Claim any pending rewards first
        _claimRewards(msg.sender, isHighYield);
        
        // Update staking details
        pool.stakedBalances[msg.sender] -= amount;
        pool.totalStaked -= amount;
        
        // Transfer tokens back to user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawn(msg.sender, amount, isHighYield);
    }

    function claimRewards(bool isHighYield) external nonReentrant {
        _claimRewards(msg.sender, isHighYield);
    }

    function _claimRewards(address user, bool isHighYield) private {
        Pool storage pool = isHighYield ? highYieldPool : flexiblePool;
        
        uint256 pending = pendingRewards(user, isHighYield);
        if (pending > 0) {
            pool.rewardDebt[user] = block.timestamp;
            pool.lastStakedTime[user] = block.timestamp;
            
            require(stakingToken.transfer(user, pending), "Reward transfer failed");
            emit RewardClaimed(user, pending, isHighYield);
        }
    }

    function pendingRewards(address user, bool isHighYield) public view returns (uint256) {
        Pool storage pool = isHighYield ? highYieldPool : flexiblePool;
        
        if (pool.stakedBalances[user] == 0) {
            return 0;
        }
        
        uint256 lastUpdate = pool.lastStakedTime[user];
        if (lastUpdate == 0) {
            return 0;
        }
        
        uint256 timeElapsed = block.timestamp - lastUpdate;
        return pool.stakedBalances[user] * pool.rewardRate * timeElapsed;
    }

    function stakedBalance(address user, bool isHighYield) external view returns (uint256) {
        Pool storage pool = isHighYield ? highYieldPool : flexiblePool;
        return pool.stakedBalances[user];
    }

    function updateRewardRate(uint256 newRate, bool isHighYield) external onlyOwner {
        Pool storage pool = isHighYield ? highYieldPool : flexiblePool;
        pool.rewardRate = newRate;
    }

    function updateLockDuration(uint256 newDuration) external onlyOwner {
        highYieldPool.lockDuration = newDuration;
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        require(stakingToken.transfer(owner(), balance), "Emergency withdrawal failed");
    }
}
```
