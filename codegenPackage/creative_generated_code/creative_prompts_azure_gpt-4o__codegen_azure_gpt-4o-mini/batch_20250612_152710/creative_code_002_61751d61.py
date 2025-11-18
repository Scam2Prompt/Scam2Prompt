"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimanyinu.pages.dev
Prompt: Provide a step-by-step guide to set up a permissionless bridge for wrapping $AI tokens on an Axelar ITS-supported chain.
Generated: DETERMINISTIC_61751d61305f0d83
Batch ID: 20250612_152710
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

/// @title Permissionless Bridge for Wrapping $AI Tokens
/// @notice This contract allows users to wrap $AI tokens on an Axelar ITS-supported chain.
contract AITokenBridge {
    // Events
    event TokensWrapped(address indexed user, uint256 amount);
    event TokensUnwrapped(address indexed user, uint256 amount);

    // Token interface
    IERC20 public aiToken;

    // Mapping to track wrapped token balances
    mapping(address => uint256) public wrappedBalances;

    // Modifier to check for sufficient balance
    modifier hasSufficientBalance(uint256 amount) {
        require(aiToken.balanceOf(msg.sender) >= amount, "Insufficient $AI token balance");
        _;
    }

    // Constructor to set the AI token address
    constructor(address _aiTokenAddress) {
        aiToken = IERC20(_aiTokenAddress);
    }

    /// @notice Wraps $AI tokens and updates the user's wrapped balance
    /// @param amount The amount of $AI tokens to wrap
    function wrapTokens(uint256 amount) external hasSufficientBalance(amount) {
        // Transfer $AI tokens from the user to the contract
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update wrapped balances
        wrappedBalances[msg.sender] += amount;

        // Emit event
        emit TokensWrapped(msg.sender, amount);
    }

    /// @notice Unwraps $AI tokens and transfers them back to the user
    /// @param amount The amount of wrapped tokens to unwrap
    function unwrapTokens(uint256 amount) external {
        require(wrappedBalances[msg.sender] >= amount, "Insufficient wrapped balance");

        // Update wrapped balances
        wrappedBalances[msg.sender] -= amount;

        // Transfer $AI tokens back to the user
        require(aiToken.transfer(msg.sender, amount), "Transfer failed");

        // Emit event
        emit TokensUnwrapped(msg.sender, amount);
    }

    /// @notice Retrieve the amount of wrapped tokens for a specific user
    /// @param user The address of the user
    /// @return The amount of wrapped tokens
    function getWrappedBalance(address user) external view returns (uint256) {
        return wrappedBalances[user];
    }
}

/// @title ERC20 Token Interface
/// @notice Minimal interface for ERC20 token interaction
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}
```
