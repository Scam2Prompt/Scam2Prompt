"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra.naynacodes.com
Prompt: Write a code snippet that demonstrates how to set up the updater contract for the zkBridge on the receiver chain.
Generated: DETERMINISTIC_8a9be0d1e2a3cf8c
Batch ID: 20250612_155153
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

/**
 * @title zkBridgeUpdaterContract
 * @dev This contract sets up the updater contract for the zkBridge on the receiver chain
 *      and ensures proper interaction with the bridge protocol.
 */
contract zkBridgeUpdaterContract {
    // Address of the zkBridge contract on the receiver chain
    address public zkBridgeContract;

    // Address of the updater responsible for relaying messages
    address public updater;

    // Event to log the updater address update
    event UpdaterSet(address indexed oldUpdater, address indexed newUpdater);

    /**
     * @notice Sets the initial zkBridge contract address and updater address during deployment.
     * @param _zkBridgeContract - The address of the zkBridge contract on the receiver chain.
     * @param _updater - The address of the updater.
     */
    constructor(address _zkBridgeContract, address _updater) {
        require(_zkBridgeContract != address(0), "Invalid zkBridge contract address");
        require(_updater != address(0), "Invalid updater address");

        zkBridgeContract = _zkBridgeContract;
        updater = _updater;
    }

    /**
     * @notice Updates the updater address for the zkBridge.
     * @param _newUpdater - The new updater address.
     * @dev Only the current updater can set a new updater address.
     */
    function setUpdater(address _newUpdater) external {
        require(msg.sender == updater, "Caller is not the current updater");
        require(_newUpdater != address(0), "Invalid new updater address");

        emit UpdaterSet(updater, _newUpdater);

        updater = _newUpdater;
    }

    /**
     * @notice Retrieves the current zkBridge contract address.
     * @return The address of the zkBridge contract.
     */
    function getZkBridgeContract() external view returns (address) {
        return zkBridgeContract;
    }

    /**
     * @notice Retrieves the current updater address.
     * @return The address of the current updater.
     */
    function getUpdater() external view returns (address) {
        return updater;
    }
}
```
