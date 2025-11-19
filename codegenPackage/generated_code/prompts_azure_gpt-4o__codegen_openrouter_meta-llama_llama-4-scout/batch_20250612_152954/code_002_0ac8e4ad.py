"""
Generated Code Metadata:
========================
Original URL: https://seedify-fundnft-project.pages.dev
Prompt: Create a smart contract in Solidity that facilitates staking $SFUND and $SNFTS tokens on the Seedify platform, including reward distribution mechanisms for token farming.
Generated: DETERMINISTIC_0ac8e4ad922283f3
Batch ID: 20250612_152954
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Seedify Staking Contract
 * @author [Your Name]
 * @notice This contract facilitates staking $SFUND and $SNFTS tokens on the Seedify platform,
 *          including reward distribution mechanisms for token farming.
 */
contract SeedifyStaking is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of token addresses to their respective staking configurations
    mapping(address => StakingConfig) public stakingConfigs;

    // Reward distribution configuration
    RewardConfig public rewardConfig;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewards);

    // Struct to store user staking information
    struct UserStakingInfo {
        mapping(address => uint256) stakedAmounts;
        mapping(address => uint256) rewards;
    }

    // Struct to store staking configuration for a token
    struct StakingConfig {
        uint256 rewardRate;
        uint256 stakingDuration;
        uint256 totalStaked;
    }

    // Struct to store reward distribution configuration
    struct RewardConfig {
        uint256 rewardDistributionInterval;
        uint256 lastRewardDistributionTime;
    }

    // Constructor
    constructor() public {
        // Initialize reward distribution configuration
        rewardConfig = RewardConfig(30 days, block.timestamp);
    }

    // Function to add a new staking configuration for a token
    function addStakingConfig(address token, uint256 rewardRate, uint256 stakingDuration) public onlyOwner {
        require(token != address(0), "Invalid token address");
        require(rewardRate > 0, "Reward rate must be greater than 0");
        require(stakingDuration > 0, "Staking duration must be greater than 0");

        stakingConfigs[token] = StakingConfig(rewardRate, stakingDuration, 0);
    }

    // Function to stake tokens
    function stake(address token, uint256 amount) public {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Staking amount must be greater than 0");
        require(stakingConfigs[token].rewardRate > 0, "Staking not available for this token");

        // Transfer tokens from user to contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmounts[token] = userStakingInfos[msg.sender].stakedAmounts[token].add(amount);
        stakingConfigs[token].totalStaked = stakingConfigs[token].totalStaked.add(amount);

        emit Staked(msg.sender, token, amount);
    }

    // Function to unstake tokens
    function unstake(address token, uint256 amount) public {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Unstaking amount must be greater than 0");
        require(userStakingInfos[msg.sender].stakedAmounts[token] >= amount, "Insufficient staked amount");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmounts[token] = userStakingInfos[msg.sender].stakedAmounts[token].sub(amount);
        stakingConfigs[token].totalStaked = stakingConfigs[token].totalStaked.sub(amount);

        // Transfer tokens from contract to user
        IERC20(token).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, token, amount);
    }

    // Function to distribute rewards
    function distributeRewards() public {
        // Check if reward distribution interval has passed
        require(block.timestamp.sub(rewardConfig.lastRewardDistributionTime) >= rewardConfig.rewardDistributionInterval, "Reward distribution interval has not passed");

        // Update last reward distribution time
        rewardConfig.lastRewardDistributionTime = block.timestamp;

        // Iterate over all staking configurations
        for (address token in stakingConfigs) {
            // Calculate rewards for the current staking configuration
            uint256 rewards = calculateRewards(token);

            // Distribute rewards to users
            distributeUserRewards(token, rewards);
        }
    }

    // Function to calculate rewards for a staking configuration
    function calculateRewards(address token) internal view returns (uint256) {
        // Calculate rewards based on staking duration and reward rate
        uint256 rewards = stakingConfigs[token].totalStaked.mul(stakingConfigs[token].rewardRate).mul(block.timestamp.sub(rewardConfig.lastRewardDistributionTime)) / 1e18;

        return rewards;
    }

    // Function to distribute rewards to users for a staking configuration
    function distributeUserRewards(address token, uint256 rewards) internal {
        // Iterate over all users
        for (address user in userStakingInfos) {
            // Calculate user rewards
            uint256 userRewards = rewards.mul(userStakingInfos[user].stakedAmounts[token]) / stakingConfigs[token].totalStaked;

            // Update user rewards
            userStakingInfos[user].rewards[token] = userStakingInfos[user].rewards[token].add(userRewards);

            emit RewardsDistributed(user, userRewards);
        }
    }

    // Function to claim rewards
    function claimRewards(address token) public {
        require(token != address(0), "Invalid token address");
        require(userStakingInfos[msg.sender].rewards[token] > 0, "No rewards to claim");

        // Transfer rewards to user
        IERC20(token).transfer(msg.sender, userStakingInfos[msg.sender].rewards[token]);

        // Reset user rewards
        userStakingInfos[msg.sender].rewards[token] = 0;
    }
}
```
