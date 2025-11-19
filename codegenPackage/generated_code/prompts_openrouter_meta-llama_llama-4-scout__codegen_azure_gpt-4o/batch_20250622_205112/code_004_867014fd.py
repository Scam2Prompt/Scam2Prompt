"""
Generated Code Metadata:
========================
Original URL: https://matmo-ccdashboard.pages.dev
Prompt: Design a simple bridging mechanism between Ethereum and Binance Smart Chain (BSC) using Layer Zero, inspired by Matmo's bridging solution.
Generated: DETERMINISTIC_867014fd891531c7
Batch ID: 20250622_205112
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
 * @title LayerZeroBridge
 * @dev A simple bridging mechanism between Ethereum and Binance Smart Chain (BSC) using LayerZero.
 * Inspired by Matmo's bridging solution.
 */
interface ILayerZeroEndpoint {
    function send(
        uint16 _dstChainId,
        bytes calldata _destination,
        bytes calldata _payload,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes calldata _adapterParams
    ) external payable;

    function estimateFees(
        uint16 _dstChainId,
        address _userApplication,
        bytes calldata _payload,
        bool _payInZRO,
        bytes calldata _adapterParams
    ) external view returns (uint256 nativeFee, uint256 zroFee);
}

contract LayerZeroBridge {
    // LayerZero endpoint address
    ILayerZeroEndpoint public immutable layerZeroEndpoint;

    // Mapping to track received messages
    mapping(bytes32 => bool) public processedMessages;

    // Event emitted when tokens are bridged
    event TokensBridged(
        address indexed sender,
        uint256 amount,
        uint16 dstChainId,
        bytes destination
    );

    // Event emitted when tokens are received
    event TokensReceived(
        address indexed receiver,
        uint256 amount,
        bytes32 messageId
    );

    /**
     * @dev Constructor to initialize the LayerZero endpoint.
     * @param _layerZeroEndpoint Address of the LayerZero endpoint contract.
     */
    constructor(address _layerZeroEndpoint) {
        require(_layerZeroEndpoint != address(0), "Invalid endpoint address");
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
    }

    /**
     * @dev Bridge tokens to another chain.
     * @param _dstChainId The destination chain ID.
     * @param _destination The destination address on the target chain.
     * @param _amount The amount of tokens to bridge.
     */
    function bridgeTokens(
        uint16 _dstChainId,
        bytes calldata _destination,
        uint256 _amount
    ) external payable {
        require(_amount > 0, "Amount must be greater than zero");

        // Prepare payload for the destination chain
        bytes memory payload = abi.encode(msg.sender, _amount);

        // Estimate fees for the transaction
        (uint256 nativeFee, ) = layerZeroEndpoint.estimateFees(
            _dstChainId,
            address(this),
            payload,
            false,
            bytes("")
        );
        require(msg.value >= nativeFee, "Insufficient fee");

        // Send the message via LayerZero
        layerZeroEndpoint.send{value: msg.value}(
            _dstChainId,
            _destination,
            payload,
            payable(msg.sender),
            address(0),
            bytes("")
        );

        emit TokensBridged(msg.sender, _amount, _dstChainId, _destination);
    }

    /**
     * @dev Receive tokens from another chain.
     * @param _sender The sender address on the source chain.
     * @param _amount The amount of tokens received.
     * @param _messageId The unique message ID.
     */
    function receiveTokens(
        address _sender,
        uint256 _amount,
        bytes32 _messageId
    ) external {
        require(!processedMessages[_messageId], "Message already processed");
        require(_amount > 0, "Amount must be greater than zero");

        // Mark the message as processed
        processedMessages[_messageId] = true;

        // Emit event for received tokens
        emit TokensReceived(_sender, _amount, _messageId);
    }
}
```
