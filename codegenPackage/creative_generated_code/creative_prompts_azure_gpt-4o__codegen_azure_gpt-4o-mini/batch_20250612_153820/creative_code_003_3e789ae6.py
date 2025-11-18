"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://store-uni-app.com
Prompt: Write a Solidity smart contract that integrates with the Uniswap protocol to automate token swaps based on predefined market conditions.
Generated: DETERMINISTIC_3e789ae645f93bc8
Batch ID: 20250612_153820
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

// Import necessary interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the smart contract
contract AutomatedTokenSwap is Ownable {
    // Uniswap router address (mainnet example, change as needed)
    IUniswapV2Router02 public uniswapRouter;
    
    // Event to log successful swaps
    event TokensSwapped(address indexed sender, uint256 amountIn, uint256 amountOut, address tokenIn, address tokenOut);

    // Constructor to set the Uniswap router address
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_router);
    }

    // Function to perform a token swap
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external onlyOwner {
        // Transfer the specified amount of tokenIn to the contract
        require(IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Approve Uniswap to spend the token
        require(IERC20(tokenIn).approve(address(uniswapRouter), amountIn), "Approval failed");

        // Define the path for the swap
        address[] memory path;
        if (tokenIn == uniswapRouter.WETH() || tokenOut == uniswapRouter.WETH()) {
            // If one of the tokens is WETH, swap directly through WETH
            path = new address[](2);
            path[0] = tokenIn;
            path[1] = tokenOut;
        } else {
            // Otherwise, swap through WETH
            path = new address[](3);
            path[0] = tokenIn;
            path[1] = uniswapRouter.WETH();
            path[2] = tokenOut;
        }

        // Perform the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        // Emit an event to log the swap details
        emit TokensSwapped(msg.sender, amounts[0], amounts[amounts.length - 1], tokenIn, tokenOut);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(msg.sender, amount), "Withdrawal failed");
    }

    // Function to withdraw Ether from the contract
    function withdrawEther(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
