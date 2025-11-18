"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Write a Solidity contract that includes a `receive()` function for handling Ether and integrates Uniswap V2 core libraries, as outlined in the Uniswap Slippage Bot.
Generated: DETERMINISTIC_573114b93ba43ace
Batch ID: 20250612_154809
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

// Import Uniswap V2 core libraries
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract SlippageBot {
    // State variable for Uniswap router
    IUniswapV2Router02 public immutable uniswapRouter;
    
    // Event to log successful trades
    event TradeExecuted(address indexed trader, uint amountIn, uint amountOutMin, address[] path);

    // Constructor to set the router address
    constructor(address _router) {
        require(_router != address(0), "Router address cannot be zero");
        uniswapRouter = IUniswapV2Router02(_router);
    }

    // Receive function to handle incoming Ether
    receive() external payable {
        // Ether received will be handled in trade function
        // Can be used to trigger trades automatically
    }

    /**
     * @dev Executes a trade on Uniswap with slippage control.
     * @param amountIn The amount of input tokens to trade.
     * @param amountOutMin The minimum amount of output tokens to receive to avoid slippage.
     * @param path The path of the tokens to trade.
     * @param to The address to send the output tokens to.
     * @param deadline The deadline for the trade to be executed.
     */
    function executeTrade(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external payable {
        // Ensure contract has enough Ether for the trade
        require(msg.value >= amountIn, "Insufficient Ether sent");
        
        // Approve the router to spend the input token
        require(IERC20(path[0]).approve(address(uniswapRouter), amountIn), "Token approval failed");

        // Execute the trade
        uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        // Emit event for trade execution
        emit TradeExecuted(msg.sender, amountIn, amountOutMin, path);
    }

    /**
     * @dev Allows contract to withdraw any ERC20 tokens sent directly to it.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint amount) external {
        require(token != address(0), "Token address cannot be zero");
        require(IERC20(token).transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Allows contract to withdraw Ether.
     * @param to The address to send Ether to.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawEther(address payable to, uint amount) external {
        require(to != address(0), "Recipient address cannot be zero");
        require(address(this).balance >= amount, "Insufficient balance");
        (bool success, ) = to.call{value: amount}("");
        require(success, "Ether transfer failed");
    }
}
```
