"""
Generated Code Metadata:
========================
Original URL: https://reef-io.pages.dev
Prompt: Write code to create a decentralized exchange (DEX) on Reef chain that supports trading REEF-20 assets.
Generated: DETERMINISTIC_ba34a4a893510e13
Batch ID: 20250612_145933
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

contract ReefDEX is ReentrancyGuard {
    using SafeMath for uint256;

    address public feeTo;
    uint256 public feePercent = 3; // 0.3% fee

    struct Pool {
        uint256 reserve0;
        uint256 reserve1;
        uint256 totalSupply;
    }

    struct TokenPair {
        address token0;
        address token1;
    }

    mapping(bytes32 => Pool) public pools;
    mapping(address => mapping(address => bytes32)) public pairToPoolId;
    mapping(address => uint256) public liquidity;

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
    event Swapped(
        address indexed sender,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    constructor(address _feeTo) {
        feeTo = _feeTo;
    }

    function createPool(address tokenA, address tokenB) external {
        require(tokenA != tokenB, "ReefDEX: IDENTICAL_ADDRESSES");
        (address token0, address token1) = tokenA < tokenB 
            ? (tokenA, tokenB) 
            : (tokenB, tokenA);
        require(token0 != address(0), "ReefDEX: ZERO_ADDRESS");
        bytes32 poolId = keccak256(abi.encodePacked(token0, token1));
        require(pools[poolId].totalSupply == 0, "ReefDEX: POOL_EXISTS");
        
        pools[poolId] = Pool(0, 0, 0);
        pairToPoolId[token0][token1] = poolId;
        pairToPoolId[token1][token0] = poolId;
    }

    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin
    ) external nonReentrant returns (uint256 liquidity) {
        require(amountADesired > 0 && amountBDesired > 0, "ReefDEX: INVALID_AMOUNT");
        
        (address token0, address token1) = tokenA < tokenB 
            ? (tokenA, tokenB) 
            : (tokenB, tokenA);
        bytes32 poolId = pairToPoolId[token0][token1];
        Pool storage pool = pools[poolId];
        
        if (pool.totalSupply == 0) {
            require(amountADesired >= amountAMin && amountBDesired >= amountBMin, 
                "ReefDEX: INSUFFICIENT_AMOUNT");
            
            _safeTransferFrom(token0, msg.sender, address(this), amountADesired);
            _safeTransferFrom(token1, msg.sender, address(this), amountBDesired);
            
            pool.reserve0 = amountADesired;
            pool.reserve1 = amountBDesired;
            liquidity = sqrt(amountADesired.mul(amountBDesired));
        } else {
            uint256 amountBOptimal = quote(amountADesired, pool.reserve0, pool.reserve1);
            if (amountBOptimal <= amountBDesired) {
                require(amountBOptimal >= amountBMin, "ReefDEX: INSUFFICIENT_B_AMOUNT");
                _safeTransferFrom(token0, msg.sender, address(this), amountADesired);
                _safeTransferFrom(token1, msg.sender, address(this), amountBOptimal);
                
                liquidity = amountADesired.mul(pool.totalSupply).div(pool.reserve0);
            } else {
                uint256 amountAOptimal = quote(amountBDesired, pool.reserve1, pool.reserve0);
                require(amountAOptimal <= amountADesired, "ReefDEX: INSUFFICIENT_A_AMOUNT");
                require(amountAOptimal >= amountAMin, "ReefDEX: INSUFFICIENT_A_AMOUNT");
                _safeTransferFrom(token0, msg.sender, address(this), amountAOptimal);
                _safeTransferFrom(token1, msg.sender, address(this), amountBDesired);
                
                liquidity = amountBDesired.mul(pool.totalSupply).div(pool.reserve1);
            }
        }
        
        require(liquidity > 0, "ReefDEX: INSUFFICIENT_LIQUIDITY_MINTED");
        pool.reserve0 = IERC20(token0).balanceOf(address(this));
        pool.reserve1 = IERC20(token1).balanceOf(address(this));
        pool.totalSupply = pool.totalSupply.add(liquidity);
        liquidity[msg.sender] = liquidity[msg.sender].add(liquidity);
        
        emit LiquidityAdded(msg.sender, token0, token1, amountADesired, amountBDesired, liquidity);
    }

    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint256 liquidity,
        uint256 amountAMin,
        uint256 amountBMin
    ) external nonReentrant returns (uint256 amountA, uint256 amountB) {
        require(liquidity > 0, "ReefDEX: INVALID_LIQUIDITY");
        
        (address token0, address token1) = tokenA < tokenB 
            ? (tokenA, tokenB) 
            : (tokenB, tokenA);
        bytes32 poolId = pairToPoolId[token0][token1];
        Pool storage pool = pools[poolId];
        
        uint256 balance0 = IERC20(token0).balanceOf(address(this));
        uint256 balance1 = IERC20(token1).balanceOf(address(this));
        
        amountA = liquidity.mul(balance0).div(pool.totalSupply);
        amountB = liquidity.mul(balance1).div(pool.totalSupply);
        
        require(amountA >= amountAMin && amountB >= amountBMin, "ReefDEX: INSUFFICIENT_AMOUNT");
        
        pool.reserve0 = balance0.sub(amountA);
        pool.reserve1 = balance1.sub(amountB);
        pool.totalSupply = pool.totalSupply.sub(liquidity);
        liquidity[msg.sender] = liquidity[msg.sender].sub(liquidity);
        
        _safeTransfer(token0, msg.sender, amountA);
        _safeTransfer(token1, msg.sender, amountB);
        
        emit LiquidityRemoved(msg.sender, token0, token1, amountA, amountB, liquidity);
    }

    function swapExactTokensForTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin
    ) external nonReentrant returns (uint256 amountOut) {
        require(amountIn > 0, "ReefDEX: INVALID_INPUT_AMOUNT");
        
        (address token0, address token1) = tokenIn < tokenOut 
            ? (tokenIn, tokenOut) 
            : (tokenOut, tokenIn);
        bytes32 poolId = pairToPoolId[token0][token1];
        Pool storage pool = pools[poolId];
        
        if (tokenIn == token0) {
            amountOut = getAmountOut(amountIn, pool.reserve0, pool.reserve1);
            require(amountOut >= amountOutMin, "ReefDEX: INSUFFICIENT_OUTPUT_AMOUNT");
            
            _safeTransferFrom(tokenIn, msg.sender, address(this), amountIn);
            uint256 fee = amountOut.mul(feePercent).div(1000);
            amountOut = amountOut.sub(fee);
            
            pool.reserve0 = pool.reserve0.add(amountIn);
            pool.reserve1 = pool.reserve1.sub(amountOut.add(fee));
            
            _safeTransfer(tokenOut, msg.sender, amountOut);
            if (fee > 0) _safeTransfer(tokenOut, feeTo, fee);
        } else {
            amountOut = getAmountOut(amountIn, pool.reserve1, pool.reserve0);
            require(amountOut >= amountOutMin, "ReefDEX: INSUFFICIENT_OUTPUT_AMOUNT");
            
            _safeTransferFrom(tokenIn, msg.sender, address(this), amountIn);
            uint256 fee = amountOut.mul(feePercent).div(1000);
            amountOut =
