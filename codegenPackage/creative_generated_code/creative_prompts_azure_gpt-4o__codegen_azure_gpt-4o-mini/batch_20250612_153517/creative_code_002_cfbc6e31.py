"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zero-815.pages.dev
Prompt: Generate a code snippet that utilizes LayerZero's `LZEndpointMock.sol` for testing cross-chain communication in a local development environment.
Generated: DETERMINISTIC_cfbc6e3175971e6b
Batch ID: 20250612_153517
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

import "@layerzerolabs/lz-contracts/contracts/mocks/LZEndpointMock.sol";

contract CrossChainMessenger {
    // Address of the LayerZero endpoint
    LZEndpointMock public endpoint;

    // Event emitted when a message is sent
    event MessageSent(address indexed sender, string message, uint16 indexed destinationChainId);

    // Event emitted when a message is received
    event MessageReceived(address indexed receiver, string message, uint16 indexed sourceChainId);

    // Constructor to set the LayerZero endpoint
    constructor(address _endpoint) {
        require(_endpoint != address(0), "Invalid endpoint address");
        endpoint = LZEndpointMock(_endpoint);
    }

    // Function to send a message to a destination chain
    function sendMessage(uint16 _destinationChainId, string calldata _message) external {
        // Ensure that the message is not empty
        require(bytes(_message).length > 0, "Message cannot be empty");

        // Prepare the payload
        bytes memory payload = abi.encode(_message);

        // Send the message via LayerZero
        endpoint.send{value: msg.value}(
            _destinationChainId,
            address(this), // The address of the contract
            payload,
            payable(msg.sender), // Refund address
            address(0), // No custom payload
            "" // No extra parameters
        );

        // Emit the event for the sent message
        emit MessageSent(msg.sender, _message, _destinationChainId);
    }

    // Function to receive messages (for testing purposes)
    function lzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64, // nonce (not used here)
        bytes memory _payload
    ) external {
        // Decode the payload to get the message
        string memory message = abi.decode(_payload, (string));

        // Emit the event for the received message
        emit MessageReceived(msg.sender, message, _srcChainId);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
