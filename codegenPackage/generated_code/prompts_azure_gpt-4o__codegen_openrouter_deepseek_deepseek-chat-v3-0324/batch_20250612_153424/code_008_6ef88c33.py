"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: Suggest a framework for implementing a "Liquidity as a Service" (LaaS) model in a multi-chain DeFi protocol, referencing iZiSwap's approach.
Generated: DETERMINISTIC_6ef88c33b7161a96
Batch ID: 20250612_153424
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title LiquidityAsAService
 * @dev Implements a multi-chain liquidity provision service inspired by iZiSwap's approach
 */
contract LiquidityAsAService is Ownable, ReentrancyGuard {
    // Struct to represent a liquidity pool
    struct Pool {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidityBalances;
    }

    // Chain ID to Pool mapping for multi-chain support
    mapping(uint256 => mapping(bytes32 => Pool)) public chainPools;
    
    // Fee parameters (in basis points)
    uint256 public constant PROTOCOL_FEE_BPS = 30; // 0.3%
    uint256 public constant LIQUIDITY_FEE_BPS = 10; // 0.1%

    // Events
    event LiquidityAdded(
        uint256 indexed chainId,
        bytes32 indexed poolId,
        address indexed provider,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    
    event LiquidityRemoved(
        uint256 indexed chainId,
        bytes32 indexed poolId,
        address indexed provider,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );
    
    event SwapExecuted(
        uint256 indexed chainId,
        bytes32 indexed poolId,
        address indexed trader,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @dev Add liquidity to a pool
     * @param chainId The chain ID where the pool exists
     * @param poolId The ID of the pool
     * @param amountA The amount of token A to add
     * @param amountB The amount of token B to add
     */
    function addLiquidity(
        uint256 chainId,
        bytes32 poolId,
        uint256 amountA,
        uint256 amountB
    ) external nonReentrant {
        Pool storage pool = chainPools[chainId][poolId];
        require(pool.tokenA != address(0) && pool.tokenB != address(0), "Pool not initialized");
        
        // Transfer tokens from user
        IERC20(pool.tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(pool.tokenB).transferFrom(msg.sender, address(this), amountB);

        uint256 liquidity;
        if (pool.totalLiquidity == 0) {
            liquidity = sqrt(amountA * amountB);
        } else {
            liquidity = min(
                (amountA * pool.totalLiquidity) / pool.reserveA,
                (amountB * pool.totalLiquidity) / pool.reserveB
            );
        }
        
        require(liquidity > 0, "Insufficient liquidity");
        
        // Update reserves and liquidity
        pool.reserveA += amountA;
        pool.reserveB += amountB;
        pool.totalLiquidity += liquidity;
        pool.liquidityBalances[msg.sender] += liquidity;
        
        emit LiquidityAdded(chainId, poolId, msg.sender, amountA, amountB, liquidity);
    }

    /**
     * @dev Remove liquidity from a pool
     * @param chainId The chain ID where the pool exists
     * @param poolId The ID of the pool
     * @param liquidity The amount of liquidity to remove
     */
    function removeLiquidity(
        uint256 chainId,
        bytes32 poolId,
        uint256 liquidity
    ) external nonReentrant {
        Pool storage pool = chainPools[chainId][poolId];
        require(pool.liquidityBalances[msg.sender] >= liquidity, "Insufficient liquidity");
        
        // Calculate token amounts
        uint256 amountA = (liquidity * pool.reserveA) / pool.totalLiquidity;
        uint256 amountB = (liquidity * pool.reserveB) / pool.totalLiquidity;
        
        // Update reserves and liquidity
        pool.reserveA -= amountA;
        pool.reserveB -= amountB;
        pool.totalLiquidity -= liquidity;
        pool.liquidityBalances[msg.sender] -= liquidity;
        
        // Transfer tokens to user
        IERC20(pool.tokenA).transfer(msg.sender, amountA);
        IERC20(pool.tokenB).transfer(msg.sender, amountB);
        
        emit LiquidityRemoved(chainId, poolId, msg.sender, amountA, amountB, liquidity);
    }

    /**
     * @dev Execute a swap in a pool
     * @param chainId The chain ID where the pool exists
     * @param poolId The ID of the pool
     * @param tokenIn The token to swap from
     * @param amountIn The amount to swap
     * @param minAmountOut The minimum amount expected out
     */
    function swap(
        uint256 chainId,
        bytes32 poolId,
        address tokenIn,
        uint256 amountIn,
        uint256 minAmountOut
    ) external nonReentrant {
        Pool storage pool = chainPools[chainId][poolId];
        require(tokenIn == pool.tokenA || tokenIn == pool.tokenB, "Invalid token");
        
        address tokenOut = tokenIn == pool.tokenA ? pool.tokenB : pool.tokenA;
        uint256 reserveIn = tokenIn == pool.tokenA ? pool.reserveA : pool.reserveB;
        uint256 reserveOut = tokenIn == pool.tokenA ? pool.reserveB : pool.reserveA;
        
        // Transfer tokenIn from user
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Calculate amount out with fee
        uint256 amountInWithFee = amountIn * (10000 - PROTOCOL_FEE_BPS - LIQUIDITY_FEE_BPS) / 10000;
        uint256 amountOut = (amountInWithFee * reserveOut) / (reserveIn + amountInWithFee);
        
        require(amountOut >= minAmountOut, "Insufficient output amount");
        
        // Update reserves
        if (tokenIn == pool.tokenA) {
            pool.reserveA += amountIn;
            pool.reserveB -= amountOut;
        } else {
            pool.reserveB += amountIn;
            pool.reserveA -= amountOut;
        }
        
        // Transfer tokenOut to user
        IERC20(tokenOut).transfer(msg.sender, amountOut);
        
        emit SwapExecuted(chainId, poolId, msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @dev Initialize a new pool
     * @param chainId The chain ID where the pool exists
     * @param poolId The ID of the pool
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     */
    function initializePool(
        uint256 chainId,
        bytes32 poolId,
        address tokenA,
        address tokenB
    ) external onlyOwner {
        require(tokenA != tokenB, "Same tokens");
        require(chainPools[chainId][poolId].tokenA == address(0), "Pool already exists");
        
        Pool storage pool = chainPools[chainId][poolId];
        pool.tokenA = tokenA;
        pool.tokenB = tokenB;
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
