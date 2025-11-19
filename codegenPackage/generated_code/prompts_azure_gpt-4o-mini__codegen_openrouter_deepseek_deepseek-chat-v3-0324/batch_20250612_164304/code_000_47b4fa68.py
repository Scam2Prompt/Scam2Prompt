"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: How can I implement the LayerZero protocol to send messages across different blockchains using the OApp contract?
Generated: DETERMINISTIC_47b4fa687e57fcac
Batch ID: 20250612_164304
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

import "@layerzerolabs/solidity-examples/contracts/lzApp/NonblockingLzApp.sol";

/**
 * @title OApp Contract for Cross-Chain Messaging via LayerZero
 * @dev Extends NonblockingLzApp to implement cross-chain message sending/receiving
 */
contract OApp is NonblockingLzApp {
    event MessageSent(uint16 dstChainId, bytes destination, bytes message);
    event MessageReceived(uint16 srcChainId, bytes sender, bytes message);

    /**
     * @dev Constructor for OApp
     * @param _endpoint The LayerZero endpoint address
     */
    constructor(address _endpoint) NonblockingLzApp(_endpoint) {}

    /**
     * @notice Send a cross-chain message
     * @param _dstChainId The destination chain ID (LayerZero chain ID)
     * @param _destination The destination address on the target chain
     * @param _message The message payload to send
     * @param _refundAddress Address to receive refunds for excess gas
     * @param _zroPaymentAddress Address to pay for ZRO token fees (address(0) for native gas)
     * @param _adapterParams Additional parameters for the adapter
     */
    function sendMessage(
        uint16 _dstChainId,
        bytes memory _destination,
        bytes memory _message,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes memory _adapterParams
    ) public payable {
        _lzSend(
            _dstChainId,
            _message,
            _refundAddress,
            _zroPaymentAddress,
            _adapterParams,
            msg.value
        );
        emit MessageSent(_dstChainId, _destination, _message);
    }

    /**
     * @dev Internal function to handle incoming messages
     * @param _srcChainId The source chain ID
     * @param _sender The sender address on the source chain
     * @param _nonce The message nonce
     * @param _payload The message payload
     */
    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _sender,
        uint64 _nonce,
        bytes memory _payload
    ) internal override {
        emit MessageReceived(_srcChainId, _sender, _payload);
    }

    /**
     * @notice Estimate the message fee
     * @param _dstChainId The destination chain ID
     * @param _message The message payload
     * @param _useZro Whether to use ZRO token for fees
     * @param _adapterParams Additional parameters for the adapter
     * @return nativeFee The estimated fee in native token
     * @return zroFee The estimated fee in ZRO tokens
     */
    function estimateFee(
        uint16 _dstChainId,
        bytes memory _message,
        bool _useZro,
        bytes memory _adapterParams
    ) public view returns (uint256 nativeFee, uint256 zroFee) {
        return
            lzEndpoint.estimateFees(
                _dstChainId,
                address(this),
                _message,
                _useZro,
                _adapterParams
            );
    }
}
```
