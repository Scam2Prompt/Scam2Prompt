"""
Generated Code Metadata:
========================
Original URL: https://doge-coin20.pages.dev
Prompt: Write a smart contract in Solidity for a staking system that distributes rewards to stakers over a period of two years, similar to Dogecoin20's staking mechanism.
Generated: DETERMINISTIC_f0c3d11f271cc2dc
Batch ID: 20250622_210348
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

contract StakingRewards is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastClaimTime;
    }

    // The staking token
    IERC20 public stakingToken;
    // The reward token
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;
    // Total rewards distributed
    uint256 public totalRewardsDistributed;
    // Total rewards allocated for distribution
    uint256 public totalRewardsAllocated;

    // Staking start time
    uint256 public startTime;
    // Staking end time (2 years from start)
    uint256 public endTime;

    // Reward rate per second
    uint256 public rewardRate;
    // Last time reward distribution was calculated
    uint256 public lastUpdateTime;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Precision factor for reward calculation
    uint256 private constant PRECISION = 1e18;

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardsDeposited(uint256 amount);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _totalRewardsAllocated,
        uint256 _startTime
    ) {
        require(_stakingToken != address(0), "Staking token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_totalRewardsAllocated > 0, "Rewards must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        totalRewardsAllocated = _totalRewardsAllocated;
        startTime = _startTime;
        endTime = _startTime + 730 days; // 2 years in seconds
        rewardRate = _totalRewardsAllocated / (730 days);
    }

    // Modifier to check if staking period is active
    modifier isStakingActive() {
        require(block.timestamp >= startTime, "Staking has not started yet");
        require(block.timestamp <= endTime, "Staking period has ended");
        _;
    }

    // Update reward variables
    function updateReward() internal {
        if (block.timestamp <= lastUpdateTime || totalStaked == 0) {
            return;
        }

        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        uint256 rewards = timeElapsed * rewardRate;

        // Ensure we don't distribute more than allocated
        if (totalRewardsDistributed + rewards > totalRewardsAllocated) {
            rewards = totalRewardsAllocated - totalRewardsDistributed;
        }

        accRewardPerShare += (rewards * PRECISION) / totalStaked;
        lastUpdateTime = block.timestamp;
        totalRewardsDistributed += rewards;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant isStakingActive {
        require(amount > 0, "Amount must be greater than zero");

        updateReward();

        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            uint256 pending = (userStake.amount * accRewardPerShare) / PRECISION - userStake.rewardDebt;
            if (pending > 0) {
                safeTransferReward(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        totalStaked += amount;
        userStake.amount += amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / PRECISION;
        userStake.lastClaimTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        updateReward();

        uint256 pending = (userStake.amount * accRewardPerShare) / PRECISION - userStake.rewardDebt;
        if (pending > 0) {
            safeTransferReward(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        totalStaked -= amount;
        userStake.amount -= amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / PRECISION;
        userStake.lastClaimTime = block.timestamp;

        stakingToken.safeTransfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");

        updateReward();

        uint256 pending = (userStake.amount * accRewardPerShare) / PRECISION - userStake.rewardDebt;
        require(pending > 0, "No rewards to claim");

        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / PRECISION;
        userStake.lastClaimTime = block.timestamp;

        safeTransferReward(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    // Safe reward transfer function
    function safeTransferReward(address to, uint256 amount) internal {
        uint256 balance = rewardToken.balanceOf(address(this));
        if (amount > balance) {
            rewardToken.safeTransfer(to, balance);
        } else {
            rewardToken.safeTransfer(to, amount);
        }
    }

    // Deposit rewards (only owner)
    function depositRewards(uint256 amount) external onlyOwner {
        require(block.timestamp < endTime, "Staking period has ended");
        rewardToken.safeTransferFrom(msg.sender, address(this), amount);
        totalRewardsAllocated += amount;
        emit RewardsDeposited(amount);
    }

    // Get pending rewards for a user
    function pendingRewards(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.timestamp > lastUpdateTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            uint256 rewards = timeElapsed * rewardRate;
            
            // Ensure we don't distribute more than allocated
            if (totalRewardsDistributed + rewards > totalRewardsAllocated) {
                rewards = totalRewardsAllocated - totalRewardsDistributed;
            }
            
            currentAccRewardPerShare += (rewards * PRECISION) / totalStaked;
        }

        return (userStake.amount * currentAccRewardPerShare) / PRECISION - userStake.rewardDebt;
    }

    // Emergency withdraw (only owner)
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        rewardToken.safeTransfer(owner(), balance);
    }
}
```
