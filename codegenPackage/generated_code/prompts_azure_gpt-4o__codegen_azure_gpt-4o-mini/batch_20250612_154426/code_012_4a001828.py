"""
Generated Code Metadata:
========================
Original URL: https://mike-token-web-1rj55ugoo-percenal-miketoken.vercel.app
Prompt: Develop a smart contract in Solidity for compounding rewards in farming pools for Mike Token ($MKT), with support for multiple token pairs.
Generated: DETERMINISTIC_4a0018280ce85736
Batch ID: 20250612_154426
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for compounding rewards in farming pools for Mike Token ($MKT)
contract FarmingPool is Ownable {
    // Struct to hold information about each farming pool
    struct Pool {
        IERC20 token; // The token being farmed
        uint256 rewardRate; // The rate at which rewards are generated
        uint256 lastUpdate; // Last time rewards were updated
        uint256 totalStaked; // Total amount staked in the pool
    }

    // Mapping of pool ID to Pool struct
    mapping(uint256 => Pool) public pools;
    // Mapping of user addresses to their staked amounts and rewards
    mapping(uint256 => mapping(address => uint256)) public stakedAmount;
    mapping(uint256 => mapping(address => uint256)) public rewards;

    // Event emitted when a user stakes tokens
    event Staked(uint256 indexed poolId, address indexed user, uint256 amount);
    // Event emitted when a user withdraws tokens
    event Withdrawn(uint256 indexed poolId, address indexed user, uint256 amount);
    // Event emitted when rewards are compounded
    event Compounded(uint256 indexed poolId, address indexed user, uint256 reward);

    // Modifier to check if the pool exists
    modifier poolExists(uint256 poolId) {
        require(address(pools[poolId].token) != address(0), "Pool does not exist");
        _;
    }

    // Function to create a new farming pool
    function createPool(uint256 poolId, IERC20 token, uint256 rewardRate) external onlyOwner {
        require(address(token) != address(0), "Invalid token address");
        require(pools[poolId].token == IERC20(address(0)), "Pool already exists");

        pools[poolId] = Pool({
            token: token,
            rewardRate: rewardRate,
            lastUpdate: block.timestamp,
            totalStaked: 0
        });
    }

    // Function to stake tokens in a pool
    function stake(uint256 poolId, uint256 amount) external poolExists(poolId) {
        require(amount > 0, "Amount must be greater than zero");

        Pool storage pool = pools[poolId];
        updateRewards(poolId, msg.sender);

        pool.token.transferFrom(msg.sender, address(this), amount);
        stakedAmount[poolId][msg.sender] += amount;
        pool.totalStaked += amount;

        emit Staked(poolId, msg.sender, amount);
    }

    // Function to withdraw staked tokens from a pool
    function withdraw(uint256 poolId, uint256 amount) external poolExists(poolId) {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[poolId][msg.sender] >= amount, "Insufficient staked amount");

        updateRewards(poolId, msg.sender);

        Pool storage pool = pools[poolId];
        stakedAmount[poolId][msg.sender] -= amount;
        pool.totalStaked -= amount;
        pool.token.transfer(msg.sender, amount);

        emit Withdrawn(poolId, msg.sender, amount);
    }

    // Function to compound rewards
    function compound(uint256 poolId) external poolExists(poolId) {
        updateRewards(poolId, msg.sender);
        uint256 reward = rewards[poolId][msg.sender];
        require(reward > 0, "No rewards to compound");

        rewards[poolId][msg.sender] = 0;
        stakedAmount[poolId][msg.sender] += reward;
        pools[poolId].totalStaked += reward;

        emit Compounded(poolId, msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function updateRewards(uint256 poolId, address user) internal {
        Pool storage pool = pools[poolId];
        uint256 timeElapsed = block.timestamp - pool.lastUpdate;

        if (timeElapsed > 0 && pool.totalStaked > 0) {
            uint256 reward = (timeElapsed * pool.rewardRate * stakedAmount[poolId][user]) / pool.totalStaked;
            rewards[poolId][user] += reward;
        }

        pool.lastUpdate = block.timestamp;
    }

    // Function to get the pending rewards for a user
    function pendingRewards(uint256 poolId, address user) external view poolExists(poolId) returns (uint256) {
        Pool storage pool = pools[poolId];
        uint256 timeElapsed = block.timestamp - pool.lastUpdate;
        uint256 reward = (timeElapsed * pool.rewardRate * stakedAmount[poolId][user]) / pool.totalStaked;

        return rewards[poolId][user] + reward;
    }
}
```
