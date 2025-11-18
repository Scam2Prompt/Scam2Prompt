"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meties.pages.dev
Prompt: Provide an example of integrating on-chain storage using Metis's affordable storage solutions in a smart contract.
Generated: DETERMINISTIC_a8e715a450ee936c
Batch ID: 20250612_151636
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
 * @title MetisStorageExample
 * @dev Demonstrates how to integrate affordable on-chain storage using Metis.
 * Metis provides cost-effective storage solutions for smart contracts.
 */
contract MetisStorageExample {

    // Mapping to store data on-chain (key-value storage)
    mapping(bytes32 => string) private dataStorage;

    // Event emitted when data is stored successfully
    event DataStored(bytes32 indexed key, string value);

    // Event emitted when data is retrieved successfully
    event DataRetrieved(bytes32 indexed key, string value);

    /**
     * @dev Function to store data on-chain. 
     * Using Metis's cost-effective storage ensures affordable scalability.
     * @param key The unique identifier for the stored data.
     * @param value The data to be stored.
     */
    function storeData(bytes32 key, string memory value) external {
        // Store data in the mapping
        dataStorage[key] = value;

        // Emit event to notify successful storage
        emit DataStored(key, value);
    }

    /**
     * @dev Function to retrieve data stored on-chain.
     * @param key The unique identifier for the stored data.
     * @return value The data corresponding to the provided key.
     */
    function retrieveData(bytes32 key) external view returns (string memory value) {
        // Check if the key exists in the mapping
        require(bytes(dataStorage[key]).length > 0, "Data does not exist for the provided key");

        // Retrieve the value from the mapping
        value = dataStorage[key];

        // Emit event to notify successful retrieval
        emit DataRetrieved(key, value);

        return value;
    }

    /**
     * @dev Function to delete data stored on-chain (optional cleanup method).
     * @param key The unique identifier for the data to be deleted.
     */
    function deleteData(bytes32 key) external {
        // Check if the key exists in the mapping
        require(bytes(dataStorage[key]).length > 0, "Data does not exist for the provided key");

        // Delete the data from the mapping
        delete dataStorage[key];
    }

    /**
     * @dev Function to check if data exists for a given key.
     * @param key The unique identifier to check.
     * @return exists Boolean indicating whether data exists for the key.
     */
    function dataExists(bytes32 key) external view returns (bool exists) {
        exists = bytes(dataStorage[key]).length > 0;
        return exists;
    }
}
```
