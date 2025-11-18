"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shardeumorgio.pages.dev
Prompt: Write a Solidity smart contract that utilizes Shardeum's EVM-based layer 1 blockchain features for deploying a decentralized application (dApp) with low gas fees and linear scalability.
Generated: DETERMINISTIC_fb3bbcae8a0845d5
Batch ID: 20250612_153401
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
 * @title ShardeumDApp
 * @dev A simple decentralized application (dApp) deployed on Shardeum's EVM-based layer 1 blockchain.
 * @notice This contract demonstrates basic low gas usage and scalability for storing and retrieving data.
 */
contract ShardeumDApp {
    // Mapping to store key-value pairs
    mapping(string => string) private dataStore;

    // Event emitted when data is set
    event DataStored(string indexed key, string value);

    // Modifier to check for valid input
    modifier validInput(string memory input) {
        require(bytes(input).length > 0, "Input cannot be empty");
        _;
    }

    /**
     * @dev Stores a value associated with a key in the contract.
     * @param key The key to identify the stored data.
     * @param value The value to be stored.
     */
    function setData(string memory key, string memory value)
        public
        validInput(key)
        validInput(value)
    {
        dataStore[key] = value;
        emit DataStored(key, value); // Emit event for transparency
    }

    /**
     * @dev Retrieves a value associated with a key.
     * @param key The key to identify the stored data.
     * @return The value associated with the given key.
     */
    function getData(string memory key) public view validInput(key) returns (string memory) {
        string memory value = dataStore[key];
        require(bytes(value).length > 0, "No data found for the given key"); // Error handling for nonexistent data
        return value;
    }

    /**
     * @dev Deletes a key-value pair from the contract.
     * @param key The key to identify the data to be deleted.
     */
    function deleteData(string memory key) public validInput(key) {
        require(bytes(dataStore[key]).length > 0, "No data exists for the given key");
        delete dataStore[key];
    }
}
```
