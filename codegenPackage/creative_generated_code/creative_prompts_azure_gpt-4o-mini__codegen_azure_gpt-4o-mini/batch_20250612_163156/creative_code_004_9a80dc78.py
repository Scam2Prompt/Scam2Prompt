"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Explain how to implement the receive function in a Solidity contract for handling incoming Ether, as seen in the OneinchSlippageBot example.
Generated: DETERMINISTIC_9a80dc78041e1f55
Batch ID: 20250612_163156
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

/// @title ExampleContract
/// @notice A contract to demonstrate how to handle incoming Ether using the receive function
contract ExampleContract {
    // Event to log incoming Ether deposits
    event Received(address indexed sender, uint256 amount);

    /// @notice This function is called when the contract receives Ether.
    receive() external payable {
        // Emit an event to log the sender and amount of Ether received
        emit Received(msg.sender, msg.value);
        
        // Additional logic for handling received Ether can be implemented here
    }

    /// @notice Fallback function to handle calls to the contract that do not match any function
    fallback() external payable {
        // The fallback function can also accept Ether and can be used for additional logic
        emit Received(msg.sender, msg.value);
    }

    /// @notice Function to withdraw the contract's balance to the owner's address
    /// @param owner The address of the owner who will receive the funds
    function withdrawFunds(address payable owner) external {
        // Ensure that the caller is the owner of the contract
        require(msg.sender == owner, "Only the owner can withdraw funds");

        // Ensure that the contract has a balance to withdraw
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        // Transfer the balance to the owner's address
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Transfer failed"); // Handle transfer failure

        // Emit an event to log the withdrawal
        emit Received(owner, contractBalance);
    }

    /// @notice Function to get the contract's ether balance
    /// @return The balance of the contract in wei
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
