"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://txtecontract.pages.dev
Prompt: Write a Solidity function that hashes a slice of memory using `keccak256`, as demonstrated in the `findNewContracts` function.
Generated: DETERMINISTIC_90674b1fc2e206ab
Batch ID: 20250612_154158
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

contract HashingExample {

    /**
     * @dev Hashes a slice of memory using the keccak256 hash function.
     * @param data The input data slice to be hashed.
     * @param offset The starting index of the slice.
     * @param length The length of the slice to be hashed.
     * @return The keccak256 hash of the specified slice of memory.
     */
    function hashSlice(bytes memory data, uint256 offset, uint256 length) public pure returns (bytes32) {
        // Ensure that the offset and length are within the bounds of the data
        require(offset + length <= data.length, "Invalid slice parameters");

        // Create a new bytes memory variable to hold the slice
        bytes memory slice = new bytes(length);
        
        // Copy the relevant slice of data into the new variable
        for (uint256 i = 0; i < length; i++) {
            slice[i] = data[offset + i];
        }

        // Return the keccak256 hash of the slice
        return keccak256(slice);
    }
}
```
