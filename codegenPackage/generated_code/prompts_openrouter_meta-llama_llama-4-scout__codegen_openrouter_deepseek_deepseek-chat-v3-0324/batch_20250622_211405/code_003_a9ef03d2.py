"""
Generated Code Metadata:
========================
Original URL: https://claims-saitachain.pages.dev
Prompt: Develop a simple staking pool contract using Solidity, inspired by the "Staking Pools" feature on SaitaSwap, with a focus on security and ease of use.
Generated: DETERMINISTIC_a9ef03d23ddf08db
Batch ID: 20250622_211405
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

/**
 * @title Simple Staking Pool
 * @dev A contract that allows users to stake ERC20 tokens and earn rewards.
 * Features:
 * - Users can stake tokens and receive staking shares
 * - Rewards are distributed proportionally based on stake amount and duration
 * - Owner can add rewards to the pool
 * - Withdraw staked tokens anytime with a penalty for early withdrawal
 * - Secure against reentrancy attacks
 */
contract StakingPool is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user stake information
    struct UserStake {
        uint256 amount;         // Amount of tokens staked
        uint256 shares;         // Shares representing the stake
        uint256 stakeTime;      // Timestamp when tokens were staked
        uint256 lastClaimTime;  // Timestamp of last reward claim
    }

    // Staking token (ERC20)
    IERC20 public immutable stakingToken;
    
    // Reward token (ERC20)
    IERC20 public immutable rewardToken;

    // Total shares in the pool
    uint256 public totalShares;
    
    // Total staked tokens
    uint256 public totalStaked;
    
    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Minimum stake duration to avoid penalty (in seconds)
    uint256 public minStakeDuration;

    // Early withdrawal penalty (percentage, 100 = 1%)
    uint256 public earlyWithdrawalPenalty;

    // Reward rate (tokens per second per share)
    uint256 public rewardRate;
    
    // Last time reward variables were updated
    uint256 public lastUpdateTime;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Mapping of user addresses to their stake info
    mapping(address => UserStake) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 shares);
    event Withdrawn(address indexed user, uint256 amount, uint256 penalty);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardAdded(uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _minStakeDuration Minimum stake duration in seconds
     * @param _earlyWithdrawalPenalty Early withdrawal penalty percentage (100 = 1%)
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _minStakeDuration,
        uint256 _earlyWithdrawalPenalty
    ) {
        require(_stakingToken != address(0), "Staking token cannot be zero address");
        require(_rewardToken != address(0), "Reward token cannot be zero address");
        require(_earlyWithdrawalPenalty <= 10000, "Penalty cannot exceed 100%");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        minStakeDuration = _minStakeDuration;
        earlyWithdrawalPenalty = _earlyWithdrawalPenalty;
    }

    /**
     * @dev Update pool rewards
     */
    modifier updateRewards() {
        if (totalShares > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            uint256 rewards = timeElapsed * rewardRate;
            accRewardPerShare += (rewards * 1e18) / totalShares;
        }
        lastUpdateTime = block.timestamp;
        _;
    }

    /**
     * @dev Stake tokens into the pool
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateRewards {
        require(amount > 0, "Cannot stake 0");
        
        UserStake storage userStake = userStakes[msg.sender];
        
        // Claim any pending rewards first
        if (userStake.shares > 0) {
            _claimRewards();
        }

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Calculate shares (1:1 for simplicity, can be adjusted)
        uint256 shares = amount;
        
        // Update user stake
        userStake.amount += amount;
        userStake.shares += shares;
        userStake.stakeTime = block.timestamp;
        userStake.lastClaimTime = block.timestamp;

        // Update totals
        totalStaked += amount;
        totalShares += shares;

        emit Staked(msg.sender, amount, shares);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant updateRewards {
        require(amount > 0, "Cannot withdraw 0");
        
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient stake");

        // Claim any pending rewards first
        _claimRewards();

        // Calculate penalty if withdrawing before min duration
        uint256 penalty = 0;
        if (block.timestamp < userStake.stakeTime + minStakeDuration) {
            penalty = (amount * earlyWithdrawalPenalty) / 10000;
        }

        // Calculate amount to actually withdraw
        uint256 withdrawAmount = amount - penalty;

        // Update user stake
        userStake.amount -= amount;
        
        // Calculate shares to remove (1:1 ratio)
        uint256 shares = amount;
        userStake.shares -= shares;

        // Update totals
        totalStaked -= amount;
        totalShares -= shares;

        // Transfer tokens to user
        stakingToken.safeTransfer(msg.sender, withdrawAmount);

        // If penalty, transfer to owner
        if (penalty > 0) {
            stakingToken.safeTransfer(owner(), penalty);
        }

        emit Withdrawn(msg.sender, withdrawAmount, penalty);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant updateRewards {
        _claimRewards();
    }

    /**
     * @dev Internal function to claim rewards
     */
    function _claimRewards() internal {
        UserStake storage userStake = userStakes[msg.sender];
        if (userStake.shares == 0) return;

        uint256 pending = (userStake.shares * accRewardPerShare) / 1e18 - 
                         (userStake.shares * userStake.lastClaimTime) / 1e18;
        
        if (pending > 0) {
            // Update last claim time
            userStake.lastClaimTime = block.timestamp;

            // Transfer rewards
            rewardToken.safeTransfer(msg.sender, pending);
            totalRewardsDistributed += pending;

            emit RewardClaimed(msg.sender, pending);
        }
    }

    /**
     * @dev Add rewards to the pool
     * @param amount Amount of reward tokens to add
     */
    function addRewards(uint256 amount) external onlyOwner updateRewards {
        require(amount > 0, "Cannot add 0 rewards");
        
        rewardToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update reward rate
        if (totalShares > 0) {
            rewardRate = amount / (7 days); // Distribute over 7 days by default
        }

        emit RewardAdded(amount);
    }

    /**
     * @dev Emergency withdraw - withdraw all staked tokens without rewards
     */
    function emergencyWithdraw() external nonReentrant {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");

        uint256 amount = userStake.amount;
        
        // Update totals
        totalStaked -= amount;
        totalShares -= userStake.shares;

        // Reset user stake
        userStake.amount = 0;
        userStake.shares = 0;
        userStake.stakeTime = 0;
        userStake.lastClaimTime = 0;

        // Transfer tokens to user
        stakingToken.safeTransfer(msg.sender, amount);

        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev View function to get pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        User
