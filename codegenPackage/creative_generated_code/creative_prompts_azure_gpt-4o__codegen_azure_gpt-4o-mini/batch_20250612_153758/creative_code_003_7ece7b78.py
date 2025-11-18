"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushi-eat-need.com
Prompt: Write a smart contract that integrates SushiSwap's multichain liquidity pools for swapping tokens across Ethereum and Polygon networks.
Generated: DETERMINISTIC_7ece7b78333acffe
Batch ID: 20250612_153758
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@sushiswap/core/contracts/interfaces/ISushiSwapRouter.sol";

// Smart contract for integrating SushiSwap's multichain liquidity pools
contract SushiSwapIntegration is Ownable {
    // SushiSwap Router for Ethereum and Polygon
    ISushiSwapRouter public sushiRouter;
    address public WETH;

    // Event emitted when a swap is performed
    event Swapped(address indexed sender, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the SushiSwap router and WETH address
    constructor(address _sushiRouter, address _WETH) {
        require(_sushiRouter != address(0), "Invalid SushiSwap router address");
        require(_WETH != address(0), "Invalid WETH address");
        
        sushiRouter = ISushiSwapRouter(_sushiRouter);
        WETH = _WETH;
    }

    // Function to swap tokens
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountOut) {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(deadline >= block.timestamp, "Deadline has passed");

        // Transfer tokens from sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the SushiSwap router to spend the tokens
        IERC20(tokenIn).approve(address(sushiRouter), amountIn);

        // Set up the path for the swap
        address[] memory path;
        if (tokenIn == WETH || tokenOut == WETH) {
            // Direct swap with WETH
            path = new address[](2);
            path[0] = tokenIn;
            path[1] = tokenOut;
        } else {
            // Swap through WETH
            path = new address[](3);
            path[0] = tokenIn;
            path[1] = WETH;
            path[2] = tokenOut;
        }

        // Perform the swap
        uint256[] memory amounts = sushiRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        // Emit the event for the swap
        emit Swapped(msg.sender, tokenIn, tokenOut, amountIn, amounts[amounts.length - 1]);

        return amounts[amounts.length - 1];
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to set a new SushiSwap router address
    function setSushiRouter(address _sushiRouter) external onlyOwner {
        require(_sushiRouter != address(0), "Invalid SushiSwap router address");
        sushiRouter = ISushiSwapRouter(_sushiRouter);
    }
}
```
