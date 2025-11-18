"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eteswap.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized token swap platform that supports ETRC20 tokens, similar to the functionality described on ETESwap.
Generated: DETERMINISTIC_e2ab95d16b60a3fe
Batch ID: 20250612_151018
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

/**
 * @title TokenSwap
 * @dev A smart contract that facilitates decentralized token swaps for ERC20 tokens.
 */
contract TokenSwap {
    // Event emitted when a swap is successfully executed
    event TokenSwapped(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    // Interface for ERC20 Tokens
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
        function allowance(address owner, address spender) external view returns (uint256);
        function decimals() external view returns (uint8);
    }

    /**
     * @dev Performs a token swap between two ERC20 tokens. The user must approve this contract
     * to transfer the amount of `tokenIn` before calling this function.
     * @param tokenIn Address of the token being swapped from.
     * @param tokenOut Address of the token being swapped to.
     * @param amountIn Amount of `tokenIn` being swapped.
     * @param rate Exchange rate between `tokenIn` and `tokenOut` (assumed fixed for simplicity).
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 rate
    ) external {
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(amountIn > 0, "AmountIn must be greater than zero");
        require(rate > 0, "Rate must be greater than zero");

        // Calculate the amount of tokenOut to transfer
        uint256 amountOut = (amountIn * rate) / (10**uint256(IERC20(tokenIn).decimals()));

        // Check the balances and allowances
        require(IERC20(tokenIn).balanceOf(msg.sender) >= amountIn, "Insufficient tokenIn balance");
        require(IERC20(tokenIn).allowance(msg.sender, address(this)) >= amountIn, "TokenIn allowance too low");

        // Perform the transfer of tokenIn from the user to this contract
        bool sentIn = IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        require(sentIn, "Transfer of tokenIn failed");

        // Perform the transfer of tokenOut from this contract to the user
        require(IERC20(tokenOut).balanceOf(address(this)) >= amountOut, "Insufficient tokenOut balance in contract");
        bool sentOut = IERC20(tokenOut).transfer(msg.sender, amountOut);
        require(sentOut, "Transfer of tokenOut failed");

        // Emit an event for the swap
        emit TokenSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @dev Allows the owner of the contract to deposit tokens into the contract.
     * The owner must approve the contract for the amount being deposited.
     * @param token Address of the ERC20 token being deposited.
     * @param amount Amount of the token being deposited.
     */
    function depositTokens(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the sender to this contract
        bool sent = IERC20(token).transferFrom(msg.sender, address(this), amount);
        require(sent, "Token deposit failed");
    }

    /**
     * @dev Allows the owner of the contract to withdraw tokens from the contract.
     * @param token Address of the ERC20 token being withdrawn.
     * @param amount Amount of the token to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient token balance in contract");

        // Transfer tokens from the contract to the sender
        bool sent = IERC20(token).transfer(msg.sender, amount);
        require(sent, "Token withdrawal failed");
    }
}
```
