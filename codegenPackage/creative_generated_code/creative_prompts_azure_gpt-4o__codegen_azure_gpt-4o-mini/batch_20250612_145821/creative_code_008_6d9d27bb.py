"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codecopyed.pages.dev
Prompt: Develop a Solidity contract that includes a `receive()` function to handle incoming Ether payments, as demonstrated in the "1inch Slippage Bot" contract.
Generated: DETERMINISTIC_6d9d27bbe6397d20
Batch ID: 20250612_145821
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

/// @title A Simple Ether Receiver Contract
/// @notice This contract implements a receive function to handle incoming Ether payments
contract EtherReceiver {

    // Event to emit when Ether is received
    event EtherReceived(address indexed sender, uint256 amount);

    /// @notice This function is called when the contract receives Ether.
    /// @dev It logs the address of the sender and the amount of Ether received.
    receive() external payable {
        require(msg.value > 0, "No Ether sent");

        // Emit an event to log the transaction
        emit EtherReceived(msg.sender, msg.value);
    }

    /// @notice Allows the owner to withdraw the Ether balance from the contract.
    /// @dev Only the owner should be able to withdraw funds.
    function withdraw() external {
        // Using 'address(this).balance' to get current balance of the contract
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the caller (assuming the caller is the owner)
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }
    
    /// @notice Returns the current Ether balance of the contract.
    /// @return The balance of Ether held by the contract.
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
