"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: How can I implement the LayerZero protocol to send messages across different blockchains using the OApp contract?
Generated: DETERMINISTIC_47b4fa687e57fcac
Batch ID: 20250612_164304
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

// Import necessary interfaces from LayerZero
import "@layerzerolabs/oz-contracts/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/oz-contracts/contracts/interfaces/ILayerZeroReceiver.sol";

// Sample OApp contract that implements LayerZero protocol to send messages across blockchains
contract OApp is ILayerZeroReceiver {
    // LayerZero endpoint interface
    ILayerZeroEndpoint public endpoint;
    
    // Event emitted when a message is sent
    event MessageSent(address indexed sender, uint256 indexed destinationChainId, bytes message);
    
    // Event emitted when a message is received
    event MessageReceived(address indexed sender, uint256 indexed sourceChainId, bytes message);

    // Constructor to initialize the LayerZero endpoint
    constructor(address _endpoint) {
        require(_endpoint != address(0), "Invalid endpoint address");
        endpoint = ILayerZeroEndpoint(_endpoint);
    }

    // Function to send a message to a specified chain
    function sendMessage(uint256 _destinationChainId, bytes calldata _message) external payable {
        // Check for non-zero message length
        require(_message.length > 0, "Message cannot be empty");

        // Send the message via LayerZero
        (bool success, bytes memory returnData) = endpoint.send{value: msg.value}(
            _destinationChainId,
            msg.sender, // The receiver's address on the destination chain
            _message,
            address(this), // The address of the contract that will handle the response
            "", // No custom payload
            "" // No extra gas limit
        );

        // Validate the success of the send message call
        require(success, "Failed to send message");

        // Emit the MessageSent event
        emit MessageSent(msg.sender, _destinationChainId, _message);
    }

    // Function to handle incoming messages from LayerZero
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64 _nonce,
        bytes calldata _payload
    ) external override {
        require(msg.sender == address(endpoint), "Unauthorized sender");

        // Emit the MessageReceived event with the details
        emit MessageReceived(address(uint160(uint256(keccak256(_srcAddress)))), _srcChainId, _payload);

        // (Optional) Add logic to process the received payload
        _processPayload(_payload);
    }

    // Optional function to process the received payload
    function _processPayload(bytes calldata _payload) internal {
        // Custom logic to handle the received message
        // This function can be overridden in derived contracts if needed
    }

    // Function to withdraw any accidentally sent Ether to the contract
    function withdraw(address payable _to, uint256 _amount) external {
        require(_to != address(0), "Invalid address");
        require(address(this).balance >= _amount, "Insufficient balance");
        
        // Transfer the specified amount of Ether to the provided address
        (bool success, ) = _to.call{value: _amount}("");
        require(success, "Transfer failed");
    }
    
    // Fallback function to receive Ether
    receive() external payable {}
}
```
