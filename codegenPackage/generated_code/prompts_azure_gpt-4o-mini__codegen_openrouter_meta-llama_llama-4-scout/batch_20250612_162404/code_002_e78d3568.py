"""
Generated Code Metadata:
========================
Original URL: https://tokencatgirl.pages.dev
Prompt: Generate a code snippet for a decentralized application (DApp) that allows users to stake CATGIRL¢ tokens and earn rewards, based on the features outlined in the Catgirl ecosystem.
Generated: DETERMINISTIC_e78d356830c29c88
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title Catgirl Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake CATGIRL¢ tokens and earn rewards.
 */
contract CatgirlStaking is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // CATGIRL¢ token contract
    IERC20 public catgirlToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Staking pool structure
    struct StakingPool {
        uint256 totalStaked;
        uint256 totalRewards;
        uint256 rewardRate; // rewards per second
        uint256 lastUpdate;
    }

    // Mapping of user staking information
    mapping(address => mapping(uint256 => uint256)) public userStakes;

    // Mapping of staking pools
    mapping(uint256 => StakingPool) public stakingPools;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 poolId, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 poolId, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 poolId, uint256 amount);

    /**
     * @param _catgirlToken CATGIRL¢ token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _catgirlToken, address _rewardToken) public {
        require(_catgirlToken != address(0), "Invalid CATGIRL¢ token address");
        require(_rewardToken != address(0), "Invalid reward token address");

        catgirlToken = IERC20(_catgirlToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Creates a new staking pool
     * @param _poolId Unique pool ID
     * @param _rewardRate Rewards per second
     */
    function createStakingPool(uint256 _poolId, uint256 _rewardRate) public onlyOwner {
        require(stakingPools[_poolId].totalStaked == 0, "Pool already exists");

        stakingPools[_poolId] = StakingPool({
            totalStaked: 0,
            totalRewards: 0,
            rewardRate: _rewardRate,
            lastUpdate: block.timestamp
        });
    }

    /**
     * @dev Stake CATGIRL¢ tokens in a pool
     * @param _poolId Pool ID to stake in
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _poolId, uint256 _amount) public nonReentrant {
        require(stakingPools[_poolId].totalStaked >= 0, "Pool does not exist");
        require(_amount > 0, "Invalid stake amount");

        // Update user's stake
        userStakes[msg.sender][_poolId] = userStakes[msg.sender][_poolId].add(_amount);

        // Update pool's total staked
        stakingPools[_poolId].totalStaked = stakingPools[_poolId].totalStaked.add(_amount);

        // Transfer tokens from user to contract
        catgirlToken.transferFrom(msg.sender, address(this), _amount);

        // Emit staked event
        emit Staked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Unstake CATGIRL¢ tokens from a pool
     * @param _poolId Pool ID to unstake from
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _poolId, uint256 _amount) public nonReentrant {
        require(stakingPools[_poolId].totalStaked >= 0, "Pool does not exist");
        require(userStakes[msg.sender][_poolId] >= _amount, "Insufficient stake");

        // Update user's stake
        userStakes[msg.sender][_poolId] = userStakes[msg.sender][_poolId].sub(_amount);

        // Update pool's total staked
        stakingPools[_poolId].totalStaked = stakingPools[_poolId].totalStaked.sub(_amount);

        // Transfer tokens from contract to user
        catgirlToken.transfer(msg.sender, _amount);

        // Emit unstaked event
        emit Unstaked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Claim rewards from a pool
     * @param _poolId Pool ID to claim rewards from
     */
    function claimRewards(uint256 _poolId) public nonReentrant {
        require(stakingPools[_poolId].totalStaked >= 0, "Pool does not exist");

        // Calculate rewards
        uint256 rewards = calculateRewards(_poolId);

        // Update pool's total rewards
        stakingPools[_poolId].totalRewards = stakingPools[_poolId].totalRewards.add(rewards);

        // Transfer rewards to user
        rewardToken.transfer(msg.sender, rewards);

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, _poolId, rewards);
    }

    /**
     * @dev Calculate rewards for a pool
     * @param _poolId Pool ID to calculate rewards for
     * @return Rewards amount
     */
    function calculateRewards(uint256 _poolId) internal view returns (uint256) {
        StakingPool storage pool = stakingPools[_poolId];
        uint256 timeElapsed = block.timestamp.sub(pool.lastUpdate);
        uint256 rewards = timeElapsed.mul(pool.rewardRate);

        return rewards;
    }

    /**
     * @dev Update reward rate for a pool
     * @param _poolId Pool ID to update
     * @param _newRewardRate New reward rate
     */
    function updateRewardRate(uint256 _poolId, uint256 _newRewardRate) public onlyOwner {
        require(stakingPools[_poolId].totalStaked >= 0, "Pool does not exist");

        stakingPools[_poolId].rewardRate = _newRewardRate;
    }
}
```
