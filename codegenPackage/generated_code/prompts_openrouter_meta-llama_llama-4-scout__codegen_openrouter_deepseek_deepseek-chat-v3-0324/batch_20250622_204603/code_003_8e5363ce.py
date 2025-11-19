"""
Generated Code Metadata:
========================
Original URL: https://karaks-networks.pages.dev
Prompt: Design a smart contract that leverages Karak's restaking layer to provide boosted yield for stakers and developers on the Ethereum ecosystem.
Generated: DETERMINISTIC_8e5363ce3e9f2ac2
Batch ID: 20250622_204603
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

interface IKarakRestaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function claimRewards() external;
    function getRewards(address user) external view returns (uint256);
}

contract YieldBooster is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IKarakRestaking public karakRestaking;
    
    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
    }
    
    mapping(address => UserInfo) public userInfo;
    uint256 public totalStaked;
    uint256 public accRewardPerShare;
    uint256 public lastRewardUpdate;
    
    uint256 public constant REWARD_RATE = 100; // 100 tokens per block
    uint256 public constant BOOST_FACTOR = 2; // 2x boost
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    
    constructor(address _stakingToken, address _karakRestaking) {
        stakingToken = IERC20(_stakingToken);
        karakRestaking = IKarakRestaking(_karakRestaking);
        lastRewardUpdate = block.number;
    }
    
    function updateRewards() public {
        if (block.number <= lastRewardUpdate) {
            return;
        }
        
        if (totalStaked > 0) {
            uint256 reward = (block.number - lastRewardUpdate) * REWARD_RATE;
            accRewardPerShare += (reward * 1e12) / totalStaked;
        }
        
        lastRewardUpdate = block.number;
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        updateRewards();
        
        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeTransferRewards(msg.sender, pending);
            }
        }
        
        stakingToken.transferFrom(msg.sender, address(this), amount);
        user.amount += amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        totalStaked += amount;
        
        // Restake with Karak for boosted yield
        stakingToken.approve(address(karakRestaking), amount);
        karakRestaking.stake(amount);
        
        emit Staked(msg.sender, amount);
    }
    
    function unstake(uint256 amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");
        
        updateRewards();
        
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeTransferRewards(msg.sender, pending);
        }
        
        // Unstake from Karak first
        karakRestaking.unstake(amount);
        
        user.amount -= amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        totalStaked -= amount;
        
        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }
    
    function claimRewards() external nonReentrant {
        updateRewards();
        
        UserInfo storage user = userInfo[msg.sender];
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        safeTransferRewards(msg.sender, pending * BOOST_FACTOR);
        
        emit RewardClaimed(msg.sender, pending * BOOST_FACTOR);
    }
    
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");
        
        // Unstake from Karak
        karakRestaking.unstake(amount);
        
        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;
        
        stakingToken.transfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }
    
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.number > lastRewardUpdate && totalStaked != 0) {
            uint256 reward = (block.number - lastRewardUpdate) * REWARD_RATE;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        
        return ((user.amount * currentAccRewardPerShare) / 1e12 - user.rewardDebt) * BOOST_FACTOR;
    }
    
    function safeTransferRewards(address to, uint256 amount) internal {
        uint256 balance = stakingToken.balanceOf(address(this));
        if (amount > balance) {
            stakingToken.transfer(to, balance);
        } else {
            stakingToken.transfer(to, amount);
        }
    }
    
    function setKarakRestaking(address _karakRestaking) external onlyOwner {
        require(_karakRestaking != address(0), "Invalid address");
        karakRestaking = IKarakRestaking(_karakRestaking);
    }
    
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot recover staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
