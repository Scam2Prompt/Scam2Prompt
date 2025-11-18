"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Write a Solidity contract that emits logs for debugging purposes and integrates Uniswap V2 interfaces, similar to the Uniswap Slippage Bot.
Generated: DETERMINISTIC_68cb05a582d7ef72
Batch ID: 20250612_154809
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

// Importing the required interfaces from Uniswap V2
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The SlippageBot contract allows for trading via Uniswap while emitting logs for debugging
contract SlippageBot is Ownable {
    IUniswapV2Router02 public uniswapRouter;
    
    // Events for logging trades and errors
    event TradeExecuted(address indexed user, address indexed tokenIn, address indexed tokenOut, uint amountIn, uint amountOut, uint slippage);
    event Error(string message);
    
    // Constructor to initialize the Uniswap router
    constructor(address _router) {
        uniswapRouter = IUniswapV2Router02(_router);
    }

    // Function to execute a token swap on Uniswap
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        address to,
        uint deadline
    ) external onlyOwner {
        // Transfer tokens from the owner to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Approve the Uniswap router to spend the tokens
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Prepare the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Execute the swap and capture any potential errors
        try uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        ) returns (uint[] memory amounts) {
            emit TradeExecuted(msg.sender, tokenIn, tokenOut, amountIn, amounts[1], amountOutMin);
        } catch {
            emit Error("Swap failed");
        }
    }

    // Function to rescue tokens sent to this contract by mistake
    function rescueTokens(address token, uint amount, address to) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(to, amount);
    }
}
```
