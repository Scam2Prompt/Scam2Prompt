"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webdappsconnectprotocol.pages.dev
Prompt: Generate a smart contract that incorporates Micropools and rapid liquidity features as outlined in the DeFi Protocol documentation.
Generated: DETERMINISTIC_7edea8348be9b301
Batch ID: 20250612_150440
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
 * @title Micropool and Rapid Liquidity Smart Contract
 * @dev Implements a decentralized finance (DeFi) protocol with features for micropools and rapid liquidity.
 */
contract MicropoolLiquidity {

    // Represents a Liquidity Pool
    struct Pool {
        address owner;             // Address of the pool creator
        uint256 totalLiquidity;    // Total liquidity in the pool
        uint256 micropoolSize;     // Maximum size of each micropool
        bool isActive;             // Status of the pool (active/inactive)
    }

    // Represents a Micropool
    struct Micropool {
        uint256 poolId;            // ID of the parent pool
        address contributor;       // Address of the contributor
        uint256 amount;            // Liquidity contributed
    }

    // Mapping to store all liquidity pools
    mapping(uint256 => Pool) public pools;

    // Mapping to store micropools by their parent pool ID
    mapping(uint256 => Micropool[]) public micropools;

    // Counter for pool IDs
    uint256 private poolCounter;

    // Event emitted when a new pool is created
    event PoolCreated(uint256 poolId, address indexed owner, uint256 micropoolSize);

    // Event emitted when liquidity is added to a micropool
    event LiquidityAdded(uint256 poolId, address indexed contributor, uint256 amount);

    // Event emitted when liquidity is withdrawn
    event LiquidityWithdrawn(uint256 poolId, address indexed contributor, uint256 amount);

    /**
     * @dev Creates a new liquidity pool.
     * @param micropoolSize The maximum size of each micropool in the pool.
     */
    function createPool(uint256 micropoolSize) external {
        require(micropoolSize > 0, "Micropool size must be greater than zero");

        poolCounter++;
        pools[poolCounter] = Pool({
            owner: msg.sender,
            totalLiquidity: 0,
            micropoolSize: micropoolSize,
            isActive: true
        });

        emit PoolCreated(poolCounter, msg.sender, micropoolSize);
    }

    /**
     * @dev Adds liquidity to a pool by creating a new micropool.
     * @param poolId The ID of the pool to contribute to.
     */
    function addLiquidity(uint256 poolId) external payable {
        Pool storage pool = pools[poolId];
        require(pool.isActive, "Pool is not active");
        require(msg.value > 0, "Liquidity amount must be greater than zero");
        require(msg.value <= pool.micropoolSize, "Exceeds micropool size limit");

        micropools[poolId].push(Micropool({
            poolId: poolId,
            contributor: msg.sender,
            amount: msg.value
        }));

        pool.totalLiquidity += msg.value;

        emit LiquidityAdded(poolId, msg.sender, msg.value);
    }

    /**
     * @dev Withdraws liquidity from a micropool.
     * @param poolId The ID of the pool to withdraw from.
     */
    function withdrawLiquidity(uint256 poolId) external {
        Micropool[] storage poolMicropools = micropools[poolId];
        uint256 withdrawAmount = 0;

        // Iterate through micropools to find the user's contribution
        for (uint256 i = 0; i < poolMicropools.length; i++) {
            if (poolMicropools[i].contributor == msg.sender) {
                withdrawAmount += poolMicropools[i].amount;

                // Remove the micropool by swapping it with the last element and popping the array
                poolMicropools[i] = poolMicropools[poolMicropools.length - 1];
                poolMicropools.pop();
            }
        }

        require(withdrawAmount > 0, "No liquidity to withdraw");

        Pool storage pool = pools[poolId];
        pool.totalLiquidity -= withdrawAmount;

        // Transfer the withdrawn amount to the user
        payable(msg.sender).transfer(withdrawAmount);

        emit LiquidityWithdrawn(poolId, msg.sender, withdrawAmount);
    }

    /**
     * @dev Deactivates a pool, preventing further contributions.
     * @param poolId The ID of the pool to deactivate.
     */
    function deactivatePool(uint256 poolId) external {
        Pool storage pool = pools[poolId];
        require(pool.owner == msg.sender, "Only the pool owner can deactivate the pool");
        require(pool.isActive, "Pool is already inactive");

        pool.isActive = false;
    }

    /**
     * @dev Reactivates a pool, allowing contributions again.
     * @param poolId The ID of the pool to reactivate.
     */
    function reactivatePool(uint256 poolId) external {
        Pool storage pool = pools[poolId];
        require(pool.owner == msg.sender, "Only the pool owner can reactivate the pool");
        require(!pool.isActive, "Pool is already active");

        pool.isActive = true;
    }

    /**
     * @dev Returns the details of a pool.
     * @param poolId The ID of the pool to query.
     * @return Pool Details of the pool.
     */
    function getPool(uint256 poolId) external view returns (Pool memory) {
        return pools[poolId];
    }

    /**
     * @dev Returns the micropools for a given pool.
     * @param poolId The ID of the pool to query.
     * @return Micropool[] List of micropools for the pool.
     */
    function getMicropools(uint256 poolId) external view returns (Micropool[] memory) {
        return micropools[poolId];
    }
}
```
