"""
Generated Code Metadata:
========================
Original URL: https://sushi-eat-need.com
Prompt: Design a simple smart contract using Solidity that utilizes SushiSwap's liquidity pools for token trading.
Generated: DETERMINISTIC_8f57cb3486a5d04c
Batch ID: 20250622_211100
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

// Import interfaces for SushiSwap
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface ISushiSwapRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
}

contract SushiSwapTrader {
    // Address of the SushiSwap router
    address public immutable sushiSwapRouter;

    // Owner of the contract
    address public owner;

    // Event emitted after a successful trade
    event TokensSwapped(
        address indexed trader,
        uint256 amountIn,
        uint256 amountOut,
        address[] path
    );

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _sushiSwapRouter) {
        require(_sushiSwapRouter != address(0), "Invalid router address");
        sushiSwapRouter = _sushiSwapRouter;
        owner = msg.sender;
    }

    /**
     * @dev Swap tokens using SushiSwap liquidity pools.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of input tokens to swap.
     * @param amountOutMin Minimum amount of output tokens expected.
     * @param deadline Timestamp by which the trade must be completed.
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(deadline > block.timestamp, "Deadline has passed");

        // Transfer input tokens from the sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve SushiSwap router to spend the input tokens
        IERC20(tokenIn).approve(sushiSwapRouter, amountIn);

        // Define the token swap path (tokenIn -> tokenOut)
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Perform the token swap
        uint256[] memory amounts = ISushiSwapRouter(sushiSwapRouter).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit an event for the successful swap
        emit TokensSwapped(msg.sender, amountIn, amounts[1], path);
    }

    /**
     * @dev Withdraw tokens from the contract (only owner).
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        IERC20(token).transferFrom(address(this), owner, amount);
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
