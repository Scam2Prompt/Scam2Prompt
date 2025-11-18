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

// Importing required interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TrustlessTokenExchange is Ownable {
    IUniswapV2Router02 public uniswapRouter;

    // Event emitted on successful token swap
    event TokenSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the Uniswap router address
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_router);
    }

    // Function to swap tokens on Uniswap
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount must be greater than 0");
        require(to != address(0), "Invalid recipient address");
        require(deadline >= block.timestamp, "Deadline has passed");

        // Transfer tokens from the sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap Router to spend tokens
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Create the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        // Emit the token swap event
        emit TokenSwapped(msg.sender, tokenIn, tokenOut, amounts[0], amounts[1]);
    }

    // Function to withdraw tokens from the contract (for potential emergencies)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
