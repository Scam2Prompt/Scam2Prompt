"""
Generated Code Metadata:
========================
Original URL: https://explorer-dapp.pages.dev
Prompt: Generate a smart contract template for a decentralized application that ensures censorship resistance and immutability, aligning with the principles outlined by Dapp Protocol.
Generated: DETERMINISTIC_1c4031f6d1b9da5e
Batch ID: 20250612_145459
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

/// @title Censorship Resistant Smart Contract
/// @author Your Name
/// @notice This contract serves as a template for a decentralized application (DApp) ensuring censorship resistance and immutability.
/// @dev This contract uses OpenZeppelin's Ownable for access control and SafeMath for safe arithmetic operations.

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CensorshipResistantDApp is Ownable {
    using SafeMath for uint256;

    // Event emitted when a new message is posted
    event MessagePosted(address indexed sender, string message, uint256 timestamp);

    // Struct to represent a message
    struct Message {
        address sender;
        string content;
        uint256 timestamp;
    }

    // Array to store messages
    Message[] private messages;

    /// @notice Posts a new message to the contract
    /// @param _message The content of the message to be posted
    /// @dev This function is public and can be called by anyone
    function postMessage(string calldata _message) external {
        require(bytes(_message).length > 0, "Message cannot be empty");

        // Create a new message and store it in the array
        messages.push(Message({
            sender: msg.sender,
            content: _message,
            timestamp: block.timestamp
        }));

        // Emit an event for the new message
        emit MessagePosted(msg.sender, _message, block.timestamp);
    }

    /// @notice Retrieves a message by its index
    /// @param index The index of the message to retrieve
    /// @return sender The address of the message sender
    /// @return content The content of the message
    /// @return timestamp The timestamp when the message was posted
    /// @dev Reverts if the index is out of bounds
    function getMessage(uint256 index) external view returns (address sender, string memory content, uint256 timestamp) {
        require(index < messages.length, "Index out of bounds");

        Message memory message = messages[index];
        return (message.sender, message.content, message.timestamp);
    }

    /// @notice Retrieves the total number of messages posted
    /// @return The total count of messages
    function getMessageCount() external view returns (uint256) {
        return messages.length;
    }

    /// @notice Allows the owner to withdraw any Ether sent to the contract
    /// @dev This function is restricted to the contract owner
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /// @notice Fallback function to accept Ether
    receive() external payable {}
}
```
