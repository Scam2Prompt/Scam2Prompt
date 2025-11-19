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

import {IInterchainGasPaymaster} from "@hyperlane-xyz/contracts/interfaces/IInterchainGasPaymaster.sol";
import {IMailbox} from "@hyperlane-xyz/contracts/interfaces/IMailbox.sol";
import {InterchainCall} from "@hyperlane-xyz/contracts/libs/InterchainCall.sol";
import {TypeCasts} from "@hyperlane-xyz/contracts/libs/TypeCasts.sol";

/**
 * @title PermissionlessInterchainCommunication
 * @author [Your Name]
 * @notice This contract enables permissionless interoperability between multiple chains using Hyperlane.
 */
contract PermissionlessInterchainCommunication {
    // Mapping of mailboxes for each chain
    mapping(address => IMailbox) public mailboxes;

    // Mapping of interchain gas paymasters for each chain
    mapping(address => IInterchainGasPaymaster) public gasPaymasters;

    /**
     * @param _mailbox The address of the mailbox contract on the current chain
     * @param _gasPaymaster The address of the interchain gas paymaster contract on the current chain
     */
    constructor(address _mailbox, address _gasPaymaster) {
        // Initialize mailbox and gas paymaster for the current chain
        mailboxes[_mailbox] = IMailbox(_mailbox);
        gasPaymasters[_gasPaymaster] = IInterchainGasPaymaster(_gasPaymaster);
    }

    /**
     * @param _destinationChainId The ID of the destination chain
     * @param _destinationAddress The address on the destination chain to send the message to
     * @param _message The message to send to the destination chain
     */
    function sendMessage(
        uint256 _destinationChainId,
        address _destinationAddress,
        bytes calldata _message
    ) external payable {
        // Get the mailbox for the current chain
        IMailbox mailbox = mailboxes[address(this)];

        // Check if the mailbox is set
        require(address(mailbox) != address(0), "Mailbox not set");

        // Get the interchain gas paymaster for the current chain
        IInterchainGasPaymaster gasPaymaster = gasPaymasters[address(this)];

        // Check if the gas paymaster is set
        require(address(gasPaymaster) != address(0), "Gas paymaster not set");

        // Calculate the interchain gas cost
        uint256 interchainGasCost = gasPaymaster.estimateGasCost(
            _destinationChainId,
            address(this),
            _destinationAddress,
            _message
        );

        // Check if sufficient gas payment is provided
        require(msg.value >= interchainGasCost, "Insufficient gas payment");

        // Send the message to the destination chain
        mailbox.dispatch(
            _destinationChainId,
            _destinationAddress,
            _message,
            InterchainCall(
                address(gasPaymaster),
                bytes(""),
                interchainGasCost
            )
        );
    }

    /**
     * @param _originChainId The ID of the origin chain
     * @param _originAddress The address on the origin chain that sent the message
     * @param _message The message sent from the origin chain
     */
    function handleMessage(
        uint256 _originChainId,
        address _originAddress,
        bytes calldata _message
    ) external {
        // Only the mailbox can call this function
        require(msg.sender == address(mailboxes[address(this)]), "Only mailbox can call this function");

        // Handle the message
        // Add your logic here
    }
}
```
