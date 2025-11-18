"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remixide.ist
Prompt: Generate a Solidity contract with a fallback function and explain how to deploy it using Remix IDE.
Generated: DETERMINISTIC_e9515486b3113aca
Batch ID: 20250612_153710
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
 * @title FallbackExample
 * @dev A basic contract demonstrating the use of a fallback function in Solidity.
 */
contract FallbackExample {
    // State variable to track received Ether
    uint256 public receivedEther;

    // Event to log fallback function calls
    event FallbackCalled(address sender, uint256 value, bytes data);

    /**
     * @dev Fallback function that is triggered when no other function matches the call.
     * It updates the receivedEther state and emits an event.
     */
    fallback() external payable {
        // Update the amount of Ether received
        receivedEther += msg.value;

        // Emit the event with details
        emit FallbackCalled(msg.sender, msg.value, msg.data);
    }

    /**
     * @dev Function to check the current balance of the contract.
     * @return The balance of the contract in wei.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * @param _amount The amount of Ether to withdraw in wei.
     */
    function withdraw(uint256 _amount) external {
        require(_amount <= address(this).balance, "Insufficient balance");
        // Transfer the amount to the caller
        payable(msg.sender).transfer(_amount);
    }

    /**
     * @dev Function to receive Ether. It is triggered when a plain transaction is sent to the contract.
     */
    receive() external payable {
        // Update the amount of Ether received
        receivedEther += msg.value;
    }
}
```
