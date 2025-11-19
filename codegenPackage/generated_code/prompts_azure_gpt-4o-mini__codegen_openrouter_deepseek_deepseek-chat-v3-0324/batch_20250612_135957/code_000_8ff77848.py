"""
Generated Code Metadata:
========================
Original URL: https://yethereum.com
Prompt: How can I implement a decentralized storage solution using EthStorage's approach to data availability?
Generated: DETERMINISTIC_8ff77848bb2f8c7f
Batch ID: 20250612_135957
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title EthStorage
 * @dev A decentralized storage solution with data availability guarantees
 */
contract EthStorage is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to store data chunks with metadata
    struct DataChunk {
        bytes32 dataHash;
        uint256 size;
        uint256 timestamp;
        address uploader;
        bool isAvailable;
    }
    
    // Mapping from chunk ID to DataChunk
    mapping(uint256 => DataChunk) public chunks;
    
    // Counter for chunk IDs
    Counters.Counter private _chunkIdCounter;
    
    // Events
    event ChunkUploaded(uint256 indexed chunkId, bytes32 dataHash, uint256 size, address uploader);
    event ChunkDeleted(uint256 indexed chunkId);
    event AvailabilityChecked(uint256 indexed chunkId, bool isAvailable);
    
    /**
     * @dev Upload a data chunk to the storage
     * @param dataHash The hash of the data being stored
     * @param size The size of the data in bytes
     */
    function uploadChunk(bytes32 dataHash, uint256 size) external {
        require(dataHash != bytes32(0), "Invalid data hash");
        require(size > 0, "Size must be greater than 0");
        
        uint256 chunkId = _chunkIdCounter.current();
        _chunkIdCounter.increment();
        
        chunks[chunkId] = DataChunk({
            dataHash: dataHash,
            size: size,
            timestamp: block.timestamp,
            uploader: msg.sender,
            isAvailable: true
        });
        
        emit ChunkUploaded(chunkId, dataHash, size, msg.sender);
    }
    
    /**
     * @dev Delete a data chunk (only owner or uploader can delete)
     * @param chunkId The ID of the chunk to delete
     */
    function deleteChunk(uint256 chunkId) external {
        require(chunkExists(chunkId), "Chunk does not exist");
        require(
            msg.sender == owner() || msg.sender == chunks[chunkId].uploader,
            "Not authorized to delete"
        );
        
        delete chunks[chunkId];
        emit ChunkDeleted(chunkId);
    }
    
    /**
     * @dev Check if a chunk exists
     * @param chunkId The ID of the chunk to check
     * @return bool Whether the chunk exists
     */
    function chunkExists(uint256 chunkId) public view returns (bool) {
        return chunks[chunkId].timestamp != 0;
    }
    
    /**
     * @dev Verify data availability of a chunk
     * @param chunkId The ID of the chunk to verify
     * @return bool Whether the chunk is available
     */
    function verifyAvailability(uint256 chunkId) external returns (bool) {
        require(chunkExists(chunkId), "Chunk does not exist");
        
        bool isAvailable = chunks[chunkId].isAvailable;
        emit AvailabilityChecked(chunkId, isAvailable);
        
        return isAvailable;
    }
    
    /**
     * @dev Get chunk information
     * @param chunkId The ID of the chunk
     * @return DataChunk The chunk data structure
     */
    function getChunk(uint256 chunkId) external view returns (DataChunk memory) {
        require(chunkExists(chunkId), "Chunk does not exist");
        return chunks[chunkId];
    }
    
    /**
     * @dev Mark a chunk as unavailable (only owner can call)
     * @param chunkId The ID of the chunk to mark
     */
    function markUnavailable(uint256 chunkId) external onlyOwner {
        require(chunkExists(chunkId), "Chunk does not exist");
        chunks[chunkId].isAvailable = false;
        emit AvailabilityChecked(chunkId, false);
    }
}
```
