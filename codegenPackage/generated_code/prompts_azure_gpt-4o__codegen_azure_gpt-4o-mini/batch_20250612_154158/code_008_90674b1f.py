"""
Generated Code Metadata:
========================
Original URL: https://txtecontract.pages.dev
Prompt: Write a Solidity function that hashes a slice of memory using `keccak256`, as demonstrated in the `findNewContracts` function.
Generated: DETERMINISTIC_90674b1fc2e206ab
Batch ID: 20250612_154158
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

contract HashingExample {
    /**
     * @dev Hashes a slice of memory using keccak256.
     * @param data The bytes array to be hashed.
     * @param start The starting index of the slice.
     * @param length The length of the slice to hash.
     * @return The keccak256 hash of the specified slice.
     */
    function hashSlice(bytes memory data, uint256 start, uint256 length) public pure returns (bytes32) {
        // Validate input parameters
        require(start + length <= data.length, "Invalid slice parameters");

        // Create a memory slice of the specified length
        bytes memory slice = new bytes(length);
        for (uint256 i = 0; i < length; i++) {
            slice[i] = data[start + i];
        }

        // Return the keccak256 hash of the slice
        return keccak256(slice);
    }
}
```
