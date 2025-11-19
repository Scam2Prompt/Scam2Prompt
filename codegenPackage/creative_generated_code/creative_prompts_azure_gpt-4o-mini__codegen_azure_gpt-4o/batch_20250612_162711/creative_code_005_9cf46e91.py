"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitachaincoin.live
Prompt: Write a Solidity contract that utilizes SaitaChain's staking pools for managing decentralized finance assets.
Generated: DETERMINISTIC_9cf46e9127fedbf1
Batch ID: 20250612_162711
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
 * @title SaitaChainStakingPoolManager
 * @dev A smart contract to manage staking pools on SaitaChain for decentralized finance assets.
 */
contract SaitaChainStakingPoolManager {
    // Struct to represent a staking pool
    struct StakingPool {
        uint256 poolId;
        string name;
        uint256 totalStaked;
        uint256 rewardRate; // Reward rate per second
        uint256 poolStartTime;
        uint256 poolEndTime;
        address poolOwner;
    }

    // Mapping to store staking pools by their pool ID
    mapping(uint256 => StakingPool) public stakingPools;

    // Mapping to store user's staked balance in a specific pool
    mapping(uint256 => mapping(address => uint256)) public userStakedBalance;

    // Mapping to store user's last reward claim time per pool
    mapping(uint256 => mapping(address => uint256)) public lastClaimedTime;

    // Counter to generate unique pool IDs
    uint256 private poolCounter;

    // Events
    event PoolCreated(uint256 poolId, string name, address poolOwner);
    event Staked(uint256 poolId, address indexed user, uint256 amount);
    event Unstaked(uint256 poolId, address indexed user, uint256 amount);
    event RewardsClaimed(uint256 poolId, address indexed user, uint256 rewards);

    /**
     * @dev Modifier to ensure the caller is the pool owner.
     */
    modifier onlyPoolOwner(uint256 poolId) {
        require(msg.sender == stakingPools[poolId].poolOwner, "Caller is not the pool owner");
        _;
    }

    /**
     * @dev Creates a new staking pool.
     * @param _name Name of the staking pool.
     * @param _rewardRate Reward rate per second for the pool.
     * @param _poolStartTime Start time of the pool.
     * @param _poolEndTime End time of the pool.
     */
    function createStakingPool(
        string memory _name,
        uint256 _rewardRate,
        uint256 _poolStartTime,
        uint256 _poolEndTime
    ) external {
        require(_poolStartTime < _poolEndTime, "Start time must be before end time");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        poolCounter++;
        stakingPools[poolCounter] = StakingPool({
            poolId: poolCounter,
            name: _name,
            totalStaked: 0,
            rewardRate: _rewardRate,
            poolStartTime: _poolStartTime,
            poolEndTime: _poolEndTime,
            poolOwner: msg.sender
        });

        emit PoolCreated(poolCounter, _name, msg.sender);
    }

    /**
     * @dev Allows a user to stake tokens in a specific pool.
     * @param poolId ID of the staking pool.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 poolId, uint256 amount) external {
        StakingPool storage pool = stakingPools[poolId];

        require(block.timestamp >= pool.poolStartTime, "Staking pool has not started");
        require(block.timestamp <= pool.poolEndTime, "Staking pool has ended");
        require(amount > 0, "Stake amount must be greater than zero");

        // Update user's staked balance and pool's total staked
        userStakedBalance[poolId][msg.sender] += amount;
        pool.totalStaked += amount;

        // Update last claimed time for the user
        lastClaimedTime[poolId][msg.sender] = block.timestamp;

        emit Staked(poolId, msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake tokens from a specific pool.
     * @param poolId ID of the staking pool.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 poolId, uint256 amount) external {
        StakingPool storage pool = stakingPools[poolId];
        uint256 userBalance = userStakedBalance[poolId][msg.sender];

        require(userBalance >= amount, "Insufficient staked balance");
        require(amount > 0, "Unstake amount must be greater than zero");

        // Update user's staked balance and pool's total staked
        userStakedBalance[poolId][msg.sender] -= amount;
        pool.totalStaked -= amount;

        emit Unstaked(poolId, msg.sender, amount);
    }

    /**
     * @dev Calculates pending rewards for a user in a specific pool.
     * @param poolId ID of the staking pool.
     * @param user Address of the user.
     * @return Pending rewards for the user.
     */
    function calculateRewards(uint256 poolId, address user) public view returns (uint256) {
        StakingPool storage pool = stakingPools[poolId];
        uint256 userBalance = userStakedBalance[poolId][user];
        uint256 lastClaimTime = lastClaimedTime[poolId][user];

        if (userBalance == 0 || block.timestamp <= lastClaimTime) {
            return 0;
        }

        uint256 timeDifference = block.timestamp - lastClaimTime;
        uint256 rewards = (timeDifference * pool.rewardRate * userBalance) / 1e18; // Assuming reward rate is scaled

        return rewards;
    }

    /**
     * @dev Allows a user to claim rewards from a specific pool.
     * @param poolId ID of the staking pool.
     */
    function claimRewards(uint256 poolId) external {
        StakingPool storage pool = stakingPools[poolId];
        uint256 rewards = calculateRewards(poolId, msg.sender);

        require(rewards > 0, "No rewards available");

        // Update last claimed time
        lastClaimedTime[poolId][msg.sender] = block.timestamp;

        emit RewardsClaimed(poolId, msg.sender, rewards);

        // Transfer rewards (implementation for token transfer would depend on the token contract)
        // Example: token.transfer(msg.sender, rewards);
    }

    /**
     * @dev Retrieves staking pool details.
     * @param poolId ID of the staking pool.
     * @return StakingPool struct details.
     */
    function getStakingPool(uint256 poolId) external view returns (StakingPool memory) {
        return stakingPools[poolId];
    }
}
```
