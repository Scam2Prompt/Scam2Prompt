"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-multiswiftdapp.pages.dev
Prompt: Generate code that integrates the Multichain "anyCall" feature into a smart contract to enable cross-chain communication. Include an example use case.
Generated: DETERMINISTIC_ceefc99d67fc70ce
Batch ID: 20250612_145933
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

// Importing Multichain's anyCall interface
import "@anycall/anycall.sol";

/**
 * @title CrossChainCommunicator
 * @dev This smart contract demonstrates the integration of Multichain's anyCall feature
 * to enable cross-chain communication.
 */
contract CrossChainCommunicator is AnyCall {
    // Event emitted when a cross-chain message is sent
    event MessageSent(uint256 indexed targetChain, address indexed target, string message);

    // Event emitted when a cross-chain message is received
    event MessageReceived(address indexed sender, string message);

    /**
     * @dev Sends a message to a specified target address on a target chain.
     * @param targetChain The ID of the target chain.
     * @param target The address to send the message to on the target chain.
     * @param message The message to send.
     */
    function sendMessage(uint256 targetChain, address target, string memory message) external {
        // Validate input parameters
        require(targetChain != 0, "Invalid target chain");
        require(target != address(0), "Invalid target address");
        require(bytes(message).length > 0, "Message cannot be empty");

        // Prepare the data to be sent
        bytes memory data = abi.encodeWithSignature("receiveMessage(address,string)", msg.sender, message);

        // Call the anyCall function to send the message
        anyCall(targetChain, target, data);

        // Emit event for tracking
        emit MessageSent(targetChain, target, message);
    }

    /**
     * @dev This function is called when a message is received from another chain.
     * @param sender The address that sent the message.
     * @param message The message received.
     */
    function receiveMessage(address sender, string memory message) external {
        // Ensure that only the anyCall contract can call this function
        require(msg.sender == address(this), "Unauthorized sender");

        // Emit the event for tracking
        emit MessageReceived(sender, message);
    }
}
```

### Example Use Case:

1. **Sending a Message:**
   - A user calls `sendMessage` on the `CrossChainCommunicator` contract with the target chain ID, target address, and message.
   
2. **Receiving a Message:**
   - The `receiveMessage` function is automatically invoked on the target chain's corresponding contract, allowing the message to be processed or acted upon as needed.

### Important Notes:
- Ensure that the contract is deployed on both chains where you want to send and receive messages.
- Integrate proper access control mechanisms if necessary, depending on the use case.
