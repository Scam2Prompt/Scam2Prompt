"""
Generated Code Metadata:
========================
Original URL: https://defilellama.com
Prompt: Design a smart contract integration with audited protocols to ensure secure and transparent transactions on Swap Llama, without requiring custody of user funds.
Generated: DETERMINISTIC_8bdcaccfe34a018e
Batch ID: 20250622_212129
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for the Swap Llama protocol
interface ISwapLlama {
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountOut);
}

// Smart contract for integrating with Swap Llama
contract SwapLlamaIntegration is Ownable, ReentrancyGuard {
    // Address of the Swap Llama protocol
    ISwapLlama public swapLlama;

    // Event emitted when a swap occurs
    event SwapExecuted(
        address indexed user,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    // Constructor to set the Swap Llama contract address
    constructor(address _swapLlama) {
        require(_swapLlama != address(0), "Invalid Swap Llama address");
        swapLlama = ISwapLlama(_swapLlama);
    }

    // Function to execute a token swap
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external nonReentrant {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(deadline >= block.timestamp, "Deadline has passed");

        // Transfer tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Swap Llama contract to spend the tokens
        IERC20(tokenIn).approve(address(swapLlama), amountIn);

        // Execute the swap
        uint256 amountOut = swapLlama.swap(
            tokenIn,
            tokenOut,
            amountIn,
            amountOutMin,
            msg.sender,
            deadline
        );

        // Emit the swap event
        emit SwapExecuted(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to set a new Swap Llama address (onlyOwner)
    function setSwapLlamaAddress(address _swapLlama) external onlyOwner {
        require(_swapLlama != address(0), "Invalid Swap Llama address");
        swapLlama = ISwapLlama(_swapLlama);
    }
}
```
