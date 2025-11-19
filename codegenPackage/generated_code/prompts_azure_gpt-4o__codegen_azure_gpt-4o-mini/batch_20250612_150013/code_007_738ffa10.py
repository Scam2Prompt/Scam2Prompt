"""
Generated Code Metadata:
========================
Original URL: https://popofrogs.pages.dev
Prompt: Write code in Solidity for a staking mechanism that supports two pools: one with locked schedules for higher returns and another with flexible withdrawal options, as described in "The War Chest."
Generated: DETERMINISTIC_738ffa1022fc0498
Batch ID: 20250612_150013
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

contract StakingMechanism {
    // Struct to hold information about each staking pool
    struct Pool {
        uint256 totalStaked;
        uint256 rewardRate; // Annual reward rate in basis points (1% = 100 basis points)
        uint256 lockDuration; // Duration for locked pool in seconds
        bool isLocked; // Indicates if the pool is locked
    }

    // Struct to hold information about each user's stake
    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Timestamp when the stake was made
        bool isLocked; // Indicates if the stake is in a locked pool
    }

    // Mapping of pool ID to Pool details
    mapping(uint256 => Pool) public pools;
    // Mapping of user address to their stakes
    mapping(address => mapping(uint256 => Stake)) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 poolId, uint256 amount);
    event Unstaked(address indexed user, uint256 poolId, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 poolId, uint256 amount);

    // Constructor to initialize pools
    constructor() {
        // Initialize locked pool with higher returns
        pools[1] = Pool({
            totalStaked: 0,
            rewardRate: 500, // 5% annual return
            lockDuration: 30 days,
            isLocked: true
        });

        // Initialize flexible pool with lower returns
        pools[2] = Pool({
            totalStaked: 0,
            rewardRate: 200, // 2% annual return
            lockDuration: 0,
            isLocked: false
        });
    }

    // Function to stake tokens in a specified pool
    function stake(uint256 poolId, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(poolId == 1 || poolId == 2, "Invalid pool ID");

        // Update the user's stake
        stakes[msg.sender][poolId].amount += amount;
        stakes[msg.sender][poolId].startTime = block.timestamp;
        stakes[msg.sender][poolId].isLocked = pools[poolId].isLocked;

        // Update the pool's total staked amount
        pools[poolId].totalStaked += amount;

        emit Staked(msg.sender, poolId, amount);
    }

    // Function to unstake tokens from a specified pool
    function unstake(uint256 poolId) external {
        Stake storage userStake = stakes[msg.sender][poolId];
        require(userStake.amount > 0, "No stake found");
        
        // Check if the pool is locked and if the lock duration has passed
        if (pools[poolId].isLocked) {
            require(block.timestamp >= userStake.startTime + pools[poolId].lockDuration, "Stake is still locked");
        }

        // Update the pool's total staked amount
        pools[poolId].totalStaked -= userStake.amount;

        // Transfer the staked amount back to the user
        // Note: In a real implementation, you would transfer tokens here
        // e.g., token.transfer(msg.sender, userStake.amount);

        emit Unstaked(msg.sender, poolId, userStake.amount);
        userStake.amount = 0; // Reset user's stake
    }

    // Function to calculate rewards for a user in a specified pool
    function calculateRewards(address user, uint256 poolId) public view returns (uint256) {
        Stake storage userStake = stakes[user][poolId];
        if (userStake.amount == 0) return 0;

        uint256 duration = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * pools[poolId].rewardRate * duration) / (365 days * 10000); // Annualized reward

        return reward;
    }

    // Function to claim rewards for a user in a specified pool
    function claimRewards(uint256 poolId) external {
        uint256 rewards = calculateRewards(msg.sender, poolId);
        require(rewards > 0, "No rewards to claim");

        // Note: In a real implementation, you would transfer rewards here
        // e.g., token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, poolId, rewards);
    }
}
```
