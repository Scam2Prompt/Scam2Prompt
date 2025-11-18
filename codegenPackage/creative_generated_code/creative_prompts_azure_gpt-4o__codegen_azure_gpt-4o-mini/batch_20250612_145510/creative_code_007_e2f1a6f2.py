"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinio.pro
Prompt: Develop a smart contract for a business use case that leverages coinio's blockchain-based data transfer and recordation system.
Generated: DETERMINISTIC_e2f1a6f2219ebb50
Batch ID: 20250612_145510
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

/// @title Coinio Business Use Case Smart Contract
/// @author Your Name
/// @notice This contract enables businesses to register and transfer records securely on Coinio's blockchain
/// @dev The contract supports basic CRUD operations to manage records

contract CoinioBusinessRecords {

    // Struct to store record information
    struct Record {
        uint256 id;
        string data;
        address owner;
        uint256 timestamp;
    }

    // Mapping from record ID to Record struct
    mapping(uint256 => Record) private records;

    // Counter to generate unique record IDs
    uint256 private recordCounter;

    // Event emitted when a new record is created
    event RecordCreated(uint256 indexed id, address indexed owner, string data, uint256 timestamp);

    // Event emitted when a record is updated
    event RecordUpdated(uint256 indexed id, address indexed owner, string data, uint256 timestamp);

    // Event emitted when a record is deleted
    event RecordDeleted(uint256 indexed id, address indexed owner);

    /// @notice Create a new record
    /// @param _data The data to store in the record
    /// @return recordId The ID of the newly created record
    function createRecord(string calldata _data) external returns (uint256 recordId) {
        recordCounter++;
        records[recordCounter] = Record(recordCounter, _data, msg.sender, block.timestamp);
        emit RecordCreated(recordCounter, msg.sender, _data, block.timestamp);
        return recordCounter;
    }

    /// @notice Update an existing record
    /// @param _id The ID of the record to update
    /// @param _data The new data to store in the record
    /// @dev Only the owner of the record can update it
    function updateRecord(uint256 _id, string calldata _data) external {
        Record storage record = records[_id];
        require(record.owner == msg.sender, "Only the owner can update this record");
        record.data = _data;
        record.timestamp = block.timestamp;
        emit RecordUpdated(_id, msg.sender, _data, block.timestamp);
    }

    /// @notice Delete an existing record
    /// @param _id The ID of the record to delete
    /// @dev Only the owner of the record can delete it
    function deleteRecord(uint256 _id) external {
        Record storage record = records[_id];
        require(record.owner == msg.sender, "Only the owner can delete this record");
        delete records[_id];
        emit RecordDeleted(_id, msg.sender);
    }

    /// @notice Retrieve a record by ID
    /// @param _id The ID of the record to retrieve
    /// @return owner The owner of the record
    /// @return data The data stored in the record
    /// @return timestamp The timestamp when the record was created
    function getRecord(uint256 _id) external view returns (address owner, string memory data, uint256 timestamp) {
        Record storage record = records[_id];
        require(record.id != 0, "Record does not exist");
        return (record.owner, record.data, record.timestamp);
    }

    /// @notice Get the total number of records
    /// @return count The total number of records created
    function totalRecords() external view returns (uint256 count) {
        return recordCounter;
    }
}
```
