"""
Generated Code Metadata:
========================
Original URL: https://bitcoinsbsc.pages.dev
Prompt: Generate Solidity code for a smart contract that mimics the staking mechanism of Bitcoin BSC, where rewards are distributed every 10 minutes based on the percentage of the staking pool.
Generated: DETERMINISTIC_b8e3005399f3de53
Batch ID: 20250612_150946
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

contract BitcoinBSCStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStaking) public userStakings;

    // Mapping of reward distribution history
    mapping(uint256 => RewardDistribution) public rewardDistributions;

    // Token contract instance
    ERC20Burnable public token;

    // Staking pool address
    address public stakingPool;

    // Reward token address
    ERC20 public rewardToken;

    // Reward distribution interval in seconds (10 minutes)
    uint256 public constant REWARD_DISTRIBUTION_INTERVAL = 600;

    // Reward per interval
    uint256 public rewardPerInterval;

    // Total staked amount
    uint256 public totalStaked;

    // Last reward distribution timestamp
    uint256 public lastRewardDistribution;

    // Reward distribution counter
    uint256 public rewardDistributionCounter;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 rewardDistributionId, uint256 totalRewards);

    // Struct to store user staking information
    struct UserStaking {
        uint256 stakedAmount;
        uint256 lastStakedTimestamp;
    }

    // Struct to store reward distribution information
    struct RewardDistribution {
        uint256 rewardDistributionId;
        uint256 totalRewards;
        uint256 distributionTimestamp;
    }

    /**
     * @notice Constructor
     * @param _token Token contract address
     * @param _stakingPool Staking pool address
     * @param _rewardToken Reward token address
     * @param _rewardPerInterval Reward per interval
     */
    constructor(
        address _token,
        address _stakingPool,
        address _rewardToken,
        uint256 _rewardPerInterval
    ) public {
        require(_token != address(0), "Token address cannot be zero");
        require(_stakingPool != address(0), "Staking pool address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardPerInterval > 0, "Reward per interval must be greater than zero");

        token = ERC20Burnable(_token);
        stakingPool = _stakingPool;
        rewardToken = ERC20(_rewardToken);
        rewardPerInterval = _rewardPerInterval;
        lastRewardDistribution = block.timestamp;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Update user staking information
        userStakings[msg.sender].stakedAmount = userStakings[msg.sender].stakedAmount.add(_amount);
        userStakings[msg.sender].lastStakedTimestamp = block.timestamp;

        // Transfer tokens from user to staking pool
        token.transferFrom(msg.sender, stakingPool, _amount);

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStakings[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update user staking information
        userStakings[msg.sender].stakedAmount = userStakings[msg.sender].stakedAmount.sub(_amount);

        // Transfer tokens from staking pool to user
        token.transfer(msg.sender, _amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Distribute rewards
     */
    function distributeRewards() external nonReentrant {
        // Check if reward distribution interval has passed
        require(block.timestamp.sub(lastRewardDistribution) >= REWARD_DISTRIBUTION_INTERVAL, "Reward distribution interval has not passed");

        // Calculate total rewards
        uint256 totalRewards = rewardPerInterval;

        // Update last reward distribution timestamp
        lastRewardDistribution = block.timestamp;

        // Update reward distribution counter
        rewardDistributionCounter = rewardDistributionCounter.add(1);

        // Store reward distribution information
        rewardDistributions[rewardDistributionCounter] = RewardDistribution(
            rewardDistributionCounter,
            totalRewards,
            block.timestamp
        );

        // Transfer rewards to staking pool
        rewardToken.transfer(stakingPool, totalRewards);

        emit RewardsDistributed(rewardDistributionCounter, totalRewards);

        // Distribute rewards to users
        for (address user in userStakings) {
            // Calculate user reward
            uint256 userReward = totalRewards.mul(userStakings[user].stakedAmount).div(totalStaked);

            // Transfer user reward
            rewardToken.transfer(user, userReward);
        }
    }

    /**
     * @notice Get user staking information
     * @param _user User address
     * @return User staking information
     */
    function getUserStaking(address _user) external view returns (uint256, uint256) {
        return (userStakings[_user].stakedAmount, userStakings[_user].lastStakedTimestamp);
    }
}
```
