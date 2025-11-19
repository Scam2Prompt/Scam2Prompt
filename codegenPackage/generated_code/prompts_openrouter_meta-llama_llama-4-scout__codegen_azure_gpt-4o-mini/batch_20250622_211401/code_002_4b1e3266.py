"""
Generated Code Metadata:
========================
Original URL: https://qieufjfksjsjj.pages.dev
Prompt: "Design a smart contract for a decentralized application that requires secure and transparent data storage solutions, incorporating end-to-end encryption and multi-factor authentication."
Generated: DETERMINISTIC_4b1e3266fb268362
Batch ID: 20250622_211401
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/SignatureChecker.sol";

contract SecureDataStorage is Ownable {
    using ECDSA for bytes32;

    // Struct to hold encrypted data and its metadata
    struct EncryptedData {
        bytes32 dataHash; // Hash of the encrypted data
        address uploader;  // Address of the data uploader
        uint256 timestamp; // Timestamp of data upload
    }

    // Mapping to store encrypted data by ID
    mapping(uint256 => EncryptedData) private dataStorage;

    // Event emitted when new data is uploaded
    event DataUploaded(uint256 indexed dataId, address indexed uploader, bytes32 dataHash);

    // Modifier to check if the data ID exists
    modifier dataExists(uint256 dataId) {
        require(dataStorage[dataId].uploader != address(0), "Data does not exist");
        _;
    }

    // Function to upload encrypted data
    function uploadData(uint256 dataId, bytes32 dataHash) external onlyOwner {
        require(dataStorage[dataId].uploader == address(0), "Data ID already exists");

        // Store the encrypted data
        dataStorage[dataId] = EncryptedData({
            dataHash: dataHash,
            uploader: msg.sender,
            timestamp: block.timestamp
        });

        emit DataUploaded(dataId, msg.sender, dataHash);
    }

    // Function to retrieve encrypted data hash
    function getDataHash(uint256 dataId) external view dataExists(dataId) returns (bytes32) {
        return dataStorage[dataId].dataHash;
    }

    // Function to verify data authenticity using signature
    function verifyData(uint256 dataId, bytes32 dataHash, bytes memory signature) external view dataExists(dataId) returns (bool) {
        // Recreate the message hash
        bytes32 messageHash = keccak256(abi.encodePacked(dataId, dataHash));
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        
        // Check if the signer is the uploader
        return signer == dataStorage[dataId].uploader;
    }

    // Function to delete data (only owner can delete)
    function deleteData(uint256 dataId) external onlyOwner dataExists(dataId) {
        delete dataStorage[dataId];
    }
}
```
