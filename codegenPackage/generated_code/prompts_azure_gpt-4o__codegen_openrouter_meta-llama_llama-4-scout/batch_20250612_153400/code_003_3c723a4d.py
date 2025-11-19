"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-token.pages.dev
Prompt: Write a Solidity smart contract that implements a staking mechanism similar to Poodl Inu, including reward distribution based on the percentage of tokens staked.
Generated: DETERMINISTIC_3c723a4dc9b3587d
Batch ID: 20250612_153400
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PoodlInuStakingContract
 * @author [Your Name]
 * @notice A staking contract similar to Poodl Inu, distributing rewards based on the percentage of tokens staked.
 */
contract PoodlInuStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward distribution
    mapping(address => uint256) public rewards;

    // Total staked tokens
    uint256 public totalStaked;

    // Total reward tokens
    uint256 public totalRewards;

    // Staking token contract
    ERC20 public stakingToken;

    // Reward token contract
    ERC20 public rewardToken;

    // Staking start timestamp
    uint256 public stakingStartTime;

    // Staking end timestamp
    uint256 public stakingEndTime;

    // Reward distribution interval
    uint256 public rewardDistributionInterval;

    // Reward per interval
    uint256 public rewardPerInterval;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Staking token contract address
     * @param _rewardToken Reward token contract address
     * @param _stakingStartTime Staking start timestamp
     * @param _stakingEndTime Staking end timestamp
     * @param _rewardDistributionInterval Reward distribution interval
     * @param _rewardPerInterval Reward per interval
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingStartTime,
        uint256 _stakingEndTime,
        uint256 _rewardDistributionInterval,
        uint256 _rewardPerInterval
    ) public {
        require(_stakingToken != address(0), "Staking token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_stakingStartTime > block.timestamp, "Staking start time must be in the future");
        require(_stakingEndTime > _stakingStartTime, "Staking end time must be after start time");

        stakingToken = ERC20(_stakingToken);
        rewardToken = ERC20(_rewardToken);
        stakingStartTime = _stakingStartTime;
        stakingEndTime = _stakingEndTime;
        rewardDistributionInterval = _rewardDistributionInterval;
        rewardPerInterval = _rewardPerInterval;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient staking token balance");
        require(stakingStartTime <= block.timestamp && block.timestamp <= stakingEndTime, "Staking period has not started or has ended");

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(amount);
        userStakingInfos[msg.sender].lastStakeTime = block.timestamp;

        // Update total staked tokens
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(userStakingInfos[msg.sender].stakedAmount >= amount, "Unstaking amount exceeds staked amount");
        require(stakingEndTime <= block.timestamp, "Staking period has not ended");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.sub(amount);

        // Transfer staking tokens from contract to user
        stakingToken.transfer(msg.sender, amount);

        // Update total staked tokens
        totalStaked = totalStaked.sub(amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards
     */
    function distributeRewards() external nonReentrant {
        require(stakingEndTime <= block.timestamp, "Staking period has not ended");

        // Calculate reward distribution
        uint256 intervalElapsed = block.timestamp.sub(stakingEndTime).div(rewardDistributionInterval);
        uint256 totalReward = intervalElapsed.mul(rewardPerInterval);

        // Update total rewards
        totalRewards = totalRewards.add(totalReward);

        // Distribute rewards to users
        for (address user in userStakingInfos) {
            uint256 userStakedAmount = userStakingInfos[user].stakedAmount;
            uint256 reward = totalReward.mul(userStakedAmount).div(totalStaked);

            // Update user reward
            rewards[user] = rewards[user].add(reward);

            // Transfer reward tokens to user
            rewardToken.transfer(user, reward);

            emit RewardsDistributed(user, reward);
        }
    }

    /**
     * @dev Get user staking information
     * @param user User address
     * @return User staking information
     */
    function getUserStakingInfo(address user) external view returns (UserStakingInfo memory) {
        return userStakingInfos[user];
    }

    /**
     * @dev Get user reward
     * @param user User address
     * @return User reward
     */
    function getUserReward(address user) external view returns (uint256) {
        return rewards[user];
    }

    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakeTime;
    }
}
```
