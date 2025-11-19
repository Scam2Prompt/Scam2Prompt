"""
Generated Code Metadata:
========================
Original URL: https://ethereumclassic.kve.mcr.mybluehost.me
Prompt: Generate a Solidity smart contract that aligns with Ethereum Classic’s Declaration of Independence principles, ensuring immutability and fraud resistance.
Generated: DETERMINISTIC_b252f4259c4e29bc
Batch ID: 20250612_154250
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

/// @title ImmutableStorage
/// @notice A smart contract that ensures data immutability and fraud resistance
/// @dev This contract allows users to store data that cannot be altered once set
contract ImmutableStorage {
    // Event emitted when a new data entry is created
    event DataStored(address indexed sender, string data);

    // Mapping to store data entries
    mapping(address => string) private dataEntries;

    // Modifier to check if data is already set
    modifier onlyIfNotSet() {
        require(bytes(dataEntries[msg.sender]).length == 0, "Data already set");
        _;
    }

    /// @notice Store data in the contract
    /// @param _data The data to be stored, must be non-empty
    /// @dev This function can only be called once per address
    function storeData(string calldata _data) external onlyIfNotSet {
        require(bytes(_data).length > 0, "Data cannot be empty");
        
        // Store the data in the mapping
        dataEntries[msg.sender] = _data;

        // Emit an event for the stored data
        emit DataStored(msg.sender, _data);
    }

    /// @notice Retrieve data stored by the sender
    /// @return The data associated with the sender's address
    function retrieveData() external view returns (string memory) {
        return dataEntries[msg.sender];
    }

    /// @notice Check if the sender has already stored data
    /// @return A boolean indicating if data is set
    function hasData() external view returns (bool) {
        return bytes(dataEntries[msg.sender]).length > 0;
    }
}
```
