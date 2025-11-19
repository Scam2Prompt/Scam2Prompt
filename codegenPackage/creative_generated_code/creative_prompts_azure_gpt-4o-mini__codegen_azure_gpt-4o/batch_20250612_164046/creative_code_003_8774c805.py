"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdnsource.pages.dev
Prompt: Explain how to import and use the Uniswap V2 interfaces in a Solidity contract for a slippage bot, as demonstrated in the OneinchSlippageBot example.
Generated: DETERMINISTIC_8774c8053df1d05b
Batch ID: 20250612_164046
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

// Import statements for Uniswap V2 interfaces
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

// Slippage Bot contract
contract SlippageBot {
    // Address of the Uniswap V2 Router
    IUniswapV2Router02 public immutable uniswapRouter;

    // Events for logging slippage detection and action
    event SlippageDetected(address tokenA, address tokenB, uint256 amountIn, uint256 expectedAmountOut, uint256 actualAmountOut);
    event TradeExecuted(address tokenA, address tokenB, uint256 amountIn, uint256 amountOut);

    // Constructor to initialize the Uniswap Router
    constructor(address _uniswapRouter) {
        require(_uniswapRouter != address(0), "Uniswap router address cannot be zero");
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    /**
     * @notice Executes a token swap and monitors slippage
     * @param tokenA The address of the first token
     * @param tokenB The address of the second token
     * @param amountIn The amount of tokenA to swap
     * @param slippageTolerance The maximum allowable slippage (in percentage)
     */
    function executeSwapWithSlippageCheck(
        address tokenA,
        address tokenB,
        uint256 amountIn,
        uint256 slippageTolerance
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(slippageTolerance <= 100, "Slippage tolerance must be <= 100%");

        // Get the pair address to ensure it exists
        address pair = IUniswapV2Factory(uniswapRouter.factory()).getPair(tokenA, tokenB);
        require(pair != address(0), "Token pair does not exist");

        // Calculate the expected amount using the current reserves
        (uint256 reserveA, uint256 reserveB, ) = IUniswapV2Pair(pair).getReserves();
        require(reserveA > 0 && reserveB > 0, "Reserves must be greater than zero");

        uint256 expectedAmountOut = uniswapRouter.getAmountOut(amountIn, reserveA, reserveB);

        // Perform the swap and capture the actual output amount
        uint256 minAmountOut = (expectedAmountOut * (100 - slippageTolerance)) / 100;
        address[] memory path = new address[](2);
        path[0] = tokenA;
        path[1] = tokenB;

        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            msg.sender,
            block.timestamp + 600 // Allow 10 minutes for the transaction
        );

        uint256 actualAmountOut = amounts[1];

        // Emit events based on the observed slippage
        if (actualAmountOut < expectedAmountOut) {
            emit SlippageDetected(tokenA, tokenB, amountIn, expectedAmountOut, actualAmountOut);
        }

        emit TradeExecuted(tokenA, tokenB, amountIn, actualAmountOut);
    }
}
```
