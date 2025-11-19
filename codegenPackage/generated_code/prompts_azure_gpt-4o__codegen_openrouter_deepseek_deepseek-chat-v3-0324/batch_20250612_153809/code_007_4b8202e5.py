"""
Generated Code Metadata:
========================
Original URL: https://izumi-finance.org
Prompt: Write a Solidity implementation of a token exchange mechanism that incorporates features of iZUMi Finance Swap for efficient and seamless token trading.
Generated: DETERMINISTIC_4b8202e50a436e40
Batch ID: 20250612_153809
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenExchange is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a liquidity pool
    struct Pool {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidity;
    }

    // Mapping of pool IDs to Pool structs
    mapping(bytes32 => Pool) public pools;

    // Fee percentage (0.3% as in iZUMi)
    uint256 public constant FEE_PERCENT = 30; // 0.3% (30 basis points)
    uint256 public constant FEE_DENOMINATOR = 10000;

    // Events
    event PoolCreated(bytes32 indexed poolId, address indexed tokenA, address indexed tokenB);
    event LiquidityAdded(bytes32 indexed poolId, address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event LiquidityRemoved(bytes32 indexed poolId, address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event Swap(bytes32 indexed poolId, address indexed sender, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    /**
     * @dev Creates a new liquidity pool for two tokens
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     */
    function createPool(address tokenA, address tokenB) external onlyOwner {
        require(tokenA != tokenB, "TokenExchange: identical tokens");
        require(tokenA != address(0) && tokenB != address(0), "TokenExchange: zero address");

        bytes32 poolId = keccak256(abi.encodePacked(tokenA, tokenB));
        require(pools[poolId].tokenA == address(0), "TokenExchange: pool exists");

        pools[poolId].tokenA = tokenA;
        pools[poolId].tokenB = tokenB;

        emit PoolCreated(poolId, tokenA, tokenB);
    }

    /**
     * @dev Adds liquidity to a pool
     * @param poolId ID of the pool
     * @param amountA Amount of tokenA to add
     * @param amountB Amount of tokenB to add
     */
    function addLiquidity(bytes32 poolId, uint256 amountA, uint256 amountB) external nonReentrant {
        Pool storage pool = pools[poolId];
        require(pool.tokenA != address(0), "TokenExchange: pool does not exist");

        IERC20 tokenA = IERC20(pool.tokenA);
        IERC20 tokenB = IERC20(pool.tokenB);

        // Transfer tokens from sender
        require(tokenA.transferFrom(msg.sender, address(this), amountA), "TokenExchange: transfer A failed");
        require(tokenB.transferFrom(msg.sender, address(this), amountB), "TokenExchange: transfer B failed");

        uint256 liquidity;
        if (pool.totalLiquidity == 0) {
            liquidity = sqrt(amountA.mul(amountB));
        } else {
            liquidity = min(
                amountA.mul(pool.totalLiquidity) / pool.reserveA,
                amountB.mul(pool.totalLiquidity) / pool.reserveB
            );
        }

        require(liquidity > 0, "TokenExchange: insufficient liquidity");

        // Update reserves and liquidity
        pool.reserveA = pool.reserveA.add(amountA);
        pool.reserveB = pool.reserveB.add(amountB);
        pool.liquidity[msg.sender] = pool.liquidity[msg.sender].add(liquidity);
        pool.totalLiquidity = pool.totalLiquidity.add(liquidity);

        emit LiquidityAdded(poolId, msg.sender, amountA, amountB, liquidity);
    }

    /**
     * @dev Removes liquidity from a pool
     * @param poolId ID of the pool
     * @param liquidity Amount of liquidity to remove
     */
    function removeLiquidity(bytes32 poolId, uint256 liquidity) external nonReentrant {
        Pool storage pool = pools[poolId];
        require(pool.tokenA != address(0), "TokenExchange: pool does not exist");
        require(pool.liquidity[msg.sender] >= liquidity, "TokenExchange: insufficient liquidity");

        IERC20 tokenA = IERC20(pool.tokenA);
        IERC20 tokenB = IERC20(pool.tokenB);

        // Calculate amounts to withdraw
        uint256 amountA = liquidity.mul(pool.reserveA) / pool.totalLiquidity;
        uint256 amountB = liquidity.mul(pool.reserveB) / pool.totalLiquidity;

        // Update reserves and liquidity
        pool.reserveA = pool.reserveA.sub(amountA);
        pool.reserveB = pool.reserveB.sub(amountB);
        pool.liquidity[msg.sender] = pool.liquidity[msg.sender].sub(liquidity);
        pool.totalLiquidity = pool.totalLiquidity.sub(liquidity);

        // Transfer tokens to sender
        require(tokenA.transfer(msg.sender, amountA), "TokenExchange: transfer A failed");
        require(tokenB.transfer(msg.sender, amountB), "TokenExchange: transfer B failed");

        emit LiquidityRemoved(poolId, msg.sender, amountA, amountB, liquidity);
    }

    /**
     * @dev Swaps one token for another in a pool
     * @param poolId ID of the pool
     * @param tokenIn Address of input token
     * @param amountIn Amount of input token
     * @param minAmountOut Minimum amount of output token expected
     */
    function swap(bytes32 poolId, address tokenIn, uint256 amountIn, uint256 minAmountOut) external nonReentrant {
        Pool storage pool = pools[poolId];
        require(pool.tokenA != address(0), "TokenExchange: pool does not exist");
        require(tokenIn == pool.tokenA || tokenIn == pool.tokenB, "TokenExchange: invalid token");

        address tokenOut = tokenIn == pool.tokenA ? pool.tokenB : pool.tokenA;
        (uint256 reserveIn, uint256 reserveOut) = tokenIn == pool.tokenA 
            ? (pool.reserveA, pool.reserveB) 
            : (pool.reserveB, pool.reserveA);

        // Transfer input token from sender
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Calculate output amount with fee
        uint256 amountInWithFee = amountIn.mul(FEE_DENOMINATOR.sub(FEE_PERCENT));
        uint256 numerator = amountInWithFee.mul(reserveOut);
        uint256 denominator = reserveIn.mul(FEE_DENOMINATOR).add(amountInWithFee);
        uint256 amountOut = numerator / denominator;

        require(amountOut >= minAmountOut, "TokenExchange: insufficient output");

        // Update reserves
        if (tokenIn == pool.tokenA) {
            pool.reserveA = pool.reserveA.add(amountIn);
            pool.reserveB = pool.reserveB.sub(amountOut);
        } else {
            pool.reserveB = pool.reserveB.add(amountIn);
            pool.reserveA = pool.reserveA.sub(amountOut);
        }

        // Transfer output token to sender
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit Swap(poolId, msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @dev Returns the amount of output tokens for a given input
     * @param poolId ID of the pool
     * @param tokenIn Address of input token
     * @param amountIn Amount of input token
     * @return amountOut Calculated amount of output token
     */
    function getAmountOut(bytes32 poolId, address tokenIn, uint256 amountIn) external view returns (uint256 amountOut) {
        Pool storage pool = pools[poolId];
        require(pool.tokenA != address(0), "TokenExchange: pool does not exist");
        require(tokenIn == pool.tokenA || tokenIn == pool.tokenB, "TokenExchange: invalid token");

        (uint256 reserveIn, uint256 reserveOut) = tokenIn == pool.tokenA 
            ? (pool.reserveA, pool.reserveB) 
            : (pool.reserveB, pool.reserveA);

        uint256 amountInWithFee = amountIn.mul(FEE_DENOMINATOR.sub(FEE_PERCENT));
        uint256 numerator = amountInWithFee.mul(reserveOut);
        uint256 denominator = reserveIn.mul(FEE_DEN
