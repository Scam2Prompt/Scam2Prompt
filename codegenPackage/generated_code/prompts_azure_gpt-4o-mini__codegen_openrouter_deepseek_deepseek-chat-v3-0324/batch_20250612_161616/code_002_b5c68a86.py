"""
Generated Code Metadata:
========================
Original URL: https://rebelsatoshi-en.web.app
Prompt: Create a staking mechanism for the Rebel Satoshi ecosystem that rewards users with percentage returns for locking up their $RBLZ tokens.
Generated: DETERMINISTIC_b5c68a86a1e7b872
Batch ID: 20250612_161616
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

contract RebelSatoshiStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Staking token (RBLZ)
    IERC20 public immutable stakingToken;

    // Struct to store user stake details
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardRate; // Annual percentage rate (APR)
        uint256 claimedRewards;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public userStakes;

    // Total staked amount
    uint256 public totalStaked;

    // Minimum and maximum staking periods (in seconds)
    uint256 public constant MIN_STAKE_DURATION = 30 days;
    uint256 public constant MAX_STAKE_DURATION = 365 days;

    // Reward rates based on staking duration
    mapping(uint256 => uint256) public rewardRates; // duration in days => APR percentage

    // Events
    event Staked(address indexed user, uint256 amount, uint256 duration, uint256 rewardRate);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 duration, uint256 newRate);

    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);

        // Initialize default reward rates
        rewardRates[30] = 10;   // 10% APR for 30 days
        rewardRates[90] = 25;   // 25% APR for 90 days
        rewardRates[180] = 60;  // 60% APR for 180 days
        rewardRates[365] = 120; // 120% APR for 365 days
    }

    /**
     * @notice Stake RBLZ tokens for a specified duration
     * @param amount Amount of tokens to stake
     * @param durationDays Staking duration in days (must be one of the predefined durations)
     */
    function stake(uint256 amount, uint256 durationDays) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(rewardRates[durationDays] > 0, "Invalid staking duration");
        
        uint256 durationSeconds = durationDays * 1 days;
        require(durationSeconds >= MIN_STAKE_DURATION && durationSeconds <= MAX_STAKE_DURATION, "Invalid duration");

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Create new stake
        userStakes[msg.sender].push(Stake({
            amount: amount,
            startTime: block.timestamp,
            rewardRate: rewardRates[durationDays],
            claimedRewards: 0
        }));

        totalStaked += amount;

        emit Staked(msg.sender, amount, durationDays, rewardRates[durationDays]);
    }

    /**
     * @notice Calculate pending rewards for a specific stake
     * @param user Address of the user
     * @param stakeIndex Index of the stake in user's stakes array
     * @return rewards Amount of pending rewards
     */
    function calculateRewards(address user, uint256 stakeIndex) public view returns (uint256 rewards) {
        require(stakeIndex < userStakes[user].length, "Invalid stake index");

        Stake memory stakeInfo = userStakes[user][stakeIndex];
        uint256 stakedDuration = block.timestamp - stakeInfo.startTime;
        uint256 stakedDurationInYears = stakedDuration * 1e18 / 365 days; // Fixed-point arithmetic

        rewards = (stakeInfo.amount * stakeInfo.rewardRate * stakedDurationInYears) / (100 * 1e18);
        rewards -= stakeInfo.claimedRewards;
    }

    /**
     * @notice Claim rewards for a specific stake
     * @param stakeIndex Index of the stake in user's stakes array
     */
    function claimRewards(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");

        Stake storage stakeInfo = userStakes[msg.sender][stakeIndex];
        uint256 rewards = calculateRewards(msg.sender, stakeIndex);
        require(rewards > 0, "No rewards to claim");

        stakeInfo.claimedRewards += rewards;
        stakingToken.safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Unstake tokens and claim remaining rewards
     * @param stakeIndex Index of the stake in user's stakes array
     */
    function unstake(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");

        Stake memory stakeInfo = userStakes[msg.sender][stakeIndex];
        uint256 stakedDuration = block.timestamp - stakeInfo.startTime;
        require(stakedDuration >= MIN_STAKE_DURATION, "Stake is still locked");

        // Calculate and transfer remaining rewards
        uint256 rewards = calculateRewards(msg.sender, stakeIndex);
        if (rewards > 0) {
            stakingToken.safeTransfer(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        // Transfer staked amount back to user
        stakingToken.safeTransfer(msg.sender, stakeInfo.amount);
        totalStaked -= stakeInfo.amount;

        // Remove the stake from array
        _removeStake(msg.sender, stakeIndex);

        emit Unstaked(msg.sender, stakeInfo.amount);
    }

    /**
     * @notice Remove a stake from user's stakes array
     * @param user Address of the user
     * @param index Index of the stake to remove
     */
    function _removeStake(address user, uint256 index) private {
        uint256 lastIndex = userStakes[user].length - 1;
        if (index != lastIndex) {
            userStakes[user][index] = userStakes[user][lastIndex];
        }
        userStakes[user].pop();
    }

    /**
     * @notice Update reward rate for a specific staking duration
     * @param durationDays Staking duration in days
     * @param newRate New APR percentage for this duration
     */
    function updateRewardRate(uint256 durationDays, uint256 newRate) external onlyOwner {
        require(durationDays >= 30 && durationDays <= 365, "Invalid duration");
        rewardRates[durationDays] = newRate;
        emit RewardRateUpdated(durationDays, newRate);
    }

    /**
     * @notice Emergency withdraw stuck tokens (only owner)
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(stakingToken) || amount <= IERC20(token).balanceOf(address(this)) - totalStaked,
            "Cannot withdraw staked tokens");
        IERC20(token).safeTransfer(owner(), amount);
    }

    /**
     * @notice Get total staked amount by a user
     * @param user Address of the user
     * @return total Total staked amount
     */
    function getUserTotalStaked(address user) external view returns (uint256 total) {
        for (uint256 i = 0; i < userStakes[user].length; i++) {
            total += userStakes[user][i].amount;
        }
    }

    /**
     * @notice Get total pending rewards for a user
     * @param user Address of the user
     * @return total Total pending rewards
     */
    function getUserTotalRewards(address user) external view returns (uint256 total) {
        for (uint256 i = 0; i < userStakes[user].length; i++) {
            total += calculateRewards(user, i);
        }
    }

    /**
     * @notice Get number of stakes for a user
     * @param user Address of the user
     * @return count Number of stakes
     */
    function getUserStakeCount(address user) external view returns (uint256 count) {
        count = userStakes[user].length;
    }
}
```
