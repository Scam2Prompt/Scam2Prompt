"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helioxdrop.web.app
Prompt: Develop a smart contract to facilitate token swaps and payments on the Solana network, incorporating Helio's merchant-first approach.
Generated: DETERMINISTIC_9c5aa87ef11907d5
Batch ID: 20250612_153648
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenSwap
 * @dev A smart contract for facilitating token swaps and payments on the Solana network.
 *      Follows Helio's merchant-first approach.
 */
contract TokenSwap is Ownable {
    // Event emitted when a swap occurs
    event TokensSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);
    
    // Mapping to store the approved tokens and their corresponding exchange rates
    mapping(address => mapping(address => uint256)) public exchangeRates;

    /**
     * @dev Set the exchange rate for a token pair.
     * @param tokenIn The address of the input token.
     * @param tokenOut The address of the output token.
     * @param rate The exchange rate from tokenIn to tokenOut (scaled by 1e18).
     */
    function setExchangeRate(address tokenIn, address tokenOut, uint256 rate) external onlyOwner {
        require(tokenIn != address(0), "Token address cannot be zero");
        require(tokenOut != address(0), "Token address cannot be zero");
        require(rate > 0, "Rate must be greater than zero");
        
        exchangeRates[tokenIn][tokenOut] = rate;
    }

    /**
     * @dev Swap tokens based on the set exchange rate.
     * @param tokenIn The address of the input token.
     * @param tokenOut The address of the output token.
     * @param amountIn The amount of the input token to swap.
     */
    function swapTokens(address tokenIn, address tokenOut, uint256 amountIn) external {
        require(amountIn > 0, "Amount must be greater than zero");
        require(exchangeRates[tokenIn][tokenOut] > 0, "Exchange rate not set for this token pair");
        
        // Calculate the amount of tokenOut to be received
        uint256 rate = exchangeRates[tokenIn][tokenOut];
        uint256 amountOut = (amountIn * rate) / 1e18;

        // Transfer tokenIn from the user to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Transfer tokenOut from the contract to the user
        require(IERC20(tokenOut).balanceOf(address(this)) >= amountOut, "Insufficient tokenOut balance in contract");
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Emit the swap event
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @dev Withdraw tokens from the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of the token to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");
        
        // Transfer tokens from the contract to the owner
        IERC20(token).transfer(msg.sender, amount);
    }

    /**
     * @dev Get the current exchange rate for a given token pair.
     * @param tokenIn The address of the input token.
     * @param tokenOut The address of the output token.
     * @return rate The exchange rate for tokenIn to tokenOut.
     */
    function getExchangeRate(address tokenIn, address tokenOut) external view returns (uint256) {
        return exchangeRates[tokenIn][tokenOut];
    }
}
```
