"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-coinbase-com.kagiproxy.com
Prompt: What are the steps to build an onchain app using Base, and can you provide a code example for a simple application?
Generated: DETERMINISTIC_4ff29fb307358272
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a simple on-chain application using Base (an Ethereum Layer 2 network). This implementation is a basic Solidity smart contract that allows users to store and retrieve messages on-chain.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleStorage
 * @dev A basic smart contract for storing and retrieving messages on-chain.
 */
contract SimpleStorage {
    // State variable to store the message
    string private message;

    // Event emitted when the message is updated
    event MessageUpdated(address indexed updater, string newMessage);

    /**
     * @dev Constructor to initialize the contract with a default message.
     * @param _initialMessage The initial message to store.
     */
    constructor(string memory _initialMessage) {
        message = _initialMessage;
    }

    /**
     * @dev Function to update the stored message.
     * @param _newMessage The new message to store.
     */
    function updateMessage(string memory _newMessage) external {
        // Update the message
        message = _newMessage;

        // Emit an event to notify about the update
        emit MessageUpdated(msg.sender, _newMessage);
    }

    /**
     * @dev Function to retrieve the stored message.
     * @return The currently stored message.
     */
    function getMessage() external view returns (string memory) {
        return message;
    }
}
```

### Steps to deploy and interact with the application:

1. **Set up your development environment**:
   - Install Solidity development tools like Hardhat or Truffle.
   - Install dependencies (e.g., `npm install hardhat ethers`).

2. **Connect to Base network**:
   - Configure your development environment to use Base RPC endpoints.
   - Use the network parameters provided by Base.

3. **Compile the contract**:
   - Run `npx hardhat compile` to compile the Solidity code.

4. **Deploy the contract**:
   - Write a deployment script (e.g., in Hardhat).
   - Deploy the contract to Base using `npx hardhat run scripts/deploy.js --network base`.

5. **Interact with the contract**:
   - Use a frontend or scripts to call the `updateMessage` and `getMessage` functions.
   - Ensure the Base network is properly integrated into your frontend (e.g., using `ethers.js`).
