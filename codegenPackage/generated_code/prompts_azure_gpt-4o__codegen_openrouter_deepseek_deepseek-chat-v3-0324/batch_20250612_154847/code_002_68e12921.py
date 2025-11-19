"""
Generated Code Metadata:
========================
Original URL: https://uniswap-clone-gray.vercel.app
Prompt: Generate code for a "Pool" feature that allows users to add liquidity to an Ethereum-based decentralized exchange, inspired by the Uniswap Clone website.
Generated: DETERMINISTIC_68e12921039ab9d1
Batch ID: 20250612_154847
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Pool is Ownable {
    using SafeMath for uint256;

    address public tokenA;
    address public tokenB;
    uint256 public reserveA;
    uint256 public reserveB;
    uint256 public totalLiquidity;
    mapping(address => uint256) public liquidity;

    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event LiquidityRemoved(address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event Swap(address indexed user, address tokenIn, uint256 amountIn, address tokenOut, uint256 amountOut);

    constructor(address _tokenA, address _tokenB) {
        require(_tokenA != address(0) && _tokenB != address(0), "Invalid token address");
        require(_tokenA != _tokenB, "Tokens must be different");
        tokenA = _tokenA;
        tokenB = _tokenB;
    }

    /**
     * @dev Add liquidity to the pool
     * @param amountA Desired amount of tokenA to add
     * @param amountB Desired amount of tokenB to add
     */
    function addLiquidity(uint256 amountA, uint256 amountB) external {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than 0");

        uint256 liquidityAmount;
        if (totalLiquidity == 0) {
            liquidityAmount = sqrt(amountA.mul(amountB));
        } else {
            uint256 liquidityA = amountA.mul(totalLiquidity).div(reserveA);
            uint256 liquidityB = amountB.mul(totalLiquidity).div(reserveB);
            liquidityAmount = (liquidityA < liquidityB) ? liquidityA : liquidityB;
        }

        require(liquidityAmount > 0, "Insufficient liquidity minted");

        // Transfer tokens from user to contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountB);

        // Update reserves
        reserveA = reserveA.add(amountA);
        reserveB = reserveB.add(amountB);

        // Mint liquidity tokens
        liquidity[msg.sender] = liquidity[msg.sender].add(liquidityAmount);
        totalLiquidity = totalLiquidity.add(liquidityAmount);

        emit LiquidityAdded(msg.sender, amountA, amountB, liquidityAmount);
    }

    /**
     * @dev Remove liquidity from the pool
     * @param liquidityAmount Amount of liquidity tokens to burn
     */
    function removeLiquidity(uint256 liquidityAmount) external {
        require(liquidityAmount > 0, "Amount must be greater than 0");
        require(liquidity[msg.sender] >= liquidityAmount, "Insufficient liquidity");

        uint256 amountA = liquidityAmount.mul(reserveA).div(totalLiquidity);
        uint256 amountB = liquidityAmount.mul(reserveB).div(totalLiquidity);

        // Burn liquidity tokens
        liquidity[msg.sender] = liquidity[msg.sender].sub(liquidityAmount);
        totalLiquidity = totalLiquidity.sub(liquidityAmount);

        // Update reserves
        reserveA = reserveA.sub(amountA);
        reserveB = reserveB.sub(amountB);

        // Transfer tokens back to user
        IERC20(tokenA).transfer(msg.sender, amountA);
        IERC20(tokenB).transfer(msg.sender, amountB);

        emit LiquidityRemoved(msg.sender, amountA, amountB, liquidityAmount);
    }

    /**
     * @dev Swap tokens
     * @param tokenIn Address of input token
     * @param amountIn Amount of input token
     * @param minAmountOut Minimum amount of output token expected
     */
    function swap(address tokenIn, uint256 amountIn, uint256 minAmountOut) external {
        require(tokenIn == tokenA || tokenIn == tokenB, "Invalid input token");
        require(amountIn > 0, "Amount must be greater than 0");

        address tokenOut = tokenIn == tokenA ? tokenB : tokenA;
        uint256 reserveIn = tokenIn == tokenA ? reserveA : reserveB;
        uint256 reserveOut = tokenIn == tokenA ? reserveB : reserveA;

        uint256 amountOut = getAmountOut(amountIn, reserveIn, reserveOut);
        require(amountOut >= minAmountOut, "Insufficient output amount");

        // Transfer input tokens from user
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Update reserves
        if (tokenIn == tokenA) {
            reserveA = reserveA.add(amountIn);
            reserveB = reserveB.sub(amountOut);
        } else {
            reserveB = reserveB.add(amountIn);
            reserveA = reserveA.sub(amountOut);
        }

        // Transfer output tokens to user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit Swap(msg.sender, tokenIn, amountIn, tokenOut, amountOut);
    }

    /**
     * @dev Calculate output amount for a swap
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

    /**
     * @dev Square root function
     * @param x Number to calculate square root of
     * @return y Square root of x
     */
    function sqrt(uint256 x) internal pure returns (uint256 y) {
        uint256 z = (x + 1) / 2;
        y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
    }
}
```
