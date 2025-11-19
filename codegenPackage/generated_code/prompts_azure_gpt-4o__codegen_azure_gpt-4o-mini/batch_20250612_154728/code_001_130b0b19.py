"""
Generated Code Metadata:
========================
Original URL: https://zkswapfinance.gitbook.io
Prompt: Generate Solidity code for deploying a smart contract that integrates zkSwap Finance's Universal Router to facilitate token swaps across multiple chains.
Generated: DETERMINISTIC_130b0b19d0441812
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the Universal Router from zkSwap Finance
interface IUniversalRouter {
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountOut);
}

// Smart contract for facilitating token swaps using zkSwap Finance's Universal Router
contract TokenSwap is Ownable {
    using Address for address;

    // Address of the Universal Router contract
    IUniversalRouter public universalRouter;

    // Event emitted when a swap is executed
    event TokensSwapped(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the Universal Router address
    constructor(address _universalRouter) {
        require(_universalRouter != address(0), "Invalid router address");
        universalRouter = IUniversalRouter(_universalRouter);
    }

    // Function to swap tokens
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(deadline >= block.timestamp, "Deadline has passed");

        // Transfer tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Universal Router to spend the tokens
        IERC20(tokenIn).approve(address(universalRouter), amountIn);

        // Execute the swap
        uint256 amountOut = universalRouter.swapTokens(tokenIn, tokenOut, amountIn, amountOutMin, msg.sender, deadline);

        // Emit the swap event
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to update the Universal Router address (only owner)
    function updateRouter(address newRouter) external onlyOwner {
        require(newRouter != address(0), "Invalid router address");
        universalRouter = IUniversalRouter(newRouter);
    }
}
```
