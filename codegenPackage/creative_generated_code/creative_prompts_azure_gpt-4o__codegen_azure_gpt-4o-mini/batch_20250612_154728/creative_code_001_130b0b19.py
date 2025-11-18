"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Generate Solidity code for deploying a smart contract that integrates zkSwap Finance's Universal Router to facilitate token swaps across multiple chains.
Generated: DETERMINISTIC_130b0b19d0441812
Batch ID: 20250612_154728
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

// Importing necessary interfaces and contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the zkSwap Universal Router
interface IUniversalRouter {
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        address to,
        uint256 deadline
    ) external returns (uint256 amountOut);
}

// Smart contract for facilitating token swaps using zkSwap Finance's Universal Router
contract TokenSwapper is Ownable {
    using Address for address;

    IUniversalRouter public universalRouter;

    // Event emitted when a swap occurs
    event SwapExecuted(
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        address indexed to
    );

    // Constructor to set the Universal Router address
    constructor(address _universalRouter) {
        require(_universalRouter != address(0), "Invalid router address");
        universalRouter = IUniversalRouter(_universalRouter);
    }

    // Function to swap tokens
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    ) external returns (uint256) {
        require(deadline >= block.timestamp, "Deadline exceeded");
        require(amountIn > 0, "Amount to swap must be greater than zero");

        // Transfer the input tokens from the sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the router to spend the tokens
        IERC20(tokenIn).approve(address(universalRouter), amountIn);

        // Execute the swap
        uint256 amountOut = universalRouter.swapTokens(
            tokenIn,
            tokenOut,
            amountIn,
            minAmountOut,
            msg.sender,
            deadline
        );

        // Emit event for the swap
        emit SwapExecuted(tokenIn, tokenOut, amountIn, amountOut, msg.sender);
        
        return amountOut;
    }

    // Function to withdraw tokens from the contract in case of emergency
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to update the Universal Router address (onlyOwner)
    function updateRouter(address newRouter) external onlyOwner {
        require(newRouter != address(0), "Invalid router address");
        universalRouter = IUniversalRouter(newRouter);
    }
}
```
