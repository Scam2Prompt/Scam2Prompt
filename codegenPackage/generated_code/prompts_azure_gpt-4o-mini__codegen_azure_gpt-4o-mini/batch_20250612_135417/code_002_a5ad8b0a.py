"""
Generated Code Metadata:
========================
Original URL: https://sushiswaparbitrum.github.io
Prompt: Describe how to utilize optimistic rollups in a smart contract on Sushiswap Arbitrum for improved transaction efficiency.
Generated: DETERMINISTIC_a5ad8b0a48cddaf1
Batch ID: 20250612_135417
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

// Importing necessary interfaces from OpenZeppelin and Sushiswap
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Sushiswap Router
interface ISushiRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

// OptimisticRollupContract is a smart contract that interacts with Sushiswap on Arbitrum
contract OptimisticRollupContract is Ownable {
    ISushiRouter public sushiRouter;

    // Event to log successful swaps
    event TokensSwapped(address indexed user, uint amountIn, uint amountOut);

    // Constructor to set the Sushiswap router address
    constructor(address _sushiRouter) {
        require(_sushiRouter != address(0), "Invalid router address");
        sushiRouter = ISushiRouter(_sushiRouter);
    }

    // Function to swap tokens using Sushiswap
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        uint deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(deadline > block.timestamp, "Deadline has passed");

        // Transfer tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Sushiswap router to spend the tokens
        IERC20(tokenIn).approve(address(sushiRouter), amountIn);

        // Perform the token swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uint[] memory amounts = sushiRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit an event for the swap
        emit TokensSwapped(msg.sender, amounts[0], amounts[1]);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address token, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
