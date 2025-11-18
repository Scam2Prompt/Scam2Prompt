"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethwswap.finance
Prompt: Create a smart contract example for token swapping that could be integrated into a platform like ethwswap.finance.
Generated: DETERMINISTIC_08c07dde98ddaa81
Batch ID: 20250612_154131
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

// Import the required interfaces from OpenZeppelin for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenSwap is Ownable {
    // Event emitted when a swap occurs
    event TokensSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping to store approved token pairs and their exchange rates
    mapping(address => mapping(address => uint256)) public exchangeRates;

    // Function to set the exchange rate for a token pair
    function setExchangeRate(address _tokenIn, address _tokenOut, uint256 _rate) external onlyOwner {
        // Ensure the rate is greater than zero
        require(_rate > 0, "Exchange rate must be greater than zero");
        exchangeRates[_tokenIn][_tokenOut] = _rate;
    }

    // Function to swap tokens
    function swapTokens(address _tokenIn, address _tokenOut, uint256 _amountIn) external {
        // Get the exchange rate for the given tokens
        uint256 rate = exchangeRates[_tokenIn][_tokenOut];
        require(rate > 0, "Swap rate not set for this token pair");

        // Calculate the amount of tokens to send out
        uint256 amountOut = (_amountIn * rate) / 1e18; // Assuming rate is scaled by 1e18 for precision

        // Transfer tokens from the user to this contract
        IERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);

        // Ensure the contract has enough tokens to swap
        require(IERC20(_tokenOut).balanceOf(address(this)) >= amountOut, "Insufficient tokens in contract");

        // Transfer the swapped tokens to the user
        IERC20(_tokenOut).transfer(msg.sender, amountOut);

        // Emit the swap event
        emit TokensSwapped(msg.sender, _tokenIn, _tokenOut, _amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(IERC20(_token).balanceOf(address(this)) >= _amount, "Insufficient balance in contract");
        IERC20(_token).transfer(msg.sender, _amount);
    }

    // Function to get the exchange rate for a given token pair
    function getExchangeRate(address _tokenIn, address _tokenOut) external view returns (uint256) {
        return exchangeRates[_tokenIn][_tokenOut];
    }
}
```
