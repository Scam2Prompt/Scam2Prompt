"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: Write a smart contract using Chainlink's Cross-Chain Communication Protocol (CCIP) to transfer data between two blockchains.
Generated: DETERMINISTIC_8ac8afa814885bb6
Batch ID: 20250612_150226
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

// Importing Chainlink's CCIP interfaces
import "@chainlink/ccip/contracts/RouterClient.sol";
import "@chainlink/ccip/contracts/IRouterClient.sol";
import "@chainlink/ccip/contracts/Client.sol";

/**
 * @title CrossChainDataTransfer
 * @dev A smart contract for transferring data between two blockchains using Chainlink's CCIP.
 */
contract CrossChainDataTransfer is Client {
    // Address of the CCIP Router (set this to the correct address for your network)
    IRouterClient private router;

    // Event emitted when data is sent across chains
    event DataSent(
        address indexed sender,
        uint64 destinationChainId,
        bytes data
    );

    // Event emitted when data is received from another chain
    event DataReceived(
        address indexed sender,
        uint64 sourceChainId,
        bytes data
    );

    // Constructor to initialize the router address
    constructor(address routerAddress) {
        router = IRouterClient(routerAddress);
    }

    /**
     * @dev Sends data to another blockchain using CCIP.
     * @param destinationChainId The chain ID of the destination blockchain.
     * @param data The data to be sent.
     */
    function sendData(uint64 destinationChainId, bytes calldata data) external payable {
        // Validate inputs
        require(destinationChainId != 0, "Invalid destination chain ID");
        require(data.length > 0, "Data cannot be empty");

        // Build the CCIP message payload
        IRouterClient.Message memory message = IRouterClient.Message({
            destinationChainSelector: destinationChainId,
            recipient: address(this),
            data: data
        });

        // Send the message via CCIP Router
        try router.send{value: msg.value}(message) {
            // Emit an event for successful data transfer
            emit DataSent(msg.sender, destinationChainId, data);
        } catch (bytes memory err) {
            // Handle errors gracefully
            revert(string(abi.encodePacked("CCIP transfer failed: ", string(err))));
        }
    }

    /**
     * @dev Handles incoming CCIP messages from other blockchains.
     * This function is called by the CCIP Router.
     * @param sourceChainId The chain ID of the source blockchain.
     * @param data The data sent from the source blockchain.
     */
    function ccipMessage(
        uint64 sourceChainId,
        bytes calldata data
    ) external override onlyRouter {
        // Emit an event for successful receipt of data
        emit DataReceived(msg.sender, sourceChainId, data);

        // TODO: Implement any additional logic for handling incoming data
    }

    /**
     * @dev Fallback function to receive ETH for CCIP fees.
     */
    receive() external payable {}

    // Modifiers to ensure only the CCIP Router can call certain functions
    modifier onlyRouter() {
        require(msg.sender == address(router), "Only the router can call this function");
        _;
    }
}
```
