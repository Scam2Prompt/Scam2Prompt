"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caldera-giftxyz.pages.dev
Prompt: Generate a smart contract that collects and displays user messages and activity logs, similar to the functionality described on the Caldera Rollups webpage.
Generated: DETERMINISTIC_6cfa6029c8e5060e
Batch ID: 20250612_152658
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

// A smart contract to collect and display user messages and activity logs
contract UserActivityLogger {
    // Struct to store user message and timestamp
    struct Message {
        address sender;
        string content;
        uint256 timestamp;
    }

    // Array to hold all messages
    Message[] private messages;

    // Event emitted when a new message is logged
    event MessageLogged(address indexed sender, string content, uint256 timestamp);

    // Function to log a new message
    function logMessage(string calldata _content) external {
        // Ensure the message is not empty
        require(bytes(_content).length > 0, "Message cannot be empty");

        // Create a new message instance
        Message memory newMessage = Message({
            sender: msg.sender,
            content: _content,
            timestamp: block.timestamp
        });

        // Store the message in the array
        messages.push(newMessage);

        // Emit the message logged event
        emit MessageLogged(msg.sender, _content, block.timestamp);
    }

    // Function to retrieve all messages
    function getMessages() external view returns (Message[] memory) {
        return messages;
    }

    // Function to retrieve a specific message by index
    function getMessage(uint256 index) external view returns (Message memory) {
        // Ensure the index is valid
        require(index < messages.length, "Index out of bounds");
        return messages[index];
    }

    // Function to get the total number of messages
    function getMessageCount() external view returns (uint256) {
        return messages.length;
    }
}
```
