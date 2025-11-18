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

interface IMetisStorage {
    function storeData(bytes32 key, string calldata data) external;
    function retrieveData(bytes32 key) external view returns (string memory);
}

/**
 * @title MetisStorageExample
 * @dev A contract to demonstrate secure storage and retrieval of data using Metis's affordable on-chain storage.
 */
contract MetisStorageExample {
    // Instance of MetisStorage interface
    IMetisStorage public metisStorage;

    // Event to emit when data is stored
    event DataStored(bytes32 indexed key, string data);

    // Event to emit when data is retrieved
    event DataRetrieved(bytes32 indexed key, string data);

    /**
     * @dev Constructor to set the Metis storage contract address.
     * @param _metisStorageAddress Address of the Metis storage contract.
     */
    constructor(address _metisStorageAddress) {
        require(_metisStorageAddress != address(0), "Invalid Metis storage address");
        metisStorage = IMetisStorage(_metisStorageAddress);
    }

    /**
     * @dev Store data in the Metis storage.
     * @param key The unique identifier for the data.
     * @param data The data to store.
     */
    function store(bytes32 key, string calldata data) external {
        require(bytes(data).length > 0, "Data cannot be empty");
        
        // Store data using Metis storage
        metisStorage.storeData(key, data);
        
        // Emit event on successful storage
        emit DataStored(key, data);
    }

    /**
     * @dev Retrieve data from the Metis storage.
     * @param key The unique identifier for the data.
     * @return The retrieved data as a string.
     */
    function retrieve(bytes32 key) external view returns (string memory) {
        string memory data = metisStorage.retrieveData(key);
        require(bytes(data).length > 0, "No data found for the given key");

        // Emit event on successful retrieval
        emit DataRetrieved(key, data);
        return data;
    }
}
```
