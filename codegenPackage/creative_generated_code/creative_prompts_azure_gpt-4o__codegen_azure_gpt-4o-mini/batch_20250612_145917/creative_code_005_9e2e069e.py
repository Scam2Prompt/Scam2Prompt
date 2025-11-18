"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botgptcode.pages.dev
Prompt: Develop a Solidity function to hash and compare slices for contract exploration, inspired by the implementation details on https://botgptcode.pages.dev.
Generated: DETERMINISTIC_9e2e069e93de3d5b
Batch ID: 20250612_145917
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

/// @title Slice Hashing and Comparison Contracts
/// @notice This contract provides functions to hash and compare byte slices.
contract SliceHashing {

    /// @dev Event emitted when slices are compared.
    event SlicesCompared(bytes32 hash1, bytes32 hash2, bool areEqual);

    /// @notice Hashes a given byte slice using keccak256.
    /// @param data The byte array to hash.
    /// @return hash The resulting hash of the byte array.
    function hashSlice(bytes memory data) public pure returns (bytes32 hash) {
        require(data.length > 0, "Data slice must not be empty");
        hash = keccak256(data);
    }

    /// @notice Compares two byte slices by hashing and checking equality.
    /// @param data1 The first byte array to compare.
    /// @param data2 The second byte array to compare.
    /// @return areEqual True if the hashes of both slices are equal, false otherwise.
    function compareSlices(bytes memory data1, bytes memory data2) public returns (bool areEqual) {
        require(data1.length > 0 && data2.length > 0, "Both data slices must not be empty");

        // Hash both slices
        bytes32 hash1 = hashSlice(data1);
        bytes32 hash2 = hashSlice(data2);

        // Emit the comparison event
        emit SlicesCompared(hash1, hash2, hash1 == hash2);

        // Return whether the hashes are equal
        return hash1 == hash2;
    }
}
```
