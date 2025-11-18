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
pragma solidity ^0.8.19;

/**
 * @title MessageBoard
 * @dev A smart contract to collect and display user messages with activity logs.
 * Users can post messages, and all interactions are recorded.
 */
contract MessageBoard {
    // Struct to represent a user message
    struct Message {
        address sender; // Address of the user who sent the message
        string text;    // The message content
        uint256 timestamp; // Timestamp when the message was posted
    }

    // Array to store all messages
    Message[] public messages;

    // Event triggered when a new message is posted
    event MessagePosted(address indexed sender, string text, uint256 timestamp);

    // Mapping to track user activity logs (number of messages posted by each user)
    mapping(address => uint256) public userActivity;

    /**
     * @dev Post a new message to the message board.
     * Emits a MessagePosted event upon success.
     * @param _text The message content.
     */
    function postMessage(string calldata _text) external {
        require(bytes(_text).length > 0, "Message cannot be empty."); // Ensure message isn't empty

        // Create a new message and add it to the messages array
        Message memory newMessage = Message({
            sender: msg.sender,
            text: _text,
            timestamp: block.timestamp
        });
        messages.push(newMessage);

        // Update the sender's activity log
        userActivity[msg.sender]++;

        // Emit the event
        emit MessagePosted(msg.sender, _text, block.timestamp);
    }

    /**
     * @dev Get the total number of messages posted on the board.
     * @return The total message count.
     */
    function getTotalMessages() external view returns (uint256) {
        return messages.length;
    }

    /**
     * @dev Get all messages posted on the board.
     * Note: Returns the entire messages array, which might be expensive for large datasets.
     * @return An array of all messages.
     */
    function getAllMessages() external view returns (Message[] memory) {
        return messages;
    }

    /**
     * @dev Get the activity log for a specific user.
     * @param _user The address of the user.
     * @return The number of messages posted by the user.
     */
    function getUserActivity(address _user) external view returns (uint256) {
        return userActivity[_user];
    }
}
```
