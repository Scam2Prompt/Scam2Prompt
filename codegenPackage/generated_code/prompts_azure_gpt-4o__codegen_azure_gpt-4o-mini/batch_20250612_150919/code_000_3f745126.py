"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: Write a Solidity smart contract that is compatible with Mazze's EVM-based blockchain and utilizes its high throughput (40,000 TPS) for processing micropayments.
Generated: DETERMINISTIC_3f7451266ee5ffb2
Batch ID: 20250612_150919
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

/// @title Micropayment Contract
/// @notice This contract allows users to make micropayments efficiently on Mazze's EVM-based blockchain
/// @dev The contract is designed to handle high throughput transactions
contract Micropayment {
    // Event emitted when a payment is made
    event PaymentMade(address indexed payer, address indexed payee, uint256 amount, string message);

    // Mapping to track balances of users
    mapping(address => uint256) private balances;

    /// @notice Allows a user to deposit funds into the contract
    /// @dev This function is payable and allows users to send Ether to the contract
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
    }

    /// @notice Allows a user to make a micropayment to another user
    /// @param payee The address of the recipient
    /// @param amount The amount to be sent (in wei)
    /// @param message An optional message to include with the payment
    /// @dev The function checks if the sender has enough balance and transfers the amount
    function makePayment(address payable payee, uint256 amount, string calldata message) external {
        require(amount > 0, "Payment amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances before transferring to prevent reentrancy attacks
        balances[msg.sender] -= amount;
        balances[payee] += amount;

        // Transfer the amount to the payee
        (bool success, ) = payee.call{value: amount}("");
        require(success, "Payment transfer failed");

        emit PaymentMade(msg.sender, payee, amount, message);
    }

    /// @notice Allows a user to withdraw their balance from the contract
    /// @dev Users can withdraw their entire balance at once
    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No balance to withdraw");

        // Reset the user's balance before transferring to prevent reentrancy attacks
        balances[msg.sender] = 0;

        // Transfer the amount to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal transfer failed");
    }

    /// @notice Returns the balance of a user
    /// @param user The address of the user
    /// @return The balance of the user in wei
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
