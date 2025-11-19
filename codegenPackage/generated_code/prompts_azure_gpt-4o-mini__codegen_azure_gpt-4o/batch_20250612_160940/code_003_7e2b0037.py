"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Generate an example of a smart contract that utilizes Chainlink CCIP for cross-chain message passing within the XSwap ecosystem.
Generated: DETERMINISTIC_7e2b00372dd61427
Batch ID: 20250612_160940
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

// Import Chainlink CCIP interfaces
import "@chainlink/contracts/src/v0.8/ccip/interfaces/ICrossChainMessageReceiver.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/ICrossChainMessageSender.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/IRouter.sol";

contract XSwapCrossChain {
    // Address of the Chainlink CCIP Router
    IRouter public immutable router;

    // Event emitted when a cross-chain message is sent
    event CrossChainMessageSent(
        uint64 indexed destinationChainId,
        address indexed receiver,
        bytes payload
    );

    // Event emitted when a cross-chain message is received
    event CrossChainMessageReceived(
        uint64 indexed sourceChainId,
        address indexed sender,
        bytes payload
    );

    // Constructor to initialize the Chainlink CCIP Router
    constructor(address _router) {
        require(_router != address(0), "Router address cannot be zero");
        router = IRouter(_router);
    }

    /**
     * @notice Sends a cross-chain message to another chain
     * @param destinationChainId The ID of the destination chain
     * @param receiver The address of the receiver contract on the destination chain
     * @param payload The data payload to send
     */
    function sendCrossChainMessage(
        uint64 destinationChainId,
        address receiver,
        bytes memory payload
    ) external payable {
        require(receiver != address(0), "Receiver address cannot be zero");
        require(payload.length > 0, "Payload cannot be empty");

        // Prepare the message
        IRouter.Message memory message = IRouter.Message({
            receiver: receiver,
            data: payload
        });

        // Send the message via Chainlink CCIP Router
        router.ccipSend{value: msg.value}(destinationChainId, message);

        emit CrossChainMessageSent(destinationChainId, receiver, payload);
    }

    /**
     * @notice Handles incoming cross-chain messages
     * @param sourceChainId The ID of the source chain
     * @param sender The address of the sender contract on the source chain
     * @param payload The data payload received
     */
    function ccipReceive(
        uint64 sourceChainId,
        address sender,
        bytes calldata payload
    ) external {
        require(msg.sender == address(router), "Unauthorized sender");
        require(sender != address(0), "Sender address cannot be zero");
        require(payload.length > 0, "Payload cannot be empty");

        // Emit an event for the received message
        emit CrossChainMessageReceived(sourceChainId, sender, payload);

        // Handle the payload (custom logic can be added here)
        // Example: Decode and process the payload
    }

    /**
     * @notice Fallback function to receive Ether
     */
    receive() external payable {}

    /**
     * @notice Withdraw Ether from the contract
     * @param to The address to send the Ether to
     */
    function withdrawEther(address payable to) external {
        require(to != address(0), "Recipient address cannot be zero");
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available to withdraw");

        to.transfer(balance);
    }
}
```
