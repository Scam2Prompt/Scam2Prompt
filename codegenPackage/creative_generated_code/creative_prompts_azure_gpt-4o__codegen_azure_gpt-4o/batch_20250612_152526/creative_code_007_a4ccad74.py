"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metisdap.pages.dev
Prompt: Write a Solidity contract that utilizes Metis's affordable on-chain storage for storing and retrieving data securely.
Generated: DETERMINISTIC_a4ccad745b750701
Batch ID: 20250612_152526
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

/**
 * @title MetisStorageContract
 * @dev A Solidity smart contract for securely storing and retrieving data using Metis's on-chain storage.
 */
contract MetisStorageContract {
    // Mapping to store data securely against an owner's address
    mapping(address => string) private storedData;

    // Event emitted when data is successfully stored
    event DataStored(address indexed owner, string data);

    // Event emitted when data is successfully retrieved
    event DataRetrieved(address indexed owner, string data);

    /**
     * @notice Store data securely in the contract.
     * @param data The string data to be stored.
     */
    function storeData(string calldata data) external {
        // Check that the input data is not empty
        require(bytes(data).length > 0, "Data cannot be empty");

        // Store the data securely against the sender's address
        storedData[msg.sender] = data;

        // Emit the DataStored event to log the storage action
        emit DataStored(msg.sender, data);
    }

    /**
     * @notice Retrieve the stored data for the message sender.
     * @return The string data stored by the sender.
     */
    function retrieveData() external view returns (string memory) {
        // Check if data exists for the sender's address
        require(bytes(storedData[msg.sender]).length > 0, "No data found for the sender");

        // Retrieve stored data for the sender's address
        string memory data = storedData[msg.sender];

        // Emit the DataRetrieved event to log the retrieval action
        emit DataRetrieved(msg.sender, data);

        return data;
    }

    /**
     * @notice Retrieve the stored data for a specific address.
     * @param owner The address whose data needs to be retrieved.
     * @return The string data stored by the owner.
     */
    function retrieveDataForAddress(address owner) external view returns (string memory) {
        // Check if data exists for the given owner's address
        require(bytes(storedData[owner]).length > 0, "No data found for the specified address");

        // Retrieve stored data for the given owner's address
        return storedData[owner];
    }

    /**
     * @notice Clear stored data for the message sender.
     */
    function clearData() external {
        // Check if data exists for the sender's address
        require(bytes(storedData[msg.sender]).length > 0, "No data found to clear");

        // Clear the stored data for the sender's address
        delete storedData[msg.sender];
    }
}
```
