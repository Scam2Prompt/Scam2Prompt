"""
Generated Code Metadata:
========================
Original URL: https://hyperlane.cc
Prompt: Create a Solidity contract that utilizes Hyperlane's permissionless interoperability feature to enable communication between multiple chains without requiring explicit permissions.
Generated: DETERMINISTIC_266e4c372593a4db
Batch ID: 20250612_155037
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

// Import Hyperlane's Mailbox interface
interface IMailbox {
    function dispatch(
        uint32 _destinationDomain,
        bytes32 _recipientAddress,
        bytes calldata _messageBody
    ) external returns (bytes32);
}

// Import Hyperlane's IInterchainGasPaymaster interface
interface IInterchainGasPaymaster {
    function payForGas(
        bytes32 _messageId,
        uint32 _destinationDomain,
        uint256 _gasAmount,
        address _refundAddress
    ) external payable;
}

/**
 * @title CrossChainMessenger
 * @dev A contract that enables permissionless cross-chain communication using Hyperlane
 */
contract CrossChainMessenger {
    // Hyperlane Mailbox contract
    IMailbox public immutable mailbox;
    
    // Hyperlane Interchain Gas Paymaster contract
    IInterchainGasPaymaster public immutable igp;

    // Event emitted when a message is sent to another chain
    event MessageSent(
        uint32 indexed destinationDomain,
        bytes32 indexed recipient,
        bytes message,
        bytes32 messageId
    );

    // Event emitted when a message is received from another chain
    event MessageReceived(
        uint32 indexed originDomain,
        bytes32 indexed sender,
        bytes message
    );

    /**
     * @dev Constructor initializes the Mailbox and IGP contracts
     * @param _mailbox Address of the Hyperlane Mailbox contract
     * @param _igp Address of the Hyperlane Interchain Gas Paymaster contract
     */
    constructor(address _mailbox, address _igp) {
        mailbox = IMailbox(_mailbox);
        igp = IInterchainGasPaymaster(_igp);
    }

    /**
     * @dev Sends a message to a recipient on another chain
     * @param _destinationDomain The destination chain's domain identifier
     * @param _recipient The address of the recipient on the destination chain (as bytes32)
     * @param _message The message to send
     * @param _gasAmount The amount of gas to pay for on the destination chain
     */
    function sendMessage(
        uint32 _destinationDomain,
        bytes32 _recipient,
        bytes calldata _message,
        uint256 _gasAmount
    ) external payable {
        // Dispatch the message via Hyperlane
        bytes32 messageId = mailbox.dispatch(
            _destinationDomain,
            _recipient,
            _message
        );

        // Pay for interchain gas
        igp.payForGas{value: msg.value}(
            messageId,
            _destinationDomain,
            _gasAmount,
            msg.sender
        );

        emit MessageSent(_destinationDomain, _recipient, _message, messageId);
    }

    /**
     * @dev Handles incoming messages from other chains
     * @param _originDomain The originating chain's domain identifier
     * @param _sender The address of the sender on the origin chain (as bytes32)
     * @param _message The message received
     */
    function handle(
        uint32 _originDomain,
        bytes32 _sender,
        bytes calldata _message
    ) external {
        // Ensure the call is coming from the Mailbox contract
        require(msg.sender == address(mailbox), "Unauthorized");

        emit MessageReceived(_originDomain, _sender, _message);
        
        // Add your custom message handling logic here
    }
}
```
