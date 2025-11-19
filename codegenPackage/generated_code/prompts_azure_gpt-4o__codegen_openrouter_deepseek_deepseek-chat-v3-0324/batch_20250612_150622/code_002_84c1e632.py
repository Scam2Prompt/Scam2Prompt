"""
Generated Code Metadata:
========================
Original URL: https://kabosu-bsc.pages.dev
Prompt: Create a smart contract in Solidity that implements Kabosu token staking functionality, referencing the staking mechanism planned in Phase 2 of the roadmap.
Generated: DETERMINISTIC_84c1e632e81adf02
Batch ID: 20250612_150622
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

contract KabosuStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakeTime;
        uint256 pendingRewards;
    }

    // The Kabosu token contract
    IERC20 public immutable kabosuToken;
    
    // The reward token contract (could be same as staking token)
    IERC20 public immutable rewardToken;
    
    // Reward rate per second per token staked
    uint256 public rewardRate;
    
    // Total amount currently staked
    uint256 public totalStaked;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Last time rewards were calculated
    uint256 public lastRewardTime;
    
    // Minimum staking duration (in seconds)
    uint256 public minStakeDuration;
    
    // Early unstake penalty (percentage)
    uint256 public earlyUnstakePenalty;
    
    // Precision factor for reward calculations
    uint256 private constant PRECISION = 1e18;
    
    // Mapping of stakers to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeDurationUpdated(uint256 newDuration);
    event EarlyUnstakePenaltyUpdated(uint256 newPenalty);

    constructor(
        address _kabosuToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakeDuration,
        uint256 _earlyUnstakePenalty
    ) {
        require(_kabosuToken != address(0), "Invalid Kabosu token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_minStakeDuration > 0, "Min stake duration must be > 0");
        require(_earlyUnstakePenalty <= 100, "Penalty cannot exceed 100%");

        kabosuToken = IERC20(_kabosuToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minStakeDuration = _minStakeDuration;
        earlyUnstakePenalty = _earlyUnstakePenalty;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Updates the reward variables
     */
    function updateReward() internal {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRate * totalStaked;
        accRewardPerShare += (reward * PRECISION) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Stakes Kabosu tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        
        updateReward();
        
        Staker storage staker = stakers[msg.sender];
        
        if (staker.amountStaked > 0) {
            uint256 pending = (staker.amountStaked * accRewardPerShare) / PRECISION - staker.rewardDebt;
            if (pending > 0) {
                staker.pendingRewards += pending;
            }
        }
        
        kabosuToken.safeTransferFrom(msg.sender, address(this), amount);
        staker.amountStaked += amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / PRECISION;
        staker.lastStakeTime = block.timestamp;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes Kabosu tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0 tokens");
        
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked balance");
        
        updateReward();
        
        // Calculate pending rewards
        uint256 pending = (staker.amountStaked * accRewardPerShare) / PRECISION - staker.rewardDebt;
        if (pending > 0) {
            staker.pendingRewards += pending;
        }
        
        // Check if unstaking before minimum duration
        bool isEarly = block.timestamp < staker.lastStakeTime + minStakeDuration;
        
        // Calculate penalty if early unstake
        uint256 penalty = 0;
        if (isEarly) {
            penalty = (amount * earlyUnstakePenalty) / 100;
            amount -= penalty;
        }
        
        // Update staker info
        staker.amountStaked -= (amount + penalty);
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / PRECISION;
        totalStaked -= (amount + penalty);
        
        // Transfer tokens back to user
        kabosuToken.safeTransfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claims accumulated rewards
     */
    function claimRewards() external nonReentrant {
        updateReward();
        
        Staker storage staker = stakers[msg.sender];
        
        uint256 pending = (staker.amountStaked * accRewardPerShare) / PRECISION - staker.rewardDebt;
        if (pending > 0 || staker.pendingRewards > 0) {
            uint256 totalRewards = pending + staker.pendingRewards;
            staker.pendingRewards = 0;
            staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / PRECISION;
            
            rewardToken.safeTransfer(msg.sender, totalRewards);
            emit RewardClaimed(msg.sender, totalRewards);
        }
    }

    /**
     * @dev Calculates pending rewards for a user
     * @param user The address of the user
     * @return pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardRate * totalStaked;
            currentAccRewardPerShare += (reward * PRECISION) / totalStaked;
        }
        
        return staker.pendingRewards + 
               ((staker.amountStaked * currentAccRewardPerShare) / PRECISION - staker.rewardDebt);
    }

    // Admin functions

    /**
     * @dev Updates the reward rate
     * @param newRate The new reward rate per second per token
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        updateReward();
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Updates the minimum stake duration
     * @param newDuration The new minimum duration in seconds
     */
    function setMinStakeDuration(uint256 newDuration) external onlyOwner {
        require(newDuration > 0, "Duration must be > 0");
        minStakeDuration = newDuration;
        emit MinStakeDurationUpdated(newDuration);
    }

    /**
     * @dev Updates the early unstake penalty
     * @param newPenalty The new penalty percentage (0-100)
     */
    function setEarlyUnstakePenalty(uint256 newPenalty) external onlyOwner {
        require(newPenalty <= 100, "Penalty cannot exceed 100%");
        earlyUnstakePenalty = newPenalty;
        emit EarlyUnstakePenaltyUpdated(newPenalty);
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress The address of the token to recover
     * @param amount The amount to recover
