"""
Generated Code Metadata:
========================
Original URL: https://aitechpad-io.pages.dev
Prompt: Generate a Solidity smart contract code snippet for creating a new staking pool on the Solidus AI Tech platform, with a specified APY, lock term, and boost option.
Generated: DETERMINISTIC_eb08c2172832e4d0
Batch ID: 20250622_210243
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

/**
 * @title StakingPool
 * @dev A smart contract for creating staking pools with specified APY, lock term, and boost options.
 */
contract StakingPool {
    // Struct to represent a staking pool
    struct Pool {
        uint256 apy; // Annual Percentage Yield (in basis points, e.g., 500 = 5%)
        uint256 lockTerm; // Lock term in seconds
        uint256 boost; // Boost percentage (in basis points, e.g., 200 = 2%)
        bool isActive; // Whether the pool is active
    }

    // Mapping to store staking pools by ID
    mapping(uint256 => Pool) public pools;

    // Counter for pool IDs
    uint256 public poolCounter;

    // Address of the contract owner
    address public owner;

    // Events
    event PoolCreated(uint256 indexed poolId, uint256 apy, uint256 lockTerm, uint256 boost);
    event PoolUpdated(uint256 indexed poolId, uint256 apy, uint256 lockTerm, uint256 boost, bool isActive);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new staking pool.
     * @param _apy Annual Percentage Yield (in basis points, e.g., 500 = 5%).
     * @param _lockTerm Lock term in seconds.
     * @param _boost Boost percentage (in basis points, e.g., 200 = 2%).
     */
    function createPool(uint256 _apy, uint256 _lockTerm, uint256 _boost) external onlyOwner {
        require(_apy > 0, "APY must be greater than zero");
        require(_lockTerm > 0, "Lock term must be greater than zero");
        require(_boost >= 0, "Boost must be non-negative");

        poolCounter++;
        pools[poolCounter] = Pool({
            apy: _apy,
            lockTerm: _lockTerm,
            boost: _boost,
            isActive: true
        });

        emit PoolCreated(poolCounter, _apy, _lockTerm, _boost);
    }

    /**
     * @dev Function to update an existing staking pool.
     * @param _poolId ID of the pool to update.
     * @param _apy New APY value.
     * @param _lockTerm New lock term value.
     * @param _boost New boost value.
     * @param _isActive Whether the pool is active.
     */
    function updatePool(
        uint256 _poolId,
        uint256 _apy,
        uint256 _lockTerm,
        uint256 _boost,
        bool _isActive
    ) external onlyOwner {
        require(_poolId > 0 && _poolId <= poolCounter, "Invalid pool ID");
        require(_apy > 0, "APY must be greater than zero");
        require(_lockTerm > 0, "Lock term must be greater than zero");
        require(_boost >= 0, "Boost must be non-negative");

        Pool storage pool = pools[_poolId];
        pool.apy = _apy;
        pool.lockTerm = _lockTerm;
        pool.boost = _boost;
        pool.isActive = _isActive;

        emit PoolUpdated(_poolId, _apy, _lockTerm, _boost, _isActive);
    }

    /**
     * @dev Function to retrieve details of a staking pool.
     * @param _poolId ID of the pool to retrieve.
     * @return Pool details (APY, lock term, boost, and active status).
     */
    function getPool(uint256 _poolId) external view returns (uint256, uint256, uint256, bool) {
        require(_poolId > 0 && _poolId <= poolCounter, "Invalid pool ID");
        Pool memory pool = pools[_poolId];
        return (pool.apy, pool.lockTerm, pool.boost, pool.isActive);
    }
}
```
