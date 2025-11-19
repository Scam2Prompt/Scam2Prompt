"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Create a smart contract to enforce lengthy lock-up periods for liquidity providers, incorporating incentives for long-term ecosystem participation.
Generated: DETERMINISTIC_79f121062213b4ec
Batch ID: 20250612_155028
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LiquidityLockup
 * @dev A contract to enforce lock-up periods for liquidity providers with incentives
 */
contract LiquidityLockup is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Struct to store lock-up details
    struct Lockup {
        uint256 amount;
        uint256 unlockTime;
        uint256 rewardMultiplier;
        bool claimed;
    }

    // Token to be locked
    IERC20 public immutable lockToken;
    
    // Reward token (can be same as lockToken)
    IERC20 public immutable rewardToken;

    // Minimum lock period in seconds (e.g., 30 days = 2592000)
    uint256 public immutable minLockPeriod;

    // Maximum lock period in seconds
    uint256 public immutable maxLockPeriod;

    // Base reward rate per second (scaled by 1e18)
    uint256 public rewardRate;

    // Mapping from user address to their lockups
    mapping(address => Lockup[]) public userLockups;

    // Total locked amount
    uint256 public totalLocked;

    // Events
    event Locked(address indexed user, uint256 amount, uint256 unlockTime, uint256 rewardMultiplier);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor
     * @param _lockToken Address of token to be locked
     * @param _rewardToken Address of reward token
     * @param _minLockPeriod Minimum lock period in seconds
     * @param _maxLockPeriod Maximum lock period in seconds
     * @param _initialRewardRate Initial reward rate per second (scaled by 1e18)
     */
    constructor(
        address _lockToken,
        address _rewardToken,
        uint256 _minLockPeriod,
        uint256 _maxLockPeriod,
        uint256 _initialRewardRate
    ) {
        require(_lockToken != address(0), "Invalid lock token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_minLockPeriod > 0, "Min lock period must be > 0");
        require(_maxLockPeriod > _minLockPeriod, "Max lock period must be > min");

        lockToken = IERC20(_lockToken);
        rewardToken = IERC20(_rewardToken);
        minLockPeriod = _minLockPeriod;
        maxLockPeriod = _maxLockPeriod;
        rewardRate = _initialRewardRate;
    }

    /**
     * @dev Lock tokens for a specified duration
     * @param amount Amount of tokens to lock
     * @param lockDuration Duration in seconds to lock tokens
     */
    function lockTokens(uint256 amount, uint256 lockDuration) external nonReentrant {
        require(amount > 0, "Amount must be > 0");
        require(lockDuration >= minLockPeriod, "Lock duration too short");
        require(lockDuration <= maxLockPeriod, "Lock duration too long");

        // Calculate reward multiplier based on lock duration
        uint256 rewardMultiplier = calculateRewardMultiplier(lockDuration);

        // Transfer tokens from user to contract
        lockToken.safeTransferFrom(msg.sender, address(this), amount);

        // Calculate unlock time
        uint256 unlockTime = block.timestamp.add(lockDuration);

        // Create new lockup
        userLockups[msg.sender].push(Lockup({
            amount: amount,
            unlockTime: unlockTime,
            rewardMultiplier: rewardMultiplier,
            claimed: false
        }));

        totalLocked = totalLocked.add(amount);

        emit Locked(msg.sender, amount, unlockTime, rewardMultiplier);
    }

    /**
     * @dev Withdraw locked tokens and claim rewards
     * @param lockIndex Index of the lockup to withdraw
     */
    function withdraw(uint256 lockIndex) external nonReentrant {
        require(lockIndex < userLockups[msg.sender].length, "Invalid lock index");

        Lockup storage lockup = userLockups[msg.sender][lockIndex];
        require(!lockup.claimed, "Already claimed");
        require(block.timestamp >= lockup.unlockTime, "Tokens still locked");

        // Calculate reward
        uint256 reward = calculateReward(
            lockup.amount,
            lockup.unlockTime.sub(lockup.unlockTime.sub(lockup.unlockTime)),
            lockup.rewardMultiplier
        );

        // Mark as claimed
        lockup.claimed = true;
        totalLocked = totalLocked.sub(lockup.amount);

        // Transfer locked tokens
        lockToken.safeTransfer(msg.sender, lockup.amount);

        // Transfer rewards if any
        if (reward > 0) {
            rewardToken.safeTransfer(msg.sender, reward);
        }

        emit Withdrawn(msg.sender, lockup.amount, reward);
    }

    /**
     * @dev Calculate reward for a lockup
     * @param amount Locked amount
     * @param lockDuration Actual locked duration
     * @param rewardMultiplier Multiplier based on lock duration
     * @return reward Calculated reward amount
     */
    function calculateReward(
        uint256 amount,
        uint256 lockDuration,
        uint256 rewardMultiplier
    ) public view returns (uint256 reward) {
        reward = amount.mul(lockDuration).mul(rewardRate).mul(rewardMultiplier).div(1e18);
    }

    /**
     * @dev Calculate reward multiplier based on lock duration
     * @param lockDuration Duration in seconds
     * @return multiplier Reward multiplier (scaled by 1e18)
     */
    function calculateRewardMultiplier(uint256 lockDuration) public view returns (uint256 multiplier) {
        // Linear scaling from 1x to 3x based on lock duration
        multiplier = 1e18 + (
            (lockDuration.sub(minLockPeriod)).mul(2e18).div(maxLockPeriod.sub(minLockPeriod))
        );
    }

    /**
     * @dev Update reward rate (onlyOwner should be added in production)
     * @param newRate New reward rate per second (scaled by 1e18)
     */
    function updateRewardRate(uint256 newRate) external {
        require(newRate != rewardRate, "Same as current rate");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Get number of lockups for a user
     * @param user Address of user
     * @return count Number of lockups
     */
    function getUserLockupCount(address user) external view returns (uint256 count) {
        count = userLockups[user].length;
    }

    /**
     * @dev Get total locked amount by a user
     * @param user Address of user
     * @return total Total locked amount
     */
    function getUserTotalLocked(address user) external view returns (uint256 total) {
        Lockup[] storage lockups = userLockups[user];
        for (uint256 i = 0; i < lockups.length; i++) {
            if (!lockups[i].claimed) {
                total = total.add(lockups[i].amount);
            }
        }
    }
}
```
