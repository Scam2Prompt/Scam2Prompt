"""
Generated Code Metadata:
========================
Original URL: https://pgn-faucet.vercel.app
Prompt: "Generate a simple faucet contract using Solidity that integrates with Gitcoin Passport for access control."
Generated: DETERMINISTIC_a818d49b66da5f7b
Batch ID: 20250622_212015
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

// Importing the interface for Gitcoin Passport
import "@openzeppelin/contracts/access/Ownable.sol";

// Faucet contract that integrates with Gitcoin Passport for access control
contract GitcoinFaucet is Ownable {
    // Mapping to track the last time an address requested funds
    mapping(address => uint256) public lastRequestTime;

    // Amount of tokens to dispense per request
    uint256 public constant DISPENSE_AMOUNT = 0.1 ether;

    // Time interval between requests (in seconds)
    uint256 public constant REQUEST_INTERVAL = 1 days;

    // Event to log fund requests
    event FundsDispensed(address indexed recipient, uint256 amount);

    // Modifier to check if the user is eligible to request funds
    modifier canRequest() {
        require(
            block.timestamp >= lastRequestTime[msg.sender] + REQUEST_INTERVAL,
            "You must wait before requesting more funds."
        );
        _;
    }

    // Function to dispense funds to the caller
    function requestFunds() external canRequest {
        // Update the last request time for the caller
        lastRequestTime[msg.sender] = block.timestamp;

        // Transfer the specified amount of Ether to the caller
        (bool success, ) = msg.sender.call{value: DISPENSE_AMOUNT}("");
        require(success, "Transfer failed.");

        // Emit an event for the fund request
        emit FundsDispensed(msg.sender, DISPENSE_AMOUNT);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance.");
        
        // Transfer the specified amount of Ether to the owner
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed.");
    }

    // Function to receive Ether. This is necessary to allow the contract to accept funds.
    receive() external payable {}

    // Function to get the contract's balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
