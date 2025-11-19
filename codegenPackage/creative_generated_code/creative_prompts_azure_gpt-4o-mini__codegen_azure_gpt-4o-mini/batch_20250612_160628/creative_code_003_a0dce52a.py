"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doptest-dop.web.app
Prompt: Generate a sample smart contract that utilizes the Data Ownership Protocol to enable user-controlled data sharing on Ethereum.
Generated: DETERMINISTIC_a0dce52a8f438a39
Batch ID: 20250612_160628
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

/// @title Data Ownership Protocol Smart Contract
/// @notice This contract enables user-controlled data sharing on Ethereum
/// @dev Implements basic functionality for data ownership and sharing

contract DataOwnership {
    // Struct to hold data associated with a user
    struct UserData {
        string dataHash; // Hash of the data for integrity
        address owner;    // Owner of the data
        bool isShared;    // Flag to indicate if the data is shared
    }

    // Mapping from data ID to UserData
    mapping(uint256 => UserData) private userDatas;
    
    // Event to notify data creation
    event DataCreated(uint256 indexed dataId, address indexed owner, string dataHash);
    
    // Event to notify data sharing
    event DataShared(uint256 indexed dataId, address indexed sharer);
    
    // Event to notify data unsharing
    event DataUnshared(uint256 indexed dataId, address indexed unsharer);

    // Modifier to check if the caller is the owner of the data
    modifier onlyOwner(uint256 dataId) {
        require(userDatas[dataId].owner == msg.sender, "Caller is not the data owner");
        _;
    }

    /// @notice Creates a new data entry
    /// @param dataId The unique identifier for the data
    /// @param dataHash The hash of the data content
    function createData(uint256 dataId, string memory dataHash) public {
        require(bytes(dataHash).length > 0, "Data hash cannot be empty");
        require(userDatas[dataId].owner == address(0), "Data ID already exists");

        // Create a new UserData entry
        userDatas[dataId] = UserData({
            dataHash: dataHash,
            owner: msg.sender,
            isShared: false
        });

        emit DataCreated(dataId, msg.sender, dataHash);
    }

    /// @notice Shares data with another address
    /// @param dataId The unique identifier for the data
    function shareData(uint256 dataId) public onlyOwner(dataId) {
        UserData storage userData = userDatas[dataId];

        // Mark the data as shared
        userData.isShared = true;
        
        emit DataShared(dataId, msg.sender);
    }

    /// @notice Unshares previously shared data
    /// @param dataId The unique identifier for the data
    function unshareData(uint256 dataId) public onlyOwner(dataId) {
        UserData storage userData = userDatas[dataId];

        // Mark the data as not shared
        userData.isShared = false;
        
        emit DataUnshared(dataId, msg.sender);
    }

    /// @notice Fetches details of a user's data
    /// @param dataId The unique identifier for the data
    /// @return dataHash The hash of the data
    /// @return owner The owner of the data
    /// @return isShared The sharing status of the data
    function getData(uint256 dataId) public view returns (string memory dataHash, address owner, bool isShared) {
        UserData memory userData = userDatas[dataId];
        require(userData.owner != address(0), "Data ID does not exist");

        return (userData.dataHash, userData.owner, userData.isShared);
    }
}
```
