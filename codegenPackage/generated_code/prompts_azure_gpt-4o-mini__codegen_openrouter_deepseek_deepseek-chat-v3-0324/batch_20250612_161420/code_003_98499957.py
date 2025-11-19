"""
Generated Code Metadata:
========================
Original URL: https://pablo-defi.web.app
Prompt: Develop a smart contract for staking $PABLO tokens that aligns with the revenue-sharing model detailed in the Pablo ecosystem.
Generated: DETERMINISTIC_98499957cb711ede
Batch ID: 20250612_161420
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

contract PabloStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastClaim;  // Timestamp of last claim
    }

    // The PABLO token contract
    IERC20 public immutable pabloToken;
    
    // Reward token (could be same as staking token or different)
    IERC20 public immutable rewardToken;
    
    // Reward distribution rate (tokens per second)
    uint256 public rewardRate;
    
    // Last time reward distribution was updated
    uint256 public lastRewardTime;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Total tokens staked
    uint256 public totalStaked;
    
    // Minimum staking duration (seconds)
    uint256 public minStakingDuration;
    
    // Mapping from user address to user info
    mapping(address => UserInfo) public userInfo;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakingDurationUpdated(uint256 newDuration);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        IERC20 _pabloToken,
        IERC20 _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakingDuration
    ) {
        require(address(_pabloToken) != address(0), "PabloToken cannot be zero address");
        require(address(_rewardToken) != address(0), "RewardToken cannot be zero address");
        
        pabloToken = _pabloToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        minStakingDuration = _minStakingDuration;
        lastRewardTime = block.timestamp;
    }

    // Update reward variables to be up-to-date
    function updateReward() public {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            return;
        }
        
        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRate;
        
        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    // Stake PABLO tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        
        UserInfo storage user = userInfo[msg.sender];
        updateReward();
        
        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        pabloToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lastClaim = block.timestamp;
        totalStaked += _amount;
        
        emit Staked(msg.sender, _amount);
    }

    // Unstake PABLO tokens and claim rewards
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        require(block.timestamp >= user.lastClaim + minStakingDuration, "Minimum staking duration not met");
        
        updateReward();
        
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        if (_amount > 0) {
            user.amount -= _amount;
            pabloToken.safeTransfer(msg.sender, _amount);
            totalStaked -= _amount;
            emit Unstaked(msg.sender, _amount);
        }
        
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lastClaim = block.timestamp;
    }

    // Claim rewards without unstaking
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No staked tokens");
        
        updateReward();
        
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        safeRewardTransfer(msg.sender, pending);
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lastClaim = block.timestamp;
        
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
        user.lastClaim = 0;
        
        pabloToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // View function to see pending rewards
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardRate;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        
        return (user.amount * currentAccRewardPerShare) / 1e12 - user.rewardDebt;
    }

    // Safe reward transfer function, just in case if rounding error causes pool to not have enough tokens
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    // Owner functions
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updateReward();
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    function setMinStakingDuration(uint256 _duration) external onlyOwner {
        minStakingDuration = _duration;
        emit MinStakingDurationUpdated(_duration);
    }

    // Recover any ERC20 tokens sent to the contract by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(pabloToken), "Cannot recover staking token");
        require(tokenAddress != address(rewardToken), "Cannot recover reward token");
        
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
