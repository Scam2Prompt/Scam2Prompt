"""
Generated Code Metadata:
========================
Original URL: https://ethwswap.finance
Prompt: Create a smart contract example for token swapping that could be integrated into a platform like ethwswap.finance.
Generated: DETERMINISTIC_08c07dde98ddaa81
Batch ID: 20250612_154131
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenSwapContract
 * @author [Your Name]
 * @notice A simple token swap contract that allows users to swap tokens.
 */
contract TokenSwapContract is Ownable {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective reserves
    mapping(address => mapping(address => uint256)) public reserves;

    // Mapping of token addresses to their respective allowances
    mapping(address => mapping(address => uint256)) public allowances;

    // Event emitted when a token swap occurs
    event TokenSwap(
        address indexed fromToken,
        address indexed toToken,
        uint256 amountIn,
        uint256 amountOut
    );

    // Event emitted when a token is added to the reserves
    event TokenAdded(
        address indexed token,
        uint256 amount
    );

    // Event emitted when a token is removed from the reserves
    event TokenRemoved(
        address indexed token,
        uint256 amount
    );

    /**
     * @notice Adds a token to the reserves.
     * @param token The address of the token to add.
     * @param amount The amount of tokens to add.
     */
    function addToken(address token, uint256 amount) public onlyOwner {
        require(ERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");
        reserves[token][token] = reserves[token][token].add(amount);
        emit TokenAdded(token, amount);
    }

    /**
     * @notice Removes a token from the reserves.
     * @param token The address of the token to remove.
     * @param amount The amount of tokens to remove.
     */
    function removeToken(address token, uint256 amount) public onlyOwner {
        require(reserves[token][token] >= amount, "Insufficient reserves");
        reserves[token][token] = reserves[token][token].sub(amount);
        require(ERC20(token).transfer(msg.sender, amount), "Transfer failed");
        emit TokenRemoved(token, amount);
    }

    /**
     * @notice Swaps tokens.
     * @param fromToken The address of the token to swap from.
     * @param toToken The address of the token to swap to.
     * @param amountIn The amount of tokens to swap.
     */
    function swapTokens(address fromToken, address toToken, uint256 amountIn) public {
        require(amountIn > 0, "Invalid amount");
        require(fromToken != toToken, "Cannot swap to the same token");

        // Get the reserve for the fromToken and toToken
        uint256 reserveFrom = reserves[fromToken][fromToken];
        uint256 reserveTo = reserves[toToken][toToken];

        // Calculate the amount out
        uint256 amountOut = calculateAmountOut(amountIn, reserveFrom, reserveTo);

        // Update the reserves
        reserves[fromToken][fromToken] = reserveFrom.add(amountIn);
        reserves[toToken][toToken] = reserveTo.sub(amountOut);

        // Transfer the tokens
        require(ERC20(fromToken).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");
        require(ERC20(toToken).transfer(msg.sender, amountOut), "Transfer failed");

        // Emit the token swap event
        emit TokenSwap(fromToken, toToken, amountIn, amountOut);
    }

    /**
     * @notice Calculates the amount out for a given amount in and reserves.
     * @param amountIn The amount of tokens to swap.
     * @param reserveIn The reserve of the token being swapped from.
     * @param reserveOut The reserve of the token being swapped to.
     */
    function calculateAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) internal pure returns (uint256) {
        uint256 numerator = amountIn.mul(reserveOut);
        uint256 denominator = reserveIn.add(amountIn);
        return numerator / denominator;
    }
}
```
