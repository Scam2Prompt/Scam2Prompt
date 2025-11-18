"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdnsource.pages.dev
Prompt: Create a Solidity contract that uses the `receive()` function to handle incoming Ether transactions, similar to the Oneinch Slippage Bot.
Generated: DETERMINISTIC_b569691129c86bad
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

/**
 * @title SlippageBotContract
 * @dev A simple contract to accept Ether transfers using the receive() function.
 */
contract SlippageBotContract {
    // Event to log Ether received
    event EtherReceived(address indexed sender, uint256 amount);

    // Variable to store the total Ether balance received by the contract
    uint256 public totalReceived;

    /**
     * @dev Fallback function to handle calls that do not match a function signature.
     * It reverts to prevent accidental loss of funds.
     */
    fallback() external payable {
        revert("Fallback function called. Use standard Ether transfer.");
    }

    /**
     * @dev Receive function to handle incoming Ether transactions.
     * Emits an event and updates the total received amount.
     */
    receive() external payable {
        // Ensure the transaction has Ether attached
        require(msg.value > 0, "No Ether sent.");
        
        // Update the total received amount
        totalReceived += msg.value;
        
        // Emit an event to log the received Ether
        emit EtherReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw the contract's Ether balance to an external address.
     * Only callable by the owner of the contract.
     * @param to The address to send the Ether to.
     */
    function withdraw(address payable to) external {
        // Ensure the destination address is valid
        require(to != address(0), "Invalid address.");
        
        // Ensure there is sufficient balance to withdraw
        require(address(this).balance > 0, "Insufficient balance.");

        // Get the current balance of the contract
        uint256 contractBalance = address(this).balance;

        // Reset the total received amount (optional for better tracking)
        totalReceived = 0;

        // Transfer the balance
        to.transfer(contractBalance);
    }

    /**
     * @dev Function to get the balance of the contract.
     * @return The Ether balance of the contract.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
