"""
Generated Code Metadata:
========================
Original URL: https://staking-paalai.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake $PAAL tokens and earn rewards based on different APY configurations (e.g., 35% APY for 14 days, 80% APY for 28 days, 105% APY for 56 days).
Generated: DETERMINISTIC_35fa378cd785475d
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PAAL Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $PAAL tokens and earn rewards based on different APY configurations.
 */
contract PAALStaking {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStaking) public userStakings;

    // Mapping of APY configurations
    mapping(uint256 => APYConfig) public apyConfigs;

    // $PAAL token contract
    IERC20 public paalToken;

    // Reward token contract (assuming same as $PAAL for simplicity)
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount, uint256 duration);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _paalToken $PAAL token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _paalToken, address _rewardToken) {
        paalToken = IERC20(_paalToken);
        rewardToken = IERC20(_rewardToken);

        // Initialize APY configurations
        apyConfigs[14 days] = APYConfig(35, 14 days);
        apyConfigs[28 days] = APYConfig(80, 28 days);
        apyConfigs[56 days] = APYConfig(105, 56 days);
    }

    /**
     * @dev Stake $PAAL tokens for a specified duration
     * @param _amount Amount of $PAAL tokens to stake
     * @param _duration Duration of staking in days
     */
    function stake(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Invalid stake amount");
        require(apyConfigs[_duration] != APYConfig(0, 0), "Invalid staking duration");

        // Transfer $PAAL tokens to contract
        paalToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        UserStaking storage userStaking = userStakings[msg.sender];
        userStaking.amount = userStaking.amount.add(_amount);
        userStaking.duration = _duration;
        userStaking.stakeTime = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount, _duration);
    }

    /**
     * @dev Unstake $PAAL tokens
     */
    function unstake() external {
        UserStaking storage userStaking = userStakings[msg.sender];
        require(userStaking.amount > 0, "No staked amount");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer $PAAL tokens and rewards to user
        paalToken.safeTransfer(msg.sender, userStaking.amount);
        if (rewards > 0) {
            rewardToken.safeTransfer(msg.sender, rewards);
        }

        // Reset user staking information
        userStaking.amount = 0;
        userStaking.duration = 0;
        userStaking.stakeTime = 0;

        // Update total staked amount
        totalStaked = totalStaked.sub(userStaking.amount);

        emit Unstaked(msg.sender, userStaking.amount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        UserStaking storage userStaking = userStakings[_user];
        if (userStaking.stakeTime == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp.sub(userStaking.stakeTime);
        if (stakingDuration < userStaking.duration) {
            return 0;
        }

        APYConfig storage apyConfig = apyConfigs[userStaking.duration];
        uint256 apy = apyConfig.apy;
        uint256 rewards = userStaking.amount.mul(apy).div(100);

        return rewards;
    }

    // Struct for user staking information
    struct UserStaking {
        uint256 amount;
        uint256 duration;
        uint256 stakeTime;
    }

    // Struct for APY configurations
    struct APYConfig {
        uint256 apy;
        uint256 duration;
    }
}
```
