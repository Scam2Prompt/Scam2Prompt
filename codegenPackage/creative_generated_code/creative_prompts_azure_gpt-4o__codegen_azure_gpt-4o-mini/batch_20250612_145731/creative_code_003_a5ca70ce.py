"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copiedcode.pages.dev
Prompt: Write a Solidity contract that interacts with the WETH and Uniswap contract addresses provided in the Oneinch Slippage Bot code to execute token swaps with slippage protection.
Generated: DETERMINISTIC_a5ca70cec208679e
Batch ID: 20250612_145731
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

// Import necessary interfaces from OpenZeppelin and Uniswap
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract SlippageProtectedSwap is Ownable {
    // Uniswap Router address for token swaps
    IUniswapV2Router02 public uniswapRouter;
    // WETH address (Wrapped Ether)
    address public WETH;

    // Event to emit swap details
    event TokensSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint amountIn, uint amountOut);

    // Constructor to set the Uniswap Router and WETH address
    constructor(address _uniswapRouter, address _WETH) {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        WETH = _WETH;
    }

    // Function to swap tokens with slippage protection
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint minAmountOut,
        uint deadline
    ) external {
        require(amountIn > 0, "Amount must be greater than 0");
        require(minAmountOut > 0, "Minimum amount out must be greater than 0");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Transfer tokenIn from sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve Uniswap Router to spend tokenIn
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Perform swap
        address[] memory path;
        if (tokenIn == WETH || tokenOut == WETH) {
            // If the swap is directly involving WETH
            path = new address[](2);
            path[0] = tokenIn; // tokenIn
            path[1] = tokenOut; // tokenOut
        } else {
            // For swaps not involving WETH
            path = new address[](3);
            path[0] = tokenIn; // tokenIn
            path[1] = WETH;    // WETH
            path[2] = tokenOut; // tokenOut
        }

        // Execute swap using Uniswap Router
        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            msg.sender,
            deadline
        );

        // Emit event for successful swap
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amounts[0], amounts[amounts.length - 1]);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint amount) external onlyOwner {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to change the Uniswap Router address (if necessary)
    function updateRouter(address newRouter) external onlyOwner {
        uniswapRouter = IUniswapV2Router02(newRouter);
    }
}
```
