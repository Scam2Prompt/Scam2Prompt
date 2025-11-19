"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://op-enocean.github.io
Prompt: How can Open Ocean be applied to create a fallback handler in Ethereum smart contracts to prevent exploitation?
Generated: DETERMINISTIC_3f146ba5e82d1ea6
Batch ID: 20250612_155554
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
 * @title OpenOceanFallbackHandler
 * @dev This contract demonstrates a secure fallback handler using best practices to prevent exploitation.
 * It includes mechanisms to ensure that fallback calls are restricted and properly logged.
 */
contract OpenOceanFallbackHandler {
    address public owner;

    event FallbackCalled(address sender, uint256 value, bytes data);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to set the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Fallback function to handle incoming Ether and data.
     * Emits an event for logging and ensures security against malicious calls.
     */
    fallback() external payable {
        // Emit an event to log the fallback call details
        emit FallbackCalled(msg.sender, msg.value, msg.data);

        // Security mechanism: Optional custom logic for handling fallback calls
        // Example: Reject calls with unexpected data or large amounts of Ether
        require(msg.value <= 1 ether, "Excessive Ether sent");
    }

    /**
     * @dev Receive function to handle plain Ether transfers.
     */
    receive() external payable {
        // Emit an event for logging plain Ether transfers
        emit FallbackCalled(msg.sender, msg.value, "");
    }

    /**
     * @dev Function to withdraw funds from the contract. Restricted to the owner.
     */
    function withdraw() external onlyOwner {
        // Transfer all Ether in the contract to the owner
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to update the owner of the contract. Restricted to the current owner.
     */
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }
}
```
