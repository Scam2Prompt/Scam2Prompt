"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lopecoin-presale.pages.dev
Prompt: Write a Solidity contract for a decentralized exchange (DEX) on Binance Smart Chain, including token swaps, liquidity pools, and yield farming features inspired by LopeSwap.
Generated: DETERMINISTIC_91d5e2a2766d1abc
Batch ID: 20250612_152235
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

// Import required libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the PancakeSwap Router
interface IPancakeSwapRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountA, uint256 amountB, uint256 liquidity);
}

// Main DEX contract
contract DecentralizedExchange is Ownable {
    using SafeMath for uint256;

    // Router address for PancakeSwap
    IPancakeSwapRouter public pancakeSwapRouter;

    // Mapping to hold user liquidity
    mapping(address => mapping(address => uint256)) public userLiquidity;

    // Events for logging
    event TokensSwapped(address indexed user, address inputToken, address outputToken, uint256 amountIn, uint256 amountOut);
    event LiquidityAdded(address indexed user, address tokenA, address tokenB, uint256 amountA, uint256 amountB);

    // Constructor to set the PancakeSwap router address
    constructor(address _routerAddress) {
        pancakeSwapRouter = IPancakeSwapRouter(_routerAddress);
    }

    // Function to swap tokens
    function swapTokens(
        address inputToken,
        address outputToken,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than 0");
        require(IERC20(inputToken).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Approve the router to spend the tokens
        IERC20(inputToken).approve(address(pancakeSwapRouter), amountIn);

        // Define the swap path
        address[] memory path = new address[](2);
        path[0] = inputToken;
        path[1] = outputToken;

        // Execute the swap
        uint256[] memory amounts = pancakeSwapRouter.swapExactTokensForTokens(amountIn, amountOutMin, path, msg.sender, deadline);
        
        emit TokensSwapped(msg.sender, inputToken, outputToken, amounts[0], amounts[1]);
    }

    // Function to add liquidity to the pool
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        uint256 deadline
    ) external {
        require(amountADesired > 0 && amountBDesired > 0, "Amounts must be greater than 0");
        
        // Transfer tokens to the contract
        require(IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired), "Transfer of tokenA failed");
        require(IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired), "Transfer of tokenB failed");

        // Approve the router to spend the tokens
        IERC20(tokenA).approve(address(pancakeSwapRouter), amountADesired);
        IERC20(tokenB).approve(address(pancakeSwapRouter), amountBDesired);

        // Add liquidity to the pool
        (uint256 amountA, uint256 amountB, uint256 liquidity) = pancakeSwapRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );

        userLiquidity[msg.sender][tokenA] = userLiquidity[msg.sender][tokenA].add(amountA);
        userLiquidity[msg.sender][tokenB] = userLiquidity[msg.sender][tokenB].add(amountB);

        emit LiquidityAdded(msg.sender, tokenA, tokenB, amountA, amountB);
    }

    // Function to withdraw tokens
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
