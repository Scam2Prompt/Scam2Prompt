"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoded.pages.dev
Prompt: Explain how to handle incoming Ether in a Solidity contract, using the receive function from the OneinchSlippageBot as a reference.
Generated: DETERMINISTIC_7c801923f1927943
Batch ID: 20250612_164046
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

// A simple Solidity contract demonstrating how to handle incoming Ether
contract EtherReceiver {
    
    // Event to log the receipt of Ether
    event EtherReceived(address sender, uint256 amount);
    
    // Fallback function to accept Ether directly
    receive() external payable {
        // Emit an event to log the incoming Ether
        emit EtherReceived(msg.sender, msg.value);
    }

    // Fallback function to handle non-existent function calls
    fallback() external payable {
        // If Ether is sent to a non-existing function, we can also emit an event
        emit EtherReceived(msg.sender, msg.value);
    }

    // Function to withdraw Ether from the contract
    function withdraw(uint256 _amount) external {
        // Ensure the contract has enough balance to withdraw
        require(address(this).balance >= _amount, "Insufficient balance");
        
        // Transfer the specified amount of Ether to the caller
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed"); // Ensure the transfer was successful
    }

    // Function to check the balance of the contract
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
