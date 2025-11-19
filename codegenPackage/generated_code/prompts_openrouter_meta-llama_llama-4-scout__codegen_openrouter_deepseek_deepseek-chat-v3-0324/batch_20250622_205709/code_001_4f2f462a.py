"""
Generated Code Metadata:
========================
Original URL: https://ronin-cyberkongz.pages.dev
Prompt: Explain the concept of on-chain two-factor authentication and its implementation in the Guardian Contract, as used by CyberKongz.
Generated: DETERMINISTIC_4f2f462a570fbc0d
Batch ID: 20250622_205709
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
 * @title Guardian Contract
 * @dev Implements on-chain two-factor authentication for CyberKongz
 * This contract allows a primary wallet to designate a secondary "guardian" wallet
 * that must approve sensitive operations, adding an extra layer of security.
 */
contract Guardian {
    // Mapping from primary wallet to guardian wallet
    mapping(address => address) private _guardians;

    // Mapping to track pending operations requiring guardian approval
    mapping(bytes32 => bool) private _pendingOperations;

    // Events
    event GuardianSet(address indexed primary, address indexed guardian);
    event OperationRequested(bytes32 indexed operationHash, address indexed primary);
    event OperationApproved(bytes32 indexed operationHash, address indexed primary);
    event OperationCancelled(bytes32 indexed operationHash, address indexed primary);

    /**
     * @dev Sets or changes the guardian for the caller
     * @param guardian Address of the guardian wallet
     */
    function setGuardian(address guardian) external {
        require(guardian != address(0), "Guardian: zero address");
        require(guardian != msg.sender, "Guardian: cannot be self");

        _guardians[msg.sender] = guardian;
        emit GuardianSet(msg.sender, guardian);
    }

    /**
     * @dev Gets the guardian for a primary wallet
     * @param primary Address of the primary wallet
     * @return Address of the guardian wallet
     */
    function getGuardian(address primary) external view returns (address) {
        return _guardians[primary];
    }

    /**
     * @dev Initiates an operation requiring guardian approval
     * @param operationDetails Hash of the operation details
     * @return operationHash The unique identifier for this operation
     */
    function requestOperation(bytes32 operationDetails) external returns (bytes32) {
        require(_guardians[msg.sender] != address(0), "Guardian: no guardian set");

        bytes32 operationHash = keccak256(abi.encodePacked(msg.sender, operationDetails));
        _pendingOperations[operationHash] = true;

        emit OperationRequested(operationHash, msg.sender);
        return operationHash;
    }

    /**
     * @dev Approves a pending operation (callable by guardian only)
     * @param primary Address of the primary wallet
     * @param operationDetails Hash of the operation details
     */
    function approveOperation(address primary, bytes32 operationDetails) external {
        require(_guardians[primary] == msg.sender, "Guardian: caller is not guardian");

        bytes32 operationHash = keccak256(abi.encodePacked(primary, operationDetails));
        require(_pendingOperations[operationHash], "Guardian: operation not pending");

        delete _pendingOperations[operationHash];
        emit OperationApproved(operationHash, primary);
    }

    /**
     * @dev Cancels a pending operation (callable by primary only)
     * @param operationDetails Hash of the operation details
     */
    function cancelOperation(bytes32 operationDetails) external {
        bytes32 operationHash = keccak256(abi.encodePacked(msg.sender, operationDetails));
        require(_pendingOperations[operationHash], "Guardian: operation not pending");

        delete _pendingOperations[operationHash];
        emit OperationCancelled(operationHash, msg.sender);
    }

    /**
     * @dev Checks if an operation is pending approval
     * @param primary Address of the primary wallet
     * @param operationDetails Hash of the operation details
     * @return bool Whether the operation is pending
     */
    function isOperationPending(address primary, bytes32 operationDetails) external view returns (bool) {
        bytes32 operationHash = keccak256(abi.encodePacked(primary, operationDetails));
        return _pendingOperations[operationHash];
    }
}
```
