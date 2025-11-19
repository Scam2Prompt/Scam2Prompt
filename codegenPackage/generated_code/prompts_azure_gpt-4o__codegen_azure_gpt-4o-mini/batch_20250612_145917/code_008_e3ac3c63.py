"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Create a Solidity contract that utilizes the `receive()` function to handle incoming Ether payments, similar to the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_e3ac3c634a39d6b3
Batch ID: 20250612_145917
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

/// @title EtherReceiver
/// @notice This contract allows users to send Ether to it and handles incoming payments using the receive() function.
contract EtherReceiver {
    // Event to log incoming Ether payments
    event Received(address indexed sender, uint256 amount);

    /// @notice Fallback function to receive Ether. This function is called when the contract receives Ether.
    receive() external payable {
        // Emit an event to log the received Ether
        emit Received(msg.sender, msg.value);
    }

    /// @notice Function to withdraw Ether from the contract
    /// @param to The address to which the Ether will be sent
    /// @param amount The amount of Ether to withdraw
    function withdraw(address payable to, uint256 amount) external {
        // Ensure the contract has enough balance to withdraw
        require(address(this).balance >= amount, "Insufficient balance");

        // Transfer the specified amount of Ether to the provided address
        (bool success, ) = to.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit an event to log the withdrawal
        emit Withdrawn(to, amount);
    }

    // Event to log withdrawals
    event Withdrawn(address indexed to, uint256 amount);

    /// @notice Function to check the contract's balance
    /// @return The balance of the contract in wei
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
