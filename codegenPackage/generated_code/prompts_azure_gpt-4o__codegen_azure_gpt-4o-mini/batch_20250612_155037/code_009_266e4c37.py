"""
Generated Code Metadata:
========================
Original URL: https://hyperlane.cc
Prompt: Create a Solidity contract that utilizes Hyperlane's permissionless interoperability feature to enable communication between multiple chains without requiring explicit permissions.
Generated: DETERMINISTIC_266e4c372593a4db
Batch ID: 20250612_155037
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

// Importing necessary interfaces from Hyperlane
import "@hyperlane-xyz/core/contracts/interfaces/IHyperlaneCore.sol";
import "@hyperlane-xyz/core/contracts/interfaces/IMessageHandler.sol";

contract InteroperableContract is IMessageHandler {
    // State variable to store the Hyperlane core contract address
    IHyperlaneCore public hyperlaneCore;

    // Event emitted when a message is sent
    event MessageSent(address indexed sender, uint256 indexed destinationChain, bytes message);

    // Event emitted when a message is received
    event MessageReceived(address indexed sender, bytes message);

    // Constructor to initialize the Hyperlane core contract
    constructor(address _hyperlaneCore) {
        require(_hyperlaneCore != address(0), "Invalid Hyperlane core address");
        hyperlaneCore = IHyperlaneCore(_hyperlaneCore);
    }

    // Function to send a message to another chain
    function sendMessage(uint256 destinationChain, bytes calldata message) external {
        require(destinationChain != 0, "Invalid destination chain");
        require(message.length > 0, "Message cannot be empty");

        // Sending the message through Hyperlane
        hyperlaneCore.sendMessage(destinationChain, message);

        emit MessageSent(msg.sender, destinationChain, message);
    }

    // Function to handle incoming messages from other chains
    function handleMessage(
        uint256 originChain,
        bytes calldata message
    ) external override {
        // Ensure the message is coming from the Hyperlane core
        require(msg.sender == address(hyperlaneCore), "Unauthorized sender");

        // Emit an event for the received message
        emit MessageReceived(msg.sender, message);

        // Here you can add logic to process the received message
        // For example, decoding the message and executing actions based on its content
    }

    // Function to withdraw any tokens accidentally sent to this contract
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token != address(0), "Invalid token address");

        // Transfer the specified amount of tokens to the caller
        // Assuming the token follows the ERC20 standard
        IERC20(token).transfer(msg.sender, amount);
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
