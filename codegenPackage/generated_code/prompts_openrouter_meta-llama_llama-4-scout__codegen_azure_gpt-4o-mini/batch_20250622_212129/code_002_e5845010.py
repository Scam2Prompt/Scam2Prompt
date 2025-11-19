"""
Generated Code Metadata:
========================
Original URL: https://buttholecoin.dev
Prompt: Generate a simple smart contract in Solidity for a token swap feature similar to the one mentioned on the Butthole Coin website.
Generated: DETERMINISTIC_e58450109652db49
Batch ID: 20250622_212129
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenSwap contract allows users to swap one ERC20 token for another
contract TokenSwap is Ownable {
    // Event emitted when a swap occurs
    event TokensSwapped(address indexed user, address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    // Mapping to store the exchange rates for token swaps
    mapping(address => mapping(address => uint256)) public exchangeRates;

    // Function to set the exchange rate for a token pair
    function setExchangeRate(address fromToken, address toToken, uint256 rate) external onlyOwner {
        require(rate > 0, "Exchange rate must be greater than zero");
        exchangeRates[fromToken][toToken] = rate;
    }

    // Function to swap tokens
    function swapTokens(address fromToken, address toToken, uint256 amountIn) external {
        // Validate that the exchange rate is set
        uint256 rate = exchangeRates[fromToken][toToken];
        require(rate > 0, "Exchange rate not set for this token pair");

        // Calculate the amount of tokens to send to the user
        uint256 amountOut = amountIn * rate;

        // Transfer the input tokens from the user to the contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn);

        // Transfer the output tokens from the contract to the user
        IERC20(toToken).transfer(msg.sender, amountOut);

        // Emit the TokensSwapped event
        emit TokensSwapped(msg.sender, fromToken, toToken, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
