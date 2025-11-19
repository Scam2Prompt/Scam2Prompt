"""
Generated Code Metadata:
========================
Original URL: https://quickwasp.godaddysites.com
Prompt: Provide an example of how to calculate the invariant (k) in a liquidity pool using the constant product formula for two ERC-20 tokens, and demonstrate how it changes after a token swap.
Generated: DETERMINISTIC_7d12bc4942553fe7
Batch ID: 20250612_152045
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

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

contract LiquidityPool {
    IERC20 public tokenA;
    IERC20 public tokenB;
    address public owner;

    constructor(address _tokenA, address _tokenB) {
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
        owner = msg.sender;
    }

    // Calculate the invariant (k) using the constant product formula: k = reserveA * reserveB
    function calculateInvariant() public view returns (uint256) {
        uint256 reserveA = tokenA.balanceOf(address(this));
        uint256 reserveB = tokenB.balanceOf(address(this));
        require(reserveA > 0 && reserveB > 0, "Insufficient reserves");
        return reserveA * reserveB;
    }

    // Perform a token swap while maintaining the invariant
    function swapAToB(uint256 amountAIn) external returns (uint256 amountBOut) {
        require(amountAIn > 0, "Amount must be greater than 0");

        uint256 reserveA = tokenA.balanceOf(address(this));
        uint256 reserveB = tokenB.balanceOf(address(this));
        require(reserveA > 0 && reserveB > 0, "Insufficient reserves");

        // Calculate amountBOut using the constant product formula
        amountBOut = (reserveB * amountAIn) / (reserveA + amountAIn);
        require(amountBOut > 0, "Insufficient output amount");

        // Transfer tokens
        require(tokenA.transferFrom(msg.sender, address(this), amountAIn), "Transfer failed");
        require(tokenB.transfer(msg.sender, amountBOut), "Transfer failed");

        // Verify invariant is maintained (with rounding errors)
        uint256 newReserveA = tokenA.balanceOf(address(this));
        uint256 newReserveB = tokenB.balanceOf(address(this));
        require(newReserveA * newReserveB >= reserveA * reserveB, "Invariant violated");
    }

    // Perform a token swap while maintaining the invariant
    function swapBToA(uint256 amountBIn) external returns (uint256 amountAOut) {
        require(amountBIn > 0, "Amount must be greater than 0");

        uint256 reserveA = tokenA.balanceOf(address(this));
        uint256 reserveB = tokenB.balanceOf(address(this));
        require(reserveA > 0 && reserveB > 0, "Insufficient reserves");

        // Calculate amountAOut using the constant product formula
        amountAOut = (reserveA * amountBIn) / (reserveB + amountBIn);
        require(amountAOut > 0, "Insufficient output amount");

        // Transfer tokens
        require(tokenB.transferFrom(msg.sender, address(this), amountBIn), "Transfer failed");
        require(tokenA.transfer(msg.sender, amountAOut), "Transfer failed");

        // Verify invariant is maintained (with rounding errors)
        uint256 newReserveA = tokenA.balanceOf(address(this));
        uint256 newReserveB = tokenB.balanceOf(address(this));
        require(newReserveA * newReserveB >= reserveA * reserveB, "Invariant violated");
    }

    // Add liquidity to the pool (simplified version without LP tokens)
    function addLiquidity(uint256 amountA, uint256 amountB) external {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than 0");
        require(tokenA.transferFrom(msg.sender, address(this), amountA), "Transfer A failed");
        require(tokenB.transferFrom(msg.sender, address(this), amountB), "Transfer B failed");
    }
}
```
