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

// Import LayerZero's LZEndpointMock contract
import "@layerzerolabs/lz-endpoint/contracts/testing/LZEndpointMock.sol";

contract CrossChainCommunicator {
    // State variable to hold the LayerZero endpoint instance
    LZEndpointMock public lzEndpoint;

    // Event emitted when a message is received
    event MessageReceived(uint16 srcChainId, bytes srcAddress, bytes payload);

    // Constructor to initialize the LayerZero endpoint for testing
    constructor(address _endpointMockAddress) {
        require(_endpointMockAddress != address(0), "Invalid endpoint address");
        lzEndpoint = LZEndpointMock(_endpointMockAddress);
    }

    /**
     * @dev Sends a message to another chain using the LayerZero endpoint
     * @param dstChainId The chain ID of the destination chain
     * @param dstAddress The address of the recipient contract on the destination chain
     * @param payload The message payload to send
     */
    function sendMessage(
        uint16 dstChainId,
        bytes memory dstAddress,
        bytes memory payload
    ) external payable {
        // Perform basic input validation
        require(dstChainId > 0, "Destination chain ID must be greater than 0");
        require(dstAddress.length > 0, "Destination address cannot be empty");
        require(payload.length > 0, "Payload cannot be empty");

        // Simulate sending the message via the LayerZero endpoint
        lzEndpoint.send{value: msg.value}(
            dstChainId,      // Destination chain ID
            dstAddress,      // Destination address
            payload,         // Payload to send
            payable(msg.sender), // Refund address
            address(0),      // Zero address for zro payment
            bytes("")        // Empty adapter parameters
        );
    }

    /**
     * @dev This function simulates receiving a cross-chain message
     * @param srcChainId The chain ID of the source chain
     * @param srcAddress The address of the sender contract on the source chain
     * @param payload The message payload received
     */
    function lzReceive(
        uint16 srcChainId,
        bytes memory srcAddress,
        uint64, // Nonce (not used in this example)
        bytes memory payload
    ) external {
        // Ensure the call is coming from the LayerZero endpoint mock
        require(msg.sender == address(lzEndpoint), "Caller is not the LayerZero endpoint");

        // Emit an event for the received message
        emit MessageReceived(srcChainId, srcAddress, payload);

        // Handle the payload (for demonstration purposes, this code does nothing)
        // Add your custom logic here to handle the received message
    }

    /**
     * @dev Allows the contract to receive Ether
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle unexpected calls
     */
    fallback() external payable {}
}
```
