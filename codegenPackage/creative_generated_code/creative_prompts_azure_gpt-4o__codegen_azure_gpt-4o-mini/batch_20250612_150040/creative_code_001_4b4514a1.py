"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://substantial-belgium-incalculable.on-fleek.app
Prompt: Generate a LayerZero-compatible smart contract that utilizes the protocol's messaging system to transfer value across supported blockchains. Ensure the contract adheres to LayerZero security stack recommendations.
Generated: DETERMINISTIC_4b4514a109cea3f2
Batch ID: 20250612_150040
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

/**
 * @title CrossChainValueTransfer
 * @dev A LayerZero-compatible smart contract for transferring value across supported blockchains.
 */
contract CrossChainValueTransfer is ILayerZeroReceiver, ILayerZeroUserApp {
    // LayerZero Endpoint for cross-chain communication
    ILayerZeroEndpoint public endpoint;

    // Event emitted when a value transfer is initiated
    event ValueTransferred(address indexed sender, uint256 amount, uint16 destinationChainId, bytes destinationAddress);

    // Mapping to track nonces for each destination chain
    mapping(uint16 => uint) public nonces;

    /**
     * @dev Constructor to initialize the LayerZero endpoint.
     * @param _endpoint Address of the LayerZero endpoint contract.
     */
    constructor(address _endpoint) {
        endpoint = ILayerZeroEndpoint(_endpoint);
    }

    /**
     * @dev Function to initiate a value transfer to another chain.
     * @param _amount The amount of value to transfer.
     * @param _destinationChainId The ID of the destination chain.
     * @param _destinationAddress The address on the destination chain to receive the value.
     */
    function transferValue(uint256 _amount, uint16 _destinationChainId, bytes calldata _destinationAddress) external payable {
        require(msg.value == _amount, "Incorrect value sent");
        
        // Increment the nonce for the destination chain
        nonces[_destinationChainId]++;

        // Prepare payload for LayerZero
        bytes memory payload = abi.encode(msg.sender, _amount);

        // Send the message to the destination chain
        (uint16 nativeChainId, uint256 nativeNonce) = endpoint.send{value: msg.value}(
            _destinationChainId,
            _destinationAddress,
            payload,
            address(0x0), // No refund address
            bytes(""), // No adapter parameters
            nonces[_destinationChainId]
        );

        emit ValueTransferred(msg.sender, _amount, _destinationChainId, _destinationAddress);
    }

    /**
     * @dev Function to handle incoming messages from LayerZero.
     * @param _srcChainId The ID of the source chain.
     * @param _srcAddress The address of the source contract.
     * @param _payload The bytes containing the incoming message payload.
     */
    function lzReceive(uint16 _srcChainId, bytes calldata _srcAddress, bytes calldata _payload) external override {
        // Validate the sender is the LayerZero endpoint
        require(msg.sender == address(endpoint), "Invalid sender");
        
        // Decode the payload
        (address receiver, uint256 amount) = abi.decode(_payload, (address, uint256));

        // Transfer the value to the specified receiver
        payable(receiver).transfer(amount);
    }

    /**
     * @dev Function to withdraw funds from the contract.
     * @param _to The address to withdraw funds to.
     * @param _amount The amount to withdraw.
     */
    function withdraw(address payable _to, uint256 _amount) external {
        require(_amount <= address(this).balance, "Insufficient balance");
        _to.transfer(_amount);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
