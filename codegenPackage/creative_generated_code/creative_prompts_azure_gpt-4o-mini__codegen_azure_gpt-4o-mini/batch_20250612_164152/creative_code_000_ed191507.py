"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://substantial-belgium-incalculable.on-fleek.app
Prompt: How can I use the LayerZero protocol to build cross-chain applications with the provided contract standards?
Generated: DETERMINISTIC_ed191507801d635a
Batch ID: 20250612_164152
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

// Import LayerZero interfaces
import "@layerzero/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzero/contracts/interfaces/ILayerZeroReceiver.sol";
import "@layerzero/contracts/interfaces/ILayerZeroUserApp.sol";

contract CrossChainApp is ILayerZeroReceiver, ILayerZeroUserApp {
    // LayerZero endpoint
    ILayerZeroEndpoint public endpoint;

    // Store the latest message from each chain
    mapping(uint16 => string) public messages;

    // Event emitted when a message is received
    event MessageReceived(uint16 srcChainId, string message);

    // Event emitted when a message is sent
    event MessageSent(uint16 dstChainId, string message);

    // Modifier to check if the message is valid
    modifier validMessage(string memory message) {
        require(bytes(message).length > 0, "Message cannot be empty");
        _;
    }

    // Constructor to set the LayerZero endpoint
    constructor(address _endpoint) {
        endpoint = ILayerZeroEndpoint(_endpoint);
    }

    // Function to send a message to another chain
    function sendMessage(uint16 _dstChainId, string calldata _message) external validMessage(_message) {
        // Encode the message for transmission
        bytes memory payload = abi.encode(_message);

        // Send the message through LayerZero
        endpoint.send{value: msg.value}(
            _dstChainId,
            payload,
            payable(msg.sender),
            address(0), // No refund address
            bytes("") // No adapter params
        );

        emit MessageSent(_dstChainId, _message);
    }

    // Function to handle incoming messages from LayerZero
    function lzReceive(uint16 _srcChainId, bytes memory _payload) external override {
        // Ensure the function is called by the LayerZero endpoint
        require(msg.sender == address(endpoint), "Invalid caller");

        // Decode the message
        string memory message = abi.decode(_payload, (string));

        // Store the message for the specific chain
        messages[_srcChainId] = message;

        // Emit event for received message
        emit MessageReceived(_srcChainId, message);
    }

    // Function to withdraw any native tokens sent to this contract
    function withdraw() external {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(msg.sender).transfer(balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
