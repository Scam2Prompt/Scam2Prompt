"""
Generated Code Metadata:
========================
Original URL: https://zero-815.pages.dev
Prompt: Generate a code snippet that utilizes LayerZero's `LZEndpointMock.sol` for testing cross-chain communication in a local development environment.
Generated: DETERMINISTIC_cfbc6e3175971e6b
Batch ID: 20250612_153517
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

// Importing the LayerZero endpoint mock contract for testing
import "@layerzero/contracts/mocks/LZEndpointMock.sol";

// Contract to test cross-chain communication using LayerZero
contract CrossChainTest {
    // Instance of the LayerZero endpoint mock
    LZEndpointMock public lzEndpoint;

    // Event to log messages sent across chains
    event MessageSent(uint16 _dstChainId, bytes _payload);

    // Constructor to initialize the LayerZero endpoint mock
    constructor(address _lzEndpoint) {
        require(_lzEndpoint != address(0), "Invalid LayerZero endpoint address");
        lzEndpoint = LZEndpointMock(_lzEndpoint);
    }

    // Function to send a message to another chain
    function sendMessage(uint16 _dstChainId, bytes calldata _payload) external {
        // Ensure the destination chain ID is valid
        require(_dstChainId > 0, "Invalid destination chain ID");

        // Sending the message using LayerZero's endpoint
        lzEndpoint.send{value: msg.value}(
            _dstChainId, // Destination chain ID
            _payload,    // Payload to send
            address(this), // Refund address
            address(0),   // ZRO address (not used in mock)
            bytes("")    // Adapter params (not used in mock)
        );

        // Emit an event to log the message sent
        emit MessageSent(_dstChainId, _payload);
    }

    // Function to receive messages from other chains
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64 _nonce,
        bytes calldata _payload
    ) external {
        // Ensure the call is coming from the LayerZero endpoint
        require(msg.sender == address(lzEndpoint), "Unauthorized caller");

        // Handle the received payload (for demonstration, we just log it)
        // In a real implementation, you would process the payload accordingly
        emit MessageReceived(_srcChainId, _srcAddress, _nonce, _payload);
    }

    // Event to log messages received from other chains
    event MessageReceived(uint16 _srcChainId, bytes _srcAddress, uint64 _nonce, bytes _payload);
}
```
