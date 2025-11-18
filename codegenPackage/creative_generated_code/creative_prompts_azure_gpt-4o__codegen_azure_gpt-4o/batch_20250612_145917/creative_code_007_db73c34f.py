"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoded.pages.dev
Prompt: Implement a Solidity contract that uses Uniswap interfaces (`IUniswapV2ERC20`, `IUniswapV2Factory`, `IUniswapV2Pair`) to facilitate token swaps, referencing the imports in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_db73c34fde3ed9e6
Batch ID: 20250612_145917
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

// Importing Uniswap interfaces
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2ERC20.sol";

contract TokenSwap {
    address public immutable factory; // Address of the Uniswap factory
    address public immutable WETH;   // Address of WETH token

    constructor(address _factory, address _WETH) {
        factory = _factory;
        WETH = _WETH;
    }

    // Function to perform a token swap
    function swapTokens(
        address tokenA,
        address tokenB,
        uint256 amountA,
        uint256 minAmountB,
        address to
    ) external {
        require(amountA > 0, "Invalid amountA");
        require(minAmountB > 0, "Invalid minAmountB");
        require(to != address(0), "Invalid recipient");

        // Get the pair address for the token pair
        address pair = IUniswapV2Factory(factory).getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");

        // Transfer tokens from sender to the pair contract
        IUniswapV2ERC20(tokenA).transferFrom(msg.sender, pair, amountA);

        // Get reserves for the pair
        (uint256 reserveA, uint256 reserveB,) = IUniswapV2Pair(pair).getReserves();
        require(reserveA > 0 && reserveB > 0, "Invalid reserves");

        // Calculate amount of tokenB using Uniswap formula
        uint256 amountBOut = getAmountOut(amountA, reserveA, reserveB);
        require(amountBOut >= minAmountB, "Slippage exceeded");

        // Perform the swap
        IUniswapV2Pair(pair).swap(
            tokenA == IUniswapV2Pair(pair).token0() ? 0 : amountBOut,
            tokenA == IUniswapV2Pair(pair).token0() ? amountBOut : 0,
            to,
            new bytes(0) // Data can be empty for standard swaps
        );
    }

    // Helper function to calculate output amount based on Uniswap's formula
    function getAmountOut(
        uint256 amountIn,
        uint256 reserveIn,
        uint256 reserveOut
    ) public pure returns (uint256) {
        require(amountIn > 0, "Invalid input amount");
        require(reserveIn > 0 && reserveOut > 0, "Invalid reserves");

        uint256 amountInWithFee = amountIn * 997; // Uniswap charges a 0.3% fee
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = reserveIn * 1000 + amountInWithFee;
        return numerator / denominator;
    }
}
```
