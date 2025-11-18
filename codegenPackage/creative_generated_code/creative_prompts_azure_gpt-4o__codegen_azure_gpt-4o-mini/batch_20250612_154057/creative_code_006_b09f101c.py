"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-coinbase-com.kagiproxy.com
Prompt: Create a smart contract on Ethereum L2 (Base) using Coinbase's developer tools to facilitate onchain payments.
Generated: DETERMINISTIC_b09f101c624254c6
Batch ID: 20250612_154057
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

/// @title Onchain Payment Smart Contract
/// @author Your Name
/// @notice This contract facilitates onchain payments on Ethereum L2 (Base) using Coinbase's developer tools.
/// @dev Ensure to deploy this on the Ethereum L2 network.

contract OnchainPayment {
    // Event to emit when a payment is made
    event PaymentReceived(address indexed payer, uint256 amount);

    // Mapping to track balances of users
    mapping(address => uint256) public balances;

    /// @notice Function to make a payment
    /// @dev Requires the sender to send ether along with the function call
    function makePayment() external payable {
        // Ensure payment is greater than zero
        require(msg.value > 0, "Payment must be greater than zero");
        
        // Update the balance of the payer
        balances[msg.sender] += msg.value;

        // Emit an event to notify that a payment has been received
        emit PaymentReceived(msg.sender, msg.value);
    }

    /// @notice Function to withdraw funds from the contract
    /// @dev Only the sender can withdraw their own funds
    /// @param amount The amount to withdraw
    function withdraw(uint256 amount) external {
        // Ensure the sender has sufficient balance
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the balance before making the transfer to prevent re-entrancy attacks
        balances[msg.sender] -= amount;

        // Transfer the specified amount to the sender
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit an event to notify that a withdrawal has been made
        emit PaymentReceived(msg.sender, -int256(amount));
    }

    /// @notice Function to check the balance of a user
    /// @param user The address of the user to check
    /// @return The balance of the specified user
    function checkBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
