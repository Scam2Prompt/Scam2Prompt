"""
Generated Code Metadata:
========================
Original URL: https://testai-qhn.pages.dev
Prompt: Write a smart contract in Solidity for staking AITECH tokens with customizable lock terms and tier-based reward boosts, similar to the staking pools described on the Solidus AI Tech platform.
Generated: DETERMINISTIC_a13e3b5aa2dc4eea
Batch ID: 20250612_152656
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

contract AITECHStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staking position
    struct Stake {
        uint256 amount;
        uint256 lockTerm;
        uint256 startTime;
        uint256 rewardDebt;
        uint256 boostMultiplier;
        bool isActive;
    }

    // Struct for lock term options
    struct LockTermOption {
        uint256 duration;
        uint256 rewardMultiplier; // Multiplier in basis points (10000 = 1x)
    }

    // Struct for tier options
    struct Tier {
        uint256 minAmount;
        uint256 boostMultiplier; // Multiplier in basis points (10000 = 1x)
    }

    IERC20 public immutable stakingToken;
    IERC20 public immutable rewardToken;

    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardPerSecond;
    uint256 public lastRewardTime;
    uint256 public accRewardPerShare;
    uint256 public constant PRECISION_FACTOR = 1e12;

    // Lock term options
    LockTermOption[] public lockTermOptions;
    // Tier options
    Tier[] public tiers;

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockTerm, uint256 boostMultiplier);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 amount);
    event LockTermOptionAdded(uint256 duration, uint256 rewardMultiplier);
    event LockTermOptionUpdated(uint256 index, uint256 duration, uint256 rewardMultiplier);
    event TierAdded(uint256 minAmount, uint256 boostMultiplier);
    event TierUpdated(uint256 index, uint256 minAmount, uint256 boostMultiplier);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerSecond
    ) {
        require(address(_stakingToken) != address(0), "Invalid staking token");
        require(address(_rewardToken) != address(0), "Invalid reward token");
        
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerSecond = _rewardPerSecond;
        lastRewardTime = block.timestamp;

        // Initialize default lock term options
        lockTermOptions.push(LockTermOption(30 days, 10000)); // 1x for 30 days
        lockTermOptions.push(LockTermOption(90 days, 12000)); // 1.2x for 90 days
        lockTermOptions.push(LockTermOption(180 days, 15000)); // 1.5x for 180 days

        // Initialize default tiers
        tiers.push(Tier(1000 ether, 10000)); // 1x for >= 1000 tokens
        tiers.push(Tier(5000 ether, 11000)); // 1.1x for >= 5000 tokens
        tiers.push(Tier(10000 ether, 12500)); // 1.25x for >= 10000 tokens
    }

    // Update reward variables
    function updatePool() internal {
        if (block.timestamp <= lastRewardTime) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardPerSecond;
        accRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    // Stake tokens with selected lock term
    function stake(uint256 _amount, uint256 _lockTermIndex) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(_lockTermIndex < lockTermOptions.length, "Invalid lock term index");

        updatePool();

        LockTermOption memory lockTerm = lockTermOptions[_lockTermIndex];
        uint256 boostMultiplier = calculateBoostMultiplier(_amount);

        // Transfer tokens from user
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Create new stake
        userStakes[msg.sender].push(Stake({
            amount: _amount,
            lockTerm: lockTerm.duration,
            startTime: block.timestamp,
            rewardDebt: (_amount * accRewardPerShare) / PRECISION_FACTOR,
            boostMultiplier: boostMultiplier * lockTerm.rewardMultiplier / 10000,
            isActive: true
        }));

        totalStaked += _amount;

        emit Staked(msg.sender, _amount, lockTerm.duration, boostMultiplier * lockTerm.rewardMultiplier / 10000);
    }

    // Unstake tokens and claim rewards
    function unstake(uint256 _stakeIndex) external nonReentrant {
        require(_stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][_stakeIndex];
        require(userStake.isActive, "Stake already withdrawn");
        require(block.timestamp >= userStake.startTime + userStake.lockTerm, "Lock term not expired");

        updatePool();

        uint256 pendingReward = ((userStake.amount * accRewardPerShare) / PRECISION_FACTOR) - userStake.rewardDebt;
        uint256 boostedReward = (pendingReward * userStake.boostMultiplier) / 10000;

        // Transfer staked tokens and rewards
        stakingToken.safeTransfer(msg.sender, userStake.amount);
        if (boostedReward > 0) {
            rewardToken.safeTransfer(msg.sender, boostedReward);
        }

        totalStaked -= userStake.amount;
        userStake.isActive = false;

        emit Unstaked(msg.sender, userStake.amount, boostedReward);
    }

    // Claim rewards without unstaking
    function claimRewards(uint256 _stakeIndex) external nonReentrant {
        require(_stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][_stakeIndex];
        require(userStake.isActive, "Stake not active");

        updatePool();

        uint256 pendingReward = ((userStake.amount * accRewardPerShare) / PRECISION_FACTOR) - userStake.rewardDebt;
        uint256 boostedReward = (pendingReward * userStake.boostMultiplier) / 10000;

        if (boostedReward > 0) {
            rewardToken.safeTransfer(msg.sender, boostedReward);
            userStake.rewardDebt = (userStake.amount * accRewardPerShare) / PRECISION_FACTOR;
            emit RewardClaimed(msg.sender, boostedReward);
        }
    }

    // Calculate boost multiplier based on staked amount and tiers
    function calculateBoostMultiplier(uint256 _amount) internal view returns (uint256) {
        uint256 multiplier = 10000; // Default 1x

        for (uint256 i = tiers.length; i > 0; i--) {
            if (_amount >= tiers[i - 1].minAmount) {
                multiplier = tiers[i - 1].boostMultiplier;
                break;
            }
        }

        return multiplier;
    }

    // View function to get pending rewards for a stake
    function pendingRewards(address _user, uint256 _stakeIndex) external view returns (uint256) {
        require(_stakeIndex < userStakes[_user].length, "Invalid stake index");
        Stake memory userStake = userStakes[_user][_stakeIndex];
        if (!userStake.isActive) {
            return 0;
        }

        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardPerSecond;
            currentAccRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        }

        uint256 pending = ((userStake.amount * currentAccRewardPerShare) / PRECISION_FACTOR) - userStake.rewardDebt;
