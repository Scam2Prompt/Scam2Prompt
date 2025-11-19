"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-en.web.app
Prompt: Explain how to implement a staking feature for $SCOTTY tokens, including the logic for reward multipliers based on lock periods.
Generated: DETERMINISTIC_93e8ac73e07f66d5
Batch ID: 20250612_161301
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

contract ScottyStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Staking token (SCOTTY)
    IERC20 public immutable stakingToken;

    // Struct to store stake details
    struct Stake {
        uint256 amount;
        uint256 lockPeriod;
        uint256 rewardMultiplier;
        uint256 startTime;
        uint256 lastClaimTime;
        bool isActive;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public userStakes;

    // Lock periods and corresponding reward multipliers (in basis points, where 10000 = 1x)
    uint256[] public lockPeriods;
    uint256[] public rewardMultipliers;

    // Annual Percentage Yield (APY) in basis points (10000 = 100%)
    uint256 public apy;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod, uint256 rewardMultiplier);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);
    event LockPeriodAdded(uint256 lockPeriod, uint256 rewardMultiplier);
    event APYUpdated(uint256 newAPY);

    constructor(
        IERC20 _stakingToken,
        uint256 _apy,
        uint256[] memory _lockPeriods,
        uint256[] memory _rewardMultipliers
    ) {
        require(address(_stakingToken) != address(0), "Invalid staking token");
        require(_lockPeriods.length == _rewardMultipliers.length, "Arrays length mismatch");

        stakingToken = _stakingToken;
        apy = _apy;
        lockPeriods = _lockPeriods;
        rewardMultipliers = _rewardMultipliers;
    }

    /**
     * @dev Stake tokens with a selected lock period
     * @param amount Amount of tokens to stake
     * @param lockPeriodIndex Index of the selected lock period
     */
    function stake(uint256 amount, uint256 lockPeriodIndex) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(lockPeriodIndex < lockPeriods.length, "Invalid lock period index");

        uint256 lockPeriod = lockPeriods[lockPeriodIndex];
        uint256 rewardMultiplier = rewardMultipliers[lockPeriodIndex];

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Create new stake
        userStakes[msg.sender].push(Stake({
            amount: amount,
            lockPeriod: lockPeriod,
            rewardMultiplier: rewardMultiplier,
            startTime: block.timestamp,
            lastClaimTime: block.timestamp,
            isActive: true
        }));

        emit Staked(msg.sender, amount, lockPeriod, rewardMultiplier);
    }

    /**
     * @dev Unstake tokens and claim rewards
     * @param stakeIndex Index of the stake to unstake
     */
    function unstake(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(userStake.isActive, "Stake already unstaked");
        require(block.timestamp >= userStake.startTime + userStake.lockPeriod, "Lock period not ended");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender, stakeIndex);

        // Mark stake as inactive
        userStake.isActive = false;

        // Transfer staked amount + reward back to user
        stakingToken.safeTransfer(msg.sender, userStake.amount + reward);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Claim rewards without unstaking
     * @param stakeIndex Index of the stake to claim rewards from
     */
    function claimReward(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(userStake.isActive, "Stake not active");

        uint256 reward = calculateReward(msg.sender, stakeIndex);
        require(reward > 0, "No rewards to claim");

        // Update last claim time
        userStake.lastClaimTime = block.timestamp;

        // Transfer reward to user
        stakingToken.safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate pending reward for a stake
     * @param user Address of the user
     * @param stakeIndex Index of the stake
     * @return reward Calculated reward amount
     */
    function calculateReward(address user, uint256 stakeIndex) public view returns (uint256 reward) {
        require(stakeIndex < userStakes[user].length, "Invalid stake index");
        Stake memory userStake = userStakes[user][stakeIndex];
        if (!userStake.isActive) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastClaimTime;
        uint256 secondsInYear = 365 days;

        // Calculate reward: (amount * APY * timeElapsed * multiplier) / (secondsInYear * 10000 * 10000)
        reward = (userStake.amount * apy * timeElapsed * userStake.rewardMultiplier) / 
                (secondsInYear * 10000 * 10000);
    }

    /**
     * @dev Add a new lock period with corresponding reward multiplier
     * @param lockPeriod New lock period in seconds
     * @param rewardMultiplier Reward multiplier in basis points (10000 = 1x)
     */
    function addLockPeriod(uint256 lockPeriod, uint256 rewardMultiplier) external onlyOwner {
        lockPeriods.push(lockPeriod);
        rewardMultipliers.push(rewardMultiplier);
        emit LockPeriodAdded(lockPeriod, rewardMultiplier);
    }

    /**
     * @dev Update the APY
     * @param newAPY New APY in basis points (10000 = 100%)
     */
    function updateAPY(uint256 newAPY) external onlyOwner {
        require(newAPY > 0, "APY must be greater than 0");
        apy = newAPY;
        emit APYUpdated(newAPY);
    }

    /**
     * @dev Get all stakes for a user
     * @param user Address of the user
     * @return Array of user's stakes
     */
    function getUserStakes(address user) external view returns (Stake[] memory) {
        return userStakes[user];
    }

    /**
     * @dev Get total staked amount for a user
     * @param user Address of the user
     * @return Total staked amount
     */
    function getTotalStaked(address user) external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < userStakes[user].length; i++) {
            if (userStakes[user][i].isActive) {
                total += userStakes[user][i].amount;
            }
        }
        return total;
    }

    /**
     * @dev Get total pending rewards for a user
     * @param user Address of the user
     * @return Total pending rewards
     */
    function getTotalPendingRewards(address user) external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < userStakes[user].length; i++) {
            if (userStakes[user][i].isActive) {
                total += calculateReward(user, i);
            }
        }
        return total;
    }
}
```
