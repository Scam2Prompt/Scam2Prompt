"""
Generated Code Metadata:
========================
Original URL: https://mindofpepe-recovery.vercel.app
Prompt: Develop a smart contract for fast cryptocurrency exchange, utilizing the "FAST EXCHANGE CHOOSE" feature highlighted on the website.
Generated: DETERMINISTIC_76c9cb0331024d4a
Batch ID: 20250612_154752
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FastExchange
 * @dev A smart contract for fast cryptocurrency exchange with a choose feature.
 */
contract FastExchange is Ownable {
    // Event emitted when a successful exchange occurs
    event ExchangeExecuted(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping to store exchange rates for different token pairs
    mapping(address => mapping(address => uint256)) public exchangeRates;

    /**
     * @dev Sets the exchange rate for a specific token pair.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param rate The exchange rate (amount of tokenOut per tokenIn).
     */
    function setExchangeRate(address tokenIn, address tokenOut, uint256 rate) external onlyOwner {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token address");
        require(rate > 0, "Rate must be greater than zero");
        exchangeRates[tokenIn][tokenOut] = rate;
    }

    /**
     * @dev Executes the exchange of tokens.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of input tokens to exchange.
     */
    function exchange(address tokenIn, address tokenOut, uint256 amountIn) external {
        require(amountIn > 0, "Amount must be greater than zero");
        uint256 rate = exchangeRates[tokenIn][tokenOut];
        require(rate > 0, "Exchange rate not set for this pair");

        // Calculate the amount of output tokens
        uint256 amountOut = amountIn * rate;

        // Transfer input tokens from the user to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Transfer output tokens from the contract to the user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Emit the exchange event
        emit ExchangeExecuted(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @dev Withdraws tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
