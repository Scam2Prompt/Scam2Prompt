"""
Generated Code Metadata:
========================
Original URL: https://renzos.pages.dev
Prompt: Develop a smart contract that interacts with Renzo's Liquid Restaking Token (LRT) to secure Actively Validated Services (AVSs) and distribute rewards.
Generated: DETERMINISTIC_78292faa4d980297
Batch ID: 20250612_153526
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface ILRT {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}

interface IAVS {
    function registerValidator(address validator) external;
    function deregisterValidator(address validator) external;
    function isActiveValidator(address validator) external view returns (bool);
    function distributeRewards(uint256 amount) external;
}

contract LRTStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    ILRT public lrtToken;
    IAVS public avs;

    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        bool isActive;
    }

    uint256 public totalStaked;
    uint256 public rewardPerToken;
    uint256 public lastRewardUpdate;
    uint256 public rewardRate;
    uint256 public rewardDuration = 7 days;

    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event AVSRegistered(address indexed validator);
    event AVSDeregistered(address indexed validator);

    constructor(address _lrtToken, address _avs) {
        require(_lrtToken != address(0), "Invalid LRT token address");
        require(_avs != address(0), "Invalid AVS address");
        
        lrtToken = ILRT(_lrtToken);
        avs = IAVS(_avs);
        lastRewardUpdate = block.timestamp;
    }

    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardUpdate;
            uint256 rewards = timeElapsed * rewardRate;
            rewardPerToken += (rewards * 1e18) / totalStaked;
        }
        lastRewardUpdate = block.timestamp;
        _;
    }

    function stake(uint256 amount) external nonReentrant updateRewards {
        require(amount > 0, "Cannot stake 0");
        
        Staker storage staker = stakers[msg.sender];
        
        if (staker.stakedAmount == 0) {
            staker.isActive = true;
            avs.registerValidator(msg.sender);
            emit AVSRegistered(msg.sender);
        }
        
        uint256 pendingRewards = (staker.stakedAmount * rewardPerToken) / 1e18 - staker.rewardDebt;
        if (pendingRewards > 0) {
            _safeTransferRewards(msg.sender, pendingRewards);
        }
        
        lrtToken.transferFrom(msg.sender, address(this), amount);
        staker.stakedAmount += amount;
        staker.rewardDebt = (staker.stakedAmount * rewardPerToken) / 1e18;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant updateRewards {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");
        
        uint256 pendingRewards = (staker.stakedAmount * rewardPerToken) / 1e18 - staker.rewardDebt;
        if (pendingRewards > 0) {
            _safeTransferRewards(msg.sender, pendingRewards);
        }
        
        staker.stakedAmount -= amount;
        staker.rewardDebt = (staker.stakedAmount * rewardPerToken) / 1e18;
        totalStaked -= amount;
        
        lrtToken.transfer(msg.sender, amount);
        
        if (staker.stakedAmount == 0 && staker.isActive) {
            staker.isActive = false;
            avs.deregisterValidator(msg.sender);
            emit AVSDeregistered(msg.sender);
        }
        
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant updateRewards {
        Staker storage staker = stakers[msg.sender];
        uint256 pendingRewards = (staker.stakedAmount * rewardPerToken) / 1e18 - staker.rewardDebt;
        require(pendingRewards > 0, "No rewards to claim");
        
        staker.rewardDebt = (staker.stakedAmount * rewardPerToken) / 1e18;
        _safeTransferRewards(msg.sender, pendingRewards);
        
        emit RewardClaimed(msg.sender, pendingRewards);
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    function _safeTransferRewards(address to, uint256 amount) internal {
        uint256 balance = lrtToken.balanceOf(address(this));
        if (amount > balance) {
            amount = balance;
        }
        if (amount > 0) {
            lrtToken.transfer(to, amount);
        }
    }

    function pendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 currentRewardPerToken = rewardPerToken;
        
        if (totalStaked > 0 && block.timestamp > lastRewardUpdate) {
            uint256 timeElapsed = block.timestamp - lastRewardUpdate;
            uint256 rewards = timeElapsed * rewardRate;
            currentRewardPerToken += (rewards * 1e18) / totalStaked;
        }
        
        return (staker.stakedAmount * currentRewardPerToken) / 1e18 - staker.rewardDebt;
    }

    function isActiveValidator(address validator) external view returns (bool) {
        return stakers[validator].isActive;
    }
}
```
