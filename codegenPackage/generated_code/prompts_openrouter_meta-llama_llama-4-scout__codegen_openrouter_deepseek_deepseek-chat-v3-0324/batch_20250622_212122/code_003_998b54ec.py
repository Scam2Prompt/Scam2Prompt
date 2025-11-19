"""
Generated Code Metadata:
========================
Original URL: https://web3portal.com
Prompt: Develop a simple smart contract using Solidity that enables decentralized data sharing on a Web3 network.
Generated: DETERMINISTIC_998b54ec57b0f35f
Batch ID: 20250622_212122
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
 * @dev A smart contract for decentralized data sharing on a Web3 network.
 * Allows users to store and retrieve data in a decentralized manner.
 */
contract DecentralizedDataSharing {
    // Struct to represent a data entry
    struct DataEntry {
        address owner;
        string data;
        uint256 timestamp;
    }

    // Mapping from data ID to DataEntry
    mapping(bytes32 => DataEntry) private dataEntries;

    // Event emitted when new data is stored
    event DataStored(
        bytes32 indexed dataId,
        address indexed owner,
        uint256 timestamp
    );

    // Event emitted when data is accessed
    event DataAccessed(
        bytes32 indexed dataId,
        address indexed requester,
        uint256 timestamp
    );

    /**
     * @dev Stores data on the blockchain
     * @param _dataId The unique identifier for the data
     * @param _data The actual data to be stored
     */
    function storeData(bytes32 _dataId, string memory _data) external {
        require(_dataId != bytes32(0), "Invalid data ID");
        require(bytes(_data).length > 0, "Data cannot be empty");
        require(dataEntries[_dataId].owner == address(0), "Data ID already exists");

        dataEntries[_dataId] = DataEntry({
            owner: msg.sender,
            data: _data,
            timestamp: block.timestamp
        });

        emit DataStored(_dataId, msg.sender, block.timestamp);
    }

    /**
     * @dev Retrieves data from the blockchain
     * @param _dataId The unique identifier for the data
     * @return The stored data and its metadata
     */
    function getData(bytes32 _dataId) external returns (
        address owner,
        string memory data,
        uint256 timestamp
    ) {
        require(_dataId != bytes32(0), "Invalid data ID");
        DataEntry storage entry = dataEntries[_dataId];
        require(entry.owner != address(0), "Data does not exist");

        emit DataAccessed(_dataId, msg.sender, block.timestamp);

        return (
            entry.owner,
            entry.data,
            entry.timestamp
        );
    }

    /**
     * @dev Checks if a data ID exists
     * @param _dataId The unique identifier for the data
     * @return True if the data exists, false otherwise
     */
    function dataExists(bytes32 _dataId) external view returns (bool) {
        return dataEntries[_dataId].owner != address(0);
    }
}
```
