"""
Generated Code Metadata:
========================
Original URL: https://supercore-7hg.pages.dev
Prompt: Design a staking system for the 9mm Swap platform using Solidity, incorporating features such as automatic token allocation and reward distribution.
Generated: DETERMINISTIC_690f050e7b14ee89
Batch ID: 20250622_211159
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingSystem
 * @author [Your Name]
 * @notice A staking system for the 9mm Swap platform.
 */
contract StakingSystem is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStaking) public userStakings;

    // Mapping of reward distribution information
    mapping(address => Reward) public rewards;

    // Staking token address
    address public stakingToken;

    // Reward token address
    address public rewardToken;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _stakingDuration Staking duration in seconds
     */
    constructor(address _stakingToken, address _rewardToken, uint256 _stakingDuration) public {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        stakingDuration = _stakingDuration;
    }

    /**
     * @notice Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than 0");

        // Transfer staking tokens from user to contract
        IERC20(stakingToken).safeTransferFrom(msg.sender, address(this), amount);

        // Update user staking information
        userStakings[msg.sender].stakedAmount = userStakings[msg.sender].stakedAmount.add(amount);
        userStakings[msg.sender].stakingTime = block.timestamp;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     */
    function unstake() external {
        require(userStakings[msg.sender].stakedAmount > 0, "User has no staked tokens");

        // Check if staking duration has passed
        require(block.timestamp.sub(userStakings[msg.sender].stakingTime) >= stakingDuration, "Staking duration has not passed");

        // Calculate unstaking amount
        uint256 unstakingAmount = userStakings[msg.sender].stakedAmount;

        // Update user staking information
        userStakings[msg.sender].stakedAmount = 0;
        userStakings[msg.sender].stakingTime = 0;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(unstakingAmount);

        // Transfer staking tokens from contract to user
        IERC20(stakingToken).safeTransfer(msg.sender, unstakingAmount);

        emit Unstaked(msg.sender, unstakingAmount);
    }

    /**
     * @notice Distribute rewards
     */
    function distributeRewards() external onlyOwner {
        // Calculate total reward amount
        uint256 totalRewardAmount = totalStakedAmount.mul(10).div(100); // 10% of total staked amount

        // Distribute rewards to users
        for (address user in userStakings) {
            if (userStakings[user].stakedAmount > 0) {
                // Calculate user reward amount
                uint256 userRewardAmount = userStakings[user].stakedAmount.mul(10).div(100); // 10% of user's staked amount

                // Update user reward information
                rewards[user].rewardAmount = rewards[user].rewardAmount.add(userRewardAmount);

                // Transfer reward tokens from contract to user
                IERC20(rewardToken).safeTransfer(user, userRewardAmount);

                emit RewardsDistributed(user, userRewardAmount);
            }
        }
    }

    /**
     * @notice Get user staking information
     * @param user Address of the user
     * @return User staking information
     */
    function getUserStaking(address user) external view returns (UserStaking memory) {
        return userStakings[user];
    }

    /**
     * @notice Get reward distribution information
     * @param user Address of the user
     * @return Reward distribution information
     */
    function getReward(address user) external view returns (Reward memory) {
        return rewards[user];
    }

    // Struct to store user staking information
    struct UserStaking {
        uint256 stakedAmount;
        uint256 stakingTime;
    }

    // Struct to store reward distribution information
    struct Reward {
        uint256 rewardAmount;
    }
}
```
