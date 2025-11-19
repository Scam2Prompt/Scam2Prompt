"""
Generated Code Metadata:
========================
Original URL: https://bluwhales.pages.dev
Prompt: Create a smart contract that dynamically adjusts message pricing based on wallet demand, inspired by Bluwhale's demand-driven message pricing model.
Generated: DETERMINISTIC_ba2bd87ea7caceb0
Batch ID: 20250612_153709
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

contract DynamicMessagePricing {
    // State variables
    address public owner;
    uint256 public basePrice; // Base price for sending a message
    uint256 public demandFactor; // Factor to adjust price based on demand
    mapping(address => uint256) public walletDemand; // Tracks demand per wallet
    mapping(address => uint256) public messageCount; // Tracks messages sent by each wallet

    // Events
    event MessageSent(address indexed sender, string message, uint256 price);
    event PriceAdjusted(uint256 newPrice);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _basePrice, uint256 _demandFactor) {
        owner = msg.sender;
        basePrice = _basePrice;
        demandFactor = _demandFactor;
    }

    // Function to send a message with dynamic pricing
    function sendMessage(string calldata message) external payable {
        uint256 currentPrice = calculatePrice(msg.sender);
        require(msg.value >= currentPrice, "Insufficient funds to send message");

        // Update demand for the sender's wallet
        walletDemand[msg.sender]++;
        messageCount[msg.sender]++;

        // Emit event for message sent
        emit MessageSent(msg.sender, message, currentPrice);
    }

    // Function to calculate the current price based on demand
    function calculatePrice(address sender) public view returns (uint256) {
        uint256 demand = walletDemand[sender];
        return basePrice + (demand * demandFactor);
    }

    // Function to adjust the base price (only owner can call)
    function adjustBasePrice(uint256 newBasePrice) external onlyOwner {
        basePrice = newBasePrice;
        emit PriceAdjusted(newBasePrice);
    }

    // Function to withdraw contract balance (only owner can call)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
