"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://store-uni-app.com
Prompt: Develop a smart contract that integrates with Uniswap to facilitate trustless token exchanges while prioritizing security and transparency.
Generated: DETERMINISTIC_98613c7f1249edd7
Batch ID: 20250612_153820
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

// Import relevant interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IERC20.sol";

// Smart contract to enable trustless token exchanges using Uniswap
contract TokenExchange {

    // Address of the Uniswap V2 Router
    IUniswapV2Router02 public immutable uniswapRouter;

    // Constructor sets the Uniswap V2 Router address
    constructor(address _uniswapRouter) {
        require(_uniswapRouter != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    // Event emitted after a successful token swap
    event TokenSwap(
        address indexed sender,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @notice Swap tokens on Uniswap
     * @param tokenIn Address of the token being swapped
     * @param tokenOut Address of the token to receive
     * @param amountIn Amount of `tokenIn` to swap
     * @param minAmountOut Minimum amount of `tokenOut` expected, for slippage protection
     * @param to Address to receive the swapped tokens
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        address to
    ) external {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token addresses");
        require(amountIn > 0, "Amount in must be greater than zero");
        require(to != address(0), "Invalid recipient address");

        // Approve the Uniswap router to spend tokenIn
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Define the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Execute the swap on Uniswap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut, // Minimum amount of tokenOut expected
            path,
            to, // Recipient of the tokenOut
            block.timestamp // Deadline (current timestamp ensures transaction won't hang indefinitely)
        );

        // Emit an event for transparency
        emit TokenSwap(msg.sender, tokenIn, tokenOut, amountIn, amounts[1]);
    }
}
```
