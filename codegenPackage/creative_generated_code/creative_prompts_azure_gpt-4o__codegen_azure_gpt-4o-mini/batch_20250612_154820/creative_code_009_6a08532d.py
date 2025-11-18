"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cruas.ru
Prompt: Create a tutorial for deploying a decentralized exchange (DEX) similar to Velodrome Finance using the AMM protocol on Ethereum.
Generated: DETERMINISTIC_6a08532d7d1e1856
Batch ID: 20250612_154820
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The interface for the AMM (Automated Market Maker)
interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);

    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
}

// The Decentralized Exchange contract
contract DecentralizedExchange is Ownable {
    IUniswapV2Router public immutable uniswapRouter;
    
    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed tokenA, address indexed tokenB, uint amountA, uint amountB);
    // Event emitted when a swap occurs
    event TokensSwapped(address indexed from, uint amountIn, uint amountOut);

    constructor(address _router) {
        require(_router != address(0), "Router address cannot be zero");
        uniswapRouter = IUniswapV2Router(_router);
    }

    // Function to swap tokens using Uniswap
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        uint deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Transfer the input tokens to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the router to spend the tokens
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Define the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Execute the swap
        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        emit TokensSwapped(msg.sender, amounts[0], amounts[1]);
    }

    // Function to add liquidity to the pool
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        uint deadline
    ) external {
        require(amountADesired > 0 && amountBDesired > 0, "Amounts must be greater than zero");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Transfer the tokens to the contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);

        // Approve the router to spend the tokens
        IERC20(tokenA).approve(address(uniswapRouter), amountADesired);
        IERC20(tokenB).approve(address(uniswapRouter), amountBDesired);

        // Add liquidity to the pool
        (uint amountA, uint amountB, ) = uniswapRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );

        emit LiquidityAdded(tokenA, tokenB, amountA, amountB);
    }
}
```
