"""
Generated Code Metadata:
========================
Original URL: https://nodechainresolve.com
Prompt: Generate code for enhancing swap functionality in a Web3 crypto exchange platform, incorporating liquidity management strategies from NodeChainResolve.
Generated: DETERMINISTIC_93f9b35c4fbb78b0
Batch ID: 20250612_154809
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
 * @title NodeChainSwap
 * @dev Enhanced swap functionality with liquidity management strategies
 */
contract NodeChainSwap is Ownable, ReentrancyGuard {
    // Struct to represent a liquidity pool
    struct Pool {
        uint256 reserve0;
        uint256 reserve1;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidity;
    }

    // Mapping of token pairs to their pool
    mapping(address => mapping(address => Pool)) public pools;

    // Events
    event LiquidityAdded(
        address indexed provider,
        address indexed token0,
        address indexed token1,
        uint256 amount0,
        uint256 amount1,
        uint256 liquidity
    );
    event LiquidityRemoved(
        address indexed provider,
        address indexed token0,
        address indexed token1,
        uint256 amount0,
        uint256 amount1,
        uint256 liquidity
    );
    event Swap(
        address indexed sender,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @dev Add liquidity to a pool
     * @param tokenA First token in the pair
     * @param tokenB Second token in the pair
     * @param amountADesired Desired amount of tokenA to add
     * @param amountBDesired Desired amount of tokenB to add
     * @param amountAMin Minimum amount of tokenA to add
     * @param amountBMin Minimum amount of tokenB to add
     * @param to Address to receive liquidity tokens
     * @return liquidity Amount of liquidity tokens minted
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        address to
    ) external nonReentrant returns (uint256 liquidity) {
        require(tokenA != tokenB, "NodeChainSwap: IDENTICAL_ADDRESSES");
        require(amountADesired > 0 && amountBDesired > 0, "NodeChainSwap: INVALID_AMOUNT");
        require(to != address(0), "NodeChainSwap: INVALID_TO_ADDRESS");

        (address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);
        Pool storage pool = pools[token0][token1];

        uint256 amount0;
        uint256 amount1;

        if (pool.totalLiquidity == 0) {
            (amount0, amount1) = (amountADesired, amountBDesired);
        } else {
            uint256 amountBOptimal = _quote(amountADesired, pool.reserve0, pool.reserve1);
            if (amountBOptimal <= amountBDesired) {
                require(amountBOptimal >= amountBMin, "NodeChainSwap: INSUFFICIENT_B_AMOUNT");
                (amount0, amount1) = (amountADesired, amountBOptimal);
            } else {
                uint256 amountAOptimal = _quote(amountBDesired, pool.reserve1, pool.reserve0);
                require(amountAOptimal <= amountADesired, "NodeChainSwap: INVALID_AMOUNT");
                require(amountAOptimal >= amountAMin, "NodeChainSwap: INSUFFICIENT_A_AMOUNT");
                (amount0, amount1) = (amountAOptimal, amountBDesired);
            }
        }

        _safeTransferFrom(token0, msg.sender, address(this), amount0);
        _safeTransferFrom(token1, msg.sender, address(this), amount1);

        liquidity = _mintLiquidity(to, token0, token1, amount0, amount1);
        emit LiquidityAdded(to, token0, token1, amount0, amount1, liquidity);
    }

    /**
     * @dev Remove liquidity from a pool
     * @param tokenA First token in the pair
     * @param tokenB Second token in the pair
     * @param liquidity Amount of liquidity tokens to burn
     * @param amountAMin Minimum amount of tokenA to receive
     * @param amountBMin Minimum amount of tokenB to receive
     * @param to Address to receive underlying tokens
     * @return amount0 Amount of token0 received
     * @return amount1 Amount of token1 received
     */
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint256 liquidity,
        uint256 amountAMin,
        uint256 amountBMin,
        address to
    ) external nonReentrant returns (uint256 amount0, uint256 amount1) {
        require(tokenA != tokenB, "NodeChainSwap: IDENTICAL_ADDRESSES");
        require(liquidity > 0, "NodeChainSwap: INVALID_LIQUIDITY");
        require(to != address(0), "NodeChainSwap: INVALID_TO_ADDRESS");

        (address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);
        Pool storage pool = pools[token0][token1];

        uint256 userLiquidity = pool.liquidity[msg.sender];
        require(userLiquidity >= liquidity, "NodeChainSwap: INSUFFICIENT_LIQUIDITY");

        amount0 = (liquidity * pool.reserve0) / pool.totalLiquidity;
        amount1 = (liquidity * pool.reserve1) / pool.totalLiquidity;
        require(amount0 >= amountAMin && amount1 >= amountBMin, "NodeChainSwap: INSUFFICIENT_AMOUNT");

        _burnLiquidity(msg.sender, token0, token1, liquidity);
        _safeTransfer(token0, to, amount0);
        _safeTransfer(token1, to, amount1);

        emit LiquidityRemoved(msg.sender, token0, token1, amount0, amount1, liquidity);
    }

    /**
     * @dev Execute a token swap
     * @param amountIn Amount of input tokens
     * @param amountOutMin Minimum amount of output tokens
     * @param path Array of token addresses representing swap path
     * @param to Address to receive output tokens
     */
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to
    ) external nonReentrant returns (uint256[] memory amounts) {
        require(path.length >= 2, "NodeChainSwap: INVALID_PATH");
        require(to != address(0), "NodeChainSwap: INVALID_TO_ADDRESS");

        amounts = new uint256[](path.length);
        amounts[0] = amountIn;

        for (uint256 i; i < path.length - 1; i++) {
            (address input, address output) = (path[i], path[i + 1]);
            (address token0, ) = input < output ? (input, output) : (output, input);
            uint256 amountOut;
            Pool storage pool = pools[token0][input == token0 ? output : input];
            
            uint256 amountInWithFee = amountIn * 997 / 1000; // 0.3% fee
            amountOut = _getAmountOut(amountInWithFee, input == token0 ? pool.reserve0 : pool.reserve1, input == token0 ? pool.reserve1 : pool.reserve0);
            
            amounts[i + 1] = amountOut;
            _update(input == token0 ? pool.reserve0 + amountIn : pool.reserve1 + amountIn, 
                   input == token0 ? pool.reserve1 - amountOut : pool.reserve0 - amountOut, 
                   token0, 
                   input == token0 ? output : input);
            
            amountIn = amountOut;
        }

        require(amounts[path.length - 1] >= amountOutMin, "NodeChainSwap: INSUFFICIENT_OUTPUT_AMOUNT");
        _safeTransferFrom(path[0], msg.sender, address(this), amounts[0]);
        _safeTransfer(path[path.length - 1], to, amounts[path.length - 1]);

        emit Swap(msg.sender, path[0], path[path.length - 1], amounts[0], amounts[path.length - 1]);
    }

    // Internal helper functions

    function _quote(uint256 amountA, uint256 reserveA, uint256 reserveB) internal pure returns (uint256 amountB) {
        require(reserveA > 0 && reserveB > 0, "NodeChainSwap: INSUFFICIENT_LIQUIDITY");
        amountB = (amountA * reserveB) / reserveA;
