"""
Generated Code Metadata:
========================
Original URL: https://dop-io.web.app
Prompt: Generate an example of a smart contract that utilizes the Data Ownership Protocol's features for customized data disclosure permissions.
Generated: DETERMINISTIC_e66b57ac57883865
Batch ID: 20250612_140250
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

/// @title Data Ownership Protocol Smart Contract
/// @notice This contract allows users to manage data ownership and disclosure permissions
/// @dev This contract utilizes a mapping to store data ownership and permissions

contract DataOwnership {
    // Struct to hold data information
    struct DataInfo {
        address owner; // Address of the data owner
        string dataHash; // Hash of the data for integrity
        mapping(address => bool) permissions; // Mapping to track who has access
    }

    // Mapping to store data by its ID
    mapping(uint256 => DataInfo) private dataRecords;

    // Event emitted when data is created
    event DataCreated(uint256 indexed dataId, address indexed owner, string dataHash);

    // Event emitted when permissions are updated
    event PermissionsUpdated(uint256 indexed dataId, address indexed accessor, bool granted);

    // Modifier to check if the caller is the owner of the data
    modifier onlyOwner(uint256 dataId) {
        require(msg.sender == dataRecords[dataId].owner, "Not the data owner");
        _;
    }

    /// @notice Create new data record
    /// @param dataId Unique identifier for the data
    /// @param dataHash Hash of the data
    function createData(uint256 dataId, string memory dataHash) public {
        require(dataRecords[dataId].owner == address(0), "Data ID already exists");

        // Initialize the data record
        DataInfo storage newData = dataRecords[dataId];
        newData.owner = msg.sender;
        newData.dataHash = dataHash;

        emit DataCreated(dataId, msg.sender, dataHash);
    }

    /// @notice Grant access to another address for the specified data
    /// @param dataId Unique identifier for the data
    /// @param accessor Address to grant access
    function grantAccess(uint256 dataId, address accessor) public onlyOwner(dataId) {
        dataRecords[dataId].permissions[accessor] = true;
        emit PermissionsUpdated(dataId, accessor, true);
    }

    /// @notice Revoke access from another address for the specified data
    /// @param dataId Unique identifier for the data
    /// @param accessor Address to revoke access
    function revokeAccess(uint256 dataId, address accessor) public onlyOwner(dataId) {
        dataRecords[dataId].permissions[accessor] = false;
        emit PermissionsUpdated(dataId, accessor, false);
    }

    /// @notice Check if an address has access to the specified data
    /// @param dataId Unique identifier for the data
    /// @param accessor Address to check access for
    /// @return bool indicating whether the accessor has permission
    function hasAccess(uint256 dataId, address accessor) public view returns (bool) {
        return dataRecords[dataId].permissions[accessor];
    }

    /// @notice Retrieve the owner of the specified data
    /// @param dataId Unique identifier for the data
    /// @return address of the data owner
    function getOwner(uint256 dataId) public view returns (address) {
        return dataRecords[dataId].owner;
    }

    /// @notice Retrieve the data hash for the specified data
    /// @param dataId Unique identifier for the data
    /// @return string representing the data hash
    function getDataHash(uint256 dataId) public view returns (string memory) {
        return dataRecords[dataId].dataHash;
    }
}
```
