"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://power-crypto-world.dexkit.app
Prompt: Develop a smart contract snippet for token swapping functionality, referencing the use case of Power Crypto World.
Generated: DETERMINISTIC_8389bef4a7a11eb8
Batch ID: 20250612_154506
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

// Importing required interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenSwap {
    using SafeMath for uint256;

    // Events for logging
    event TokensSwapped(address indexed sender, address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    // Mapping to store token balances of the contract
    mapping(address => mapping(address => uint256)) public tokenBalances;

    // Function to swap tokens
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 amountOut
    ) external {
        // Validate input parameters
        require(amountIn > 0, "Amount in must be greater than 0");
        require(amountOut > 0, "Amount out must be greater than 0");
        require(fromToken != toToken, "Cannot swap the same token");

        // Transfer tokens from sender to the contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn);

        // Check if the contract has enough tokens to swap
        uint256 balanceOut = IERC20(toToken).balanceOf(address(this));
        require(balanceOut >= amountOut, "Insufficient liquidity for swap");

        // Transfer the requested amount of output tokens to the sender
        IERC20(toToken).transfer(msg.sender, amountOut);

        // Emit event for token swap
        emit TokensSwapped(msg.sender, fromToken, toToken, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external {
        // Validate withdrawal amount
        require(amount > 0, "Amount must be greater than 0");
        require(tokenBalances[msg.sender][token] >= amount, "Insufficient balance to withdraw");

        // Update balance before transferring to prevent reentrancy
        tokenBalances[msg.sender][token] = tokenBalances[msg.sender][token].sub(amount);

        // Transfer tokens to the sender
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to receive tokens and update the balance mapping
    function receiveTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the sender to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Update the balance mapping
        tokenBalances[msg.sender][token] = tokenBalances[msg.sender][token].add(amount);
    }
}
```
