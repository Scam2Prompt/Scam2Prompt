"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scottytheai-io.pages.dev
Prompt: Develop a Solidity contract to facilitate token swaps on Scotty Swap, ensuring secure and optimized transactions for $SCOTTY tokens.
Generated: DETERMINISTIC_4ad2c1f7aea43716
Batch ID: 20250612_152620
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for secure token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ScottySwap
 * @dev A smart contract for facilitating swaps between $SCOTTY tokens and other ERC20 tokens.
 */
contract ScottySwap is Ownable {
    // Event emitted when a swap occurs
    event TokensSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping to keep track of token reserves for swaps
    mapping(address => uint256) public reserves;

    // Sets the reserves for a specific token
    function setReserve(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        reserves[token] = amount;
    }

    /**
     * @dev Swaps an amount of an input token for an output token.
     * @param tokenIn The address of the token being swapped in.
     * @param tokenOut The address of the token being swapped out.
     * @param amountIn The amount of tokenIn to swap.
     */
    function swapTokens(address tokenIn, address tokenOut, uint256 amountIn) external {
        require(amountIn > 0, "Amount must be greater than zero");
        require(reserves[tokenIn] >= amountIn, "Insufficient reserves for tokenIn");

        // Calculate output amount (simple 1:1 swap for demonstration purposes)
        uint256 amountOut = amountIn; // This should be replaced with a proper price calculation

        // Transfer tokenIn from user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Transfer tokenOut from this contract to user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Update reserves
        reserves[tokenIn] -= amountIn;
        reserves[tokenOut] += amountOut;

        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @dev Allows the contract owner to withdraw tokens from the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount <= IERC20(token).balanceOf(address(this)), "Insufficient balance");

        IERC20(token).transfer(msg.sender, amount);
    }

    /**
     * @dev Allows users to check the balance of a specific token held by the contract.
     * @param token The address of the token to check.
     * @return The balance of the specified token.
     */
    function getTokenBalance(address token) external view returns (uint256) {
        return IERC20(token).balanceOf(address(this));
    }
}
```
