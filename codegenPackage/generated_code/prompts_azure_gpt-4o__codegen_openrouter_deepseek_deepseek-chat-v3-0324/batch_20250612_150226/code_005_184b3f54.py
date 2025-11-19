"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Explain how to integrate LayerZero's `OAppSender` and `OAppReceiver` interfaces into a Solidity contract for seamless cross-chain communication.
Generated: DETERMINISTIC_184b3f5414a55dd7
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {IOAppCore} from "@layerzero/contracts/oapp/interfaces/IOAppCore.sol";
import {OAppSender} from "@layerzero/contracts/oapp/OAppSender.sol";
import {OAppReceiver} from "@layerzero/contracts/oapp/OAppReceiver.sol";
import {OApp} from "@layerzero/contracts/oapp/OApp.sol";
import {MessagingFee, MessagingReceipt} from "@layerzero/contracts/interfaces/ILayerZeroEndpointV2.sol";

/**
 * @title CrossChainMessenger
 * @dev A contract that integrates LayerZero's OAppSender and OAppReceiver for cross-chain communication.
 */
contract CrossChainMessenger is OAppSender, OAppReceiver {
    // Custom error for unauthorized access
    error Unauthorized();

    // Event emitted when a message is sent
    event MessageSent(
        uint32 indexed destinationChainId,
        bytes32 indexed receiver,
        bytes message,
        MessagingReceipt receipt
    );

    // Event emitted when a message is received
    event MessageReceived(
        uint32 indexed originChainId,
        bytes32 indexed sender,
        bytes message
    );

    /**
     * @dev Constructor initializes the OApp with the LayerZero endpoint and delegate.
     * @param _endpoint The address of the LayerZero endpoint
     * @param _delegate The address that can set message execution options
     */
    constructor(
        address _endpoint,
        address _delegate
    ) OApp(_endpoint, _delegate) {}

    /**
     * @notice Sends a message to a receiver on a destination chain
     * @param _destinationChainId The destination chain ID
     * @param _receiver The receiver address in bytes32 format
     * @param _message The message payload
     * @param _options The messaging options (gas, etc.)
     * @param _payInLzToken Whether to pay fees in LZ token or native currency
     * @return receipt The messaging receipt containing GUID and fee information
     */
    function sendMessage(
        uint32 _destinationChainId,
        bytes32 _receiver,
        bytes calldata _message,
        bytes calldata _options,
        bool _payInLzToken
    ) external payable returns (MessagingReceipt memory receipt) {
        // Only allow the owner to send messages
        if (msg.sender != owner()) revert Unauthorized();

        // Encode the receiver address
        bytes memory _receiverBytes = abi.encodePacked(_receiver);

        // Calculate the messaging fee
        MessagingFee memory fee = _quote(
            _destinationChainId,
            _message,
            _options,
            _payInLzToken
        );

        // Send the message via LayerZero
        receipt = _lzSend(
            _destinationChainId,
            _message,
            _options,
            fee,
            payable(msg.sender)
        );

        emit MessageSent(
            _destinationChainId,
            _receiver,
            _message,
            receipt
        );

        return receipt;
    }

    /**
     * @notice Internal function to handle incoming messages
     * @param _origin The origin chain information
     * @param _guid The unique message identifier
     * @param _message The message payload
     * @param _executor The address that executed the message
     * @param _extraData Additional execution data
     */
    function _lzReceive(
        Origin calldata _origin,
        bytes32 _guid,
        bytes calldata _message,
        address _executor,
        bytes calldata _extraData
    ) internal override {
        // Decode the sender address from the message
        bytes32 sender;
        assembly {
            sender := calldataload(_message.offset)
        }

        emit MessageReceived(
            _origin.srcEid,
            sender,
            _message
        );

        // Process the message (custom logic would go here)
        // ...
    }

    /**
     * @notice Sets the message execution options for a destination chain
     * @param _eid The endpoint ID of the destination chain
     * @param _messageOptions The options to set
     */
    function setExecutionOptions(
        uint32 _eid,
        bytes calldata _messageOptions
    ) external onlyOwner {
        _setExecutionOptions(_eid, _messageOptions);
    }

    /**
     * @notice Allows the contract to receive native currency
     */
    receive() external payable {}
}
```
