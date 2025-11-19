"""
Generated Code Metadata:
========================
Original URL: https://dggg-7er.pages.dev
Prompt: Develop a smart contract that utilizes Dmail's messaging protocol for secure communication between dApps and users.
Generated: DETERMINISTIC_1137a3d99dcbc8b8
Batch ID: 20250612_151947
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title DmailMessaging
 * @dev A smart contract for secure communication between dApps and users using Dmail's protocol
 */
contract DmailMessaging is Ownable {
    using ECDSA for bytes32;

    // Struct to represent a message
    struct Message {
        address sender;
        address recipient;
        string content;
        uint256 timestamp;
        bool isRead;
    }

    // Mapping from user address to their messages
    mapping(address => Message[]) private _userMessages;

    // Mapping to track nonces for replay protection
    mapping(address => uint256) private _nonces;

    // Event emitted when a new message is sent
    event MessageSent(
        address indexed sender,
        address indexed recipient,
        string content,
        uint256 timestamp
    );

    /**
     * @dev Send a message to a recipient
     * @param recipient The address of the message recipient
     * @param content The content of the message
     */
    function sendMessage(address recipient, string memory content) external {
        require(recipient != address(0), "Invalid recipient address");
        require(bytes(content).length > 0, "Message content cannot be empty");

        Message memory newMessage = Message({
            sender: msg.sender,
            recipient: recipient,
            content: content,
            timestamp: block.timestamp,
            isRead: false
        });

        _userMessages[recipient].push(newMessage);
        emit MessageSent(msg.sender, recipient, content, block.timestamp);
    }

    /**
     * @dev Send a signed message (for meta-transactions)
     * @param sender The address of the message sender
     * @param recipient The address of the message recipient
     * @param content The content of the message
     * @param nonce The nonce for replay protection
     * @param signature The signature of the message
     */
    function sendSignedMessage(
        address sender,
        address recipient,
        string memory content,
        uint256 nonce,
        bytes memory signature
    ) external {
        require(recipient != address(0), "Invalid recipient address");
        require(bytes(content).length > 0, "Message content cannot be empty");
        require(nonce == _nonces[sender], "Invalid nonce");

        bytes32 messageHash = keccak256(
            abi.encodePacked(sender, recipient, content, nonce)
        );
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        require(signer == sender, "Invalid signature");

        _nonces[sender]++;

        Message memory newMessage = Message({
            sender: sender,
            recipient: recipient,
            content: content,
            timestamp: block.timestamp,
            isRead: false
        });

        _userMessages[recipient].push(newMessage);
        emit MessageSent(sender, recipient, content, block.timestamp);
    }

    /**
     * @dev Get all messages for the calling user
     * @return An array of Message structs
     */
    function getMyMessages() external view returns (Message[] memory) {
        return _userMessages[msg.sender];
    }

    /**
     * @dev Mark a message as read
     * @param messageIndex The index of the message to mark as read
     */
    function markAsRead(uint256 messageIndex) external {
        require(messageIndex < _userMessages[msg.sender].length, "Invalid message index");
        _userMessages[msg.sender][messageIndex].isRead = true;
    }

    /**
     * @dev Get the current nonce for a sender
     * @param sender The address to get the nonce for
     * @return The current nonce
     */
    function getNonce(address sender) external view returns (uint256) {
        return _nonces[sender];
    }

    /**
     * @dev Get the number of unread messages for the calling user
     * @return The count of unread messages
     */
    function getUnreadCount() external view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < _userMessages[msg.sender].length; i++) {
            if (!_userMessages[msg.sender][i].isRead) {
                count++;
            }
        }
        return count;
    }
}
```
