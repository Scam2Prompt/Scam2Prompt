"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Develop a Solidity contract that listens for incoming Ether payments using the `receive()` function and logs a custom event, inspired by the Oneinch Slippage Bot implementation.
Generated: DETERMINISTIC_acb8dd54f5cba529
Batch ID: 20250612_150902
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

contract EtherReceiver {
    // Event to log incoming Ether payments
    event EtherReceived(address indexed sender, uint256 amount);

    // Fallback function that is called when the contract receives Ether
    receive() external payable {
        // Emit the EtherReceived event with the sender's address and the amount received
        emit EtherReceived(msg.sender, msg.value);
    }

    // Function to retrieve the contract's balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to withdraw Ether from the contract
    function withdraw(uint256 amount) external {
        // Ensure the requested amount is less than or equal to the contract's balance
        require(amount <= address(this).balance, "Insufficient balance");

        // Transfer the requested amount to the sender
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Function to withdraw all Ether from the contract
    function withdrawAll() external {
        uint256 balance = address(this).balance;

        // Ensure the contract has a positive balance before attempting to withdraw
        require(balance > 0, "No Ether to withdraw");

        // Transfer the entire balance to the sender
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }
}
```
