"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Provide code examples for integrating LayerZero's messaging lifecycle in a decentralized application.
Generated: DETERMINISTIC_77aaf03636aeaa3c
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is clean and production-ready code for integrating LayerZero's messaging lifecycle in a decentralized application using Solidity.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for LayerZero's endpoint contract
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
        bool _useZro,
        bytes calldata _adapterParams
    ) external view returns (uint256 nativeFee, uint256 zroFee);
}

// Interface for LayerZero's Receiver contract
interface ILayerZeroReceiver {
    function lzReceive(uint16 _srcChainId, bytes calldata _srcAddress, uint64 _nonce, bytes calldata _payload) external;
}

contract LayerZeroMessaging is ILayerZeroReceiver {
    address public owner;
    ILayerZeroEndpoint public immutable layerZeroEndpoint;

    // Event emitted for successful message sending
    event MessageSent(uint16 indexed dstChainId, bytes destination, bytes payload);

    // Event emitted when a message is received
    event MessageReceived(uint16 indexed srcChainId, bytes srcAddress, uint64 nonce, bytes payload);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor(address _layerZeroEndpoint) {
        require(_layerZeroEndpoint != address(0), "Invalid endpoint address");
        owner = msg.sender;
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
    }

    /**
     * @dev Sends a message to another chain via LayerZero.
     * @param _dstChainId The destination chain ID.
     * @param _destination The receiving contract's address on the destination chain (encoded as bytes).
     * @param _payload The message payload to send.
     */
    function sendMessage(
        uint16 _dstChainId,
        bytes calldata _destination,
        bytes calldata _payload
    ) external payable onlyOwner {
        // Estimate fees for the message
        (uint256 nativeFee, ) = layerZeroEndpoint.estimateFees(
            _dstChainId,
            address(this),
            _payload,
            false,
            ""
        );

        require(msg.value >= nativeFee, "Insufficient fee");

        // Send the message via LayerZero
        layerZeroEndpoint.send{value: msg.value}(
            _dstChainId,
            _destination,
            _payload,
            payable(msg.sender), // Refund excess fees back to the sender
            address(0),          // No ZRO payment (use native currency)
            ""                   // Default adapter parameters
        );

        emit MessageSent(_dstChainId, _destination, _payload);
    }

    /**
     * @dev Function to handle incoming LayerZero messages.
     * @param _srcChainId The source chain ID.
     * @param _srcAddress The address of the sender on the source chain.
     * @param _nonce The message nonce.
     * @param _payload The message payload.
     */
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64 _nonce,
        bytes calldata _payload
    ) external override {
        require(msg.sender == address(layerZeroEndpoint), "Unauthorized caller");

        // Emit event for received message
        emit MessageReceived(_srcChainId, _srcAddress, _nonce, _payload);

        // Further processing of the payload can be implemented here
    }

    /**
     * @dev Allows the owner to withdraw any leftover funds in the contract.
     * @param _recipient The address to send the funds to.
     */
    function withdraw(address payable _recipient) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available");
        _recipient.transfer(balance);
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }

    // Fallback function to receive funds
    receive() external payable {}
}
```

This code fulfills the outlined requirements and integrates LayerZero’s messaging lifecycle effectively.
