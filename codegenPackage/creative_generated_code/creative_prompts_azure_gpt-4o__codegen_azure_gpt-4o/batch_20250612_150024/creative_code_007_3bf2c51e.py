"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkbridge.pages.dev
Prompt: Explain how to use zkBridge's 2-layer recursive proof system to minimize on-chain verification gas costs for cross-chain applications.
Generated: DETERMINISTIC_3bf2c51e7d42d616
Batch ID: 20250612_150024
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
 * @title zkBridgeRecursiveProof
 * @dev Demonstrates usage of zkBridge's 2-layer recursive proof system
 * to minimize on-chain verification gas costs for cross-chain applications.
 * This contract assumes zkBridge's recursive proof API availability.
 */

interface IZkBridge {
    /**
     * @notice Verify a single proof layer (Layer 1 proof).
     * @param proof The proof data.
     * @return bool Whether the proof is valid.
     */
    function verifyProof(bytes calldata proof) external view returns (bool);

    /**
     * @notice Verify a recursive proof (Layer 2 proof).
     * @param recursiveProof The recursive proof data.
     * @return bool Whether the recursive proof is valid.
     */
    function verifyRecursiveProof(bytes calldata recursiveProof) external view returns (bool);
}

contract ZkBridgeManager {
    // Address of the zkBridge contract
    address public zkBridgeContract;

    // Event emitted after successful cross-chain validation
    event CrossChainValidated(address indexed sender, uint256 indexed chainId, bytes data);

    /**
     * @dev Constructor initializes the zkBridge contract address.
     * @param _zkBridgeContract Address of the zkBridge contract.
     */
    constructor(address _zkBridgeContract) {
        require(_zkBridgeContract != address(0), "Invalid zkBridge address");
        zkBridgeContract = _zkBridgeContract;
    }

    /**
     * @dev Verify and validate a cross-chain message using zkBridge's 2-layer recursive proof system.
     * @param layer1Proof Layer 1 proof for initial validation.
     * @param layer2Proof Layer 2 recursive proof for the compact validation.
     * @param chainId The origin chain ID of the message.
     * @param message The cross-chain message data.
     */
    function validateCrossChainMessage(
        bytes calldata layer1Proof,
        bytes calldata layer2Proof,
        uint256 chainId,
        bytes calldata message
    ) external {
        // Step 1: Verify Layer 1 proof
        bool layer1Valid = IZkBridge(zkBridgeContract).verifyProof(layer1Proof);
        require(layer1Valid, "Invalid Layer 1 proof");

        // Step 2: Verify Layer 2 recursive proof
        bool layer2Valid = IZkBridge(zkBridgeContract).verifyRecursiveProof(layer2Proof);
        require(layer2Valid, "Invalid Layer 2 recursive proof");

        // Step 3: Emit validation event
        emit CrossChainValidated(msg.sender, chainId, message);
    }

    /**
     * @dev Update the zkBridge contract address.
     * @param _zkBridgeContract New address of the zkBridge contract.
     */
    function updateZkBridgeContract(address _zkBridgeContract) external {
        require(_zkBridgeContract != address(0), "Invalid zkBridge address");
        zkBridgeContract = _zkBridgeContract;
    }
}
```
