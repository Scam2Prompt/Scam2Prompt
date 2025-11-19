"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectautofixing.vercel.app
Prompt: Provide an example of a smart contract that facilitates the swapping and exchanging of cryptocurrencies on a decentralized platform.
Generated: DETERMINISTIC_4c161f0fe2de574e
Batch ID: 20250612_155632
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

// Importing necessary interfaces for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title DecentralizedExchange
/// @notice This contract allows users to swap and exchange ERC20 tokens
contract DecentralizedExchange is Ownable {
    // Event emitted when a swap occurs
    event TokensSwapped(address indexed user, address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    // Function to swap tokens
    /// @notice Swaps `amountIn` of `fromToken` for `amountOut` of `toToken`
    /// @param fromToken The address of the ERC20 token to swap from
    /// @param toToken The address of the ERC20 token to swap to
    /// @param amountIn The amount of `fromToken` to swap
    /// @param amountOut The amount of `toToken` to receive
    function swapTokens(address fromToken, address toToken, uint256 amountIn, uint256 amountOut) external {
        // Ensure the user has approved the exchange to spend their tokens
        require(IERC20(fromToken).allowance(msg.sender, address(this)) >= amountIn, "Insufficient allowance for fromToken");

        // Transfer `amountIn` of `fromToken` from user to the contract
        require(IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn), "Transfer of fromToken failed");

        // Transfer `amountOut` of `toToken` from the contract to user
        require(IERC20(toToken).balanceOf(address(this)) >= amountOut, "Insufficient balance of toToken in the exchange");
        require(IERC20(toToken).transfer(msg.sender, amountOut), "Transfer of toToken failed");

        // Emit the swap event
        emit TokensSwapped(msg.sender, fromToken, toToken, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (for owner)
    /// @notice Allows the owner to withdraw any ERC20 token from the contract
    /// @param token The address of the ERC20 token to withdraw
    /// @param amount The amount of tokens to withdraw
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
    }
}
```
