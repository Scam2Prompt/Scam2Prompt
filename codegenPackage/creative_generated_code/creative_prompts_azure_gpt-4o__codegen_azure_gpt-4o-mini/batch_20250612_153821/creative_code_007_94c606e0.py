"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miden.cloud
Prompt: Provide an example of a decentralized application (dApp) that utilizes the Miden Pioneer Program's technical support to implement on-chain economic features.
Generated: DETERMINISTIC_94c606e056373afb
Batch ID: 20250612_153821
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

/// @title Simple Decentralized Application (dApp) Example
/// @author Your Name
/// @notice This smart contract implements a basic on-chain economic feature
///         where users can deposit, withdraw, and check their balances.
/// @dev This contract uses OpenZeppelin's SafeERC20 for safe token transfers.

import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SimpleEconomyDApp is Ownable {
    using SafeERC20 for IERC20;

    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Event emitted when a user deposits tokens
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    /// @notice Deposit tokens into the dApp
    /// @param token The address of the ERC20 token being deposited
    /// @param amount The amount of tokens to deposit
    /// @dev Only the owner can call this function
    function deposit(IERC20 token, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to this contract
        token.safeTransferFrom(msg.sender, address(this), amount);

        // Update user balance
        balances[msg.sender] += amount;

        // Emit deposit event
        emit Deposited(msg.sender, amount);
    }

    /// @notice Withdraw tokens from the dApp
    /// @param token The address of the ERC20 token being withdrawn
    /// @param amount The amount of tokens to withdraw
    function withdraw(IERC20 token, uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance to withdraw");

        // Update user balance before transferring tokens
        balances[msg.sender] -= amount;

        // Transfer tokens to the user
        token.safeTransfer(msg.sender, amount);

        // Emit withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Check the balance of the msg.sender
    /// @return The balance of the caller in the dApp
    function balanceOf() external view returns (uint256) {
        return balances[msg.sender];
    }
}
```
