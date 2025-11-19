"""
Generated Code Metadata:
========================
Original URL: https://txtecontract.pages.dev
Prompt: Create a Solidity contract that interacts with Uniswap's ERC20, Factory, and Pair interfaces to explore mempool data and withdraw profits, as demonstrated in the 1inch Slippage Bot.
Generated: DETERMINISTIC_639aa7580a4bd318
Batch ID: 20250612_154158
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

// Importing necessary interfaces from Uniswap
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Main contract for interacting with Uniswap
contract MempoolArbitrageBot is Ownable {
    IUniswapV2Router02 public uniswapRouter;
    IUniswapV2Factory public uniswapFactory;

    // Event to log profit withdrawals
    event ProfitWithdrawn(address indexed token, uint256 amount);

    // Constructor to initialize the Uniswap router and factory
    constructor(address _router, address _factory) {
        uniswapRouter = IUniswapV2Router02(_router);
        uniswapFactory = IUniswapV2Factory(_factory);
    }

    // Function to execute arbitrage
    function executeArbitrage(
        address tokenA,
        address tokenB,
        uint256 amountIn,
        uint256 minAmountOut
    ) external onlyOwner {
        // Approve the router to spend the specified amount of tokenA
        IERC20(tokenA).approve(address(uniswapRouter), amountIn);

        // Perform the swap from tokenA to tokenB
        address[] memory path = new address[](2);
        path[0] = tokenA;
        path[1] = tokenB;

        // Execute the swap
        uniswapRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            address(this),
            block.timestamp
        );
    }

    // Function to withdraw profits in a specified token
    function withdrawProfits(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No profits to withdraw");

        // Transfer the profits to the owner's address
        IERC20(token).transfer(msg.sender, balance);
        emit ProfitWithdrawn(token, balance);
    }

    // Function to get the current balance of a token held by the contract
    function getTokenBalance(address token) external view returns (uint256) {
        return IERC20(token).balanceOf(address(this));
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(msg.sender).transfer(balance);
    }
}
```
