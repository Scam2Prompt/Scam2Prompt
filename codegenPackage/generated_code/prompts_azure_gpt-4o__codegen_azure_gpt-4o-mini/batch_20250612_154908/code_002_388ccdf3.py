"""
Generated Code Metadata:
========================
Original URL: https://uniswap-clone-theta.vercel.app
Prompt: Create a smart contract function to manage a liquidity pool similar to the one described in the Uniswap clone.
Generated: DETERMINISTIC_388ccdf35de4f44d
Batch ID: 20250612_154908
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

contract LiquidityPool is Ownable {
    // Events for logging
    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB);
    event LiquidityRemoved(address indexed provider, uint256 amountA, uint256 amountB);
    event Swapped(address indexed trader, uint256 amountIn, uint256 amountOut);

    // Token interfaces
    IERC20 public tokenA;
    IERC20 public tokenB;

    // Liquidity balances
    uint256 public totalLiquidityA;
    uint256 public totalLiquidityB;

    // Constructor to initialize the contract with token addresses
    constructor(address _tokenA, address _tokenB) {
        require(_tokenA != address(0) && _tokenB != address(0), "Invalid token address");
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }

    // Function to add liquidity to the pool
    function addLiquidity(uint256 amountA, uint256 amountB) external {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than zero");

        // Transfer tokens from the provider to the contract
        tokenA.transferFrom(msg.sender, address(this), amountA);
        tokenB.transferFrom(msg.sender, address(this), amountB);

        // Update total liquidity
        totalLiquidityA += amountA;
        totalLiquidityB += amountB;

        emit LiquidityAdded(msg.sender, amountA, amountB);
    }

    // Function to remove liquidity from the pool
    function removeLiquidity(uint256 amountA, uint256 amountB) external {
        require(amountA <= totalLiquidityA && amountB <= totalLiquidityB, "Insufficient liquidity");

        // Update total liquidity
        totalLiquidityA -= amountA;
        totalLiquidityB -= amountB;

        // Transfer tokens back to the provider
        tokenA.transfer(msg.sender, amountA);
        tokenB.transfer(msg.sender, amountB);

        emit LiquidityRemoved(msg.sender, amountA, amountB);
    }

    // Function to swap tokens in the pool
    function swap(uint256 amountIn, bool isAToB) external {
        require(amountIn > 0, "Amount must be greater than zero");

        uint256 amountOut;
        if (isAToB) {
            require(amountIn <= totalLiquidityA, "Insufficient liquidity for token A");
            amountOut = getAmountOut(amountIn, totalLiquidityA, totalLiquidityB);
            require(amountOut <= totalLiquidityB, "Insufficient liquidity for token B");

            // Transfer token A from trader to contract
            tokenA.transferFrom(msg.sender, address(this), amountIn);
            // Transfer token B to trader
            tokenB.transfer(msg.sender, amountOut);

            // Update liquidity
            totalLiquidityA += amountIn;
            totalLiquidityB -= amountOut;
        } else {
            require(amountIn <= totalLiquidityB, "Insufficient liquidity for token B");
            amountOut = getAmountOut(amountIn, totalLiquidityB, totalLiquidityA);
            require(amountOut <= totalLiquidityA, "Insufficient liquidity for token A");

            // Transfer token B from trader to contract
            tokenB.transferFrom(msg.sender, address(this), amountIn);
            // Transfer token A to trader
            tokenA.transfer(msg.sender, amountOut);

            // Update liquidity
            totalLiquidityB += amountIn;
            totalLiquidityA -= amountOut;
        }

        emit Swapped(msg.sender, amountIn, amountOut);
    }

    // Internal function to calculate output amount based on input amount and reserves
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) internal pure returns (uint256) {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(reserveIn > 0 && reserveOut > 0, "Reserves must be greater than zero");

        // Simple constant product formula
        uint256 amountInWithFee = amountIn * 997; // Assuming a 0.3% fee
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = (reserveIn * 1000) + amountInWithFee;
        return numerator / denominator;
    }
}
```
