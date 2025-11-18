"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://modifchainapp.pages.dev
Prompt: Write code to implement a swap or exchange functionality for tokens, following the guidelines provided by DApp Rectification.
Generated: DETERMINISTIC_bd03fb4306db107c
Batch ID: 20250612_152235
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
 * @dev Implements a simple token exchange functionality between two ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract TokenSwap {
    address public owner; // Owner of the contract

    event Swap(address indexed user, address token1, address token2, uint256 amount1, uint256 amount2);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Facilitates token swap between `token1` and `token2`.
     * @param token1 Address of the first token contract.
     * @param token2 Address of the second token contract.
     * @param amount1 Amount of token1 to swap.
     * @param amount2 Amount of token2 to be received in return.
     */
    function swapTokens(
        address token1,
        address token2,
        uint256 amount1,
        uint256 amount2
    ) external {
        require(token1 != address(0) && token2 != address(0), "Invalid token address");
        require(amount1 > 0 && amount2 > 0, "Token amounts must be greater than zero");

        IERC20 token1Contract = IERC20(token1);
        IERC20 token2Contract = IERC20(token2);

        // Ensure the user has approved the contract to spend token1 and has enough balance
        require(token1Contract.allowance(msg.sender, address(this)) >= amount1, "Insufficient allowance for token1");
        require(token1Contract.balanceOf(msg.sender) >= amount1, "Insufficient balance for token1");

        // Ensure the contract has enough balance of token2 to provide for the swap
        require(token2Contract.balanceOf(address(this)) >= amount2, "Insufficient contract balance of token2");

        // Transfer token1 from the user to the contract
        require(token1Contract.transferFrom(msg.sender, address(this), amount1), "Token1 transfer failed");

        // Transfer token2 from the contract to the user
        require(token2Contract.transfer(msg.sender, amount2), "Token2 transfer failed");

        emit Swap(msg.sender, token1, token2, amount1, amount2);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 tokenContract = IERC20(token);

        // Ensure the contract has enough balance
        require(tokenContract.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer tokens to the owner
        require(tokenContract.transfer(owner, amount), "Token withdrawal failed");
    }
}
```
