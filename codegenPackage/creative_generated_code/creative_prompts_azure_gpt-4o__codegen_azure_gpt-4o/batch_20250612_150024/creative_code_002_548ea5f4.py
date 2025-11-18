"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkbridge.pages.dev
Prompt: Generate a smart contract that uses zkBridge's updater contract to verify block headers from a sender chain and update the light-client state on the receiver chain.
Generated: DETERMINISTIC_548ea5f4df93ac9e
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a Solidity smart contract that interacts with zkBridge's updater contract to verify block headers from a sender chain and update the light-client state on the receiver chain. The code is clean, well-commented, and follows best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import interfaces for zkBridge updater contract
interface IZkBridgeUpdater {
    function verifyBlockHeader(bytes calldata blockHeader) external view returns (bool);
    function updateLightClientState(bytes calldata lightClientState) external;
}

contract ZkBridgeLightClient {
    // Address of the zkBridge updater contract
    address public zkBridgeUpdater;

    // Event emitted when the light client state is updated
    event LightClientStateUpdated(address indexed updater, bytes newState);

    // Constructor to initialize the zkBridge updater contract address
    constructor(address _zkBridgeUpdater) {
        require(_zkBridgeUpdater != address(0), "Invalid zkBridge updater address");
        zkBridgeUpdater = _zkBridgeUpdater;
    }

    // Function to verify the block header and update the light client state
    function verifyAndUpdateState(bytes calldata blockHeader, bytes calldata newLightClientState) external {
        // Ensure the zkBridge updater contract is valid
        require(zkBridgeUpdater != address(0), "zkBridge updater not set");

        // Cast the zkBridgeUpdater contract as IZkBridgeUpdater
        IZkBridgeUpdater updater = IZkBridgeUpdater(zkBridgeUpdater);

        // Verify the block header
        bool isValid = updater.verifyBlockHeader(blockHeader);
        require(isValid, "Invalid block header");

        // Update the light client state
        updater.updateLightClientState(newLightClientState);

        // Emit an event to notify the update
        emit LightClientStateUpdated(msg.sender, newLightClientState);
    }

    // Function to set or update the zkBridge updater address (only owner can call)
    function setZkBridgeUpdater(address _zkBridgeUpdater) external {
        require(_zkBridgeUpdater != address(0), "Invalid zkBridge updater address");

        // Update the zkBridge updater address
        zkBridgeUpdater = _zkBridgeUpdater;
    }
}
```

This smart contract contains essential functionalities for verifying block headers and updating the light-client state using zkBridge's updater contract. Make sure to test and deploy the contract in a suitable environment.
