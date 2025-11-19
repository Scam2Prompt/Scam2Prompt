"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Write a smart contract in Solidity for a staking pool that operates on the Linea network, supports compounding rewards, and adjusts investor tiers based on staking duration, similar to the pools described on SidusPad.
Generated: DETERMINISTIC_4d26f8820ab267d3
Batch ID: 20250612_152235
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

contract SidusStakingPool is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Structs
    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
        uint256 tier;
    }

    struct PoolInfo {
        IERC20 stakingToken;
        IERC20 rewardToken;
        uint256 allocPoint;
        uint256 lastRewardBlock;
        uint256 accRewardPerShare;
        uint256 totalStaked;
    }

    // Constants
    uint256 public constant TIER_1_DURATION = 30 days;
    uint256 public constant TIER_2_DURATION = 90 days;
    uint256 public constant TIER_3_DURATION = 180 days;
    
    uint256 public constant TIER_1_MULTIPLIER = 100; // 1x
    uint256 public constant TIER_2_MULTIPLIER = 120; // 1.2x
    uint256 public constant TIER_3_MULTIPLIER = 150; // 1.5x

    // Variables
    PoolInfo public pool;
    uint256 public rewardPerBlock;
    uint256 public startBlock;
    uint256 public endBlock;

    mapping(address => UserInfo) public userInfo;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TierUpgraded(address indexed user, uint256 newTier);

    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) {
        require(_startBlock >= block.number, "Start block must be in future");
        require(_endBlock > _startBlock, "End block must be after start block");

        pool.stakingToken = _stakingToken;
        pool.rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;

        pool.lastRewardBlock = _startBlock;
    }

    // Update reward variables of the pool
    function updatePool() public {
        if (block.number <= pool.lastRewardBlock) {
            return;
        }

        if (pool.totalStaked == 0) {
            pool.lastRewardBlock = block.number;
            return;
        }

        uint256 multiplier = getMultiplier(pool.lastRewardBlock, block.number);
        uint256 reward = multiplier * rewardPerBlock;
        pool.accRewardPerShare += (reward * 1e12) / pool.totalStaked;
        pool.lastRewardBlock = block.number;
    }

    // Get multiplier based on blocks
    function getMultiplier(uint256 _from, uint256 _to) public view returns (uint256) {
        if (_to <= endBlock) {
            return _to - _from;
        } else if (_from >= endBlock) {
            return 0;
        } else {
            return endBlock - _from;
        }
    }

    // Stake tokens
    function deposit(uint256 _amount) external nonReentrant {
        require(block.number >= startBlock, "Pool not started");
        require(block.number < endBlock, "Pool ended");
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        pool.stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;
        user.lastStakeTime = block.timestamp;
        pool.totalStaked += _amount;

        emit Deposit(msg.sender, _amount);
    }

    // Withdraw staked tokens and claim rewards
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        if (_amount > 0) {
            user.amount -= _amount;
            pool.stakingToken.safeTransfer(msg.sender, _amount);
            pool.totalStaked -= _amount;
        }

        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;
        emit Withdraw(msg.sender, _amount);
    }

    // Emergency withdraw without claiming rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        user.amount = 0;
        user.rewardDebt = 0;
        pool.totalStaked -= amount;

        pool.stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // Claim rewards without withdrawing staked tokens
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;
        safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    // Update user tier based on staking duration
    function updateTier(address _user) public {
        UserInfo storage user = userInfo[_user];
        if (user.amount == 0) return;

        uint256 stakingDuration = block.timestamp - user.lastStakeTime;
        uint256 newTier;

        if (stakingDuration >= TIER_3_DURATION) {
            newTier = 3;
        } else if (stakingDuration >= TIER_2_DURATION) {
            newTier = 2;
        } else if (stakingDuration >= TIER_1_DURATION) {
            newTier = 1;
        } else {
            newTier = 0;
        }

        if (newTier > user.tier) {
            user.tier = newTier;
            emit TierUpgraded(_user, newTier);
        }
    }

    // Get pending rewards for a user
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 accRewardPerShare = pool.accRewardPerShare;
        uint256 stakedSupply = pool.totalStaked;

        if (block.number > pool.lastRewardBlock && stakedSupply != 0) {
            uint256 multiplier = getMultiplier(pool.lastRewardBlock, block.number);
            uint256 reward = multiplier * rewardPerBlock;
            accRewardPerShare += (reward * 1e12) / stakedSupply;
        }

        return (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
    }

    // Get user tier multiplier
    function getUserMultiplier(address _user) public view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        if (user.tier == 1) return TIER_1_MULTIPLIER;
        if (user.tier == 2) return TIER_2_MULTIPLIER;
        if (user.tier == 3) return TIER_3_MULTIPLIER;
        return 100; // Default 1x
    }

    // Safe reward transfer function
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = pool.rewardToken.balanceOf(address(this));
        if
