"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://izumi-finance.org
Prompt: Write a Solidity implementation of a token exchange mechanism that incorporates features of iZUMi Finance Swap for efficient and seamless token trading.
Generated: DETERMINISTIC_4b8202e50a436e40
Batch ID: 20250612_153809
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenExchange
 * @dev A simple token exchange mechanism inspired by iZUMi Finance Swap.
 */
contract TokenExchange is Ownable {
    using SafeERC20 for IERC20;

    // Event emitted when a swap occurs
    event TokensSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping of token pairs to swap rates (tokenIn => tokenOut => rate)
    mapping(address => mapping(address => uint256)) private _swapRates;

    /**
     * @dev Set the swap rate for a given token pair.
     * @param tokenIn The address of the input token.
     * @param tokenOut The address of the output token.
     * @param rate The swap rate (amount of tokenOut per amount of tokenIn).
     */
    function setSwapRate(address tokenIn, address tokenOut, uint256 rate) external onlyOwner {
        require(tokenIn != address(0), "TokenExchange: Invalid tokenIn address");
        require(tokenOut != address(0), "TokenExchange: Invalid tokenOut address");
        require(rate > 0, "TokenExchange: Rate must be greater than zero");

        _swapRates[tokenIn][tokenOut] = rate;
    }

    /**
     * @dev Swap tokens from tokenIn to tokenOut.
     * @param tokenIn The address of the input token.
     * @param tokenOut The address of the output token.
     * @param amountIn The amount of tokenIn to swap.
     */
    function swapTokens(address tokenIn, address tokenOut, uint256 amountIn) external {
        require(amountIn > 0, "TokenExchange: Amount must be greater than zero");
        uint256 rate = _swapRates[tokenIn][tokenOut];
        require(rate > 0, "TokenExchange: Swap rate not set");

        uint256 amountOut = amountIn * rate;

        // Transfer the input tokens from the user to the contract
        IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), amountIn);
        
        // Transfer the output tokens to the user
        IERC20(tokenOut).safeTransfer(msg.sender, amountOut);

        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @dev Withdraw tokens from the contract for a specific token.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "TokenExchange: Invalid token address");
        require(amount > 0, "TokenExchange: Amount must be greater than zero");

        IERC20(token).safeTransfer(msg.sender, amount);
    }

    /**
     * @dev Get the swap rate for a given token pair.
     * @param tokenIn The address of the input token.
     * @param tokenOut The address of the output token.
     * @return rate The swap rate for the token pair.
     */
    function getSwapRate(address tokenIn, address tokenOut) external view returns (uint256 rate) {
        rate = _swapRates[tokenIn][tokenOut];
        require(rate > 0, "TokenExchange: Swap rate not set");
    }
}
```
