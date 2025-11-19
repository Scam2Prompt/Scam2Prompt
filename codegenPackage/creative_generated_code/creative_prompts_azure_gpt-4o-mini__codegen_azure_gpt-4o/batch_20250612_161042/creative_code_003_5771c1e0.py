"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-dmailapp.pages.dev
Prompt: Describe how to use the Dmail messaging protocol in a smart contract for secure communication. Include example code.
Generated: DETERMINISTIC_5771c1e0e9723533
Batch ID: 20250612_161042
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
 * @title DmailSecureMessaging
 * @dev Implements secure messaging using the Dmail protocol
 */
contract DmailSecureMessaging {
    // Struct to store a message
    struct Message {
        address sender;      // Address of the sender
        address recipient;   // Address of the recipient
        string encryptedMessage; // Encrypted message content
        uint256 timestamp;   // Timestamp of when the message was sent
    }

    // Mapping to store messages for each recipient
    mapping(address => Message[]) private inbox;

    /**
     * @dev Event emitted when a message is sent
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param timestamp Timestamp of the message sent
     */
    event MessageSent(address indexed sender, address indexed recipient, uint256 timestamp);

    /**
     * @dev Modifier to ensure the message is not empty
     * @param _encryptedMessage The message to be checked
     */
    modifier validMessage(string memory _encryptedMessage) {
        require(bytes(_encryptedMessage).length > 0, "Message cannot be empty");
        _;
    }

    /**
     * @dev Sends an encrypted message to the recipient
     * @param _recipient Address of the recipient
     * @param _encryptedMessage Encrypted message string
     */
    function sendMessage(address _recipient, string memory _encryptedMessage)
        external
        validMessage(_encryptedMessage)
    {
        require(_recipient != address(0), "Recipient address cannot be zero");

        // Create a new message
        Message memory newMessage = Message({
            sender: msg.sender,
            recipient: _recipient,
            encryptedMessage: _encryptedMessage,
            timestamp: block.timestamp
        });

        // Add the message to the recipient's inbox
        inbox[_recipient].push(newMessage);

        // Emit the event
        emit MessageSent(msg.sender, _recipient, block.timestamp);
    }

    /**
     * @dev Retrieves all messages for the caller
     * @return An array of messages
     */
    function getInbox() external view returns (Message[] memory) {
        return inbox[msg.sender];
    }

    /**
     * @dev Retrieves the count of messages for the caller
     * @return Number of messages in the inbox
     */
    function getInboxSize() external view returns (uint256) {
        return inbox[msg.sender].length;
    }

    /**
     * @dev Deletes all messages for the caller
     */
    function clearInbox() external {
        delete inbox[msg.sender];
    }
}
```
