"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lanimal443331.github.io
Prompt: Write a smart contract in Solidity for launching an LBP that prioritizes equitable token distribution and reduces bot manipulation, as described by Fjord Foundry.
Generated: DETERMINISTIC_0f741e7440bbac8f
Batch ID: 20250612_153648
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LBP is Ownable {
    using SafeMath for uint256;

    // Struct to store pool information
    struct Pool {
        IERC20 tokenA;
        IERC20 tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    // Mapping of pool ID to Pool data
    mapping(uint256 => Pool) public pools;
    uint256 public poolCount;

    // Event declarations
    event PoolCreated(uint256 poolId, address tokenA, address tokenB, uint256 startTime, uint256 endTime);
    event LiquidityAdded(uint256 poolId, address provider, uint256 amountA, uint256 amountB);
    event Swapped(uint256 poolId, address trader, uint256 amountIn, uint256 amountOut);

    // Modifier to check if the pool is active
    modifier onlyActivePool(uint256 poolId) {
        require(pools[poolId].isActive, "Pool is not active");
        _;
    }

    // Function to create a new liquidity bootstrapping pool
    function createPool(
        IERC20 _tokenA,
        IERC20 _tokenB,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(_startTime < _endTime, "Invalid time range");
        
        poolCount++;
        pools[poolCount] = Pool({
            tokenA: _tokenA,
            tokenB: _tokenB,
            reserveA: 0,
            reserveB: 0,
            startTime: _startTime,
            endTime: _endTime,
            isActive: true
        });

        emit PoolCreated(poolCount, address(_tokenA), address(_tokenB), _startTime, _endTime);
    }

    // Function to add liquidity to a pool
    function addLiquidity(uint256 poolId, uint256 amountA, uint256 amountB) external onlyActivePool(poolId) {
        Pool storage pool = pools[poolId];
        require(block.timestamp >= pool.startTime && block.timestamp <= pool.endTime, "Pool is not active");

        // Transfer tokens from user to the contract
        require(pool.tokenA.transferFrom(msg.sender, address(this), amountA), "Transfer of token A failed");
        require(pool.tokenB.transferFrom(msg.sender, address(this), amountB), "Transfer of token B failed");

        pool.reserveA = pool.reserveA.add(amountA);
        pool.reserveB = pool.reserveB.add(amountB);

        emit LiquidityAdded(poolId, msg.sender, amountA, amountB);
    }

    // Function to swap tokens in the pool
    function swap(uint256 poolId, uint256 amountIn, bool isTokenAtoB) external onlyActivePool(poolId) {
        Pool storage pool = pools[poolId];
        require(block.timestamp >= pool.startTime && block.timestamp <= pool.endTime, "Pool is not active");

        uint256 amountOut;

        if (isTokenAtoB) {
            require(pool.tokenA.balanceOf(msg.sender) >= amountIn, "Insufficient balance of token A");
            require(pool.tokenA.transferFrom(msg.sender, address(this), amountIn), "Transfer of token A failed");
            amountOut = getAmountOut(amountIn, pool.reserveA, pool.reserveB);
            pool.reserveA = pool.reserveA.add(amountIn);
            pool.reserveB = pool.reserveB.sub(amountOut);
            require(pool.tokenB.transfer(msg.sender, amountOut), "Transfer of token B failed");
        } else {
            require(pool.tokenB.balanceOf(msg.sender) >= amountIn, "Insufficient balance of token B");
            require(pool.tokenB.transferFrom(msg.sender, address(this), amountIn), "Transfer of token B failed");
            amountOut = getAmountOut(amountIn, pool.reserveB, pool.reserveA);
            pool.reserveB = pool.reserveB.add(amountIn);
            pool.reserveA = pool.reserveA.sub(amountOut);
            require(pool.tokenA.transfer(msg.sender, amountOut), "Transfer of token A failed");
        }

        emit Swapped(poolId, msg.sender, amountIn, amountOut);
    }

    // Internal function to calculate output amount based on reserves
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) internal pure returns (uint256) {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(reserveIn > 0 && reserveOut > 0, "Insufficient liquidity");

        uint256 amountInWithFee = amountIn.mul(997); // Applying a 0.3% fee
        uint256 numerator = amountInWithFee.mul(reserveOut);
        uint256 denominator = reserveIn.mul(1000).add(amountInWithFee);
        return numerator / denominator;
    }

    // Function to deactivate a pool
    function deactivatePool(uint256 poolId) external onlyOwner onlyActivePool(poolId) {
        pools[poolId].isActive = false;
    }
}
```
