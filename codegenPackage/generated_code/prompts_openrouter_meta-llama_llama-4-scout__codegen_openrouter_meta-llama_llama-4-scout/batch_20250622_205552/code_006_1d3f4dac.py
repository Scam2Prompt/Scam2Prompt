"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: Write a smart contract in Solidity to manage the $BIGTIME token's functionality, including token distribution, transfer, and staking mechanisms, suitable for the Big Time game's economy.
Generated: DETERMINISTIC_1d3f4dac8c09e2ee
Batch ID: 20250622_205552
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
 * @title BigTimeToken Contract
 * @author [Your Name]
 * @notice This contract manages the $BIGTIME token's functionality, including token distribution, transfer, and staking mechanisms.
 */
contract BigTimeToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker's address to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of staking pool's id to its information
    mapping(uint256 => StakingPool) public stakingPools;

    // Total number of staking pools
    uint256 public totalStakingPools;

    // Event emitted when a new staking pool is created
    event NewStakingPool(uint256 indexed poolId, uint256 rewardRate, uint256 duration);

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 indexed poolId, uint256 amount);

    /**
     * @dev Struct to represent a staker's information
     */
    struct Staker {
        uint256[] poolIds;
        mapping(uint256 => uint256) stakedAmounts;
        mapping(uint256 => uint256) rewards;
    }

    /**
     * @dev Struct to represent a staking pool's information
     */
    struct StakingPool {
        uint256 id;
        uint256 rewardRate;
        uint256 duration;
        uint256 endTime;
        bool active;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param initialSupply The initial supply of the token
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Creates a new staking pool
     * @param rewardRate The reward rate of the pool
     * @param duration The duration of the pool
     */
    function createStakingPool(uint256 rewardRate, uint256 duration) public {
        require(rewardRate > 0, "Reward rate must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        StakingPool memory newPool;
        newPool.id = totalStakingPools;
        newPool.rewardRate = rewardRate;
        newPool.duration = duration;
        newPool.endTime = block.timestamp.add(duration);
        newPool.active = true;

        stakingPools[totalStakingPools] = newPool;
        totalStakingPools++;

        emit NewStakingPool(newPool.id, newPool.rewardRate, newPool.duration);
    }

    /**
     * @dev Stakes tokens in a specified pool
     * @param poolId The id of the staking pool
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 poolId, uint256 amount) public {
        require(stakingPools[poolId].active, "Staking pool is not active");
        require(stakingPools[poolId].endTime > block.timestamp, "Staking pool has ended");
        require(amount > 0, "Staking amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        Staker storage staker = stakers[msg.sender];
        staker.poolIds.push(poolId);
        staker.stakedAmounts[poolId] = staker.stakedAmounts[poolId].add(amount);

        _transfer(msg.sender, address(this), amount);

        emit Staked(msg.sender, poolId, amount);
    }

    /**
     * @dev Unstakes tokens from a specified pool
     * @param poolId The id of the staking pool
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 poolId, uint256 amount) public {
        require(stakers[msg.sender].stakedAmounts[poolId] >= amount, "Insufficient staked amount");
        require(stakingPools[poolId].active, "Staking pool is not active");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmounts[poolId] = staker.stakedAmounts[poolId].sub(amount);

        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, poolId, amount);
    }

    /**
     * @dev Claims rewards from a specified pool
     * @param poolId The id of the staking pool
     */
    function claimRewards(uint256 poolId) public {
        require(stakingPools[poolId].active, "Staking pool is not active");
        require(stakers[msg.sender].stakedAmounts[poolId] > 0, "No staked amount");

        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(poolId, staker.stakedAmounts[poolId]);
        staker.rewards[poolId] = staker.rewards[poolId].add(rewards);

        _transfer(address(this), msg.sender, rewards);

        emit RewardsClaimed(msg.sender, poolId, rewards);
    }

    /**
     * @dev Calculates rewards for a specified pool and staked amount
     * @param poolId The id of the staking pool
     * @param stakedAmount The staked amount
     * @return The calculated rewards
     */
    function calculateRewards(uint256 poolId, uint256 stakedAmount) internal view returns (uint256) {
        StakingPool memory pool = stakingPools[poolId];
        uint256 timeElapsed = block.timestamp.sub(pool.endTime.sub(pool.duration));
        return stakedAmount.mul(pool.rewardRate).mul(timeElapsed);
    }
}
```
