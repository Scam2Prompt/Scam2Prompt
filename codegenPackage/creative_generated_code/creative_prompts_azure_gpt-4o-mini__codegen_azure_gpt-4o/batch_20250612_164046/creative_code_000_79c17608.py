"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoden.pages.dev
Prompt: Write a Solidity contract that implements a slippage bot for the 1inch exchange, referencing the provided code structure and Uniswap interfaces.
Generated: DETERMINISTIC_79c17608f4e0f113
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
pragma solidity ^0.8.17;

// Import required interfaces from Uniswap and external libraries
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

// Interface for the 1inch aggregation protocol
interface I1InchAggregationRouterV4 {
    function swap(
        address caller,
        bytes calldata swapDescription,
        bytes calldata data
    ) external payable returns (uint256 returnAmount, uint256 spentAmount);
}

contract SlippageBot {
    // State variables
    address public owner; // Owner of the contract
    I1InchAggregationRouterV4 public oneInchRouter; // 1inch router address
    IUniswapV2Router02 public uniswapRouter; // Uniswap router address

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "SlippageBot: Only owner can call this function");
        _;
    }

    // Events for logging activities
    event SwapExecuted(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Contract constructor
    constructor(I1InchAggregationRouterV4 _oneInchRouter, IUniswapV2Router02 _uniswapRouter) {
        owner = msg.sender; // Set the contract owner
        oneInchRouter = _oneInchRouter; // Initialize 1inch router
        uniswapRouter = _uniswapRouter; // Initialize Uniswap router
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "SlippageBot: New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Function to execute a swap on 1inch
    function executeOneInchSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        bytes calldata swapData
    ) external onlyOwner returns (uint256 amountOut) {
        // Approve the 1inch router to spend tokens
        IERC20(tokenIn).approve(address(oneInchRouter), amountIn);

        // Perform the swap
        (uint256 returnAmount, ) = oneInchRouter.swap(
            address(this),
            swapData,
            swapData
        );

        // Emit the swap event
        emit SwapExecuted(tokenIn, tokenOut, amountIn, returnAmount);

        // Return the swapped amount
        return returnAmount;
    }

    // Function to execute a swap on Uniswap
    function executeUniswapSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path
    ) external onlyOwner returns (uint256 amountOut) {
        // Approve the Uniswap router to spend tokens
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Perform the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            address(this),
            block.timestamp
        );

        // Emit the swap event
        emit SwapExecuted(tokenIn, tokenOut, amountIn, amounts[amounts.length - 1]);

        // Return the swapped amount
        return amounts[amounts.length - 1];
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to withdraw Ether from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "SlippageBot: Insufficient balance");
        payable(owner).transfer(amount);
    }

    // Function to withdraw ERC20 tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).balanceOf(address(this)) >= amount, "SlippageBot: Insufficient token balance");
        IERC20(token).transfer(owner, amount);
    }
}
```
