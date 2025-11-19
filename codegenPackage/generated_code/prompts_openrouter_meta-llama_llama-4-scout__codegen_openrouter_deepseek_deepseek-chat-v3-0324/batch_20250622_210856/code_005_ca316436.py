"""
Generated Code Metadata:
========================
Original URL: https://zero-815.pages.dev
Prompt: Compare and contrast the use of LayerZero's PingPong.sol and LZEndpointMock.sol in a cross-chain application.
Generated: DETERMINISTIC_ca31643677fdac04
Batch ID: 20250622_210856
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

import "@layerzerolabs/solidity-examples/contracts/lzApp/mocks/LZEndpointMock.sol";
import "@layerzerolabs/solidity-examples/contracts/examples/PingPong.sol";

/**
 * @title CrossChainDemo
 * @dev Demonstrates the interaction between PingPong.sol and LZEndpointMock.sol
 */
contract CrossChainDemo {
    // Instance of PingPong contract
    PingPong public pingPong;

    // Instance of LZEndpointMock contract
    LZEndpointMock public lzEndpointMock;

    /**
     * @dev Constructor initializes both contracts
     * @param _lzEndpointId The LayerZero endpoint ID for the mock
     */
    constructor(uint16 _lzEndpointId) {
        // Initialize the mock endpoint
        lzEndpointMock = new LZEndpointMock(_lzEndpointId);
        
        // Initialize PingPong with the mock endpoint address
        pingPong = new PingPong(address(lzEndpointMock));
    }

    /**
     * @dev Demonstrates sending a ping to another chain using PingPong
     * @param _dstChainId The destination chain ID
     * @param _message The message to send
     */
    function sendPing(uint16 _dstChainId, string memory _message) external payable {
        // Encode the adapter parameters (empty in this case)
        bytes memory adapterParams = "";

        // Estimate the message fee
        (uint256 messageFee,) = pingPong.estimateFees(
            _dstChainId,
            false,
            adapterParams
        );

        // Verify sufficient payment
        require(msg.value >= messageFee, "Insufficient fee");

        // Send the ping message
        pingPong.ping{value: msg.value}(
            _dstChainId,
            _message,
            payable(msg.sender),
            address(0), // No refund address
            adapterParams
        );
    }

    /**
     * @dev Demonstrates simulating a ping response using LZEndpointMock
     * @param _srcChainId The source chain ID to simulate
     * @param _from The source address to simulate
     * @param _message The message to simulate
     */
    function simulatePong(
        uint16 _srcChainId,
        bytes memory _from,
        string memory _message
    ) external {
        // Encode the payload as it would be received
        bytes memory payload = abi.encode(_message);

        // Simulate receiving a message through the endpoint
        lzEndpointMock.receivePayload(
            _srcChainId,
            _from,
            address(pingPong),
            0, // Nonce doesn't matter for mock
            payload
        );
    }

    /**
     * @dev Returns the current message count from PingPong
     * @return The current message count
     */
    function getMessageCount() external view returns (uint256) {
        return pingPong.messageCount();
    }
}
```
