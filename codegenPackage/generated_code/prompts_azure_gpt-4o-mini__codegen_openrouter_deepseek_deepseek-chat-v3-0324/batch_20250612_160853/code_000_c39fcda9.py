"""
Generated Code Metadata:
========================
Original URL: https://bafybeih3gn5wsayvygu6qq4vwexe2dl4nf4ag25hrw2srld2z5zlirzzgi.ipfs.dweb.link
Prompt: How can I implement a liquidity protocol for modular blockchains similar to Mitosis?
Generated: DETERMINISTIC_c39fcda9fe8d4c35
Batch ID: 20250612_160853
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Liquidity Protocol for Modular Blockchains
 * @dev Inspired by Mitosis architecture, this contract manages cross-chain liquidity pools
 */
contract ModularLiquidityProtocol is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a liquidity pool
    struct Pool {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidityBalances;
    }

    // Mapping from pool ID to Pool struct
    mapping(bytes32 => Pool) public pools;

    // Events
    event PoolCreated(bytes32 indexed poolId, address tokenA, address tokenB);
    event LiquidityAdded(bytes32 indexed poolId, address provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event LiquidityRemoved(bytes32 indexed poolId, address provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event Swapped(bytes32 indexed poolId, address sender, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    /**
     * @dev Creates a new liquidity pool
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @return poolId The ID of the newly created pool
     */
    function createPool(address tokenA, address tokenB) external returns (bytes32 poolId) {
        require(tokenA != tokenB, "Tokens must be different");
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");

        poolId = keccak256(abi.encodePacked(tokenA, tokenB));
        require(pools[poolId].tokenA == address(0), "Pool already exists");

        pools[poolId].tokenA = tokenA;
        pools[poolId].tokenB = tokenB;

        emit PoolCreated(poolId, tokenA, tokenB);
        return poolId;
    }

    /**
     * @dev Adds liquidity to a pool
     * @param poolId ID of the pool
     * @param amountA Amount of tokenA to add
     * @param amountB Amount of tokenB to add
     */
    function addLiquidity(bytes32 poolId, uint256 amountA, uint256 amountB) external nonReentrant {
        Pool storage pool = pools[poolId];
        require(pool.tokenA != address(0), "Pool does not exist");
        require(amountA > 0 && amountB > 0, "Amounts must be positive");

        // Transfer tokens from user
        IERC20(pool.tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(pool.tokenB).transferFrom(msg.sender, address(this), amountB);

        uint256 liquidity;
        if (pool.totalLiquidity == 0) {
            liquidity = sqrt(amountA.mul(amountB));
        } else {
            liquidity = min(
                amountA.mul(pool.totalLiquidity).div(pool.reserveA),
                amountB.mul(pool.totalLiquidity).div(pool.reserveB)
            );
        }

        require(liquidity > 0, "Insufficient liquidity minted");

        // Update reserves and liquidity
        pool.reserveA = pool.reserveA.add(amountA);
        pool.reserveB = pool.reserveB.add(amountB);
        pool.totalLiquidity = pool.totalLiquidity.add(liquidity);
        pool.liquidityBalances[msg.sender] = pool.liquidityBalances[msg.sender].add(liquidity);

        emit LiquidityAdded(poolId, msg.sender, amountA, amountB, liquidity);
    }

    /**
     * @dev Removes liquidity from a pool
     * @param poolId ID of the pool
     * @param liquidity Amount of liquidity to remove
     */
    function removeLiquidity(bytes32 poolId, uint256 liquidity) external nonReentrant {
        Pool storage pool = pools[poolId];
        require(pool.tokenA != address(0), "Pool does not exist");
        require(liquidity > 0, "Liquidity must be positive");
        require(pool.liquidityBalances[msg.sender] >= liquidity, "Insufficient liquidity");

        uint256 amountA = liquidity.mul(pool.reserveA).div(pool.totalLiquidity);
        uint256 amountB = liquidity.mul(pool.reserveB).div(pool.totalLiquidity);

        // Update reserves and liquidity
        pool.reserveA = pool.reserveA.sub(amountA);
        pool.reserveB = pool.reserveB.sub(amountB);
        pool.totalLiquidity = pool.totalLiquidity.sub(liquidity);
        pool.liquidityBalances[msg.sender] = pool.liquidityBalances[msg.sender].sub(liquidity);

        // Transfer tokens back to user
        IERC20(pool.tokenA).transfer(msg.sender, amountA);
        IERC20(pool.tokenB).transfer(msg.sender, amountB);

        emit LiquidityRemoved(poolId, msg.sender, amountA, amountB, liquidity);
    }

    /**
     * @dev Swaps tokens in a pool
     * @param poolId ID of the pool
     * @param tokenIn Address of input token
     * @param amountIn Amount of input token
     * @param minAmountOut Minimum amount of output token expected
     */
    function swap(bytes32 poolId, address tokenIn, uint256 amountIn, uint256 minAmountOut) external nonReentrant {
        Pool storage pool = pools[poolId];
        require(pool.tokenA != address(0), "Pool does not exist");
        require(tokenIn == pool.tokenA || tokenIn == pool.tokenB, "Invalid input token");
        require(amountIn > 0, "Amount must be positive");

        address tokenOut = tokenIn == pool.tokenA ? pool.tokenB : pool.tokenA;
        uint256 reserveIn = tokenIn == pool.tokenA ? pool.reserveA : pool.reserveB;
        uint256 reserveOut = tokenIn == pool.tokenA ? pool.reserveB : pool.reserveA;

        uint256 amountOut = getAmountOut(amountIn, reserveIn, reserveOut);
        require(amountOut >= minAmountOut, "Insufficient output amount");

        // Transfer input token from user
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Update reserves
        if (tokenIn == pool.tokenA) {
            pool.reserveA = pool.reserveA.add(amountIn);
            pool.reserveB = pool.reserveB.sub(amountOut);
        } else {
            pool.reserveB = pool.reserveB.add(amountIn);
            pool.reserveA = pool.reserveA.sub(amountOut);
        }

        // Transfer output token to user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit Swapped(poolId, msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @dev Calculates output amount for a swap
     * @param amountIn Input amount
     * @param reserveIn Reserve of input token
     * @param reserveOut Reserve of output token
     * @return amountOut Output amount
     */
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) public pure returns (uint256 amountOut) {
        require(amountIn > 0, "Invalid input amount");
        require(reserveIn > 0 && reserveOut > 0, "Insufficient liquidity");
        
        uint256 amountInWithFee = amountIn.mul(997);
        uint256 numerator = amountInWithFee.mul(reserveOut);
        uint256 denominator = reserveIn.mul(1000).add(amountInWithFee);
        amountOut = numerator.div(denominator);
    }

    // Helper functions
    function sqrt(uint256 y) internal pure returns (uint256 z) {
        if (y > 3) {
            z = y;
            uint256 x = y / 2 + 1;
            while (x < z) {
                z = x;
                x = (y / x + x) / 2;
            }
        } else if (y != 0) {
            z = 1;
        }
    }

    function min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
    }
}
```
