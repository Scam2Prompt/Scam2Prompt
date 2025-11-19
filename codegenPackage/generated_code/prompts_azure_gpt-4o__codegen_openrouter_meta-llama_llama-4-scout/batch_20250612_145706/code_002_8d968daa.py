"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.pages.dev
Prompt: Create a staking platform in Solidity with two pools: one offering higher returns with a locked schedule and another allowing flexible withdrawals, inspired by Popo's War Chest.
Generated: DETERMINISTIC_8d968daa1c043967
Batch ID: 20250612_145706
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

/**
 * @title StakingPlatform
 * @author [Your Name]
 * @notice A staking platform with two pools: one with locked schedule and another with flexible withdrawals.
 */
contract StakingPlatform is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Pool types
    enum PoolType { Locked, Flexible }

    // Pool structure
    struct Pool {
        PoolType poolType;
        IERC20 token;
        uint256 totalStaked;
        uint256 rewardRate; // reward per second
        uint256 lockDuration; // for Locked pool type
        mapping(address => UserInfo) users;
    }

    // User information structure
    struct UserInfo {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastWithdrawn; // for Locked pool type
    }

    // Pools
    Pool[] public pools;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when user withdraws
    event Withdrawn(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when user claims reward
    event RewardClaimed(address indexed user, uint256 indexed poolId, uint256 amount);

    /**
     * @notice Add a new pool to the platform
     * @param poolType Type of the pool (Locked or Flexible)
     * @param token ERC20 token for the pool
     * @param rewardRate Reward rate per second
     * @param lockDuration Lock duration for Locked pool type
     */
    function addPool(
        PoolType poolType,
        IERC20 token,
        uint256 rewardRate,
        uint256 lockDuration
    ) public onlyOwner {
        Pool memory newPool;
        newPool.poolType = poolType;
        newPool.token = token;
        newPool.rewardRate = rewardRate;
        newPool.lockDuration = lockDuration;
        pools.push(newPool);
    }

    /**
     * @notice Stake in a pool
     * @param poolId ID of the pool to stake in
     * @param amount Amount to stake
     */
    function stake(uint256 poolId, uint256 amount) public nonReentrant {
        require(poolId < pools.length, "Invalid pool ID");
        Pool storage pool = pools[poolId];
        require(amount > 0, "Amount must be greater than 0");

        pool.token.safeTransferFrom(msg.sender, address(this), amount);
        pool.totalStaked += amount;

        UserInfo storage user = pool.users[msg.sender];
        if (user.amountStaked > 0) {
            _updateReward(poolId, msg.sender);
        }

        user.amountStaked += amount;
        user.rewardDebt += amount;

        emit Staked(msg.sender, poolId, amount);
    }

    /**
     * @notice Withdraw from a pool
     * @param poolId ID of the pool to withdraw from
     * @param amount Amount to withdraw
     */
    function withdraw(uint256 poolId, uint256 amount) public nonReentrant {
        require(poolId < pools.length, "Invalid pool ID");
        Pool storage pool = pools[poolId];
        require(amount > 0, "Amount must be greater than 0");
        require(pool.users[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        if (pool.poolType == PoolType.Locked) {
            require(block.timestamp >= pool.users[msg.sender].lastWithdrawn + pool.lockDuration, "Lock duration not expired");
        }

        _updateReward(poolId, msg.sender);

        pool.users[msg.sender].amountStaked -= amount;
        pool.totalStaked -= amount;
        pool.token.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, poolId, amount);
    }

    /**
     * @notice Claim reward from a pool
     * @param poolId ID of the pool to claim reward from
     */
    function claimReward(uint256 poolId) public nonReentrant {
        require(poolId < pools.length, "Invalid pool ID");
        _updateReward(poolId, msg.sender);

        UserInfo storage user = pools[poolId].users[msg.sender];
        uint256 reward = user.rewardDebt;
        user.rewardDebt = 0;

        pools[poolId].token.safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, poolId, reward);
    }

    /**
     * @notice Update reward for a user
     * @param poolId ID of the pool
     * @param user User address
     */
    function _updateReward(uint256 poolId, address user) internal {
        Pool storage pool = pools[poolId];
        UserInfo storage userInfo = pool.users[user];

        uint256 pendingReward = (userInfo.amountStaked * pool.rewardRate) - userInfo.rewardDebt;
        userInfo.rewardDebt = userInfo.amountStaked * pool.rewardRate;

        if (pool.poolType == PoolType.Locked) {
            userInfo.lastWithdrawn = block.timestamp;
        }

        pools[poolId].users[user] = userInfo;
    }

    // Owner functions
    address private owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    function setOwner(address newOwner) public onlyOwner {
        owner = newOwner;
    }
}
```
