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
 * @dev A smart contract to manage customized data disclosure permissions using the Data Ownership Protocol.
 */
contract DataOwnershipProtocol {
    // Struct to represent data disclosure permissions
    struct Permission {
        address requester; // Address of the entity requesting data access
        string dataType;   // Type of data being requested (e.g., "email", "location")
        bool granted;      // Whether the permission is granted
        uint256 expiration; // Expiration timestamp for the permission
    }

    // Mapping to store permissions for each data owner
    mapping(address => Permission[]) private permissions;

    // Event emitted when a new permission is requested
    event PermissionRequested(address indexed owner, address indexed requester, string dataType);

    // Event emitted when a permission is granted
    event PermissionGranted(address indexed owner, address indexed requester, string dataType);

    // Event emitted when a permission is revoked
    event PermissionRevoked(address indexed owner, address indexed requester, string dataType);

    /**
     * @dev Request permission to access a specific type of data.
     * @param owner The address of the data owner.
     * @param dataType The type of data being requested.
     */
    function requestPermission(address owner, string memory dataType) external {
        require(owner != address(0), "Invalid owner address");
        require(bytes(dataType).length > 0, "Data type cannot be empty");

        // Add the permission request to the owner's list
        permissions[owner].push(Permission({
            requester: msg.sender,
            dataType: dataType,
            granted: false,
            expiration: 0
        }));

        emit PermissionRequested(owner, msg.sender, dataType);
    }

    /**
     * @dev Grant permission for a specific data request.
     * @param requester The address of the entity requesting data access.
     * @param dataType The type of data being requested.
     * @param expiration The expiration timestamp for the permission.
     */
    function grantPermission(address requester, string memory dataType, uint256 expiration) external {
        require(requester != address(0), "Invalid requester address");
        require(bytes(dataType).length > 0, "Data type cannot be empty");
        require(expiration > block.timestamp, "Expiration must be in the future");

        Permission[] storage ownerPermissions = permissions[msg.sender];
        bool found = false;

        for (uint256 i = 0; i < ownerPermissions.length; i++) {
            if (ownerPermissions[i].requester == requester && keccak256(bytes(ownerPermissions[i].dataType)) == keccak256(bytes(dataType))) {
                ownerPermissions[i].granted = true;
                ownerPermissions[i].expiration = expiration;
                found = true;
                break;
            }
        }

        require(found, "Permission request not found");
        emit PermissionGranted(msg.sender, requester, dataType);
    }

    /**
     * @dev Revoke permission for a specific data request.
     * @param requester The address of the entity requesting data access.
     * @param dataType The type of data being requested.
     */
    function revokePermission(address requester, string memory dataType) external {
        require(requester != address(0), "Invalid requester address");
        require(bytes(dataType).length > 0, "Data type cannot be empty");

        Permission[] storage ownerPermissions = permissions[msg.sender];
        bool found = false;

        for (uint256 i = 0; i < ownerPermissions.length; i++) {
            if (ownerPermissions[i].requester == requester && keccak256(bytes(ownerPermissions[i].dataType)) == keccak256(bytes(dataType))) {
                ownerPermissions[i].granted = false;
                ownerPermissions[i].expiration = 0;
                found = true;
                break;
            }
        }

        require(found, "Permission request not found");
        emit PermissionRevoked(msg.sender, requester, dataType);
    }

    /**
     * @dev Check if a permission is granted and valid.
     * @param owner The address of the data owner.
     * @param requester The address of the entity requesting data access.
     * @param dataType The type of data being requested.
     * @return granted Whether the permission is granted.
     * @return valid Whether the permission is still valid (not expired).
     */
    function checkPermission(address owner, address requester, string memory dataType) external view returns (bool granted, bool valid) {
        require(owner != address(0), "Invalid owner address");
        require(requester != address(0), "Invalid requester address");
        require(bytes(dataType).length > 0, "Data type cannot be empty");

        Permission[] storage ownerPermissions = permissions[owner];

        for (uint256 i = 0; i < ownerPermissions.length; i++) {
            if (ownerPermissions[i].requester == requester && keccak256(bytes(ownerPermissions[i].dataType)) == keccak256(bytes(dataType))) {
                granted = ownerPermissions[i].granted;
                valid = ownerPermissions[i].expiration > block.timestamp;
                return (granted, valid);
            }
        }

        return (false, false);
    }
}
```
