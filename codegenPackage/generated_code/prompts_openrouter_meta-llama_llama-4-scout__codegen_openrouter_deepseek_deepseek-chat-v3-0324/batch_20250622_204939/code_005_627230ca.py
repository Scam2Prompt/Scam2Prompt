"""
Generated Code Metadata:
========================
Original URL: https://dogswapdex.netlify.app
Prompt: "Create a basic example of how Dogswap might use smart contracts for token swaps on the Ethereum blockchain."
Generated: DETERMINISTIC_627230cac155bfe6
Batch ID: 20250622_204939
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DogSwap
 * @dev A simple token swap contract allowing users to swap ERC20 tokens
 */
contract DogSwap is Ownable, ReentrancyGuard {
    // Mapping to track supported tokens
    mapping(address => bool) public supportedTokens;

    // Event emitted when a swap occurs
    event TokensSwapped(
        address indexed user,
        address indexed fromToken,
        address indexed toToken,
        uint256 fromAmount,
        uint256 toAmount,
        uint256 timestamp
    );

    /**
     * @dev Add a token to the list of supported tokens
     * @param tokenAddress Address of the ERC20 token to support
     */
    function addSupportedToken(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        supportedTokens[tokenAddress] = true;
    }

    /**
     * @dev Remove a token from the list of supported tokens
     * @param tokenAddress Address of the ERC20 token to remove
     */
    function removeSupportedToken(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        supportedTokens[tokenAddress] = false;
    }

    /**
     * @dev Execute a token swap
     * @param fromToken Address of the token to swap from
     * @param toToken Address of the token to swap to
     * @param fromAmount Amount of fromToken to swap
     * @param toAmount Minimum amount of toToken expected in return
     */
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 toAmount
    ) external nonReentrant {
        require(fromToken != toToken, "Cannot swap same tokens");
        require(supportedTokens[fromToken], "From token not supported");
        require(supportedTokens[toToken], "To token not supported");
        require(fromAmount > 0, "Amount must be greater than 0");

        IERC20 fromERC20 = IERC20(fromToken);
        IERC20 toERC20 = IERC20(toToken);

        // Check user's balance and allowance
        require(
            fromERC20.balanceOf(msg.sender) >= fromAmount,
            "Insufficient balance"
        );
        require(
            fromERC20.allowance(msg.sender, address(this)) >= fromAmount,
            "Insufficient allowance"
        );

        // Transfer tokens from user to contract
        require(
            fromERC20.transferFrom(msg.sender, address(this), fromAmount),
            "Transfer failed"
        );

        // Check contract's balance of toToken
        uint256 contractBalance = toERC20.balanceOf(address(this));
        require(contractBalance >= toAmount, "Insufficient liquidity");

        // Transfer tokens to user
        require(toERC20.transfer(msg.sender, toAmount), "Transfer failed");

        emit TokensSwapped(
            msg.sender,
            fromToken,
            toToken,
            fromAmount,
            toAmount,
            block.timestamp
        );
    }

    /**
     * @dev Withdraw tokens from the contract (owner only)
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount)
        external
        onlyOwner
    {
        IERC20 token = IERC20(tokenAddress);
        require(
            token.balanceOf(address(this)) >= amount,
            "Insufficient contract balance"
        );
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
