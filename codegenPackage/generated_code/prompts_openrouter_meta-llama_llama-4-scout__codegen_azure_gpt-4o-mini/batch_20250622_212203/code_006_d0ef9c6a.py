"""
Generated Code Metadata:
========================
Original URL: https://drrnnxx.xyz
Prompt: Design a basic PancakeSwap-like DEX platform using a popular blockchain network such as BNB Chain.
Generated: DETERMINISTIC_d0ef9c6af506e724
Batch ID: 20250622_212203
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PancakeSwap-like DEX contract
contract PancakeSwapDEX is Ownable {
    // Event emitted when a swap occurs
    event Swap(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping to store token reserves
    mapping(address => mapping(address => uint256)) public reserves;

    // Function to add liquidity to the DEX
    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external onlyOwner {
        require(amountA > 0 && amountB > 0, "Invalid amounts");

        // Transfer tokens from the owner to the contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountB);

        // Update reserves
        reserves[tokenA][tokenB] += amountA;
        reserves[tokenB][tokenA] += amountB;
    }

    // Function to swap tokens
    function swap(address tokenIn, address tokenOut, uint256 amountIn) external {
        require(amountIn > 0, "Invalid amount");
        require(reserves[tokenIn][tokenOut] > 0, "Insufficient liquidity");

        // Calculate amount out based on reserves (simple ratio)
        uint256 amountOut = getAmountOut(amountIn, tokenIn, tokenOut);
        require(amountOut > 0, "Insufficient output amount");

        // Transfer input tokens from user to contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        // Transfer output tokens from contract to user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Update reserves
        reserves[tokenIn][tokenOut] += amountIn;
        reserves[tokenOut][tokenIn] -= amountOut;

        // Emit swap event
        emit Swap(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to get amount out based on reserves
    function getAmountOut(uint256 amountIn, address tokenIn, address tokenOut) public view returns (uint256) {
        uint256 reserveIn = reserves[tokenIn][tokenOut];
        uint256 reserveOut = reserves[tokenOut][tokenIn];

        // Simple formula for amount out
        return (amountIn * reserveOut) / (reserveIn + amountIn);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Invalid amount");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
