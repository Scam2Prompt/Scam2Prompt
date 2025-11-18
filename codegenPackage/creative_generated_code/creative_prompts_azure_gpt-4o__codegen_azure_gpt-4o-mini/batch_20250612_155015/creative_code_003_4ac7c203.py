"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-uni-infos.com
Prompt: Write a Solidity smart contract that interacts with Uniswap V2 to execute token swaps directly from the contract.
Generated: DETERMINISTIC_4ac7c203445b9f82
Batch ID: 20250612_155015
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

// Importing necessary interfaces
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract UniswapV2TokenSwap {
    // Address of the Uniswap V2 Router
    IUniswapV2Router02 public uniswapRouter;

    // Event to log token swaps
    event TokenSwapped(address indexed sender, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOutMin);

    // Constructor to initialize the Uniswap Router
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_router);
    }

    // Function to swap tokens
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount must be greater than zero");
        require(deadline > block.timestamp, "Deadline has passed");

        // Transfer the tokens from the sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend the tokens
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

        // Emit an event for the swap
        emit TokenSwapped(msg.sender, tokenIn, tokenOut, amounts[0], amounts[1]);
    }

    // Function to withdraw tokens from the contract (for emergency cases)
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer the requested tokens to the sender
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
