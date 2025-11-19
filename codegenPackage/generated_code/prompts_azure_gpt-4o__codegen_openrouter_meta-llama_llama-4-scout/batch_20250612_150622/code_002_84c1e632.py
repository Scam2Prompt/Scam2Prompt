"""
Generated Code Metadata:
========================
Original URL: https://kabosu-bsc.pages.dev
Prompt: Create a smart contract in Solidity that implements Kabosu token staking functionality, referencing the staking mechanism planned in Phase 2 of the roadmap.
Generated: DETERMINISTIC_84c1e632e81adf02
Batch ID: 20250612_150622
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
 * @title Kabosu Staking Contract
 * @author [Your Name]
 * @notice This contract implements the staking functionality for Kabosu token.
 */
contract KabosuStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => Staker) public stakers;

    // Mapping of staking pool information
    mapping(uint256 => StakingPool) public stakingPools;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 indexed poolId, uint256 amount);

    // Kabosu token contract
    ERC20 public kabosuToken;

    // Total number of staking pools
    uint256 public poolCount;

    /**
     * @param _kabosuToken Address of the Kabosu token contract
     */
    constructor(ERC20 _kabosuToken) {
        require(address(_kabosuToken) != address(0), "Kabosu token contract address is zero");

        kabosuToken = _kabosuToken;
        poolCount = 0;
    }

    /**
     * @dev Creates a new staking pool
     * @param _rewardPerBlock Reward per block for the pool
     * @param _poolDuration Duration of the pool in blocks
     */
    function createStakingPool(uint256 _rewardPerBlock, uint256 _poolDuration) public {
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(_poolDuration > 0, "Pool duration must be greater than zero");

        stakingPools[poolCount] = StakingPool(_rewardPerBlock, _poolDuration, block.timestamp);
        poolCount++;
    }

    /**
     * @dev Stake tokens in a pool
     * @param _poolId ID of the staking pool
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _poolId, uint256 _amount) public {
        require(_poolId < poolCount, "Invalid pool ID");
        require(_amount > 0, "Stake amount must be greater than zero");
        require(kabosuToken.balanceOf(msg.sender) >= _amount, "Insufficient Kabosu token balance");

        Staker storage staker = stakers[msg.sender];
        StakingPool storage pool = stakingPools[_poolId];

        // Update staker information
        staker.poolId = _poolId;
        staker.amount = staker.amount.add(_amount);
        staker.lastUpdate = block.timestamp;

        // Update pool information
        pool.totalStaked = pool.totalStaked.add(_amount);

        // Transfer tokens to the contract
        kabosuToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Unstake tokens from a pool
     * @param _poolId ID of the staking pool
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _poolId, uint256 _amount) public {
        require(_poolId < poolCount, "Invalid pool ID");
        require(_amount > 0, "Unstake amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        StakingPool storage pool = stakingPools[_poolId];

        require(staker.poolId == _poolId, "Invalid pool ID for staker");
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update staker information
        staker.amount = staker.amount.sub(_amount);
        staker.lastUpdate = block.timestamp;

        // Update pool information
        pool.totalStaked = pool.totalStaked.sub(_amount);

        // Transfer tokens to the user
        kabosuToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Claims rewards for a staker
     * @param _poolId ID of the staking pool
     */
    function claimRewards(uint256 _poolId) public {
        require(_poolId < poolCount, "Invalid pool ID");

        Staker storage staker = stakers[msg.sender];
        StakingPool storage pool = stakingPools[_poolId];

        require(staker.poolId == _poolId, "Invalid pool ID for staker");

        // Calculate rewards
        uint256 rewards = calculateRewards(staker, pool);

        // Update staker information
        staker.lastUpdate = block.timestamp;
        staker.rewards = staker.rewards.add(rewards);

        // Transfer rewards to the user
        kabosuToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, _poolId, rewards);
    }

    /**
     * @dev Calculates rewards for a staker
     * @param _staker Staker information
     * @param _pool Pool information
     * @return Rewards for the staker
     */
    function calculateRewards(Staker memory _staker, StakingPool memory _pool) internal view returns (uint256) {
        // Calculate elapsed time
        uint256 elapsed = block.timestamp.sub(_staker.lastUpdate);

        // Calculate rewards
        uint256 rewards = _staker.amount.mul(_pool.rewardPerBlock).mul(elapsed);

        return rewards;
    }

    // Struct for staker information
    struct Staker {
        uint256 poolId;
        uint256 amount;
        uint256 lastUpdate;
        uint256 rewards;
    }

    // Struct for staking pool information
    struct StakingPool {
        uint256 rewardPerBlock;
        uint256 poolDuration;
        uint256 startTime;
        uint256 totalStaked;
    }
}
```
