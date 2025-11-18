"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepe-recovery.vercel.app
Prompt: Develop a smart contract for fast cryptocurrency exchange, utilizing the "FAST EXCHANGE CHOOSE" feature highlighted on the website.
Generated: DETERMINISTIC_76c9cb0331024d4a
Batch ID: 20250612_154752
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

// Importing required libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for Fast Cryptocurrency Exchange
contract FastExchange is Ownable {
    // Structure to hold exchange rates for different tokens
    struct ExchangeRate {
        uint256 rate; // Rate of token conversion
        bool isActive; // Status of the exchange rate
    }

    // Mapping to store exchange rates for tokens
    mapping(address => mapping(address => ExchangeRate)) public exchangeRates;

    // Event emitted when an exchange occurs
    event Exchanged(address indexed fromToken, address indexed toToken, address indexed user, uint256 amountIn, uint256 amountOut);

    // Function to set exchange rates
    function setExchangeRate(address fromToken, address toToken, uint256 rate) external onlyOwner {
        require(rate > 0, "Rate must be greater than zero");
        exchangeRates[fromToken][toToken] = ExchangeRate(rate, true);
    }

    // Function to disable an exchange rate
    function disableExchangeRate(address fromToken, address toToken) external onlyOwner {
        exchangeRates[fromToken][toToken].isActive = false;
    }

    // Function to enable an exchange rate
    function enableExchangeRate(address fromToken, address toToken) external onlyOwner {
        exchangeRates[fromToken][toToken].isActive = true;
    }

    // Function to perform the token exchange
    function exchange(address fromToken, address toToken, uint256 amountIn) external {
        // Retrieve the exchange rate
        ExchangeRate memory rate = exchangeRates[fromToken][toToken];
        
        // Check if the exchange rate is active
        require(rate.isActive, "Exchange rate not active");
        
        // Calculate amount to be received
        uint256 amountOut = amountIn * rate.rate / 1e18; // Assuming rate has 18 decimals

        // Transfer from user to this contract
        require(IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Transfer the exchanged tokens to the user
        require(IERC20(toToken).transfer(msg.sender, amountOut), "Transfer failed");

        // Emit exchange event
        emit Exchanged(fromToken, toToken, msg.sender, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
    }
}
```
