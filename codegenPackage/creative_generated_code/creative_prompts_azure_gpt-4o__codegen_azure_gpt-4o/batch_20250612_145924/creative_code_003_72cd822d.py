"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: Create a smart contract on the Base chain that supports cross-pool staking programs for $MAFIA tokens and other meme coin projects.
Generated: DETERMINISTIC_72cd822d893a8d43
Batch ID: 20250612_145924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready smart contract written in Solidity for cross-pool staking programs. The contract is designed generically for the Base chain and supports staking $MAFIA tokens and other meme coins.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title CrossPoolStaking
 * @dev A smart contract for cross-pool staking programs for $MAFIA tokens and other meme coins.
 */
contract CrossPoolStaking {
    // Struct for holding staking pool information
    struct Pool {
        address token; // Address of the stakable token
        uint256 rewardRate; // Reward rate (tokens per second)
        uint256 totalStaked; // Total tokens staked in the pool
        uint256 lastUpdated; // Last time the rewards were updated
        uint256 rewardPerTokenStored; // Accumulated rewards per token (scaled by 1e18)
    }

    // Struct for holding staker information in a specific pool
    struct Staker {
        uint256 balance; // Amount of tokens staked by the user
        uint256 rewardDebt; // Rewards already accounted for
        uint256 pendingRewards; // Pending rewards to be claimed
    }

    // State variables
    address public owner; // Contract owner
    mapping(uint256 => Pool) public pools; // Pool ID -> Pool details
    mapping(uint256 => mapping(address => Staker)) public stakers; // Pool ID -> Staker address -> Staker details
    uint256 public poolCount; // Total number of pools

    // Events
    event PoolCreated(uint256 poolId, address token, uint256 rewardRate);
    event Staked(address indexed user, uint256 poolId, uint256 amount);
    event Withdrawn(address indexed user, uint256 poolId, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 poolId, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    modifier updatePool(uint256 poolId) {
        Pool storage pool = pools[poolId];
        uint256 currentTime = block.timestamp;
        if (currentTime > pool.lastUpdated && pool.totalStaked > 0) {
            uint256 timeElapsed = currentTime - pool.lastUpdated;
            uint256 reward = timeElapsed * pool.rewardRate;
            pool.rewardPerTokenStored += (reward * 1e18) / pool.totalStaked;
        }
        pool.lastUpdated = currentTime;
        _;
    }

    modifier updateRewards(uint256 poolId, address staker) {
        Pool storage pool = pools[poolId];
        Staker storage user = stakers[poolId][staker];
        user.pendingRewards +=
            ((user.balance * (pool.rewardPerTokenStored - user.rewardDebt)) / 1e18);
        user.rewardDebt = pool.rewardPerTokenStored;
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Creates a new staking pool.
     * @param token Address of the stakable token.
     * @param rewardRate Reward rate (tokens per second).
     */
    function createPool(address token, uint256 rewardRate) external onlyOwner {
        require(token != address(0), "Invalid token address");
        pools[poolCount] = Pool({
            token: token,
            rewardRate: rewardRate,
            totalStaked: 0,
            lastUpdated: block.timestamp,
            rewardPerTokenStored: 0
        });
        emit PoolCreated(poolCount, token, rewardRate);
        poolCount++;
    }

    /**
     * @dev Stake tokens into a specified pool.
     * @param poolId ID of the staking pool.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 poolId, uint256 amount)
        external
        updatePool(poolId)
        updateRewards(poolId, msg.sender)
    {
        require(amount > 0, "Amount must be greater than zero");
        Pool storage pool = pools[poolId];
        Staker storage user = stakers[poolId][msg.sender];

        // Transfer tokens from user to contract
        require(
            IERC20(pool.token).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        user.balance += amount;
        pool.totalStaked += amount;

        emit Staked(msg.sender, poolId, amount);
    }

    /**
     * @dev Withdraw staked tokens from a specified pool.
     * @param poolId ID of the staking pool.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 poolId, uint256 amount)
        external
        updatePool(poolId)
        updateRewards(poolId, msg.sender)
    {
        require(amount > 0, "Amount must be greater than zero");
        Pool storage pool = pools[poolId];
        Staker storage user = stakers[poolId][msg.sender];
        require(user.balance >= amount, "Insufficient balance");

        user.balance -= amount;
        pool.totalStaked -= amount;

        // Transfer tokens back to the user
        require(IERC20(pool.token).transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, poolId, amount);
    }

    /**
     * @dev Claim rewards from a specified pool.
     * @param poolId ID of the staking pool.
     */
    function claimRewards(uint256 poolId)
        external
        updatePool(poolId)
        updateRewards(poolId, msg.sender)
    {
        Staker storage user = stakers[poolId][msg.sender];
        uint256 reward = user.pendingRewards;
        require(reward > 0, "No rewards to claim");

        user.pendingRewards = 0;

        // Transfer rewards to the user
        Pool storage pool = pools[poolId];
        require(IERC20(pool.token).transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, poolId, reward);
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

Ensure you deploy the contract on the Base chain and test it thoroughly before using it in production.
