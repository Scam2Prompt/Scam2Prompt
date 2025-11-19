"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcdaily.info
Prompt: Construct a Solidity smart contract that utilizes Ethereum's infrastructure for decentralized applications, reflecting the use cases highlighted in the article.
Generated: DETERMINISTIC_a3f39fd86d9cff5b
Batch ID: 20250612_163156
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
 * @title Decentralized Application Smart Contract
 * @dev A sample Solidity smart contract leveraging Ethereum's infrastructure for decentralized applications (DAPs).
 * This contract allows users to store and retrieve key-value pairs and tracks ownership of the data.
 */
contract DecentralizedApp {

    // Mapping to store data with user addresses as keys
    mapping(address => mapping(string => string)) private dataStore;

    // Event emitted when new data is stored
    event DataStored(address indexed user, string key, string value);

    // Event emitted when data is retrieved
    event DataRetrieved(address indexed user, string key, string value);

    /**
     * @dev Function to store data in the contract.
     * @param key The key under which data will be stored.
     * @param value The value to be stored.
     */
    function storeData(string memory key, string memory value) public {
        require(bytes(key).length > 0, "Key cannot be empty");
        require(bytes(value).length > 0, "Value cannot be empty");

        // Store the key-value pair for the caller
        dataStore[msg.sender][key] = value;

        // Emit the event to notify data storage
        emit DataStored(msg.sender, key, value);
    }

    /**
     * @dev Function to retrieve data stored in the contract.
     * @param key The key whose value needs to be retrieved.
     * @return value The value associated with the given key.
     */
    function retrieveData(string memory key) public view returns (string memory value) {
        require(bytes(key).length > 0, "Key cannot be empty");

        value = dataStore[msg.sender][key];
        require(bytes(value).length > 0, "No value found for the given key");

        // Emit the event to notify data retrieval
        emit DataRetrieved(msg.sender, key, value);
    }

    /**
     * @dev Function to check if data exists for a given key.
     * @param key The key to check for existence.
     * @return exists Boolean indicating whether data exists for the given key.
     */
    function dataExists(string memory key) public view returns (bool exists) {
        require(bytes(key).length > 0, "Key cannot be empty");

        exists = bytes(dataStore[msg.sender][key]).length > 0;
    }
}
```
