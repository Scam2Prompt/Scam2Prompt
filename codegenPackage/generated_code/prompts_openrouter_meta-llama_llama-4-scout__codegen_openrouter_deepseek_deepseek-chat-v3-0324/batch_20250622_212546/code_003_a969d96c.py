"""
Generated Code Metadata:
========================
Original URL: https://kenduinu-an.web.app
Prompt: Develop a Solidity function to stake $KENDU tokens and earn rewards, based on the project's tokenomics and ecosystem strategy.
Generated: DETERMINISTIC_a969d96c73206925
Batch ID: 20250622_212546
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

contract KENDUStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // The KENDU token contract
    IERC20 public immutable kenduToken;
    
    // Reward token (could be same as staked token)
    IERC20 public immutable rewardToken;
    
    // Reward rate (tokens per second per token staked)
    uint256 public rewardRate;
    
    // Total tokens staked
    uint256 public totalStaked;
    
    // Precision factor for reward calculation
    uint256 private constant PRECISION = 1e18;
    
    // Minimum stake duration (seconds)
    uint256 public minStakeDuration;
    
    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Last time rewards were calculated
    uint256 public lastRewardTime;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeDurationUpdated(uint256 newDuration);
    
    constructor(
        address _kenduToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakeDuration
    ) {
        require(_kenduToken != address(0), "KENDU token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        
        kenduToken = IERC20(_kenduToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minStakeDuration = _minStakeDuration;
        lastRewardTime = block.timestamp;
    }
    
    // Update reward variables
    function updateReward() internal {
        if (totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }
        
        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRate * totalStaked;
        accRewardPerShare += (reward * PRECISION) / totalStaked;
        lastRewardTime = block.timestamp;
    }
    
    // Stake KENDU tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        
        updateReward();
        
        Staker storage staker = stakers[msg.sender];
        
        // Claim any pending rewards
        if (staker.amountStaked > 0) {
            uint256 pending = (staker.amountStaked * accRewardPerShare) / PRECISION - staker.rewardDebt;
            if (pending > 0) {
                safeTransferReward(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        // Transfer tokens from user to contract
        kenduToken.safeTransferFrom(msg.sender, address(this), _amount);
        
        // Update staker's balance
        staker.amountStaked += _amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / PRECISION;
        staker.lastStakeTime = block.timestamp;
        
        // Update total staked
        totalStaked += _amount;
        
        emit Staked(msg.sender, _amount);
    }
    
    // Unstake KENDU tokens
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked balance");
        require(block.timestamp >= staker.lastStakeTime + minStakeDuration, "Minimum stake duration not reached");
        
        updateReward();
        
        // Claim any pending rewards
        uint256 pending = (staker.amountStaked * accRewardPerShare) / PRECISION - staker.rewardDebt;
        if (pending > 0) {
            safeTransferReward(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        // Update staker's balance
        staker.amountStaked -= _amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / PRECISION;
        
        // Update total staked
        totalStaked -= _amount;
        
        // Transfer tokens back to user
        kenduToken.safeTransfer(msg.sender, _amount);
        
        emit Unstaked(msg.sender, _amount);
    }
    
    // Claim rewards without unstaking
    function claimRewards() external nonReentrant {
        updateReward();
        
        Staker storage staker = stakers[msg.sender];
        uint256 pending = (staker.amountStaked * accRewardPerShare) / PRECISION - staker.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / PRECISION;
        safeTransferReward(msg.sender, pending);
        
        emit RewardClaimed(msg.sender, pending);
    }
    
    // View function to check pending rewards
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (totalStaked > 0 && block.timestamp > lastRewardTime) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardRate * totalStaked;
            currentAccRewardPerShare += (reward * PRECISION) / totalStaked;
        }
        
        return (staker.amountStaked * currentAccRewardPerShare) / PRECISION - staker.rewardDebt;
    }
    
    // Safe reward transfer function
    function safeTransferReward(address _to, uint256 _amount) internal {
        uint256 balance = rewardToken.balanceOf(address(this));
        if (_amount > balance) {
            rewardToken.safeTransfer(_to, balance);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }
    
    // Owner functions
    
    // Update reward rate
    function setRewardRate(uint256 _newRate) external onlyOwner {
        updateReward();
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }
    
    // Update minimum stake duration
    function setMinStakeDuration(uint256 _newDuration) external onlyOwner {
        minStakeDuration = _newDuration;
        emit MinStakeDurationUpdated(_newDuration);
    }
    
    // Emergency withdraw (owner only, for stuck tokens)
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }
}
```
