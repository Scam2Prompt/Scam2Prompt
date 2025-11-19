"""
Generated Code Metadata:
========================
Original URL: https://stake-saakuru.pages.dev
Prompt: Write a smart contract on an EVM-compatible blockchain using the Saakuru Developer Suite to create a gas-less decentralized application with real-time interactions.
Generated: DETERMINISTIC_d359af60cd40d5c4
Batch ID: 20250612_145933
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

import "@saakuru/core/contracts/SaakuruApp.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title GaslessDApp
 * @dev A gas-less decentralized application with real-time interactions
 */
contract GaslessDApp is SaakuruApp, Pausable {
    // Event emitted when a new message is posted
    event MessagePosted(address indexed sender, string message, uint256 timestamp);

    // Struct to store message data
    struct Message {
        address sender;
        string content;
        uint256 timestamp;
    }

    // Array to store all messages
    Message[] public messages;

    // Mapping to store user message counts
    mapping(address => uint256) public userMessageCounts;

    /**
     * @dev Initialize the contract with SaakuruApp parameters
     * @param _trustedForwarder The address of the trusted forwarder for meta-transactions
     */
    constructor(address _trustedForwarder) SaakuruApp(_trustedForwarder) {
        // Initialization logic if needed
    }

    /**
     * @dev Post a new message (gas-less via meta-transaction)
     * @param _message The content of the message to post
     */
    function postMessage(string memory _message) external whenNotPaused {
        require(bytes(_message).length > 0, "Message cannot be empty");
        require(bytes(_message).length <= 280, "Message too long");

        messages.push(Message({
            sender: _msgSender(),
            content: _message,
            timestamp: block.timestamp
        }));

        userMessageCounts[_msgSender()]++;

        emit MessagePosted(_msgSender(), _message, block.timestamp);
    }

    /**
     * @dev Get total message count
     * @return The total number of messages posted
     */
    function getTotalMessageCount() external view returns (uint256) {
        return messages.length;
    }

    /**
     * @dev Get messages in paginated form
     * @param _offset Starting index
     * @param _limit Number of messages to return
     * @return Array of Message structs
     */
    function getMessages(uint256 _offset, uint256 _limit) external view returns (Message[] memory) {
        require(_limit > 0 && _limit <= 100, "Limit must be between 1 and 100");

        uint256 end = _offset + _limit;
        if (end > messages.length) {
            end = messages.length;
        }

        Message[] memory result = new Message[](end - _offset);
        for (uint256 i = _offset; i < end; i++) {
            result[i - _offset] = messages[i];
        }

        return result;
    }

    /**
     * @dev Pause the contract (admin only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract (admin only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override _msgSender to support meta-transactions
     */
    function _msgSender() internal view override(Context, SaakuruApp) returns (address) {
        return super._msgSender();
    }

    /**
     * @dev Override _msgData to support meta-transactions
     */
    function _msgData() internal view override(Context, SaakuruApp) returns (bytes calldata) {
        return super._msgData();
    }
}
```
