"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-en.web.app
Prompt: Create a Solidity smart contract that implements a staking mechanism similar to InQubeta's $QUBE staking system, where rewards are distributed from a sell tax pool.
Generated: DETERMINISTIC_3d1bd0d6a3c173be
Batch ID: 20250612_152620
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

contract QubeStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastClaim;  // Timestamp of last claim
    }

    // The staking token (QUBE)
    IERC20 public immutable stakingToken;
    
    // The reward token (same as staking token)
    IERC20 public immutable rewardToken;
    
    // Reward distribution variables
    uint256 public rewardPerSecond;
    uint256 public lastRewardTime;
    uint256 public accRewardPerShare;
    uint256 public totalStaked;
    
    // Staking period and lockup
    uint256 public constant MIN_STAKE_DURATION = 7 days;
    uint256 public constant MAX_STAKE_DURATION = 365 days;
    
    // Reward calculation precision
    uint256 private constant PRECISION = 1e12;
    
    // Mapping of user addresses to their staking info
    mapping(address => UserInfo) public userInfo;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    
    constructor(IERC20 _stakingToken, IERC20 _rewardToken) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        lastRewardTime = block.timestamp;
    }
    
    // Update reward variables
    function updatePool() public {
        if (block.timestamp <= lastRewardTime) {
            return;
        }
        
        if (totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }
        
        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardPerSecond;
        
        accRewardPerShare += (reward * PRECISION) / totalStaked;
        lastRewardTime = block.timestamp;
    }
    
    // Stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");
        
        UserInfo storage user = userInfo[msg.sender];
        updatePool();
        
        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        user.lastClaim = block.timestamp;
        totalStaked += _amount;
        
        emit Staked(msg.sender, _amount);
    }
    
    // Unstake tokens
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        require(block.timestamp >= user.lastClaim + MIN_STAKE_DURATION, "Too early to unstake");
        
        updatePool();
        
        uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        user.lastClaim = block.timestamp;
        totalStaked -= _amount;
        
        stakingToken.safeTransfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _amount);
    }
    
    // Claim rewards without unstaking
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No staked amount");
        
        updatePool();
        
        uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        user.lastClaim = block.timestamp;
        
        safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }
    
    // Emergency withdraw without rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");
        
        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked -= amount;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }
    
    // Safe reward transfer function
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }
    
    // Set reward rate (only owner)
    function setRewardRate(uint256 _rewardPerSecond) external onlyOwner {
        updatePool();
        rewardPerSecond = _rewardPerSecond;
        emit RewardRateUpdated(_rewardPerSecond);
    }
    
    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
    
    // View function to see pending rewards
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardPerSecond;
            currentAccRewardPerShare += (reward * PRECISION) / totalStaked;
        }
        
        return (user.amount * currentAccRewardPerShare) / PRECISION - user.rewardDebt;
    }
    
    // View function to get user info
    function getUserInfo(address _user) external view returns (uint256, uint256, uint256) {
        UserInfo storage user = userInfo[_user];
        return (user.amount, user.rewardDebt, user.lastClaim);
    }
}
```
