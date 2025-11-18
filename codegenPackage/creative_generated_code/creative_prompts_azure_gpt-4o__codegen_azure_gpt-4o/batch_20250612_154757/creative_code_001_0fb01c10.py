"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni-store-info.at
Prompt: Generate Solidity code for a smart contract that interacts with Uniswap V2 to perform ERC-20 token swaps.
Generated: DETERMINISTIC_0fb01c10027401f6
Batch ID: 20250612_154757
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

// Importing the interfaces for ERC-20 tokens and Uniswap V2 router
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract TokenSwap {
    // Address of the Uniswap V2 Router
    address private constant UNISWAP_ROUTER = 0xYourUniswapRouterAddress; // Replace with actual router address

    // Instance of the Uniswap V2 Router
    IUniswapV2Router02 private immutable uniswapRouter;

    constructor() {
        uniswapRouter = IUniswapV2Router02(UNISWAP_ROUTER);
    }

    /**
     * @dev Swap tokens on Uniswap V2.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of input tokens to swap.
     * @param amountOutMin Minimum amount of output tokens expected.
     * @param to Recipient of the output tokens.
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to
    ) external {
        require(amountIn > 0, "TokenSwap: Input amount must be greater than zero");
        require(to != address(0), "TokenSwap: Invalid recipient address");

        // Approve Uniswap Router to spend the input tokens
        IERC20(tokenIn).approve(UNISWAP_ROUTER, amountIn);

        // Define the path for the swap (input token -> output token)
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Perform the token swap using Uniswap V2 Router
        try uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            block.timestamp
        ) {
            // Successful swap
        } catch {
            revert("TokenSwap: Swap failed");
        }
    }

    /**
     * @dev Emergency function to recover stuck tokens.
     * @param token Address of the token to recover.
     * @param to Address to send the recovered tokens.
     * @param amount Amount of tokens to recover.
     */
    function recoverTokens(
        address token,
        address to,
        uint256 amount
    ) external {
        require(to != address(0), "TokenSwap: Invalid recipient address");
        require(amount > 0, "TokenSwap: Amount must be greater than zero");

        // Transfer the tokens to the provided address
        IERC20(token).transfer(to, amount);
    }
}
```
