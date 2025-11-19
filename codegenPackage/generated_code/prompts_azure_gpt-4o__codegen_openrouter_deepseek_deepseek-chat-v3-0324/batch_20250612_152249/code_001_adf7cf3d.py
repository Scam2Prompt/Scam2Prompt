"""
Generated Code Metadata:
========================
Original URL: https://feg-chain.pages.dev
Prompt: Generate code to implement the FEG SmartDeFi™ Staking Protocol for a token, including asset-backing and smart lending features, and ensure it works seamlessly on both BSC and ETH chains.
Generated: DETERMINISTIC_adf7cf3d5bdc12ae
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FEG SmartDeFi Staking Protocol
 * @dev Implements asset-backed staking with smart lending features
 * Works on both BSC and ETH chains
 */
contract FEGSmartDeFiStaking is ReentrancyGuard, Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Struct to store user staking details
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
        uint256 unlockTime;
    }

    // Token addresses
    IERC20 public stakingToken;
    IERC20 public rewardToken;
    IERC20 public assetBackingToken;

    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardPerBlock;
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare;
    uint256 public stakingLockDuration;
    uint256 public earlyUnstakePenalty; // Percentage (e.g., 10 for 10%)

    // Lending parameters
    uint256 public totalLent;
    uint256 public lendingInterestRate; // APR percentage
    uint256 public maxLendingRatio; // Max percentage of staked tokens that can be lent

    // Mappings
    mapping(address => Stake) public stakes;
    mapping(address => uint256) public borrowedAmounts;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TokensLent(address indexed borrower, uint256 amount);
    event TokensRepaid(address indexed borrower, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract
     * @param _stakingToken Address of the token to be staked
     * @param _rewardToken Address of the reward token
     * @param _assetBackingToken Address of the asset backing token
     * @param _rewardPerBlock Reward tokens per block
     * @param _stakingLockDuration Duration staked tokens are locked (in seconds)
     * @param _earlyUnstakePenalty Penalty for early unstaking (percentage)
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        address _assetBackingToken,
        uint256 _rewardPerBlock,
        uint256 _stakingLockDuration,
        uint256 _earlyUnstakePenalty
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_assetBackingToken != address(0), "Invalid backing token address");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        assetBackingToken = IERC20(_assetBackingToken);
        rewardPerBlock = _rewardPerBlock;
        stakingLockDuration = _stakingLockDuration;
        earlyUnstakePenalty = _earlyUnstakePenalty;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update the staking pool with any pending rewards
     */
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksPassed = block.number.sub(lastRewardBlock);
        uint256 reward = blocksPassed.mul(rewardPerBlock);
        
        // Ensure we don't distribute more rewards than available
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (reward > rewardBalance) {
            reward = rewardBalance;
        }

        accRewardPerShare = accRewardPerShare.add(reward.mul(1e12).div(totalStaked));
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");

        updatePool();

        Stake storage userStake = stakes[msg.sender];
        
        // Claim any pending rewards first
        if (userStake.amount > 0) {
            uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e12).sub(userStake.rewardDebt);
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        // Transfer tokens from user
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update user stake
        userStake.amount = userStake.amount.add(amount);
        userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e12);
        userStake.lastStakeTime = block.timestamp;
        userStake.unlockTime = block.timestamp.add(stakingLockDuration);

        // Update total staked
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked balance");

        updatePool();

        // Claim any pending rewards
        uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e12).sub(userStake.rewardDebt);
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        // Check if unstaking before unlock time
        uint256 penaltyAmount = 0;
        if (block.timestamp < userStake.unlockTime) {
            penaltyAmount = amount.mul(earlyUnstakePenalty).div(100);
            amount = amount.sub(penaltyAmount);
        }

        // Update user stake
        userStake.amount = userStake.amount.sub(amount.add(penaltyAmount));
        userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e12);

        // Update total staked
        totalStaked = totalStaked.sub(amount.add(penaltyAmount));

        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);

        // Burn or redistribute penalty
        if (penaltyAmount > 0) {
            stakingToken.safeTransfer(address(0xdead), penaltyAmount);
        }

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");

        updatePool();

        uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e12).sub(userStake.rewardDebt);
        require(pending > 0, "No rewards to claim");

        userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e12);
        safeRewardTransfer(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Lend staked tokens to borrowers (only owner)
     * @param borrower Address of the borrower
     * @param amount Amount to lend
     */
    function lendTokens(address borrower, uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot lend 0 tokens");
        require(totalStaked > 0, "No staked tokens available");
        
        uint256 availableToLend = totalStaked.mul(maxLendingRatio).div(100);
        require(totalLent.add(amount) <= availableToLend, "Exceeds max lending ratio");

        stakingToken.safeTransfer(borrower, amount);
        borrowedAmounts[borrower] = borrowedAmounts[borrower].add(amount);
        totalLent = totalLent.add(amount);

        emit TokensLent(borrower, amount);
    }

    /**
     * @dev
