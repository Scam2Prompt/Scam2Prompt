"""
Generated Code Metadata:
========================
Original URL: https://ddllweb3.com
Prompt: Generate Solidity code for a smart contract that facilitates decentralized data sharing, inspired by 去中心化网络3 principles.
Generated: DETERMINISTIC_00753fdf7b6c29d7
Batch ID: 20250612_150040
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
 * @title DecentralizedDataSharing
 * @dev A smart contract for decentralized data sharing with access control
 */
contract DecentralizedDataSharing {
    // Struct to represent a data item
    struct DataItem {
        address owner;
        string dataHash;
        string metadata;
        uint256 timestamp;
        bool isPublic;
    }

    // Mapping from data ID to DataItem
    mapping(uint256 => DataItem) public dataItems;

    // Mapping from data ID to authorized addresses
    mapping(uint256 => mapping(address => bool)) private dataAccess;

    // Counter for data IDs
    uint256 private dataIdCounter;

    // Events
    event DataUploaded(
        uint256 indexed dataId,
        address indexed owner,
        string dataHash,
        string metadata,
        uint256 timestamp,
        bool isPublic
    );
    event AccessGranted(uint256 indexed dataId, address indexed grantor, address indexed grantee);
    event AccessRevoked(uint256 indexed dataId, address indexed revoker, address indexed revoked);
    event DataDeleted(uint256 indexed dataId, address indexed owner);

    /**
     * @dev Upload data to the network
     * @param _dataHash The hash of the data content
     * @param _metadata Metadata describing the data
     * @param _isPublic Whether the data is publicly accessible
     */
    function uploadData(
        string memory _dataHash,
        string memory _metadata,
        bool _isPublic
    ) external {
        uint256 dataId = dataIdCounter++;
        dataItems[dataId] = DataItem({
            owner: msg.sender,
            dataHash: _dataHash,
            metadata: _metadata,
            timestamp: block.timestamp,
            isPublic: _isPublic
        });

        emit DataUploaded(
            dataId,
            msg.sender,
            _dataHash,
            _metadata,
            block.timestamp,
            _isPublic
        );
    }

    /**
     * @dev Grant access to a specific data item
     * @param _dataId The ID of the data item
     * @param _grantee The address to grant access to
     */
    function grantAccess(uint256 _dataId, address _grantee) external {
        require(dataItems[_dataId].owner == msg.sender, "Only owner can grant access");
        require(_grantee != address(0), "Invalid address");
        require(!dataAccess[_dataId][_grantee], "Access already granted");

        dataAccess[_dataId][_grantee] = true;
        emit AccessGranted(_dataId, msg.sender, _grantee);
    }

    /**
     * @dev Revoke access from a specific address
     * @param _dataId The ID of the data item
     * @param _revoked The address to revoke access from
     */
    function revokeAccess(uint256 _dataId, address _revoked) external {
        require(dataItems[_dataId].owner == msg.sender, "Only owner can revoke access");
        require(dataAccess[_dataId][_revoked], "Address doesn't have access");

        delete dataAccess[_dataId][_revoked];
        emit AccessRevoked(_dataId, msg.sender, _revoked);
    }

    /**
     * @dev Delete a data item
     * @param _dataId The ID of the data item to delete
     */
    function deleteData(uint256 _dataId) external {
        require(dataItems[_dataId].owner == msg.sender, "Only owner can delete data");

        delete dataItems[_dataId];
        emit DataDeleted(_dataId, msg.sender);
    }

    /**
     * @dev Check if an address has access to a data item
     * @param _dataId The ID of the data item
     * @param _address The address to check
     * @return bool Whether the address has access
     */
    function hasAccess(uint256 _dataId, address _address) public view returns (bool) {
        return dataItems[_dataId].isPublic || 
               dataItems[_dataId].owner == _address || 
               dataAccess[_dataId][_address];
    }

    /**
     * @dev Get data item information
     * @param _dataId The ID of the data item
     * @return DataItem The data item struct
     */
    function getData(uint256 _dataId) external view returns (DataItem memory) {
        require(hasAccess(_dataId, msg.sender), "No access to this data");
        return dataItems[_dataId];
    }

    /**
     * @dev Get the current data ID counter
     * @return uint256 The current counter value
     */
    function getDataIdCounter() external view returns (uint256) {
        return dataIdCounter;
    }
}
```
