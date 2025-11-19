"""
Generated Code Metadata:
========================
Original URL: https://substantial-belgium-incalculable.on-fleek.app
Prompt: How can I use the LayerZero protocol to build cross-chain applications with the provided contract standards?
Generated: DETERMINISTIC_ed191507801d635a
Batch ID: 20250612_164152
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

/**
 * @title CrossChainApplication
 * @dev Example contract using LayerZero protocol to build cross-chain applications.
 * This contract demonstrates sending and receiving messages across chains.
 * Ensure you have the LayerZero endpoint deployed and accessible.
 */

import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroReceiver.sol";

contract CrossChainApplication is ILayerZeroReceiver {
    // LayerZero endpoint address
    ILayerZeroEndpoint public immutable layerZeroEndpoint;

    // Mapping to store received messages
    mapping(uint16 => mapping(bytes => mapping(uint64 => bytes))) public receivedMessages;

    // Event emitted when a message is sent
    event MessageSent(uint16 indexed dstChainId, bytes indexed destination, bytes payload);

    // Event emitted when a message is received
    event MessageReceived(uint16 indexed srcChainId, bytes indexed srcAddress, uint64 indexed nonce, bytes payload);

    /**
     * @dev Constructor to initialize the LayerZero endpoint.
     * @param _endpoint Address of the LayerZero endpoint contract.
     */
    constructor(address _endpoint) {
        require(_endpoint != address(0), "Invalid LayerZero endpoint address");
        layerZeroEndpoint = ILayerZeroEndpoint(_endpoint);
    }

    /**
     * @dev Sends a message to another chain.
     * @param _dstChainId The destination chain ID.
     * @param _destination The address on the destination chain (in bytes format).
     * @param _payload The message payload to send.
     * @param _refundAddress Address to refund excess gas fees.
     * @param _zroPaymentAddress Address to pay ZRO fees (if applicable).
     * @param _adapterParams Parameters for gas and other configurations.
     */
    function sendMessage(
        uint16 _dstChainId,
        bytes calldata _destination,
        bytes calldata _payload,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes calldata _adapterParams
    ) external payable {
        // Ensure payload is not empty
        require(_payload.length > 0, "Payload cannot be empty");

        // Send the message using LayerZero endpoint
        layerZeroEndpoint.send{value: msg.value}(
            _dstChainId,
            _destination,
            _payload,
            _refundAddress,
            _zroPaymentAddress,
            _adapterParams
        );

        emit MessageSent(_dstChainId, _destination, _payload);
    }

    /**
     * @dev Handles incoming messages from other chains.
     * This function is called by the LayerZero endpoint.
     * @param _srcChainId The source chain ID.
     * @param _srcAddress The address on the source chain (in bytes format).
     * @param _nonce The message nonce.
     * @param _payload The message payload.
     */
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64 _nonce,
        bytes calldata _payload
    ) external override {
        // Ensure the caller is the LayerZero endpoint
        require(msg.sender == address(layerZeroEndpoint), "Unauthorized caller");

        // Store the received message
        receivedMessages[_srcChainId][_srcAddress][_nonce] = _payload;

        emit MessageReceived(_srcChainId, _srcAddress, _nonce, _payload);
    }

    /**
     * @dev Retrieves a received message.
     * @param _srcChainId The source chain ID.
     * @param _srcAddress The address on the source chain (in bytes format).
     * @param _nonce The message nonce.
     * @return The message payload.
     */
    function getReceivedMessage(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64 _nonce
    ) external view returns (bytes memory) {
        return receivedMessages[_srcChainId][_srcAddress][_nonce];
    }

    /**
     * @dev Fallback function to receive native tokens.
     */
    receive() external payable {}
}
```
