"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: Generate an example of a smart contract that utilizes the Data Ownership Protocol's features for customized data disclosure permissions.
Generated: DETERMINISTIC_e66b57ac57883865
Batch ID: 20250612_140250
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

// Smart contract to manage data ownership and disclosure permissions
contract DataOwnership is Ownable {
    // Struct to represent a data record
    struct DataRecord {
        address owner;
        string data; // Encrypted or hashed data
        mapping(address => bool) permittedAddresses;
    }

    // Mapping from a unique identifier to DataRecord
    mapping(uint256 => DataRecord) private dataRecords;
    uint256 private nextId;

    // Event emitted when data is added
    event DataAdded(uint256 indexed id, address indexed owner);

    // Event emitted when permission is given
    event PermissionGranted(uint256 indexed id, address indexed grantee);

    // Event emitted when permission is revoked
    event PermissionRevoked(uint256 indexed id, address indexed revokee);

    // Function to add new data to the contract
    function addData(string calldata _data) external onlyOwner returns (uint256) {
        uint256 recordId = nextId++;
        DataRecord storage newRecord = dataRecords[recordId];
        newRecord.owner = msg.sender;
        newRecord.data = _data;

        emit DataAdded(recordId, msg.sender);
        return recordId;
    }

    // Function to grant permission to access data
    function grantPermission(uint256 _id, address _grantee) external {
        DataRecord storage record = dataRecords[_id];

        require(msg.sender == record.owner, "Only the owner can grant permission");
        require(record.permittedAddresses[_grantee] == false, "Permission already granted");

        record.permittedAddresses[_grantee] = true;

        emit PermissionGranted(_id, _grantee);
    }

    // Function to revoke permission to access data
    function revokePermission(uint256 _id, address _grantee) external {
        DataRecord storage record = dataRecords[_id];

        require(msg.sender == record.owner, "Only the owner can revoke permission");
        require(record.permittedAddresses[_grantee] == true, "No permission granted to revoke");

        record.permittedAddresses[_grantee] = false;

        emit PermissionRevoked(_id, _grantee);
    }

    // Function to retrieve data if the caller has permission
    function getData(uint256 _id) external view returns (string memory) {
        DataRecord storage record = dataRecords[_id];

        require(msg.sender == record.owner || record.permittedAddresses[msg.sender], "Access denied");

        return record.data;
    }

    // Function to check if an address has permission to access data
    function hasPermission(uint256 _id, address _address) external view returns (bool) {
        DataRecord storage record = dataRecords[_id];
        return record.permittedAddresses[_address];
    }
}
```
