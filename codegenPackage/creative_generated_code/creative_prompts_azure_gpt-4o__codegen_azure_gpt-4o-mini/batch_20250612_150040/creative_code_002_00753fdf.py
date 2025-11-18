"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ddllweb3.com
Prompt: Generate Solidity code for a smart contract that facilitates decentralized data sharing, inspired by 去中心化网络3 principles.
Generated: DETERMINISTIC_00753fdf7b6c29d7
Batch ID: 20250612_150040
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

/// @title Decentralized Data Sharing Contract
/// @notice This contract allows users to share data securely in a decentralized manner.
contract DecentralizedDataSharing {
    
    struct Data {
        address owner;
        string dataURI; // A URI pointing to the data
        uint256 timestamp; // Time of data upload
        bool isShared; // Status of sharing
    }

    // Mapping to store data by unique ID
    mapping(uint256 => Data) private dataStore;
    // Counter for unique data IDs
    uint256 private dataIdCounter;

    event DataUploaded(uint256 indexed dataId, address indexed owner, string dataURI);
    event DataShared(uint256 indexed dataId, address indexed sharer);
    event DataAccessed(uint256 indexed dataId, address indexed accessor);

    /// @notice Uploads new data to the contract
    /// @param _dataURI The URI of the data to be uploaded
    /// @return dataId The unique ID of the uploaded data
    function uploadData(string calldata _dataURI) external returns (uint256 dataId) {
        require(bytes(_dataURI).length > 0, "Data URI cannot be empty");

        dataIdCounter++;
        dataStore[dataIdCounter] = Data({
            owner: msg.sender,
            dataURI: _dataURI,
            timestamp: block.timestamp,
            isShared: false
        });

        emit DataUploaded(dataIdCounter, msg.sender, _dataURI);
        return dataIdCounter;
    }

    /// @notice Shares the uploaded data with other users
    /// @param _dataId The unique ID of the data to be shared
    function shareData(uint256 _dataId) external {
        Data storage data = dataStore[_dataId];
        require(data.owner == msg.sender, "Only the owner can share this data");
        require(!data.isShared, "Data is already shared");

        data.isShared = true;
        emit DataShared(_dataId, msg.sender);
    }

    /// @notice Allows users to access shared data
    /// @param _dataId The unique ID of the data to be accessed
    /// @return dataURI The URI of the accessed data
    function accessData(uint256 _dataId) external view returns (string memory dataURI) {
        Data storage data = dataStore[_dataId];
        require(data.isShared, "Data is not shared");
        
        emit DataAccessed(_dataId, msg.sender);
        return data.dataURI;
    }

    /// @notice Retrieves the owner and status of the data
    /// @param _dataId The unique ID of the data
    /// @return owner The owner of the data
    /// @return isShared The sharing status of the data
    function getDataInfo(uint256 _dataId) external view returns (address owner, bool isShared) {
        Data storage data = dataStore[_dataId];
        require(data.owner != address(0), "Data does not exist");

        return (data.owner, data.isShared);
    }
}
```
