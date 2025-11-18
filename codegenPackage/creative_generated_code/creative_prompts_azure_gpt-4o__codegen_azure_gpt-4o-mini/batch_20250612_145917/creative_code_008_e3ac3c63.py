"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoded.pages.dev
Prompt: Create a Solidity contract that utilizes the `receive()` function to handle incoming Ether payments, similar to the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_e3ac3c634a39d6b3
Batch ID: 20250612_145917
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

import "@openzeppelin/contracts/access/Ownable.sol";

/// @title EtherReceiver
/// @notice This contract allows for receiving Ether and keeps track of the balance
contract EtherReceiver is Ownable {
    // Event to log received Ether
    event Received(address indexed sender, uint256 amount);

    // Fallback function to receive Ether. This function is called when 
    // the contract receives Ether without any data.
    receive() external payable {
        emit Received(msg.sender, msg.value);
    }

    // Function to withdraw Ether from the contract
    /// @notice Withdraws the contract's balance to the owner's address.
    /// @dev Only the owner can call this function.
    function withdraw() external onlyOwner {
        // Ensure there's a balance to withdraw
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");

        // Emit an event for transparency
        emit Withdrawn(msg.sender, balance);
    }

    // Event to log the withdrawal of Ether
    event Withdrawn(address indexed owner, uint256 amount);

    // Function to check the contract's balance
    /// @return The balance of the contract in wei
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
