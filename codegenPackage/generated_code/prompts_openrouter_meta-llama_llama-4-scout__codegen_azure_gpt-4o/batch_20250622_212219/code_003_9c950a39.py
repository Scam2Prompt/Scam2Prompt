"""
Generated Code Metadata:
========================
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Create a Solidity contract that inherits from the Uniswap V2 core contracts and adds custom functionality for slippage protection, referencing the Uniswap Slippage Bot contract.
Generated: DETERMINISTIC_9c950a3908ce2e85
Batch ID: 20250622_212219
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

// Import Uniswap V2 core contracts
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2ERC20.sol";

contract SlippageProtectedSwap {
    // Address of the Uniswap V2 Factory
    address public immutable factory;

    // Address of the WETH token (used for swaps)
    address public immutable WETH;

    // Constructor to initialize factory and WETH addresses
    constructor(address _factory, address _WETH) {
        require(_factory != address(0), "Factory address cannot be zero");
        require(_WETH != address(0), "WETH address cannot be zero");
        factory = _factory;
        WETH = _WETH;
    }

    /**
     * @dev Perform a token swap with slippage protection.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of input tokens to swap.
     * @param amountOutMin Minimum amount of output tokens expected (slippage protection).
     * @param to Address to receive the output tokens.
     */
    function swapWithSlippageProtection(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to
    ) external {
        require(tokenIn != address(0), "TokenIn address cannot be zero");
        require(tokenOut != address(0), "TokenOut address cannot be zero");
        require(to != address(0), "Recipient address cannot be zero");
        require(amountIn > 0, "AmountIn must be greater than zero");

        // Get the pair address for the token pair
        address pair = IUniswapV2Factory(factory).getPair(tokenIn, tokenOut);
        require(pair != address(0), "Pair does not exist");

        // Transfer input tokens to the pair contract
        IUniswapV2ERC20(tokenIn).transferFrom(msg.sender, pair, amountIn);

        // Get reserves from the pair contract
        (uint256 reserve0, uint256 reserve1, ) = IUniswapV2Pair(pair).getReserves();

        // Determine the correct reserve order
        (uint256 reserveIn, uint256 reserveOut) = tokenIn < tokenOut
            ? (reserve0, reserve1)
            : (reserve1, reserve0);

        // Calculate the output amount using Uniswap's formula
        uint256 amountOut = getAmountOut(amountIn, reserveIn, reserveOut);
        require(amountOut >= amountOutMin, "Slippage protection triggered");

        // Perform the swap
        (uint256 amount0Out, uint256 amount1Out) = tokenIn < tokenOut
            ? (uint256(0), amountOut)
            : (amountOut, uint256(0));

        IUniswapV2Pair(pair).swap(amount0Out, amount1Out, to, new bytes(0));
    }

    /**
     * @dev Calculate the output amount based on Uniswap's formula.
     * @param amountIn Amount of input tokens.
     * @param reserveIn Reserve of input tokens in the pair.
     * @param reserveOut Reserve of output tokens in the pair.
     * @return Amount of output tokens.
     */
    function getAmountOut(
        uint256 amountIn,
        uint256 reserveIn,
        uint256 reserveOut
    ) public pure returns (uint256) {
        require(amountIn > 0, "AmountIn must be greater than zero");
        require(reserveIn > 0 && reserveOut > 0, "Reserves must be greater than zero");

        uint256 amountInWithFee = amountIn * 997; // Uniswap fee is 0.3%
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = reserveIn * 1000 + amountInWithFee;
        return numerator / denominator;
    }
}
```
