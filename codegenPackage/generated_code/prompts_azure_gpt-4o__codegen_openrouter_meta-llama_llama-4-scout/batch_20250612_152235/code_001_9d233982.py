"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20support.pages.dev
Prompt: Generate Solidity code for a staking smart contract similar to DOGE20, which distributes rewards proportionally to stakers based on their percentage of the staking pool.
Generated: DETERMINISTIC_9d2339829274389b
Batch ID: 20250612_152235
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
 * @title Staking Contract
 * @author [Your Name]
 * @notice A staking smart contract that distributes rewards proportionally to stakers based on their percentage of the staking pool.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward token addresses to their corresponding staking pool information
    mapping(address => StakingPool) public stakingPools;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed to stakers
    event RewardsDistributed(address indexed token, uint256 totalRewards);

    // Struct to represent a staker's information
    struct Staker {
        uint256 stakedAmount;
        uint256 lastClaimed;
    }

    // Struct to represent a staking pool's information
    struct StakingPool {
        uint256 totalStaked;
        uint256 totalRewards;
        uint256 lastRewardDistribution;
    }

    /**
     * @notice Adds a new staking pool for a given reward token
     * @param _rewardToken The address of the reward token
     */
    function addStakingPool(address _rewardToken) public {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(stakingPools[_rewardToken].totalStaked == 0, "Staking pool already exists for this reward token");

        stakingPools[_rewardToken] = StakingPool(0, 0, block.timestamp);
    }

    /**
     * @notice Stake tokens in a staking pool
     * @param _rewardToken The address of the reward token
     * @param _amount The amount of tokens to stake
     */
    function stake(address _rewardToken, uint256 _amount) public {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_amount > 0, "Invalid stake amount");
        require(stakingPools[_rewardToken].totalStaked >= 0, "Staking pool does not exist for this reward token");

        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        stakingPools[_rewardToken].totalStaked = stakingPools[_rewardToken].totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens from a staking pool
     * @param _rewardToken The address of the reward token
     * @param _amount The amount of tokens to unstake
     */
    function unstake(address _rewardToken, uint256 _amount) public {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_amount > 0, "Invalid unstake amount");
        require(stakingPools[_rewardToken].totalStaked >= 0, "Staking pool does not exist for this reward token");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(_amount);
        stakingPools[_rewardToken].totalStaked = stakingPools[_rewardToken].totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Distributes rewards to stakers in a staking pool
     * @param _rewardToken The address of the reward token
     * @param _rewards The amount of rewards to distribute
     */
    function distributeRewards(address _rewardToken, uint256 _rewards) public {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewards > 0, "Invalid rewards amount");
        require(stakingPools[_rewardToken].totalStaked > 0, "Staking pool does not exist or is empty");

        stakingPools[_rewardToken].totalRewards = stakingPools[_rewardToken].totalRewards.add(_rewards);
        stakingPools[_rewardToken].lastRewardDistribution = block.timestamp;

        emit RewardsDistributed(_rewardToken, _rewards);
    }

    /**
     * @notice Claims rewards for a staker in a staking pool
     * @param _rewardToken The address of the reward token
     */
    function claimRewards(address _rewardToken) public {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(stakingPools[_rewardToken].totalStaked > 0, "Staking pool does not exist or is empty");
        require(stakers[msg.sender].stakedAmount > 0, "Insufficient staked amount");

        uint256 rewards = calculateRewards(_rewardToken, msg.sender);
        require(rewards > 0, "No rewards to claim");

        stakers[msg.sender].lastClaimed = block.timestamp;

        // Transfer rewards to staker
        ERC20(_rewardToken).transfer(msg.sender, rewards);
    }

    /**
     * @notice Calculates rewards for a staker in a staking pool
     * @param _rewardToken The address of the reward token
     * @param _staker The address of the staker
     * @return The rewards amount
     */
    function calculateRewards(address _rewardToken, address _staker) internal view returns (uint256) {
        Staker memory staker = stakers[_staker];
        StakingPool memory pool = stakingPools[_rewardToken];

        uint256 stakerShare = staker.stakedAmount.mul(100).div(pool.totalStaked);
        uint256 rewards = pool.totalRewards.mul(stakerShare).div(100);

        return rewards;
    }
}
```
