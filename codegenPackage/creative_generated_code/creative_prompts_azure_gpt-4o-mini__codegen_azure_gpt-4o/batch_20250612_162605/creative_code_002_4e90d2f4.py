"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validation-cv7.pages.dev
Prompt: Can you provide a code example for integrating a smart contract with a multichain setup as described by the Chain Solution Center?
Generated: DETERMINISTIC_4e90d2f4c1968e9b
Batch ID: 20250612_162605
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

// Import OpenZeppelin's Ownable contract to manage access control
import "@openzeppelin/contracts/access/Ownable.sol";

// Import the Chainlink Cross-chain Interoperability Protocol (CCIP) libraries
import "@chainlink/contracts/src/v0.8/interfaces/ICrossChainMessageReceiver.sol";
import "@chainlink/contracts/src/v0.8/interfaces/ICrossChainMessageSender.sol";

/**
 * @title MultichainSmartContract
 * @dev A smart contract that integrates with Chainlink's CCIP for multichain messaging.
 */
contract MultichainSmartContract is Ownable {
    // Address of the Chainlink CCIP router on the source chain
    address public ccipRouterAddress;

    // Mapping to keep track of received messages from other chains
    mapping(bytes32 => bool) public processedMessages;

    // Event emitted when a cross-chain message is sent
    event MessageSent(
        uint256 destinationChainId,
        address destinationAddress,
        string message
    );

    // Event emitted when a cross-chain message is received
    event MessageReceived(
        uint256 sourceChainId,
        address sourceAddress,
        string message
    );

    /**
     * @dev Constructor to set initial CCIP router address.
     * @param _ccipRouterAddress The address of the CCIP router on the source chain.
     */
    constructor(address _ccipRouterAddress) {
        require(
            _ccipRouterAddress != address(0),
            "CCIP router address cannot be zero."
        );
        ccipRouterAddress = _ccipRouterAddress;
    }

    /**
     * @dev Updates the CCIP router address.
     * @param _ccipRouterAddress The new address of the CCIP router.
     */
    function updateCCIPRouterAddress(address _ccipRouterAddress)
        external
        onlyOwner
    {
        require(
            _ccipRouterAddress != address(0),
            "CCIP router address cannot be zero."
        );
        ccipRouterAddress = _ccipRouterAddress;
    }

    /**
     * @dev Sends a cross-chain message to a destination address on another chain.
     * @param destinationChainId The ID of the destination chain.
     * @param destinationAddress The address of the recipient on the destination chain.
     * @param message The message to send.
     */
    function sendMessage(
        uint256 destinationChainId,
        address destinationAddress,
        string memory message
    ) external payable {
        require(
            destinationAddress != address(0),
            "Destination address cannot be zero."
        );

        // Interface for the CCIP router
        ICrossChainMessageSender ccipRouter = ICrossChainMessageSender(
            ccipRouterAddress
        );

        // Send the cross-chain message
        ccipRouter.sendMessage{value: msg.value}(
            destinationChainId,
            destinationAddress,
            abi.encode(message)
        );

        emit MessageSent(destinationChainId, destinationAddress, message);
    }

    /**
     * @dev Handles incoming cross-chain messages.
     * This function must be implemented in line with the CCIP router's requirements.
     * @param payload The message payload.
     * @param sourceChainId The ID of the source chain.
     * @param sourceAddress The address of the sender on the source chain.
     */
    function receiveMessage(
        bytes memory payload,
        uint256 sourceChainId,
        address sourceAddress
    ) external {
        require(msg.sender == ccipRouterAddress, "Unauthorized sender.");

        // Decode the payload
        string memory decodedMessage = abi.decode(payload, (string));

        // Generate a unique hash for the message to ensure it's not processed twice
        bytes32 messageHash = keccak256(
            abi.encodePacked(sourceChainId, sourceAddress, decodedMessage)
        );
        require(!processedMessages[messageHash], "Message already processed.");

        // Mark the message as processed
        processedMessages[messageHash] = true;

        // Emit an event for the received message
        emit MessageReceived(sourceChainId, sourceAddress, decodedMessage);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraws Ether from the contract.
     * @param recipient Address to send the Ether to.
     */
    function withdrawEther(address payable recipient) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero.");
        recipient.transfer(address(this).balance);
    }
}
```
