"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: How can I use Chainlink's Cross-Chain Interoperability Protocol (CCIP) to move data between different blockchains?
Generated: DETERMINISTIC_73c224e20f4b57d9
Batch ID: 20250612_160853
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

// Import Chainlink CCIP interfaces and libraries
import "@chainlink/contracts/src/v0.8/ccip/Client.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/ICrossChainMessaging.sol";

// Contract to facilitate cross-chain communication using Chainlink CCIP
contract CrossChainDataTransfer {
    // Address of the Chainlink CCIP Router
    address public immutable ccipRouter;

    // Mapping to store received data for tracking purposes
    mapping(bytes32 => bytes) public receivedMessages;

    // Event emitted when data is successfully sent cross-chain
    event DataSent(bytes32 messageId, address destinationChain, address receiver, bytes data);

    // Event emitted when data is successfully received cross-chain
    event DataReceived(bytes32 messageId, bytes data);

    /**
     * @dev Constructor to initialize the CCIP Router address.
     * @param _ccipRouter Address of the Chainlink CCIP Router contract.
     */
    constructor(address _ccipRouter) {
        require(_ccipRouter != address(0), "CCIP Router address cannot be zero");
        ccipRouter = _ccipRouter;
    }

    /**
     * @dev Sends data to a destination chain using Chainlink CCIP.
     * @param destinationChain The target chain ID.
     * @param receiver The address on the destination chain to receive the data.
     * @param data The payload of data to be sent.
     */
    function sendData(
        bytes32 destinationChain,
        address receiver,
        bytes calldata data
    ) external {
        // Prepare the message payload
        Client.EVM2AnyMessage memory message = Client.EVM2AnyMessage({
            receiver: receiver,
            data: data,
            tokenAmounts: new Client.TokenAmount[](0), // No token transfer in this example
            feeToken: address(0) // Use native token for fees
        });

        // Send the message using the CCIP Router
        bytes32 messageId = ICrossChainMessaging(ccipRouter).send(destinationChain, message);

        // Emit event for tracking purposes
        emit DataSent(messageId, destinationChain, receiver, data);
    }

    /**
     * @dev Handles the incoming message received from another chain.
     * @param messageId The unique ID of the message.
     * @param data The payload of data received.
     */
    function ccipReceive(bytes32 messageId, bytes calldata data) external {
        // Ensure the message is coming from the valid CCIP Router
        require(msg.sender == ccipRouter, "Unauthorized sender");

        // Store the received message in the mapping
        receivedMessages[messageId] = data;

        // Emit event for tracking purposes
        emit DataReceived(messageId, data);
    }
}
```

### Notes:
Place this Solidity code in a file (e.g., `CrossChainDataTransfer.sol`) and ensure you have the Chainlink CCIP libraries installed in your project. You can use tools like Hardhat or Truffle to deploy and test this contract on supported blockchains that integrate Chainlink CCIP.
