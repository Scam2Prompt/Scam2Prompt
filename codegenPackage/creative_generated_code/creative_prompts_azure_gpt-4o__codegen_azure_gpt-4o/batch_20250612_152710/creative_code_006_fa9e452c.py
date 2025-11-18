"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Develop a smart contract that supports multiple staking pools for AITECH tokens with varying lock terms, reward compositions, and tier boosts, as outlined on the Solidus AI Tech platform.
Generated: DETERMINISTIC_fa9e452cb2af083b
Batch ID: 20250612_152710
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

/**
 * @title MultiPoolStakingContract
 * @dev Smart contract for staking AITECH tokens with multiple staking pools, lock terms, tier boosts, and reward compositions.
 */
contract MultiPoolStakingContract {
    // Struct to represent a staking pool
    struct Pool {
        uint256 lockTerm; // Locking period in seconds
        uint256 rewardRate; // Reward rate per second
        uint256 tierBoost; // Boost percentage for higher tiers
        uint256 totalStaked; // Total tokens staked in the pool
        mapping(address => uint256) stakes; // Mapping of user stakes
        mapping(address => uint256) stakeTimestamps; // Mapping of user stake timestamps
    }

    // AITECH token interface
    IERC20 public immutable AITECH;

    // Mapping of pools (pool ID => Pool)
    mapping(uint256 => Pool) public pools;

    // Event declarations
    event Staked(address indexed user, uint256 poolId, uint256 amount);
    event Unstaked(address indexed user, uint256 poolId, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to set up the AITECH token address
     * @param _aitech Address of the AITECH token
     */
    constructor(address _aitech) {
        require(_aitech != address(0), "Invalid token address");
        AITECH = IERC20(_aitech);
    }

    /**
     * @dev Function to create a new staking pool
     * @param poolId Unique identifier for the pool
     * @param lockTerm Locking period in seconds
     * @param rewardRate Reward rate per second
     * @param tierBoost Boost percentage for higher tiers (e.g., 10 for 10%)
     */
    function createPool(
        uint256 poolId,
        uint256 lockTerm,
        uint256 rewardRate,
        uint256 tierBoost
    ) external {
        require(pools[poolId].lockTerm == 0, "Pool already exists");
        pools[poolId] = Pool({
            lockTerm: lockTerm,
            rewardRate: rewardRate,
            tierBoost: tierBoost,
            totalStaked: 0
        });
    }

    /**
     * @dev Stake tokens in a specific pool
     * @param poolId ID of the pool
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 poolId, uint256 amount) external {
        Pool storage pool = pools[poolId];
        require(pool.lockTerm > 0, "Invalid pool");
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens to the contract
        require(AITECH.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking details
        pool.stakes[msg.sender] += amount;
        pool.stakeTimestamps[msg.sender] = block.timestamp;
        pool.totalStaked += amount;

        emit Staked(msg.sender, poolId, amount);
    }

    /**
     * @dev Unstake tokens from a specific pool
     * @param poolId ID of the pool
     */
    function unstake(uint256 poolId) external {
        Pool storage pool = pools[poolId];
        require(pool.lockTerm > 0, "Invalid pool");
        require(pool.stakes[msg.sender] > 0, "No stake found");

        uint256 amount = pool.stakes[msg.sender];
        uint256 stakedTime = pool.stakeTimestamps[msg.sender];
        require(block.timestamp >= stakedTime + pool.lockTerm, "Tokens are still locked");

        // Calculate rewards
        uint256 duration = block.timestamp - stakedTime;
        uint256 reward = (amount * pool.rewardRate * duration) / 1e18;

        // Apply tier boost
        if (pool.tierBoost > 0) {
            reward += (reward * pool.tierBoost) / 100;
        }

        // Update staking details
        pool.stakes[msg.sender] = 0;
        pool.totalStaked -= amount;

        // Transfer tokens and rewards to the user
        require(AITECH.transfer(msg.sender, amount + reward), "Token transfer failed");

        emit Unstaked(msg.sender, poolId, amount, reward);
    }

    /**
     * @dev Get the current stake and reward for a user in a pool
     * @param poolId ID of the pool
     * @param user Address of the user
     * @return stake Amount staked
     * @return reward Current reward
     */
    function getStakeInfo(uint256 poolId, address user) external view returns (uint256 stake, uint256 reward) {
        Pool storage pool = pools[poolId];
        require(pool.lockTerm > 0, "Invalid pool");

        stake = pool.stakes[user];
        if (stake > 0) {
            uint256 duration = block.timestamp - pool.stakeTimestamps[user];
            reward = (stake * pool.rewardRate * duration) / 1e18;

            // Apply tier boost
            if (pool.tierBoost > 0) {
                reward += (reward * pool.tierBoost) / 100;
            }
        }
    }
}

// Minimal IERC20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
