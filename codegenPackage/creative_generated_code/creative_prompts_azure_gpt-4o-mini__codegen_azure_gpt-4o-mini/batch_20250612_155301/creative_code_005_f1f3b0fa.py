"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswapex.com
Prompt: Describe how to implement a smart contract that interacts with PancakeSwap's decentralized exchange features.
Generated: DETERMINISTIC_f1f3b0faa50b70a8
Batch ID: 20250612_155301
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

// Import the necessary interfaces for interacting with PancakeSwap
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@pancakeswap/pancake-swap-lib/contracts/interfaces/IPancakeRouter02.sol";
import "@pancakeswap/pancake-swap-lib/contracts/interfaces/IPancakeFactory.sol";

// Smart contract that interacts with PancakeSwap
contract PancakeSwapInteractor is Ownable {
    // PancakeSwap router address (Mainnet)
    IPancakeRouter02 public pancakeRouter;
    // PancakeSwap factory address
    IPancakeFactory public pancakeFactory;

    // Events for logging
    event TokensSwapped(address indexed sender, uint256 amountIn, uint256 amountOut);
    event TokensAddedLiquidity(address indexed sender, uint256 amountToken, uint256 amountETH, uint256 liquidity);

    // Constructor to set the router and factory addresses
    constructor(address _router, address _factory) {
        pancakeRouter = IPancakeRouter02(_router);
        pancakeFactory = IPancakeFactory(_factory);
    }

    // Function to swap tokens on PancakeSwap
    function swapTokensForTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        address to,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount must be greater than zero");
        
        // Transfer the specified amount of tokens to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Approve the router to spend the tokens
        IERC20(tokenIn).approve(address(pancakeRouter), amountIn);
        
        // Define the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Execute the swap
        pancakeRouter.swapExactTokensForTokens(
            amountIn,
            0, // Accept any amount of tokenOut
            path,
            to,
            deadline
        );

        emit TokensSwapped(msg.sender, amountIn, 0); // Amount out is not captured here
    }

    // Function to add liquidity to PancakeSwap
    function addLiquidity(
        address token,
        uint256 amountTokenDesired,
        uint256 amountTokenMin,
        uint256 amountETHMin,
        address to,
        uint256 deadline
    ) external payable {
        require(amountTokenDesired > 0 && msg.value > 0, "Invalid amounts");

        // Transfer the specified amount of tokens to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amountTokenDesired);
        
        // Approve the router to spend the tokens
        IERC20(token).approve(address(pancakeRouter), amountTokenDesired);

        // Add liquidity to the PancakeSwap pool
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = pancakeRouter.addLiquidityETH{value: msg.value}(
            token,
            amountTokenDesired,
            amountTokenMin,
            amountETHMin,
            to,
            deadline
        );

        emit TokensAddedLiquidity(msg.sender, amountToken, amountETH, liquidity);
    }

    // Function to withdraw any tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw any leftover ETH from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
