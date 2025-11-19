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

/**
 * @title DataOwnershipProtocol
 * @dev A smart contract demonstrating customized data disclosure permissions
 * using the Data Ownership Protocol principles.
 */
contract DataOwnershipProtocol {
    // Struct to represent a data record
    struct DataRecord {
        address owner;
        string dataHash;
        uint256 timestamp;
        bool isActive;
    }

    // Struct to represent disclosure permission
    struct Permission {
        address requester;
        uint256 dataId;
        uint256 expiryTimestamp;
        bool isApproved;
    }

    // Mapping of data records by ID
    mapping(uint256 => DataRecord) public dataRecords;

    // Mapping of permissions by permission ID
    mapping(uint256 => Permission) public permissions;

    // Mapping of owner to their data IDs
    mapping(address => uint256[]) public ownerDataIds;

    // Mapping of requester to their permission IDs
    mapping(address => uint256[]) public requesterPermissionIds;

    // Counter for data records
    uint256 public dataRecordCounter;

    // Counter for permissions
    uint256 public permissionCounter;

    // Events
    event DataRecordCreated(uint256 indexed dataId, address indexed owner, string dataHash);
    event PermissionRequested(uint256 indexed permissionId, address indexed requester, uint256 indexed dataId);
    event PermissionApproved(uint256 indexed permissionId, bool isApproved);
    event DataDisclosed(uint256 indexed dataId, address indexed requester, string dataHash);

    /**
     * @dev Create a new data record
     * @param _dataHash The hash of the data being stored
     */
    function createDataRecord(string memory _dataHash) external {
        uint256 dataId = dataRecordCounter++;
        dataRecords[dataId] = DataRecord({
            owner: msg.sender,
            dataHash: _dataHash,
            timestamp: block.timestamp,
            isActive: true
        });
        ownerDataIds[msg.sender].push(dataId);
        emit DataRecordCreated(dataId, msg.sender, _dataHash);
    }

    /**
     * @dev Request permission to access data
     * @param _dataId The ID of the data record to request access to
     * @param _expiryTimestamp When the permission should expire
     */
    function requestPermission(uint256 _dataId, uint256 _expiryTimestamp) external {
        require(dataRecords[_dataId].isActive, "Data record does not exist or is inactive");
        require(dataRecords[_dataId].owner != msg.sender, "Cannot request permission for own data");

        uint256 permissionId = permissionCounter++;
        permissions[permissionId] = Permission({
            requester: msg.sender,
            dataId: _dataId,
            expiryTimestamp: _expiryTimestamp,
            isApproved: false
        });
        requesterPermissionIds[msg.sender].push(permissionId);
        emit PermissionRequested(permissionId, msg.sender, _dataId);
    }

    /**
     * @dev Approve or reject a permission request
     * @param _permissionId The ID of the permission to approve/reject
     * @param _isApproved Whether to approve the request
     */
    function approvePermission(uint256 _permissionId, bool _isApproved) external {
        Permission storage permission = permissions[_permissionId];
        require(permission.requester != address(0), "Permission does not exist");
        require(dataRecords[permission.dataId].owner == msg.sender, "Only data owner can approve permissions");
        require(!permission.isApproved, "Permission already approved");

        permission.isApproved = _isApproved;
        emit PermissionApproved(_permissionId, _isApproved);
    }

    /**
     * @dev Access data if permission is granted
     * @param _dataId The ID of the data to access
     */
    function accessData(uint256 _dataId) external view returns (string memory) {
        require(dataRecords[_dataId].isActive, "Data record does not exist or is inactive");

        // Check if requester is the owner
        if (dataRecords[_dataId].owner == msg.sender) {
            return dataRecords[_dataId].dataHash;
        }

        // Check for valid permission
        bool hasPermission = false;
        uint256[] memory permissionIds = requesterPermissionIds[msg.sender];
        
        for (uint256 i = 0; i < permissionIds.length; i++) {
            Permission storage permission = permissions[permissionIds[i]];
            if (permission.dataId == _dataId && 
                permission.isApproved && 
                permission.expiryTimestamp >= block.timestamp) {
                hasPermission = true;
                break;
            }
        }

        require(hasPermission, "No valid permission to access this data");
        return dataRecords[_dataId].dataHash;
    }

    /**
     * @dev Deactivate a data record (soft delete)
     * @param _dataId The ID of the data to deactivate
     */
    function deactivateDataRecord(uint256 _dataId) external {
        require(dataRecords[_dataId].owner == msg.sender, "Only data owner can deactivate");
        require(dataRecords[_dataId].isActive, "Data record already inactive");
        dataRecords[_dataId].isActive = false;
    }

    /**
     * @dev Get data IDs owned by an address
     * @param _owner The address to query
     */
    function getDataIdsByOwner(address _owner) external view returns (uint256[] memory) {
        return ownerDataIds[_owner];
    }

    /**
     * @dev Get permission IDs requested by an address
     * @param _requester The address to query
     */
    function getPermissionIdsByRequester(address _requester) external view returns (uint256[] memory) {
        return requesterPermissionIds[_requester];
    }
}
```
