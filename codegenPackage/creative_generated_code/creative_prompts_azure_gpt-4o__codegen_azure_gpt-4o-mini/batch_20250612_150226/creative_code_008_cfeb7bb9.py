"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Write a Solidity contract that uses LayerZero's `OApp` to implement a generic message-passing interface for decentralized applications.
Generated: DETERMINISTIC_cfeb7bb980dee3e0
Batch ID: 20250612_150226
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

// Import the interface for LayerZero's OApp
import "@layerzero/og/ILayerZeroOApp.sol";

// Interface for the message passing functionality
interface IMessageReceiver {
    function onReceiveMessage(uint16 srcChainId, bytes calldata message) external;
}

// Generic message-passing contract utilizing LayerZero's OApp
contract GenericMessagePasser is ILayerZeroOApp {
    // Declare the owner of the contract
    address public owner;

    // Event emitted when a message is sent
    event MessageSent(uint16 indexed dstChainId, bytes message);

    // Modifiers to restrict access to owner only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to send a message across chains
    function sendMessage(uint16 _dstChainId, bytes calldata _message) external onlyOwner {
        // Emit event for message sent
        emit MessageSent(_dstChainId, _message);

        // Call LayerZero's send function to transmit the message
        _sendMessage(_dstChainId, _message);
    }

    // Internal function to handle message sending logic
    function _sendMessage(uint16 _dstChainId, bytes memory _message) internal {
        // LayerZero send function would be called here
        // Placeholder for LayerZero's sending logic
        // require(ILayerZeroOApp(msg.sender).send(_dstChainId, _message), "Send failed");
    }

    // Function to handle incoming messages from LayerZero
    function onReceiveMessage(uint16 _srcChainId, bytes calldata _message) external override {
        // Ensure that the call comes from the LayerZero contract
        require(msg.sender == address(this), "Unauthorized sender");

        // Process the received message
        _processReceivedMessage(_srcChainId, _message);
    }

    // Internal function to process incoming messages
    function _processReceivedMessage(uint16 _srcChainId, bytes memory _message) internal {
        // Implement your logic for handling the received message here
        // e.g., parsing the message, triggering functions, etc.
    }

    // Function to withdraw mistakenly sent Ether to the contract
    function withdrawEther(address payable _to) external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        _to.transfer(balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
