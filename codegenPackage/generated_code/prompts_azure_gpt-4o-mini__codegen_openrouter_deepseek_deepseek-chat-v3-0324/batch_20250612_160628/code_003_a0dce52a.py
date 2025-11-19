"""
Generated Code Metadata:
========================
Original URL: https://doptest-dop.web.app
Prompt: Generate a sample smart contract that utilizes the Data Ownership Protocol to enable user-controlled data sharing on Ethereum.
Generated: DETERMINISTIC_a0dce52a8f438a39
Batch ID: 20250612_160628
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
 * @title DataOwnershipProtocol
 * @dev A smart contract for user-controlled data sharing on Ethereum
 */
contract DataOwnershipProtocol {
    // Struct to represent a data record
    struct DataRecord {
        address owner;
        string dataHash; // IPFS or similar content-addressable hash
        uint256 creationTimestamp;
        mapping(address => bool) authorizedUsers;
    }

    // Mapping from record ID to DataRecord
    mapping(uint256 => DataRecord) private records;

    // Counter for record IDs
    uint256 private recordCounter;

    // Events
    event DataRecordCreated(
        uint256 indexed recordId,
        address indexed owner,
        string dataHash,
        uint256 timestamp
    );
    event AccessGranted(
        uint256 indexed recordId,
        address indexed owner,
        address indexed user
    );
    event AccessRevoked(
        uint256 indexed recordId,
        address indexed owner,
        address indexed user
    );
    event DataRecordDeleted(uint256 indexed recordId, address indexed owner);

    /**
     * @dev Creates a new data record
     * @param _dataHash The content-addressable hash of the data
     * @return recordId The ID of the newly created record
     */
    function createDataRecord(string memory _dataHash)
        external
        returns (uint256 recordId)
    {
        require(bytes(_dataHash).length > 0, "Data hash cannot be empty");

        recordId = recordCounter++;
        DataRecord storage newRecord = records[recordId];
        newRecord.owner = msg.sender;
        newRecord.dataHash = _dataHash;
        newRecord.creationTimestamp = block.timestamp;

        emit DataRecordCreated(
            recordId,
            msg.sender,
            _dataHash,
            block.timestamp
        );
        return recordId;
    }

    /**
     * @dev Grants access to a data record to another user
     * @param _recordId The ID of the record
     * @param _user The address of the user to grant access to
     */
    function grantAccess(uint256 _recordId, address _user) external {
        require(_recordExists(_recordId), "Record does not exist");
        require(
            records[_recordId].owner == msg.sender,
            "Only owner can grant access"
        );
        require(_user != address(0), "Invalid user address");
        require(
            !records[_recordId].authorizedUsers[_user],
            "User already has access"
        );

        records[_recordId].authorizedUsers[_user] = true;
        emit AccessGranted(_recordId, msg.sender, _user);
    }

    /**
     * @dev Revokes access to a data record from a user
     * @param _recordId The ID of the record
     * @param _user The address of the user to revoke access from
     */
    function revokeAccess(uint256 _recordId, address _user) external {
        require(_recordExists(_recordId), "Record does not exist");
        require(
            records[_recordId].owner == msg.sender,
            "Only owner can revoke access"
        );
        require(
            records[_recordId].authorizedUsers[_user],
            "User does not have access"
        );

        records[_recordId].authorizedUsers[_user] = false;
        emit AccessRevoked(_recordId, msg.sender, _user);
    }

    /**
     * @dev Deletes a data record (only owner can delete)
     * @param _recordId The ID of the record to delete
     */
    function deleteDataRecord(uint256 _recordId) external {
        require(_recordExists(_recordId), "Record does not exist");
        require(
            records[_recordId].owner == msg.sender,
            "Only owner can delete record"
        );

        delete records[_recordId];
        emit DataRecordDeleted(_recordId, msg.sender);
    }

    /**
     * @dev Checks if a user has access to a data record
     * @param _recordId The ID of the record
     * @param _user The address of the user to check
     * @return True if the user has access, false otherwise
     */
    function hasAccess(uint256 _recordId, address _user)
        external
        view
        returns (bool)
    {
        require(_recordExists(_recordId), "Record does not exist");
        return records[_recordId].authorizedUsers[_user] ||
            records[_recordId].owner == _user;
    }

    /**
     * @dev Gets the details of a data record
     * @param _recordId The ID of the record
     * @return owner The address of the record owner
     * @return dataHash The content-addressable hash of the data
     * @return creationTimestamp The timestamp when the record was created
     */
    function getDataRecord(uint256 _recordId)
        external
        view
        returns (
            address owner,
            string memory dataHash,
            uint256 creationTimestamp
        )
    {
        require(_recordExists(_recordId), "Record does not exist");
        DataRecord storage record = records[_recordId];
        return (record.owner, record.dataHash, record.creationTimestamp);
    }

    /**
     * @dev Internal function to check if a record exists
     * @param _recordId The ID of the record to check
     * @return True if the record exists, false otherwise
     */
    function _recordExists(uint256 _recordId) internal view returns (bool) {
        return records[_recordId].owner != address(0);
    }
}
```
