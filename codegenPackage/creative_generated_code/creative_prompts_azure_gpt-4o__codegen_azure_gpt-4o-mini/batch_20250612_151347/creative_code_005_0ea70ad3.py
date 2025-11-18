"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: Create a Solidity contract that emits a custom event (`Log`) for debugging purposes, similar to the constructor and event setup in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_0ea70ad3be48c149
Batch ID: 20250612_151347
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

contract DebuggingContract {
    // Event declaration for logging purposes
    event Log(string message, address indexed sender, uint256 value);

    // State variable to store the owner's address
    address public owner;

    // Modifier to restrict functions to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract and emit a log event
    constructor() {
        owner = msg.sender; // Set the owner to the account that deploys the contract
        emit Log("Contract deployed", owner, 0);
    }

    // Function to emit a log event with custom message and value
    function logEvent(string calldata message, uint256 value) external onlyOwner {
        emit Log(message, msg.sender, value);
    }

    // Function to retrieve the owner's address
    function getOwner() external view returns (address) {
        return owner;
    }

    // Fallback function to handle Ether transfers to the contract
    receive() external payable {
        emit Log("Ether received", msg.sender, msg.value);
    }

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get the contract's balance
        require(balance > 0, "No Ether to withdraw"); // Ensure there is a balance
        payable(owner).transfer(balance); // Transfer balance to the owner
        emit Log("Funds withdrawn", owner, balance);
    }
}
```
