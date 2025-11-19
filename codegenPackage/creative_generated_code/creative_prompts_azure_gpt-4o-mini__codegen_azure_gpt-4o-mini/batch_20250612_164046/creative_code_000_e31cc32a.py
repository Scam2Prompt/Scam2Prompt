"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botgptcode.pages.dev
Prompt: Write a Solidity contract that implements a slippage bot for the Uniswap exchange, referencing the OneinchSlippageBot structure and its use of WETH and token contract addresses.
Generated: DETERMINISTIC_e31cc32ae043473b
Batch ID: 20250612_164046
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

// Importing necessary interfaces from OpenZeppelin and Uniswap
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract OneinchSlippageBot is Ownable {
    // Address of WETH and the Uniswap router
    address private constant WETH = 0xC02aaa39b223FE8D0A0e6E25d4a6c4d0A4A3C1d3; // Example WETH address
    IUniswapV2Router02 public uniswapRouter;

    // Event emitted when a swap is executed
    event Swapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the Uniswap router address
    constructor(address _uniswapRouter) {
        require(_uniswapRouter != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    // Function to execute a swap with slippage protection
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 minAmountOut,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external onlyOwner returns (uint256[] memory amounts) {
        require(path.length >= 2, "Invalid path");
        require(deadline > block.timestamp, "Deadline expired");

        // Transfer the tokens from the caller to this contract
        IERC20(path[0]).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend the tokens
        IERC20(path[0]).approve(address(uniswapRouter), amountIn);

        // Execute the swap
        amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            to,
            deadline
        );

        // Emit an event for the swap
        emit Swapped(msg.sender, path[0], path[path.length - 1], amountIn, amounts[amounts.length - 1]);

        return amounts;
    }

    // Function to withdraw tokens from the contract (for cleaning up)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
