"""
Generated Code Metadata:
========================
Original URL: https://rabotaentnet.pages.dev
Prompt: Generate code to implement staking functionality for the $ZUSHI token, ensuring users can stake their tokens and receive rewards based on the distribution model outlined in the Zushi ecosystem.
Generated: DETERMINISTIC_dbf34574892d1921
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ZushiStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastClaim;  // Timestamp of last claim
    }

    // The ZUSHI token contract
    IERC20 public immutable zushiToken;
    
    // Reward token (could be same as staking token)
    IERC20 public immutable rewardToken;
    
    // Reward rate per second
    uint256 public rewardRate;
    
    // Precision factor for reward calculations
    uint256 public constant PRECISION_FACTOR = 1e18;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Last time reward distribution was updated
    uint256 public lastRewardUpdate;
    
    // Total tokens staked
    uint256 public totalStaked;
    
    // Mapping from user address to user info
    mapping(address => UserInfo) public userInfo;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        IERC20 _zushiToken,
        IERC20 _rewardToken,
        uint256 _rewardRate
    ) {
        require(address(_zushiToken) != address(0), "Invalid ZUSHI token");
        require(address(_rewardToken) != address(0), "Invalid reward token");
        
        zushiToken = _zushiToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        lastRewardUpdate = block.timestamp;
    }

    // Update reward variables
    function updateReward() internal {
        if (block.timestamp <= lastRewardUpdate || totalStaked == 0) {
            return;
        }
        
        uint256 timeElapsed = block.timestamp - lastRewardUpdate;
        uint256 reward = timeElapsed * rewardRate;
        
        accRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        lastRewardUpdate = block.timestamp;
    }

    // Stake ZUSHI tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");
        
        updateReward();
        
        UserInfo storage user = userInfo[msg.sender];
        
        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        zushiToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastClaim = block.timestamp;
        totalStaked += _amount;
        
        emit Staked(msg.sender, _amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        
        updateReward();
        
        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastClaim = block.timestamp;
        totalStaked -= _amount;
        
        zushiToken.safeTransfer(msg.sender, _amount);
        emit Withdrawn(msg.sender, _amount);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        updateReward();
        
        UserInfo storage user = userInfo[msg.sender];
        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        
        require(pending > 0, "No rewards to claim");
        
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastClaim = block.timestamp;
        
        safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        
        require(amount > 0, "Nothing to withdraw");
        
        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;
        
        zushiToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // View function to see pending rewards
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        
        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.timestamp > lastRewardUpdate && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardUpdate;
            uint256 reward = timeElapsed * rewardRate;
            currentAccRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        }
        
        return (user.amount * currentAccRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
    }

    // Update reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updateReward();
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Safe reward transfer function
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (_amount > rewardBalance) {
            rewardToken.safeTransfer(_to, rewardBalance);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(zushiToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
