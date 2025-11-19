"""
Generated Code Metadata:
========================
Original URL: https://metisdap.pages.dev
Prompt: Write a Solidity contract that utilizes Metis's affordable on-chain storage for storing and retrieving data securely.
Generated: DETERMINISTIC_a4ccad745b750701
Batch ID: 20250612_152526
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

// Importing the Metis storage interface
import "@metis.io/metis-storage/contracts/IMetisStorage.sol";

contract SecureDataStorage {
    // Instance of the Metis storage contract
    IMetisStorage private metisStorage;

    // Event emitted when data is stored
    event DataStored(address indexed user, string key, string value);

    // Event emitted when data is retrieved
    event DataRetrieved(address indexed user, string key, string value);

    // Constructor to initialize the Metis storage contract
    constructor(address _metisStorageAddress) {
        require(_metisStorageAddress != address(0), "Invalid Metis storage address");
        metisStorage = IMetisStorage(_metisStorageAddress);
    }

    // Function to store data securely
    function storeData(string memory key, string memory value) public {
        require(bytes(key).length > 0, "Key cannot be empty");
        require(bytes(value).length > 0, "Value cannot be empty");

        // Storing data in Metis storage
        metisStorage.set(key, value);

        // Emitting event after successful storage
        emit DataStored(msg.sender, key, value);
    }

    // Function to retrieve data securely
    function retrieveData(string memory key) public returns (string memory) {
        require(bytes(key).length > 0, "Key cannot be empty");

        // Retrieving data from Metis storage
        string memory value = metisStorage.get(key);
        require(bytes(value).length > 0, "No data found for the given key");

        // Emitting event after successful retrieval
        emit DataRetrieved(msg.sender, key, value);

        return value;
    }
}
```
