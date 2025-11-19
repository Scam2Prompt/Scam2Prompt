"""
Generated Code Metadata:
========================
Original URL: https://ethereumcv.io
Prompt: Design a smart contract on Ethereum Classic Vision (ETCV) that utilizes sharding for scalability and IPFS integration for decentralized file storage, and provide a Solidity code snippet for the contract.
Generated: DETERMINISTIC_4a1aedf84f2ba9a0
Batch ID: 20250622_205523
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

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ShardedStorageContract
 * @dev A smart contract for decentralized file storage with sharding support
 *      and IPFS integration on Ethereum Classic Vision (ETCV)
 */
contract ShardedStorageContract is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to represent a file shard
    struct FileShard {
        bytes32 shardHash;
        uint256 shardIndex;
        address uploader;
        uint256 timestamp;
    }
    
    // Struct to represent a complete file
    struct File {
        string ipfsCID; // IPFS Content Identifier for the complete file
        uint256 totalShards;
        bool isComplete;
        mapping(uint256 => FileShard) shards;
    }
    
    // Mapping from file ID to File struct
    mapping(bytes32 => File) private files;
    
    // Counter for generating unique file IDs
    Counters.Counter private _fileIdCounter;
    
    // Events
    event FileCreated(bytes32 indexed fileId, string ipfsCID);
    event ShardUploaded(bytes32 indexed fileId, uint256 shardIndex, bytes32 shardHash);
    event FileCompleted(bytes32 indexed fileId);
    
    /**
     * @dev Creates a new file entry with the given IPFS CID
     * @param ipfsCID The IPFS Content Identifier for the complete file
     * @return fileId The generated file ID
     */
    function createFile(string memory ipfsCID) public returns (bytes32) {
        _fileIdCounter.increment();
        bytes32 fileId = keccak256(abi.encodePacked(_fileIdCounter.current(), block.timestamp, msg.sender));
        
        File storage newFile = files[fileId];
        newFile.ipfsCID = ipfsCID;
        newFile.totalShards = 0;
        newFile.isComplete = false;
        
        emit FileCreated(fileId, ipfsCID);
        return fileId;
    }
    
    /**
     * @dev Uploads a shard for a specific file
     * @param fileId The ID of the file to upload the shard to
     * @param shardHash The hash of the shard data
     * @param shardIndex The index of the shard
     */
    function uploadShard(bytes32 fileId, bytes32 shardHash, uint256 shardIndex) public {
        require(files[fileId].totalShards > 0 || shardIndex == 0, "Invalid first shard index");
        
        File storage file = files[fileId];
        
        // Ensure shard doesn't already exist
        require(file.shards[shardIndex].shardHash == bytes32(0), "Shard already exists");
        
        // Create and store the shard
        file.shards[shardIndex] = FileShard({
            shardHash: shardHash,
            shardIndex: shardIndex,
            uploader: msg.sender,
            timestamp: block.timestamp
        });
        
        file.totalShards++;
        
        emit ShardUploaded(fileId, shardIndex, shardHash);
    }
    
    /**
     * @dev Marks a file as complete when all shards are uploaded
     * @param fileId The ID of the file to mark as complete
     */
    function completeFile(bytes32 fileId) public {
        File storage file = files[fileId];
        require(!file.isComplete, "File already complete");
        
        // In a production environment, you would verify all shards are present
        file.isComplete = true;
        
        emit FileCompleted(fileId);
    }
    
    /**
     * @dev Retrieves file information
     * @param fileId The ID of the file to retrieve
     * @return ipfsCID The IPFS CID of the file
     * @return totalShards Total number of shards
     * @return isComplete Whether the file is complete
     */
    function getFileInfo(bytes32 fileId) public view returns (
        string memory ipfsCID,
        uint256 totalShards,
        bool isComplete
    ) {
        File storage file = files[fileId];
        return (file.ipfsCID, file.totalShards, file.isComplete);
    }
    
    /**
     * @dev Retrieves shard information
     * @param fileId The ID of the file
     * @param shardIndex The index of the shard to retrieve
     * @return shardHash The hash of the shard
     * @return uploader The address that uploaded the shard
     * @return timestamp The timestamp of the upload
     */
    function getShardInfo(bytes32 fileId, uint256 shardIndex) public view returns (
        bytes32 shardHash,
        address uploader,
        uint256 timestamp
    ) {
        FileShard storage shard = files[fileId].shards[shardIndex];
        require(shard.shardHash != bytes32(0), "Shard does not exist");
        return (shard.shardHash, shard.uploader, shard.timestamp);
    }
}
```
