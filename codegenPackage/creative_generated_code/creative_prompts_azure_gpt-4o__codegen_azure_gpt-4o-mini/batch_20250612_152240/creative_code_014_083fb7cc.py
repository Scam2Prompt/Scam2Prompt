"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layerzero-networks.pages.dev
Prompt: Provide a code example for using LayerZero's `OAppReceiver` interface to handle incoming cross-chain messages in a Solidity contract.
Generated: DETERMINISTIC_083fb7ccc301deb5
Batch ID: 20250612_152240
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

// Importing the LayerZero interface for cross-chain messaging
import "@layerzero/lz-solidity/contracts/interfaces/ILayerZeroReceiver.sol";
import "@layerzero/lz-solidity/contracts/interfaces/ILayerZeroEndpoint.sol";

contract CrossChainReceiver is ILayerZeroReceiver {
    // LayerZero endpoint to send and receive messages
    ILayerZeroEndpoint public lzEndpoint;

    // Event emitted when a message is received
    event MessageReceived(address indexed from, uint256 indexed srcChainId, bytes message);

    // Constructor to initialize the LayerZero endpoint address
    constructor(address _lzEndpoint) {
        require(_lzEndpoint != address(0), "Invalid endpoint address");
        lzEndpoint = ILayerZeroEndpoint(_lzEndpoint);
    }

    // Function to receive cross-chain messages
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64 _nonce,
        bytes calldata _payload
    ) external override {
        // Ensure the call is coming from the LayerZero endpoint
        require(msg.sender == address(lzEndpoint), "Unauthorized caller");

        // Emit the event to log the received message
        emit MessageReceived(address(uint160(bytes20(_srcAddress))), _srcChainId, _payload);

        // Here, you can add custom logic to handle the incoming payload.
        // For instance, you might decode it and take action based on its contents.
        // Example: handlePayload(_payload);
    }

    // Function to send a message to another chain
    function sendMessage(
        uint16 _dstChainId,
        bytes calldata _dstAddress,
        bytes calldata _payload
    ) external payable {
        // Check if the provided destination address is valid
        require(_dstAddress.length == 20, "Invalid destination address length");

        // Sending message through LayerZero endpoint
        (uint256 nativeFee, ) = lzEndpoint.estimateFees(_dstChainId, address(this), _payload, false, "");

        require(msg.value >= nativeFee, "Insufficient funds for transaction fee");

        // Send the message
        lzEndpoint.send{value: msg.value}(
            _dstChainId,
            _dstAddress,
            _payload,
            payable(msg.sender),
            address(0), // refund address
            "" // options
        );
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to withdraw Ether from the contract
    function withdrawEther(address payable _to, uint256 _amount) external {
        require(_to != address(0), "Invalid recipient");
        require(address(this).balance >= _amount, "Insufficient balance");
        _to.transfer(_amount);
    }
}
```
