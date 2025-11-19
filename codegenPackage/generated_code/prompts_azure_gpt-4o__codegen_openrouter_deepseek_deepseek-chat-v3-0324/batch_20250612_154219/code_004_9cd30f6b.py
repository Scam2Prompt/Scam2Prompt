"""
Generated Code Metadata:
========================
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Develop a smart contract for staking AIXCB tokens that integrates with the AIXCB Staking protocol and calculates rewards distribution based on the staking duration.
Generated: DETERMINISTIC_9cd30f6b23507cde
Batch ID: 20250612_154219
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

contract AIXCBStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking details
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 duration;
        uint256 rewardRate;
        bool claimed;
    }

    // Staking token (AIXCB)
    IERC20 public immutable stakingToken;

    // Reward tiers based on duration (in seconds)
    mapping(uint256 => uint256) public rewardRates; // duration => rate (percentage)

    // User stakes
    mapping(address => Stake[]) public userStakes;

    // Total staked amount
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 duration);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 duration, uint256 newRate);

    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);

        // Initialize default reward rates (example values)
        rewardRates[30 days] = 5;  // 5% for 30 days
        rewardRates[90 days] = 15; // 15% for 90 days
        rewardRates[180 days] = 35; // 35% for 180 days
    }

    /**
     * @notice Stake AIXCB tokens for a specified duration
     * @param amount Amount of tokens to stake
     * @param duration Staking duration in seconds
     */
    function stake(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(rewardRates[duration] > 0, "Invalid staking duration");

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Create new stake
        userStakes[msg.sender].push(Stake({
            amount: amount,
            startTime: block.timestamp,
            duration: duration,
            rewardRate: rewardRates[duration],
            claimed: false
        }));

        totalStaked += amount;

        emit Staked(msg.sender, amount, duration);
    }

    /**
     * @notice Unstake tokens and claim rewards
     * @param stakeIndex Index of the stake to unstake
     */
    function unstake(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");

        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(!userStake.claimed, "Already claimed");
        require(block.timestamp >= userStake.startTime + userStake.duration, "Staking period not ended");

        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateReward(msg.sender, stakeIndex);

        // Mark as claimed
        userStake.claimed = true;

        // Update total staked
        totalStaked -= stakedAmount;

        // Transfer staked amount + reward
        stakingToken.safeTransfer(msg.sender, stakedAmount + reward);

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @notice Calculate reward for a specific stake
     * @param user Address of the user
     * @param stakeIndex Index of the stake
     * @return reward Calculated reward amount
     */
    function calculateReward(address user, uint256 stakeIndex) public view returns (uint256 reward) {
        require(stakeIndex < userStakes[user].length, "Invalid stake index");

        Stake memory userStake = userStakes[user][stakeIndex];
        if (userStake.claimed) return 0;

        reward = (userStake.amount * userStake.rewardRate) / 100;
        return reward;
    }

    /**
     * @notice Get all stakes for a user
     * @param user Address of the user
     * @return Array of user's stakes
     */
    function getUserStakes(address user) external view returns (Stake[] memory) {
        return userStakes[user];
    }

    /**
     * @notice Update reward rate for a specific duration
     * @param duration Staking duration in seconds
     * @param newRate New reward rate (percentage)
     */
    function updateRewardRate(uint256 duration, uint256 newRate) external onlyOwner {
        require(duration > 0, "Duration must be greater than 0");
        rewardRates[duration] = newRate;
        emit RewardRateUpdated(duration, newRate);
    }

    /**
     * @notice Recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot recover staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
