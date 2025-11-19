"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Write a smart contract in Solidity for staking $GGG tokens, referencing the staking platform details from Good Games Guild documentation.
Generated: DETERMINISTIC_9bc49b47b0c0c857
Batch ID: 20250612_153820
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
 * @title GGG Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $GGG tokens and earn rewards.
 * @dev This contract references the staking platform details from Good Games Guild documentation.
 */
contract GGGStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token contract instance
    IERC20 public token;

    // Staking platform details
    uint256 public stakingDuration; // in seconds
    uint256 public stakingStartTime;
    uint256 public stakingEndTime;
    uint256 public rewardPerSecond;
    uint256 public totalStaked;
    uint256 public totalRewards;

    // User staking information
    mapping(address => uint256) public userStakedAmounts;
    mapping(address => uint256) public userRewardDebt;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor function
     * @param _token $GGG token contract address
     * @param _stakingDuration Staking duration in seconds
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        address _token,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond
    ) public {
        require(_token != address(0), "Token address cannot be zero");
        require(_stakingDuration > 0, "Staking duration must be greater than zero");
        require(_rewardPerSecond > 0, "Reward per second must be greater than zero");

        token = IERC20(_token);
        stakingDuration = _stakingDuration;
        rewardPerSecond = _rewardPerSecond;
        stakingStartTime = block.timestamp;
        stakingEndTime = stakingStartTime.add(stakingDuration);
    }

    /**
     * @notice Stake $GGG tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(stakingStartTime <= block.timestamp, "Staking not started yet");
        require(stakingEndTime >= block.timestamp, "Staking period has ended");
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from user to contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staked amount and reward debt
        if (userStakedAmounts[msg.sender] > 0) {
            _distributeRewards(msg.sender);
        }
        userStakedAmounts[msg.sender] = userStakedAmounts[msg.sender].add(_amount);
        userRewardDebt[msg.sender] = _getRewardDebt(msg.sender);

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $GGG tokens
     */
    function unstake() external nonReentrant {
        require(stakingEndTime < block.timestamp, "Staking period has not ended");
        require(userStakedAmounts[msg.sender] > 0, "User has no staked tokens");

        // Distribute rewards to user
        _distributeRewards(msg.sender);

        // Transfer staked tokens back to user
        uint256 stakedAmount = userStakedAmounts[msg.sender];
        userStakedAmounts[msg.sender] = 0;
        userRewardDebt[msg.sender] = 0;
        token.safeTransfer(msg.sender, stakedAmount);

        // Update total staked amount
        totalStaked = totalStaked.sub(stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Distribute rewards to user
     * @param _user User address
     */
    function _distributeRewards(address _user) internal {
        uint256 reward = _getReward(_user);
        if (reward > 0) {
            userRewardDebt[_user] = _getRewardDebt(_user);
            token.safeTransfer(_user, reward);
            emit RewardsDistributed(_user, reward);
        }
    }

    /**
     * @notice Get user's reward debt
     * @param _user User address
     * @return Reward debt
     */
    function _getRewardDebt(address _user) internal view returns (uint256) {
        return userStakedAmounts[_user].mul(rewardPerSecond).mul(block.timestamp.sub(stakingStartTime));
    }

    /**
     * @notice Get user's reward
     * @param _user User address
     * @return Reward
     */
    function _getReward(address _user) internal view returns (uint256) {
        uint256 stakedDuration = block.timestamp.sub(stakingStartTime);
        return userStakedAmounts[_user].mul(rewardPerSecond).mul(stakedDuration).sub(userRewardDebt[_user]);
    }

    /**
     * @notice Get contract's balance
     * @return Balance
     */
    function getBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
