"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Create a Solidity contract that utilizes Hyperlane's permissionless interoperability feature to enable communication between multiple chains without requiring explicit permissions.
Generated: DETERMINISTIC_266e4c372593a4db
Batch ID: 20250612_155037
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

// Import Hyperlane interfaces
import "@hyperlane-xyz/interfaces/IMailbox.sol";
import "@hyperlane-xyz/interfaces/IInterchainGasPaymaster.sol";

/**
 * @title CrossChainMessenger
 * @dev A Solidity contract utilizing Hyperlane's permissionless interoperability feature
 *      to enable communication between multiple chains without requiring explicit permissions.
 */
contract CrossChainMessenger {
    // Address of the Hyperlane Mailbox contract
    IMailbox public mailbox;

    // Address of the Hyperlane Interchain Gas Paymaster contract
    IInterchainGasPaymaster public interchainGasPaymaster;

    // Mapping to store received messages from other chains
    mapping(bytes32 => string) public receivedMessages;

    // Event to log outgoing messages
    event MessageSent(uint32 destinationDomain, string message);

    // Event to log incoming messages
    event MessageReceived(bytes32 messageId, string message);

    /**
     * @dev Constructor to initialize the Hyperlane Mailbox and Gas Paymaster addresses.
     * @param _mailbox Address of the Hyperlane Mailbox contract.
     * @param _interchainGasPaymaster Address of the Hyperlane Interchain Gas Paymaster contract.
     */
    constructor(address _mailbox, address _interchainGasPaymaster) {
        require(_mailbox != address(0), "Invalid mailbox address");
        require(_interchainGasPaymaster != address(0), "Invalid gas paymaster address");

        mailbox = IMailbox(_mailbox);
        interchainGasPaymaster = IInterchainGasPaymaster(_interchainGasPaymaster);
    }

    /**
     * @dev Sends a message to another chain.
     * @param destinationDomain The Hyperlane domain ID of the destination chain.
     * @param message The message to send.
     */
    function sendMessage(uint32 destinationDomain, string memory message) external payable {
        // Encode the message as bytes
        bytes memory encodedMessage = abi.encode(message);

        // Send the message via Hyperlane Mailbox
        bytes32 messageId = mailbox.dispatch(destinationDomain, address(this), encodedMessage);

        // Pay for interchain gas
        interchainGasPaymaster.payForGas{value: msg.value}(messageId, destinationDomain, msg.sender);

        emit MessageSent(destinationDomain, message);
    }

    /**
     * @dev Handle incoming messages from other chains.
     * @param origin Domain ID of the origin chain.
     * @param sender Address of the sender on the origin chain.
     * @param message The incoming message as bytes.
     */
    function handle(uint32 origin, bytes32 sender, bytes calldata message) external {
        // Only the Hyperlane Mailbox can call this function
        require(msg.sender == address(mailbox), "Unauthorized sender");

        // Decode the incoming message
        string memory decodedMessage = abi.decode(message, (string));

        // Generate a unique key for the message using keccak256
        bytes32 messageId = keccak256(abi.encodePacked(origin, sender, message));

        // Store the received message in the mapping
        receivedMessages[messageId] = decodedMessage;

        emit MessageReceived(messageId, decodedMessage);
    }

    /**
     * @dev Retrieve a received message using its unique message ID.
     * @param messageId The unique ID of the message.
     * @return The received message.
     */
    function getMessage(bytes32 messageId) external view returns (string memory) {
        return receivedMessages[messageId];
    }

    /**
     * @dev Fallback function to receive funds for interchain gas payments.
     */
    receive() external payable {}
}
```
