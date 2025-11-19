"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-claim.pages.dev
Prompt: Write a smart contract in Solidity that mimics the staking mechanism described in WienerAI, allowing users to stake tokens and earn rewards with a high APY.
Generated: DETERMINISTIC_9992729fa5c40bf3
Batch ID: 20250612_152358
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

contract WienerAIStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by user
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastClaim;  // Timestamp of last claim
    }

    // The staking token
    IERC20 public stakingToken;
    
    // The reward token (same as staking token in this case)
    IERC20 public rewardToken;
    
    // Reward rate per second (calculated from APY)
    uint256 public rewardRate;
    
    // Precision factor for reward calculations
    uint256 public constant PRECISION = 1e18;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Last time reward distribution occurred
    uint256 public lastRewardTime;
    
    // Staking duration in seconds (e.g., 30 days)
    uint256 public stakingDuration;
    
    // High APY (e.g., 10000 for 10000%)
    uint256 public highAPY;
    
    // Mapping of user addresses to their info
    mapping(address => UserInfo) public userInfo;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        IERC20 _stakingToken,
        uint256 _highAPY,
        uint256 _stakingDuration
    ) {
        stakingToken = _stakingToken;
        rewardToken = _stakingToken;
        highAPY = _highAPY;
        stakingDuration = _stakingDuration;
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
        uint256 reward = (timeElapsed * rewardRate);
        
        accRewardPerShare += (reward * PRECISION) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    // Stake tokens to earn rewards
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
        
        // Update reward rate based on current APY and total staked
        rewardRate = (totalStaked * highAPY) / (100 * 365 days);
        
        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens and claim rewards
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        require(block.timestamp >= user.lastClaim + stakingDuration, "Staking duration not reached");
        
        updatePool();
        
        uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        if (_amount > 0) {
            user.amount -= _amount;
            stakingToken.safeTransfer(msg.sender, _amount);
            totalStaked -= _amount;
            emit Unstaked(msg.sender, _amount);
        }
        
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        user.lastClaim = block.timestamp;
        
        // Update reward rate based on current APY and total staked
        rewardRate = (totalStaked * highAPY) / (100 * 365 days);
    }

    // Claim rewards without unstaking
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No staked amount");
        
        updatePool();
        
        uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        safeRewardTransfer(msg.sender, pending);
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        user.lastClaim = block.timestamp;
        
        emit RewardClaimed(msg.sender, pending);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");
        
        user.amount = 0;
        user.rewardDebt = 0;
        user.lastClaim = 0;
        
        totalStaked -= amount;
        stakingToken.safeTransfer(msg.sender, amount);
        
        // Update reward rate based on current APY and total staked
        rewardRate = (totalStaked * highAPY) / (100 * 365 days);
        
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

    // Owner functions for maintenance
    function setHighAPY(uint256 _highAPY) external onlyOwner {
        require(_highAPY > 0, "APY must be greater than 0");
        highAPY = _highAPY;
        rewardRate = (totalStaked * highAPY) / (100 * 365 days);
    }

    function setStakingDuration(uint256 _stakingDuration) external onlyOwner {
        stakingDuration = _stakingDuration;
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
