"""
Generated Code Metadata:
========================
Original URL: https://substantial-belgium-incalculable.on-fleek.app
Prompt: Design a bridge between Aptos and Bitcoin using LayerZero's protocol overview and contract standards.
Generated: DETERMINISTIC_0beb96fc28dfdaef
Batch ID: 20250622_205030
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

/**
 * @title AptosToBitcoinBridge
 * @dev A bridge contract to facilitate token transfers between Aptos and Bitcoin using LayerZero protocol.
 * This contract assumes LayerZero's messaging standards for cross-chain communication.
 */

import "@layerzerolabs/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/contracts/interfaces/ILayerZeroReceiver.sol";

contract AptosToBitcoinBridge is ILayerZeroReceiver {
    // LayerZero endpoint for cross-chain communication
    ILayerZeroEndpoint public immutable layerZeroEndpoint;

    // Owner of the contract
    address public owner;

    // Mapping to track processed messages to prevent double-spending
    mapping(bytes32 => bool) public processedMessages;

    // Events
    event TokensSent(address indexed sender, uint256 amount, string bitcoinAddress);
    event TokensReceived(address indexed receiver, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the LayerZero endpoint and set the contract owner.
     * @param _layerZeroEndpoint Address of the LayerZero endpoint contract.
     */
    constructor(address _layerZeroEndpoint) {
        require(_layerZeroEndpoint != address(0), "Invalid LayerZero endpoint address");
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
        owner = msg.sender;
    }

    /**
     * @dev Sends tokens from Aptos to Bitcoin.
     * @param amount Amount of tokens to send.
     * @param bitcoinAddress Bitcoin address to receive the tokens.
     * @param destinationChainId LayerZero chain ID of the Bitcoin network.
     */
    function sendTokensToBitcoin(uint256 amount, string memory bitcoinAddress, uint16 destinationChainId) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(bitcoinAddress).length > 0, "Invalid Bitcoin address");

        // Encode payload for LayerZero
        bytes memory payload = abi.encode(msg.sender, amount, bitcoinAddress);

        // Estimate fees for LayerZero message
        (uint256 nativeFee, ) = layerZeroEndpoint.estimateFees(destinationChainId, address(this), payload, false, "");

        require(msg.value >= nativeFee, "Insufficient fee");

        // Send message to LayerZero endpoint
        layerZeroEndpoint.send{value: msg.value}(
            destinationChainId, // Destination chain ID
            abi.encodePacked(address(this)), // Destination address
            payload, // Payload
            payable(msg.sender), // Refund address
            address(0), // ZRO payment address
            "" // Adapter parameters
        );

        emit TokensSent(msg.sender, amount, bitcoinAddress);
    }

    /**
     * @dev Receives tokens from Bitcoin to Aptos.
     * @param srcChainId Source chain ID (Bitcoin network).
     * @param srcAddress Source address (LayerZero contract on Bitcoin network).
     * @param payload Encoded payload containing receiver and amount.
     */
    function lzReceive(uint16 srcChainId, bytes calldata srcAddress, uint64, bytes calldata payload) external override {
        require(msg.sender == address(layerZeroEndpoint), "Unauthorized caller");

        // Decode payload
        (address receiver, uint256 amount) = abi.decode(payload, (address, uint256));

        // Generate unique message hash
        bytes32 messageHash = keccak256(abi.encodePacked(srcChainId, srcAddress, payload));
        require(!processedMessages[messageHash], "Message already processed");

        // Mark message as processed
        processedMessages[messageHash] = true;

        // Transfer tokens to receiver
        // Note: Token transfer logic should be implemented here (e.g., minting or transferring tokens).
        // For simplicity, we emit an event.
        emit TokensReceived(receiver, amount);
    }

    /**
     * @dev Updates the contract owner.
     * @param newOwner Address of the new owner.
     */
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner address");
        owner = newOwner;
    }

    /**
     * @dev Withdraws any native tokens (ETH) sent to the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to receive native tokens.
     */
    receive() external payable {}
}
```
