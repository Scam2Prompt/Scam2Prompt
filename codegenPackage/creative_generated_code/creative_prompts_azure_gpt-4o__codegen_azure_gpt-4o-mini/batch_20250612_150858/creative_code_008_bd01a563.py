"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy-io.github.io
Prompt: Write a Solidity smart contract for managing liquidity pools on Zealy, including ORB/USDT and ORB/DAI trading pairs.
Generated: DETERMINISTIC_bd01a5637f3d3993
Batch ID: 20250612_150858
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

// This contract manages liquidity pools for the ORB/USDT and ORB/DAI trading pairs.
contract LiquidityPoolManager is Ownable {
    struct Pool {
        IERC20 tokenA;
        IERC20 tokenB;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidityProviders;
    }

    // Mapping of pool identifiers to their respective Pool structs
    mapping(string => Pool) public pools;

    // Events to emit on liquidity addition/removal
    event LiquidityAdded(string poolId, address provider, uint256 amountA, uint256 amountB);
    event LiquidityRemoved(string poolId, address provider, uint256 amountA, uint256 amountB);

    // Modifier to check if a pool exists
    modifier poolExists(string memory poolId) {
        require(pools[poolId].tokenA != IERC20(address(0)) && pools[poolId].tokenB != IERC20(address(0)), "Pool does not exist");
        _;
    }

    // Function to create a new liquidity pool
    function createPool(string memory poolId, IERC20 _tokenA, IERC20 _tokenB) external onlyOwner {
        require(pools[poolId].tokenA == IERC20(address(0)), "Pool already exists");

        pools[poolId].tokenA = _tokenA;
        pools[poolId].tokenB = _tokenB;
    }

    // Function to add liquidity to a pool
    function addLiquidity(string memory poolId, uint256 amountA, uint256 amountB) external poolExists(poolId) {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than zero");

        Pool storage pool = pools[poolId];

        // Transfer tokens from provider to the contract
        require(pool.tokenA.transferFrom(msg.sender, address(this), amountA), "Transfer of token A failed");
        require(pool.tokenB.transferFrom(msg.sender, address(this), amountB), "Transfer of token B failed");

        // Update total liquidity and provider's shares
        pool.totalLiquidity += amountA + amountB;
        pool.liquidityProviders[msg.sender] += amountA + amountB;

        emit LiquidityAdded(poolId, msg.sender, amountA, amountB);
    }

    // Function to remove liquidity from a pool
    function removeLiquidity(string memory poolId, uint256 amountA, uint256 amountB) external poolExists(poolId) {
        Pool storage pool = pools[poolId];

        require(pool.liquidityProviders[msg.sender] >= amountA + amountB, "Insufficient liquidity");

        // Update provider's shares and total liquidity
        pool.liquidityProviders[msg.sender] -= amountA + amountB;
        pool.totalLiquidity -= amountA + amountB;

        // Transfer tokens back to provider
        require(pool.tokenA.transfer(msg.sender, amountA), "Transfer of token A failed");
        require(pool.tokenB.transfer(msg.sender, amountB), "Transfer of token B failed");

        emit LiquidityRemoved(poolId, msg.sender, amountA, amountB);
    }

    // Function to get total liquidity of a pool
    function getTotalLiquidity(string memory poolId) external view poolExists(poolId) returns (uint256) {
        return pools[poolId].totalLiquidity;
    }

    // Function to get liquidity of a specific provider
    function getProviderLiquidity(string memory poolId, address provider) external view poolExists(poolId) returns (uint256) {
        return pools[poolId].liquidityProviders[provider];
    }
}
```
