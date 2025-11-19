"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: What are the best practices for using ParaSwaps in Solidity to avoid reentrancy attacks and ensure safe execution of external functions?
Generated: DETERMINISTIC_8c17330a08c737eb
Batch ID: 20250612_155712
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract ParaSwapSafe is ReentrancyGuard {
    using Address for address;

    // Event to log successful swaps
    event SwapExecuted(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Function to execute a swap using ParaSwap
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        address recipient,
        bytes calldata swapData
    ) external nonReentrant {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Call the ParaSwap contract to execute the swap
        (bool success, bytes memory returnData) = address(this).functionCall(swapData, "Swap failed");
        require(success, "Swap execution failed");

        // Decode the returned data to get the amount out
        uint256 amountOut = abi.decode(returnData, (uint256));
        require(amountOut >= minAmountOut, "Insufficient output amount");

        // Transfer the swapped tokens to the recipient
        IERC20(tokenOut).transfer(recipient, amountOut);

        emit SwapExecuted(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
