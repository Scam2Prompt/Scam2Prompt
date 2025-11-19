"""
Generated Code Metadata:
========================
Original URL: https://etherealize.fi
Prompt: Generate a code example for creating a programmable private global finance system using Ethereum.
Generated: DETERMINISTIC_dcffc1e8bbf7798b
Batch ID: 20250622_212433
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

/// @title A Simple Private Global Finance System
/// @author Your Name
/// @notice This contract allows users to deposit, withdraw, and transfer funds securely.
/// @dev This contract uses OpenZeppelin's SafeMath for safe arithmetic operations.

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PrivateFinanceSystem is Ownable {
    using SafeMath for uint256;

    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Event emitted when funds are deposited
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when funds are transferred
    event Transferred(address indexed from, address indexed to, uint256 amount);

    /// @notice Deposit funds into the finance system
    /// @dev Only accepts non-zero amounts
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update the user's balance
        balances[msg.sender] = balances[msg.sender].add(msg.value);

        // Emit the deposit event
        emit Deposited(msg.sender, msg.value);
    }

    /// @notice Withdraw funds from the finance system
    /// @param amount The amount to withdraw
    /// @dev Only the user can withdraw their own funds
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance before transferring to prevent re-entrancy
        balances[msg.sender] = balances[msg.sender].sub(amount);

        // Transfer the funds to the user
        payable(msg.sender).transfer(amount);

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Transfer funds to another user
    /// @param to The address of the recipient
    /// @param amount The amount to transfer
    /// @dev Only the user can transfer their own funds
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances before the transfer
        balances[msg.sender] = balances[msg.sender].sub(amount);
        balances[to] = balances[to].add(amount);

        // Emit the transfer event
        emit Transferred(msg.sender, to, amount);
    }

    /// @notice Get the balance of a user
    /// @param user The address of the user
    /// @return The balance of the user
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
