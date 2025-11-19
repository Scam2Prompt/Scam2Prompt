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
 * @title Decentralized Data Sharing Contract
 * @dev This contract allows users to share data in a decentralized manner.
 * Users can upload data, retrieve data, and delete their own data.
 */
contract DecentralizedDataSharing {
    // Struct to store data details
    struct Data {
        string content; // The actual data content
        address owner;  // Address of the data owner
    }

    // Mapping to store data by unique ID
    mapping(uint256 => Data) private dataStore;

    // Counter to generate unique IDs for data
    uint256 private dataCounter;

    // Event emitted when data is uploaded
    event DataUploaded(uint256 indexed dataId, address indexed owner, string content);

    // Event emitted when data is deleted
    event DataDeleted(uint256 indexed dataId, address indexed owner);

    /**
     * @dev Upload data to the contract.
     * @param _content The content of the data to be uploaded.
     * @return The unique ID of the uploaded data.
     */
    function uploadData(string memory _content) external returns (uint256) {
        require(bytes(_content).length > 0, "Data content cannot be empty");

        // Increment the data counter to generate a new ID
        dataCounter++;

        // Store the data in the mapping
        dataStore[dataCounter] = Data({
            content: _content,
            owner: msg.sender
        });

        // Emit the DataUploaded event
        emit DataUploaded(dataCounter, msg.sender, _content);

        // Return the unique ID of the uploaded data
        return dataCounter;
    }

    /**
     * @dev Retrieve data by its unique ID.
     * @param _dataId The ID of the data to retrieve.
     * @return The content of the data and the owner's address.
     */
    function getData(uint256 _dataId) external view returns (string memory, address) {
        require(_dataId > 0 && _dataId <= dataCounter, "Invalid data ID");

        Data memory data = dataStore[_dataId];
        return (data.content, data.owner);
    }

    /**
     * @dev Delete data by its unique ID. Only the owner of the data can delete it.
     * @param _dataId The ID of the data to delete.
     */
    function deleteData(uint256 _dataId) external {
        require(_dataId > 0 && _dataId <= dataCounter, "Invalid data ID");

        Data memory data = dataStore[_dataId];
        require(data.owner == msg.sender, "Only the owner can delete this data");

        // Delete the data from the mapping
        delete dataStore[_dataId];

        // Emit the DataDeleted event
        emit DataDeleted(_dataId, msg.sender);
    }

    /**
     * @dev Get the total number of data entries stored in the contract.
     * @return The total number of data entries.
     */
    function getTotalDataCount() external view returns (uint256) {
        return dataCounter;
    }
}
```
