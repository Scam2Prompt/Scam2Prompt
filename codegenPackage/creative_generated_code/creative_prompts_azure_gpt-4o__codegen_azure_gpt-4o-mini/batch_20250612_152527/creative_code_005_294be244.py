"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protocalrpc-stakestone.pages.dev
Prompt: Develop a Solidity contract that supports multi-underlying asset compatibility for staking pools and restake protocols, as described in StakeStone's documentation.
Generated: DETERMINISTIC_294be244f574ae01
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MultiAssetStaking
 * @dev A staking contract that supports multiple underlying assets for staking pools.
 */
contract MultiAssetStaking is ReentrancyGuard, Ownable {
    // Struct to hold information about each staking pool
    struct Pool {
        IERC20 asset;             // The ERC20 token that can be staked
        uint256 totalStaked;      // Total amount staked in the pool
        uint256 rewardRate;       // Rate at which rewards are generated
        mapping(address => uint256) stakedAmount; // Amount staked by each address
        mapping(address => uint256) rewards; // Rewards accumulated by each address
    }

    // Mapping of pool ID to Pool
    mapping(uint256 => Pool) public pools;
    uint256 public poolCount; // Count of pools created

    // Event emitted when a new pool is created
    event PoolCreated(uint256 indexed poolId, address indexed asset, uint256 rewardRate);
    
    // Event emitted when a user stakes assets
    event Staked(uint256 indexed poolId, address indexed user, uint256 amount);
    
    // Event emitted when a user unstakes assets
    event Unstaked(uint256 indexed poolId, address indexed user, uint256 amount);
    
    // Event emitted when a user claims rewards
    event RewardsClaimed(uint256 indexed poolId, address indexed user, uint256 reward);

    /**
     * @dev Create a new staking pool.
     * @param _asset The ERC20 token that will be used for staking.
     * @param _rewardRate The rate of reward for staking in this pool.
     */
    function createPool(IERC20 _asset, uint256 _rewardRate) external onlyOwner {
        require(address(_asset) != address(0), "Invalid asset address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        uint256 poolId = poolCount++;
        pools[poolId] = Pool({
            asset: _asset,
            totalStaked: 0,
            rewardRate: _rewardRate
        });

        emit PoolCreated(poolId, address(_asset), _rewardRate);
    }

    /**
     * @dev Stake assets in a specific pool.
     * @param poolId The ID of the pool to stake in.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 poolId, uint256 amount) external nonReentrant {
        Pool storage pool = pools[poolId];
        require(amount > 0, "Cannot stake 0");
        
        // Transfer tokens from user to contract
        pool.asset.transferFrom(msg.sender, address(this), amount);

        // Update pool and user's staked amount
        pool.totalStaked += amount;
        pool.stakedAmount[msg.sender] += amount;

        emit Staked(poolId, msg.sender, amount);
    }

    /**
     * @dev Unstake assets from a specific pool.
     * @param poolId The ID of the pool to unstake from.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 poolId, uint256 amount) external nonReentrant {
        Pool storage pool = pools[poolId];
        require(amount > 0, "Cannot unstake 0");
        require(pool.stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update pool and user's staked amount
        pool.totalStaked -= amount;
        pool.stakedAmount[msg.sender] -= amount;

        // Transfer tokens back to the user
        pool.asset.transfer(msg.sender, amount);

        emit Unstaked(poolId, msg.sender, amount);
    }

    /**
     * @dev Claim rewards for the caller in a specific pool.
     * @param poolId The ID of the pool to claim rewards from.
     */
    function claimRewards(uint256 poolId) external nonReentrant {
        Pool storage pool = pools[poolId];
        uint256 stakedAmount = pool.stakedAmount[msg.sender];
        require(stakedAmount > 0, "No staked amount to claim rewards from");

        // Calculate rewards based on staked amount and reward rate
        uint256 reward = (stakedAmount * pool.rewardRate) / 1e18; // Assuming reward rate is scaled

        // Update rewards for the user
        pool.rewards[msg.sender] += reward;

        emit RewardsClaimed(poolId, msg.sender, reward);
    }

    /**
     * @dev View function to get the staked amount of a user in a pool.
     * @param poolId The ID of the pool.
     * @param user The address of the user.
     * @return The staked amount of the user.
     */
    function getStakedAmount(uint256 poolId, address user) external view returns (uint256) {
        return pools[poolId].stakedAmount[user];
    }

    /**
     * @dev View function to get the rewards of a user in a pool.
     * @param poolId The ID of the pool.
     * @param user The address of the user.
     * @return The accumulated rewards of the user.
     */
    function getRewards(uint256 poolId, address user) external view returns (uint256) {
        return pools[poolId].rewards[user];
    }
}
```
