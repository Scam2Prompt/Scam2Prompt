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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Struct to store details of each staking pool
struct StakingPool {
    uint256 lockTerm; // Lock term in seconds
    uint256 rewardRate; // Reward rate per lock term
    uint256 tierBoost; // Boost percentage for the tier
    uint256 totalStaked; // Total staked amount in the pool
    mapping(address => uint256) stakes; // User stakes in the pool
    mapping(address => uint256) rewards; // User accrued rewards
}

// Smart contract for multi-staking pools
contract MultiStakingPool is Ownable, ReentrancyGuard {
    // Mapping of pool IDs to StakingPools
    mapping(uint256 => StakingPool) public stakingPools;
    // Counter for the number of pools
    uint256 public poolCount;
    // ERC20 token for staking
    IERC20 public aitechToken;

    // Events for logging actions
    event PoolCreated(uint256 indexed poolId, uint256 lockTerm, uint256 rewardRate, uint256 tierBoost);
    event Staked(uint256 indexed poolId, address indexed staker, uint256 amount);
    event Unstaked(uint256 indexed poolId, address indexed staker, uint256 amount);
    event RewardsClaimed(uint256 indexed poolId, address indexed staker, uint256 reward);

    // Constructor to initialize the token
    constructor(IERC20 _aitechToken) {
        aitechToken = _aitechToken;
    }

    // Function to create a new staking pool
    function createPool(uint256 _lockTerm, uint256 _rewardRate, uint256 _tierBoost) external onlyOwner {
        require(_lockTerm > 0, "Lock term must be greater than zero");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        require(_tierBoost >= 0, "Tier boost must be non-negative");

        StakingPool storage newPool = stakingPools[poolCount];
        newPool.lockTerm = _lockTerm;
        newPool.rewardRate = _rewardRate;
        newPool.tierBoost = _tierBoost;

        emit PoolCreated(poolCount, _lockTerm, _rewardRate, _tierBoost);
        poolCount++;
    }

    // Function to stake tokens in a specified pool
    function stake(uint256 poolId, uint256 amount) external nonReentrant {
        require(poolId < poolCount, "Invalid pool ID");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the staker to the contract
        aitechToken.transferFrom(msg.sender, address(this), amount);

        StakingPool storage pool = stakingPools[poolId];

        // Update the staker's stake and total staked amount
        pool.stakes[msg.sender] += amount;
        pool.totalStaked += amount;

        emit Staked(poolId, msg.sender, amount);
    }

    // Function to unstake tokens from a specified pool
    function unstake(uint256 poolId) external nonReentrant {
        require(poolId < poolCount, "Invalid pool ID");
        StakingPool storage pool = stakingPools[poolId];

        uint256 userStake = pool.stakes[msg.sender];
        require(userStake > 0, "No staked amount");

        // Ensure the lock term has expired
        // Note: In production, you should implement a timestamp tracking mechanism
        require(block.timestamp >= pool.lockTerm, "Lock term not expired");

        // Update the user's stake and total staked amount
        pool.totalStaked -= userStake;
        pool.stakes[msg.sender] = 0;

        // Transfer tokens back to the staker
        aitechToken.transfer(msg.sender, userStake);

        emit Unstaked(poolId, msg.sender, userStake);
    }

    // Function to claim rewards for a specified pool
    function claimRewards(uint256 poolId) external nonReentrant {
        require(poolId < poolCount, "Invalid pool ID");
        StakingPool storage pool = stakingPools[poolId];

        uint256 reward = calculateRewards(msg.sender, poolId);
        require(reward > 0, "No rewards available");

        // Reset the user's accrued rewards
        pool.rewards[msg.sender] = 0;

        // Transfer rewards to the staker
        aitechToken.transfer(msg.sender, reward);

        emit RewardsClaimed(poolId, msg.sender, reward);
    }

    // Function to calculate rewards for a user in a specified pool
    function calculateRewards(address staker, uint256 poolId) internal view returns (uint256) {
        StakingPool storage pool = stakingPools[poolId];
        uint256 userStake = pool.stakes[staker];

        // Example reward calculation based on stake and reward rate
        return (userStake * pool.rewardRate * pool.tierBoost) / 100;
    }

    // Function to retrieve the user's stake in a specified pool
    function userStakeInPool(address user, uint256 poolId) external view returns (uint256) {
        return stakingPools[poolId].stakes[user];
    }

    // Function to retrieve the total rewards accrued by a user in a specified pool
    function userRewardsInPool(address user, uint256 poolId) external view returns (uint256) {
        return calculateRewards(user, poolId);
    }
}
```
