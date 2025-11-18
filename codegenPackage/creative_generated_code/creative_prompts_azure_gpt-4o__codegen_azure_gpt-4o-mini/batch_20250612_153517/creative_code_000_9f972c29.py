"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zero-815.pages.dev
Prompt: Write a Solidity smart contract that uses LayerZero's `OmniCounter.sol` example to implement a cross-chain counter. Include code for sending and receiving messages between chains.
Generated: DETERMINISTIC_9f972c2963e5c8c5
Batch ID: 20250612_153517
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

// Importing the LayerZero interfaces for cross-chain communication
import "@layerzero/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzero/contracts/interfaces/ILayerZeroReceiver.sol";
import "@layerzero/contracts/interfaces/ILayerZeroUserApp.sol";
import "@layerzero/contracts/interfaces/ILayerZeroMessage.sol";

// Define the OmniCounter contract
contract OmniCounter is ILayerZeroReceiver {
    // State variables
    ILayerZeroEndpoint public endpoint; // LayerZero endpoint for cross-chain communication
    uint256 public counter; // Counter variable
    mapping(uint16 => mapping(bytes => uint256)) public remoteCounter; // Store counters for remote chains

    // Event emitted when the counter is incremented
    event CounterIncremented(uint256 newValue);
    // Event emitted when a message is received from another chain
    event MessageReceived(uint256 value);

    // Constructor to initialize the LayerZero endpoint
    constructor(address _endpoint) {
        endpoint = ILayerZeroEndpoint(_endpoint);
        counter = 0; // Initialize counter
    }

    // Function to increment the counter and send a message to another chain
    function incrementCounterAndSend(uint16 _dstChainId, bytes memory _payload) public {
        counter++; // Increment local counter
        emit CounterIncremented(counter); // Emit event

        // Prepare the message to send
        bytes memory message = abi.encode(counter, _payload);
        
        // Sending message to the destination chain
        bytes memory adapterParams = ""; // Extra parameters can be specified here
        endpoint.send{value: msg.value}(
            _dstChainId, // Destination chain ID
            message, // Message to send
            payable(msg.sender), // Address to refund gas
            address(0), // Address to send the message to
            adapterParams // Optional adapter parameters
        );
    }

    // Function to receive messages from other chains
    function lzReceive(
        uint16 _srcChainId, // Source chain ID
        bytes memory _srcAddress, // Source address
        uint64, // Nonce (not used)
        bytes memory _payload // The payload sent from the source
    ) external override {
        require(msg.sender == address(endpoint), "Invalid caller"); // Ensure the caller is the endpoint

        // Decode the payload
        (uint256 receivedCounter, bytes memory receivedPayload) = abi.decode(_payload, (uint256, bytes));

        // Update the remote counter
        remoteCounter[_srcChainId][_srcAddress] = receivedCounter;

        emit MessageReceived(receivedCounter); // Emit event with the received counter
    }

    // Function to get the counter value from a specific remote chain
    function getRemoteCounter(uint16 _srcChainId, bytes memory _srcAddress) public view returns (uint256) {
        return remoteCounter[_srcChainId][_srcAddress]; // Return the remote counter value
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
