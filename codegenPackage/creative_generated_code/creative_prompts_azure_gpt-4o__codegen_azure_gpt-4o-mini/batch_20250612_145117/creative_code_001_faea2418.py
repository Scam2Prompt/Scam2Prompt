"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ponyswap.finance
Prompt: Provide an example of how to use a smart contract to enable token swapping functionality in a DeFi app similar to PonySwap.
Generated: DETERMINISTIC_faea24187a5ec660
Batch ID: 20250612_145117
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the token swap functionality
interface ISwapRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

// The main contract for token swapping
contract TokenSwap is Ownable {
    // State variable to hold the swap router address
    ISwapRouter public swapRouter;

    // Event to emit details of token swaps
    event TokensSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint amountIn, uint amountOut);

    // Constructor to initialize the swap router
    constructor(ISwapRouter _swapRouter) {
        swapRouter = _swapRouter;
    }

    // Function to swap tokens
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        uint deadline
    ) external {
        // Ensure the input amount is greater than zero
        require(amountIn > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the swap router to spend the tokens
        IERC20(tokenIn).approve(address(swapRouter), amountIn);

        // Define the path for the token swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Perform the token swap
        uint[] memory amounts = swapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit an event for the swap
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amounts[1]);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawToken(address token, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
