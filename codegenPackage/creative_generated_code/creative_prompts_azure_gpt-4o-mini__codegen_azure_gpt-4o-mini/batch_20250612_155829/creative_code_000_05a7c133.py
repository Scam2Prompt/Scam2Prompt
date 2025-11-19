"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://txtecontract.pages.dev
Prompt: Write a Solidity contract that implements a slippage bot for the 1inch exchange, referencing the Uniswap V2 interfaces as shown in the provided code.
Generated: DETERMINISTIC_05a7c1333f89c984
Batch ID: 20250612_155829
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

// Import the required interfaces
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// SlippageBot contract for executing trades with slippage control
contract SlippageBot is Ownable {
    IUniswapV2Router02 public uniswapRouter;
    uint256 public slippage; // Slippage percentage, e.g., 500 for 5%

    // Events for logging actions
    event TokensSwapped(address indexed sender, uint256 amountIn, uint256 amountOutMin, address[] path);

    // Constructor to initialize the router address and slippage percentage
    constructor(address _router, uint256 _slippage) {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_router);
        slippage = _slippage;
    }

    // Function to set a new slippage percentage
    function setSlippage(uint256 _slippage) external onlyOwner {
        slippage = _slippage;
    }

    // Swap function that executes the trade with slippage control
    function swapTokens(
        address[] calldata path,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external onlyOwner {
        require(path.length >= 2, "Invalid path length");
        require(amountIn > 0, "Amount must be greater than zero");

        // Approve token transfer to the router
        IERC20(path[0]).transferFrom(msg.sender, address(this), amountIn);
        IERC20(path[0]).approve(address(uniswapRouter), amountIn);

        // Calculate the minimum amount out considering slippage
        uint256 amountOutMinWithSlippage = (amountOutMin * (10000 - slippage)) / 10000;

        // Execute the swap
        try uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMinWithSlippage,
            path,
            to,
            deadline
        ) {
            emit TokensSwapped(msg.sender, amountIn, amountOutMinWithSlippage, path);
        } catch {
            revert("Swap failed due to unexpected error");
        }
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Invalid amount");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Invalid amount");
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH withdrawal failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
