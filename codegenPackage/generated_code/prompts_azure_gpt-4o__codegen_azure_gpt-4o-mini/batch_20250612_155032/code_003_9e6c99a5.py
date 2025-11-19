"""
Generated Code Metadata:
========================
Original URL: https://kantor-usdc.com
Prompt: Provide an example of a smart contract or script for facilitating cryptocurrency exchanges (e.g., Bitcoin to PLN) using the Ari10 crypto terminal.
Generated: DETERMINISTIC_9e6c99a52e4e57b4
Batch ID: 20250612_155032
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

// Importing necessary interfaces for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for facilitating cryptocurrency exchanges
contract CryptoExchange is Ownable {
    // Event to log successful exchanges
    event ExchangeExecuted(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping to store exchange rates (token address => rate in PLN)
    mapping(address => uint256) public exchangeRates;

    // Function to set exchange rate for a specific token
    function setExchangeRate(address token, uint256 rate) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(rate > 0, "Rate must be greater than zero");
        exchangeRates[token] = rate;
    }

    // Function to exchange tokens
    function exchangeTokens(address tokenIn, uint256 amountIn) external {
        require(exchangeRates[tokenIn] > 0, "Exchange rate not set for this token");
        
        // Calculate the amount of PLN equivalent to the input token
        uint256 rate = exchangeRates[tokenIn];
        uint256 amountOut = amountIn * rate;

        // Transfer tokens from user to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Transfer equivalent PLN (or another token) to the user
        // Assuming the contract holds PLN or equivalent token
        // Replace 'PLN_TOKEN_ADDRESS' with the actual token address for PLN
        IERC20(PLN_TOKEN_ADDRESS).transfer(msg.sender, amountOut);

        // Emit event for successful exchange
        emit ExchangeExecuted(msg.sender, tokenIn, PLN_TOKEN_ADDRESS, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (for owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
