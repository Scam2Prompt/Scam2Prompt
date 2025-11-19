"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-ai.web.app
Prompt: Create a smart contract in Solidity that mimics the staking functionality described on the Scotty AI platform, including reward multipliers based on lock periods.
Generated: DETERMINISTIC_13f4f7ab008f3f0f
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ScottyAIStaking is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct Stake {
        uint256 amount;
        uint256 lockPeriod;
        uint256 rewardMultiplier;
        uint256 startTime;
        uint256 claimedRewards;
        bool isActive;
    }

    struct LockPeriod {
        uint256 duration; // in seconds
        uint256 multiplier; // multiplier in basis points (10000 = 1x)
    }

    mapping(address => Stake[]) public userStakes;
    LockPeriod[] public lockPeriods;
    uint256 public totalStaked;
    uint256 public rewardRate; // rewards per second per token staked (in wei)

    event Staked(address indexed user, uint256 amount, uint256 lockPeriod, uint256 rewardMultiplier);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 amount);
    event LockPeriodAdded(uint256 duration, uint256 multiplier);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Staking token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;

        // Initialize with default lock periods
        lockPeriods.push(LockPeriod(30 days, 10000)); // 1x for 30 days
        lockPeriods.push(LockPeriod(90 days, 15000)); // 1.5x for 90 days
        lockPeriods.push(LockPeriod(180 days, 20000)); // 2x for 180 days
    }

    /**
     * @dev Stake tokens with selected lock period
     * @param amount Amount of tokens to stake
     * @param lockPeriodIndex Index of the selected lock period
     */
    function stake(uint256 amount, uint256 lockPeriodIndex) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(lockPeriodIndex < lockPeriods.length, "Invalid lock period index");

        LockPeriod memory period = lockPeriods[lockPeriodIndex];
        uint256 multiplier = period.multiplier;

        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Create new stake
        userStakes[msg.sender].push(Stake({
            amount: amount,
            lockPeriod: period.duration,
            rewardMultiplier: multiplier,
            startTime: block.timestamp,
            claimedRewards: 0,
            isActive: true
        }));

        totalStaked += amount;

        emit Staked(msg.sender, amount, period.duration, multiplier);
    }

    /**
     * @dev Unstake tokens and claim rewards
     * @param stakeIndex Index of the stake to unstake
     */
    function unstake(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(userStake.isActive, "Stake is already inactive");

        // Check if lock period has ended
        require(block.timestamp >= userStake.startTime + userStake.lockPeriod, "Lock period not ended");

        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateReward(msg.sender, stakeIndex);

        // Mark stake as inactive
        userStake.isActive = false;
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to user
        require(stakingToken.transfer(msg.sender, stakedAmount), "Transfer failed");

        // Transfer rewards if any
        if (reward > 0) {
            require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
            userStake.claimedRewards += reward;
            emit RewardClaimed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Claim rewards without unstaking
     * @param stakeIndex Index of the stake to claim rewards from
     */
    function claimReward(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(userStake.isActive, "Stake is inactive");

        uint256 reward = calculateReward(msg.sender, stakeIndex);
        require(reward > 0, "No rewards to claim");

        userStake.claimedRewards += reward;
        userStake.startTime = block.timestamp; // reset reward calculation period

        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate pending rewards for a stake
     * @param user Address of the user
     * @param stakeIndex Index of the stake
     * @return reward Amount of pending rewards
     */
    function calculateReward(address user, uint256 stakeIndex) public view returns (uint256 reward) {
        require(stakeIndex < userStakes[user].length, "Invalid stake index");
        Stake memory userStake = userStakes[user][stakeIndex];
        if (!userStake.isActive) return 0;

        uint256 elapsedTime = block.timestamp - userStake.startTime;
        uint256 effectiveRate = (rewardRate * userStake.rewardMultiplier) / 10000;
        reward = (userStake.amount * elapsedTime * effectiveRate) / 1e18;
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
     * @dev Add a new lock period option
     * @param duration Duration in seconds
     * @param multiplier Multiplier in basis points (10000 = 1x)
     */
    function addLockPeriod(uint256 duration, uint256 multiplier) external onlyOwner {
        require(duration > 0, "Duration must be greater than zero");
        require(multiplier >= 10000, "Multiplier must be at least 1x (10000)");
        lockPeriods.push(LockPeriod(duration, multiplier));
        emit LockPeriodAdded(duration, multiplier);
    }

    /**
     * @dev Update the reward rate
     * @param newRate New reward rate (rewards per second per token staked in wei)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate != rewardRate, "New rate must be different");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Withdraw any ERC20 tokens from the contract (emergency only)
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawERC20(address token, uint256 amount) external onlyOwner {
        require(token != address(stakingToken), "Cannot withdraw staking token");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
