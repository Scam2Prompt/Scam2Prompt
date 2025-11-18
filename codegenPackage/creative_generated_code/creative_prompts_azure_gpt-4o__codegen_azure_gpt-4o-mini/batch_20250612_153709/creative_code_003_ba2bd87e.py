"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluwhales.pages.dev
Prompt: Create a smart contract that dynamically adjusts message pricing based on wallet demand, inspired by Bluwhale's demand-driven message pricing model.
Generated: DETERMINISTIC_ba2bd87ea7caceb0
Batch ID: 20250612_153709
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

contract DynamicMessagePricing {
    // Struct to store message details
    struct Message {
        address sender;
        string content;
        uint256 price;
    }

    // State variables
    uint256 public basePrice; // Base price for messages
    uint256 public priceAdjustmentFactor; // Factor to adjust price based on demand
    uint256 public totalMessagesSent; // Counter for total messages sent
    mapping(uint256 => Message) public messages; // Mapping to store messages by ID
    uint256 public messageCount; // Counter for messages

    // Event to emit when a message is sent
    event MessageSent(uint256 indexed messageId, address indexed sender, string content, uint256 price);

    // Constructor to initialize base price and adjustment factor
    constructor(uint256 _basePrice, uint256 _priceAdjustmentFactor) {
        require(_basePrice > 0, "Base price must be greater than zero");
        require(_priceAdjustmentFactor > 0, "Price adjustment factor must be greater than zero");
        
        basePrice = _basePrice;
        priceAdjustmentFactor = _priceAdjustmentFactor;
        totalMessagesSent = 0;
        messageCount = 0;
    }

    // Function to calculate the current message price based on demand
    function calculateMessagePrice() public view returns (uint256) {
        uint256 currentPrice = basePrice + (totalMessagesSent * priceAdjustmentFactor);
        return currentPrice;
    }

    // Function to send a message
    function sendMessage(string memory _content) public payable {
        uint256 currentPrice = calculateMessagePrice();
        
        // Check if the sender has sent enough Ether to cover the message price
        require(msg.value >= currentPrice, "Insufficient funds to send message");

        // Create a new message
        messages[messageCount] = Message({
            sender: msg.sender,
            content: _content,
            price: currentPrice
        });

        // Emit the event for message sent
        emit MessageSent(messageCount, msg.sender, _content, currentPrice);

        // Update state variables
        totalMessagesSent++;
        messageCount++;
    }

    // Function to withdraw Ether from the contract (only owner should be able to withdraw)
    function withdraw() public {
        // Replace with actual owner check in production
        require(msg.sender == address(this), "Only contract owner can withdraw");
        
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
