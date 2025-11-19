"""
Generated Code Metadata:
========================
Original URL: https://rabbittherious.pages.dev
Prompt: Write a smart contract in Solidity for staking tokens, inspired by the functionality described on the "Rious The Rabbit" website.
Generated: DETERMINISTIC_d53ecf2b25d13f65
Batch ID: 20250612_152906
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

contract RiousStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staking position
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // The staking token
    IERC20 public stakingToken;
    
    // The reward token
    IERC20 public rewardToken;
    
    // Reward rate per second
    uint256 public rewardRate;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Last time rewards were calculated
    uint256 public lastRewardTime;
    
    // Minimum stake duration in seconds
    uint256 public minStakeDuration;
    
    // Early unstake penalty percentage (100 = 1%)
    uint256 public earlyUnstakePenalty;
    
    // Penalty collector address
    address public penaltyCollector;
    
    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdrawn(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeDurationUpdated(uint256 newDuration);
    event EarlyUnstakePenaltyUpdated(uint256 newPenalty);
    event PenaltyCollectorUpdated(address newCollector);
    
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakeDuration,
        uint256 _earlyUnstakePenalty,
        address _penaltyCollector
    ) {
        require(address(_stakingToken) != address(0), "Staking token cannot be zero address");
        require(address(_rewardToken) != address(0), "Reward token cannot be zero address");
        require(_penaltyCollector != address(0), "Penalty collector cannot be zero address");
        
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        minStakeDuration = _minStakeDuration;
        earlyUnstakePenalty = _earlyUnstakePenalty;
        penaltyCollector = _penaltyCollector;
        lastRewardTime = block.timestamp;
    }
    
    // Update reward variables
    function updateReward() internal {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            return;
        }
        
        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRate;
        
        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardTime = block.timestamp;
    }
    
    // Stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        
        updateReward();
        
        Stake storage userStake = stakes[msg.sender];
        
        if (userStake.amount > 0) {
            uint256 pending = (userStake.amount * accRewardPerShare) / 1e12 - userStake.rewardDebt;
            if (pending > 0) {
                safeTransferReward(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        userStake.amount += amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e12;
        userStake.lastStakeTime = block.timestamp;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    // Unstake tokens and claim rewards
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        
        updateReward();
        
        uint256 amount = userStake.amount;
        uint256 pending = (amount * accRewardPerShare) / 1e12 - userStake.rewardDebt;
        
        // Check if early unstake
        bool isEarly = block.timestamp < userStake.lastStakeTime + minStakeDuration;
        uint256 penalty = 0;
        
        if (isEarly && earlyUnstakePenalty > 0) {
            penalty = (amount * earlyUnstakePenalty) / 10000;
            amount -= penalty;
            
            if (penalty > 0) {
                stakingToken.safeTransfer(penaltyCollector, penalty);
            }
        }
        
        // Transfer staked tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);
        
        // Transfer rewards if any
        if (pending > 0) {
            safeTransferReward(msg.sender, pending);
        }
        
        totalStaked -= userStake.amount;
        delete stakes[msg.sender];
        
        emit Unstaked(msg.sender, amount, pending);
    }
    
    // Claim rewards without unstaking
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to claim rewards from");
        
        updateReward();
        
        uint256 pending = (userStake.amount * accRewardPerShare) / 1e12 - userStake.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e12;
        safeTransferReward(msg.sender, pending);
        
        emit RewardClaimed(msg.sender, pending);
    }
    
    // Emergency withdraw without rewards
    function emergencyWithdraw() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");
        
        uint256 amount = userStake.amount;
        totalStaked -= amount;
        delete stakes[msg.sender];
        
        stakingToken.safeTransfer(msg.sender, amount);
        
        emit EmergencyWithdrawn(msg.sender, amount);
    }
    
    // Safe reward transfer function
    function safeTransferReward(address to, uint256 amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (amount > rewardBalance) {
            rewardToken.safeTransfer(to, rewardBalance);
        } else {
            rewardToken.safeTransfer(to, amount);
        }
    }
    
    // Owner functions
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updateReward();
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }
    
    function setMinStakeDuration(uint256 _minStakeDuration) external onlyOwner {
        minStakeDuration = _minStakeDuration;
        emit MinStakeDurationUpdated(_minStakeDuration);
    }
    
    function setEarlyUnstakePenalty(uint256 _earlyUnstakePenalty) external onlyOwner {
        require(_earlyUnstakePenalty <= 10000, "Penalty cannot exceed 100%");
        earlyUnstakePenalty = _earlyUnstakePenalty;
        emit EarlyUnstakePenaltyUpdated(_earlyUnstakePenalty);
    }
    
    function setPenaltyCollector(address _penaltyCollector) external onlyOwner {
        require(_penaltyCollector != address(0), "Penalty collector cannot be zero address");
        penaltyCollector = _penaltyCollector;
        emit PenaltyCollectorUpdated(_penaltyCollector);
    }
    
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot recover staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
    
    // View functions
    function pendingRewards(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        
        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256
