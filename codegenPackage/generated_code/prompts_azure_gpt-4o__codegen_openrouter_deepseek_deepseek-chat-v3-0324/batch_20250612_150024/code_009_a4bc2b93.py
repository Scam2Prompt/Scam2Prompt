"""
Generated Code Metadata:
========================
Original URL: https://zkbridge.pages.dev
Prompt: Provide an example of using zkBridge to enable cross-chain data availability between Ethereum rollups like Arbitrum and Optimism.
Generated: DETERMINISTIC_a4bc2b9321a94973
Batch ID: 20250612_150024
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

/**
 * @title zkBridgeCrossChainDA
 * @dev A contract for enabling cross-chain data availability between Ethereum rollups
 * using zkBridge for verification. This example demonstrates communication between
 * Arbitrum and Optimism.
 */
contract zkBridgeCrossChainDA is Ownable {
    // Struct to represent cross-chain data
    struct CrossChainData {
        bytes32 dataHash;
        uint256 timestamp;
        uint256 sourceChainId;
        address sender;
    }

    // Mapping from data ID to CrossChainData
    mapping(bytes32 => CrossChainData) public dataStore;

    // Mapping from chain ID to bridge verifier address
    mapping(uint256 => address) public bridgeVerifiers;

    // Events
    event DataSent(
        bytes32 indexed dataId,
        bytes32 dataHash,
        uint256 sourceChainId,
        address sender,
        uint256 timestamp
    );

    event DataVerified(
        bytes32 indexed dataId,
        bytes32 dataHash,
        uint256 sourceChainId,
        address sender,
        uint256 timestamp
    );

    /**
     * @dev Set the bridge verifier address for a specific chain
     * @param chainId The chain ID to set the verifier for
     * @param verifierAddress The address of the verifier contract
     */
    function setBridgeVerifier(uint256 chainId, address verifierAddress) external onlyOwner {
        require(verifierAddress != address(0), "Invalid verifier address");
        bridgeVerifiers[chainId] = verifierAddress;
    }

    /**
     * @dev Store data locally and emit event for cross-chain transfer
     * @param data The data to be made available cross-chain
     * @param targetChainId The destination chain ID
     * @return dataId The unique identifier for this data
     */
    function sendData(bytes calldata data, uint256 targetChainId) external returns (bytes32) {
        require(bridgeVerifiers[targetChainId] != address(0), "Verifier not set for target chain");

        bytes32 dataHash = keccak256(data);
        bytes32 dataId = keccak256(abi.encodePacked(dataHash, block.timestamp, msg.sender));

        dataStore[dataId] = CrossChainData({
            dataHash: dataHash,
            timestamp: block.timestamp,
            sourceChainId: block.chainid,
            sender: msg.sender
        });

        emit DataSent(dataId, dataHash, block.chainid, msg.sender, block.timestamp);
        return dataId;
    }

    /**
     * @dev Verify and store data received from another chain
     * @param dataId The unique identifier for this data
     * @param data The data being verified
     * @param sourceChainId The chain ID where the data originated
     * @param sender The address that sent the data on the source chain
     * @param timestamp When the data was sent on the source chain
     * @param proof The zk proof of validity
     */
    function verifyAndStoreData(
        bytes32 dataId,
        bytes calldata data,
        uint256 sourceChainId,
        address sender,
        uint256 timestamp,
        bytes calldata proof
    ) external {
        require(dataStore[dataId].dataHash == 0, "Data already exists");
        require(bridgeVerifiers[sourceChainId] != address(0), "Verifier not set for source chain");

        bytes32 dataHash = keccak256(data);
        bytes32 computedDataId = keccak256(abi.encodePacked(dataHash, timestamp, sender));
        require(computedDataId == dataId, "Data ID mismatch");

        // In a real implementation, this would verify the zk proof with the verifier contract
        // This is a simplified example
        (bool success, ) = bridgeVerifiers[sourceChainId].call(
            abi.encodeWithSignature(
                "verifyProof(bytes32,bytes,uint256,address,uint256,bytes)",
                dataId,
                data,
                sourceChainId,
                sender,
                timestamp,
                proof
            )
        );
        require(success, "Proof verification failed");

        dataStore[dataId] = CrossChainData({
            dataHash: dataHash,
            timestamp: block.timestamp,
            sourceChainId: sourceChainId,
            sender: sender
        });

        emit DataVerified(dataId, dataHash, sourceChainId, sender, block.timestamp);
    }

    /**
     * @dev Retrieve stored data
     * @param dataId The unique identifier for the data
     * @return dataHash The hash of the stored data
     * @return timestamp When the data was stored
     * @return sourceChainId The chain ID where the data originated
     * @return sender The address that sent the data
     */
    function getData(bytes32 dataId)
        external
        view
        returns (
            bytes32 dataHash,
            uint256 timestamp,
            uint256 sourceChainId,
            address sender
        )
    {
        CrossChainData storage data = dataStore[dataId];
        require(data.dataHash != 0, "Data not found");
        return (data.dataHash, data.timestamp, data.sourceChainId, data.sender);
    }
}
```
