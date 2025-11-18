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
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenSwap {
    // Uniswap router address (for the mainnet, you would set this to the actual router address)
    address private constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D; 
    IUniswapV2Router02 private uniswapRouter;

    // Event emitted for token swaps
    event TokensSwapped(address indexed sender, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to initialize the Uniswap router
    constructor() {
        uniswapRouter = IUniswapV2Router02(UNISWAP_ROUTER_ADDRESS);
    }

    // Function to swap tokens on Uniswap
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts) {
        // Ensure the input token is approved for transfer
        require(IERC20(tokenIn).approve(address(uniswapRouter), amountIn), "Token approval failed");

        // Set up the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Performing the swap
        try uniswapRouter.swapExactTokensForTokens(amountIn, amountOutMin, path, to, deadline) returns (uint256[] memory receivedAmounts) {
            emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, receivedAmounts[1]);
            return receivedAmounts;
        } catch {
            revert("Swap failed");
        }
    }

    // Function to estimate the amount of tokens received for a given input amount
    function getAmountsOut(uint256 amountIn, address tokenIn, address tokenOut) external view returns (uint256[] memory amounts) {
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        return uniswapRouter.getAmountsOut(amountIn, path);
    }
}
```
