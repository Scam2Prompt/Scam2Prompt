"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Write a Solidity contract that interacts with the HyperEVM Native Dex for automated token swaps based on predefined conditions.
Generated: DETERMINISTIC_366acbca5e6d2da2
Batch ID: 20250612_154057
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

// Importing required OpenZeppelin contracts for safe token handling
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the HyperEVM Native Dex
interface IHyperEvmDex {
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountOut);
}

// Automated Token Swap Contract
contract AutomatedTokenSwap is Ownable {
    // The address of the HyperEVM Native Dex
    IHyperEvmDex public dex;

    // Event to log successful swaps
    event TokenSwapped(
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    // Constructor to set the Dex address
    constructor(IHyperEvmDex _dex) {
        require(address(_dex) != address(0), "Invalid Dex address");
        dex = _dex;
    }

    // Function to perform a token swap based on predefined conditions
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external onlyOwner {
        require(amountIn > 0, "Amount in must be greater than 0");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Transfer tokens from the contract to the Dex
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Approve the Dex to spend the tokens
        IERC20(tokenIn).approve(address(dex), amountIn);

        // Execute the swap
        uint256 amountOut = dex.swap(tokenIn, tokenOut, amountIn, amountOutMin, msg.sender, deadline);

        // Emit an event for the swap
        emit TokenSwapped(tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (only in case of emergencies)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
