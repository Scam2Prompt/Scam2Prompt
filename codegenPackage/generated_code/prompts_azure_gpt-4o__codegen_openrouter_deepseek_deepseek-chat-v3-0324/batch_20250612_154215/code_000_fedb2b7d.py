"""
Generated Code Metadata:
========================
Original URL: https://ahsjdkkk.pages.dev
Prompt: Write a smart contract for a decentralized application (DApp) using Solidity that ensures censorship resistance and immutability, as described in the Chain Solution Center's decentralized architecture.
Generated: DETERMINISTIC_fedb2b7d97df0147
Batch ID: 20250612_154215
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
 * @title CensorshipResistantDApp
 * @dev A decentralized application contract ensuring censorship resistance and immutability
 */
contract CensorshipResistantDApp {
    // Struct to represent a data record
    struct Record {
        address creator;
        string content;
        uint256 timestamp;
        bool isDeleted;
    }

    // Mapping to store records by their unique IDs
    mapping(bytes32 => Record) private records;

    // Event emitted when a new record is created
    event RecordCreated(bytes32 indexed recordId, address indexed creator, string content, uint256 timestamp);

    // Event emitted when a record is marked as deleted
    event RecordDeleted(bytes32 indexed recordId, address indexed deleter);

    // Modifier to check if the record exists and isn't deleted
    modifier recordExistsAndActive(bytes32 recordId) {
        require(records[recordId].creator != address(0), "Record does not exist");
        require(!records[recordId].isDeleted, "Record is deleted");
        _;
    }

    /**
     * @dev Creates a new immutable record
     * @param content The content to be stored
     * @return recordId The unique ID of the created record
     */
    function createRecord(string memory content) external returns (bytes32) {
        require(bytes(content).length > 0, "Content cannot be empty");

        bytes32 recordId = keccak256(abi.encodePacked(msg.sender, content, block.timestamp));
        
        // Ensure the record doesn't already exist (extremely unlikely but possible)
        require(records[recordId].creator == address(0), "Record already exists");

        records[recordId] = Record({
            creator: msg.sender,
            content: content,
            timestamp: block.timestamp,
            isDeleted: false
        });

        emit RecordCreated(recordId, msg.sender, content, block.timestamp);
        return recordId;
    }

    /**
     * @dev Marks a record as deleted (only creator can do this)
     * @param recordId The ID of the record to mark as deleted
     */
    function deleteRecord(bytes32 recordId) external recordExistsAndActive(recordId) {
        require(records[recordId].creator == msg.sender, "Only creator can delete record");
        
        records[recordId].isDeleted = true;
        emit RecordDeleted(recordId, msg.sender);
    }

    /**
     * @dev Retrieves a record's content
     * @param recordId The ID of the record to retrieve
     * @return content The content of the record
     * @return creator The address of the creator
     * @return timestamp The creation timestamp
     * @return isDeleted Whether the record is marked as deleted
     */
    function getRecord(bytes32 recordId) external view returns (
        string memory content,
        address creator,
        uint256 timestamp,
        bool isDeleted
    ) {
        require(records[recordId].creator != address(0), "Record does not exist");
        
        Record storage record = records[recordId];
        return (
            record.content,
            record.creator,
            record.timestamp,
            record.isDeleted
        );
    }

    /**
     * @dev Checks if a record exists and is active (not deleted)
     * @param recordId The ID of the record to check
     * @return exists True if the record exists and is active
     */
    function isRecordActive(bytes32 recordId) external view returns (bool) {
        return records[recordId].creator != address(0) && !records[recordId].isDeleted;
    }
}
```
