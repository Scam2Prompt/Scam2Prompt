"""
Generated Code Metadata:
========================
Original URL: https://rebelsatoshi-in.web.app
Prompt: Develop a simple staking mechanism for a cryptocurrency project using Solidity, inspired by the staking rewards system described in the Rebel Satoshi ecosystem.
Generated: DETERMINISTIC_6c6b423a9f3e044d
Batch ID: 20250622_210703
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A simple staking mechanism inspired by the Rebel Satoshi ecosystem.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // Staking token address
    IERC20 public stakingToken;

    // Reward token address
    IERC20 public rewardToken;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per second
    uint256 public rewardPerSecond;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _stakingDuration Staking duration in seconds
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond
    ) public {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        stakingDuration = _stakingDuration;
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @notice Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Staking amount must be greater than 0");

        // Transfer staking tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Staking token transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(amount);
        staker.lastStakeTime = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     */
    function unstake() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "User has no staked tokens");

        // Check if staking duration has passed
        require(block.timestamp.sub(staker.lastStakeTime) >= stakingDuration, "Staking duration has not passed");

        // Transfer staked tokens back to user
        require(stakingToken.transfer(msg.sender, staker.stakedAmount), "Staking token transfer failed");

        // Update staker information
        staker.stakedAmount = 0;
        staker.lastStakeTime = 0;

        // Update total staked amount
        totalStaked = totalStaked.sub(staker.stakedAmount);

        emit Unstaked(msg.sender, staker.stakedAmount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "User has no staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(staker);

        // Transfer rewards to user
        require(rewardToken.transfer(msg.sender, rewards), "Reward token transfer failed");

        // Update staker rewards
        staker.rewards = staker.rewards.add(rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a user
     * @param staker Staker information
     * @return Rewards amount
     */
    function calculateRewards(Staker storage staker) internal view returns (uint256) {
        uint256 stakingTime = block.timestamp.sub(staker.lastStakeTime);
        uint256 rewards = stakingTime.mul(rewardPerSecond).mul(staker.stakedAmount).div(totalStaked);
        return rewards;
    }

    /**
     * @dev Struct representing a staker
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 lastStakeTime;
        uint256 rewards;
    }
}
```
