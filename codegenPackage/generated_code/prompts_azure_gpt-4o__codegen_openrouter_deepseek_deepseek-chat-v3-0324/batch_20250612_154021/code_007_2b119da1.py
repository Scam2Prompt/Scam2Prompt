"""
Generated Code Metadata:
========================
Original URL: https://asterdx.com
Prompt: Write a Solidity smart contract to integrate staking functionality for assets like CAKE and BTC, inspired by Aster's staking model.
Generated: DETERMINISTIC_2b119da10ed616f4
Batch ID: 20250612_154021
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingContract is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staking pool
    struct PoolInfo {
        IERC20 stakingToken;       // Address of the staking token contract
        IERC20 rewardToken;        // Address of the reward token contract
        uint256 rewardRate;        // Reward tokens distributed per second
        uint256 lastUpdateTime;    // Last time reward distribution was updated
        uint256 rewardPerTokenStored; // Accumulated rewards per token
        uint256 totalStaked;       // Total amount of tokens staked in the pool
    }

    // Struct to track user staking information
    struct UserInfo {
        uint256 amount;            // Amount of tokens staked by user
        uint256 rewards;           // Reward amount claimable by user
        uint256 userRewardPerTokenPaid; // User's reward per token paid
    }

    // Mapping from pool index to PoolInfo
    mapping(uint256 => PoolInfo) public pools;

    // Mapping from user address to pool index to UserInfo
    mapping(address => mapping(uint256 => UserInfo)) public userInfo;

    // Array of all pool indices
    uint256[] public poolIndices;

    // Events
    event PoolAdded(uint256 indexed poolId, address stakingToken, address rewardToken);
    event Staked(address indexed user, uint256 indexed poolId, uint256 amount);
    event Withdrawn(address indexed user, uint256 indexed poolId, uint256 amount);
    event RewardPaid(address indexed user, uint256 indexed poolId, uint256 reward);

    // Add a new staking pool
    function addPool(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardRate
    ) external onlyOwner {
        require(address(_stakingToken) != address(0), "Invalid staking token");
        require(address(_rewardToken) != address(0), "Invalid reward token");
        require(_rewardRate > 0, "Reward rate must be positive");

        uint256 poolId = poolIndices.length;
        pools[poolId] = PoolInfo({
            stakingToken: _stakingToken,
            rewardToken: _rewardToken,
            rewardRate: _rewardRate,
            lastUpdateTime: block.timestamp,
            rewardPerTokenStored: 0,
            totalStaked: 0
        });
        poolIndices.push(poolId);

        emit PoolAdded(poolId, address(_stakingToken), address(_rewardToken));
    }

    // Update reward variables for a pool
    function updatePool(uint256 poolId) internal {
        PoolInfo storage pool = pools[poolId];
        if (pool.totalStaked == 0) {
            pool.lastUpdateTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - pool.lastUpdateTime;
        uint256 reward = timeElapsed * pool.rewardRate;
        pool.rewardPerTokenStored += (reward * 1e18) / pool.totalStaked;
        pool.lastUpdateTime = block.timestamp;
    }

    // Calculate earned rewards for a user in a pool
    function earned(address account, uint256 poolId) public view returns (uint256) {
        UserInfo storage user = userInfo[account][poolId];
        PoolInfo storage pool = pools[poolId];

        uint256 currentRewardPerToken = pool.rewardPerTokenStored;
        if (pool.totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - pool.lastUpdateTime;
            uint256 reward = timeElapsed * pool.rewardRate;
            currentRewardPerToken += (reward * 1e18) / pool.totalStaked;
        }

        return (user.amount * (currentRewardPerToken - user.userRewardPerTokenPaid)) / 1e18 + user.rewards;
    }

    // Stake tokens into a pool
    function stake(uint256 poolId, uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        PoolInfo storage pool = pools[poolId];
        UserInfo storage user = userInfo[msg.sender][poolId];

        updatePool(poolId);
        if (user.amount > 0) {
            user.rewards = earned(msg.sender, poolId);
        }
        user.userRewardPerTokenPaid = pool.rewardPerTokenStored;

        pool.totalStaked += amount;
        user.amount += amount;
        pool.stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, poolId, amount);
    }

    // Withdraw staked tokens from a pool
    function withdraw(uint256 poolId, uint256 amount) public nonReentrant {
        require(amount > 0, "Cannot withdraw 0");
        PoolInfo storage pool = pools[poolId];
        UserInfo storage user = userInfo[msg.sender][poolId];
        require(user.amount >= amount, "Withdraw amount exceeds balance");

        updatePool(poolId);
        user.rewards = earned(msg.sender, poolId);
        user.userRewardPerTokenPaid = pool.rewardPerTokenStored;

        pool.totalStaked -= amount;
        user.amount -= amount;
        pool.stakingToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, poolId, amount);
    }

    // Claim rewards from a pool
    function getReward(uint256 poolId) public nonReentrant {
        PoolInfo storage pool = pools[poolId];
        UserInfo storage user = userInfo[msg.sender][poolId];

        updatePool(poolId);
        uint256 reward = earned(msg.sender, poolId);
        if (reward > 0) {
            user.rewards = 0;
            user.userRewardPerTokenPaid = pool.rewardPerTokenStored;
            pool.rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, poolId, reward);
        }
    }

    // Exit a pool by withdrawing all staked tokens and claiming rewards
    function exit(uint256 poolId) external {
        withdraw(poolId, userInfo[msg.sender][poolId].amount);
        getReward(poolId);
    }

    // Emergency function to recover ERC20 tokens sent by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }

    // Update reward rate for a pool
    function setRewardRate(uint256 poolId, uint256 _rewardRate) external onlyOwner {
        updatePool(poolId);
        pools[poolId].rewardRate = _rewardRate;
    }
}
```
