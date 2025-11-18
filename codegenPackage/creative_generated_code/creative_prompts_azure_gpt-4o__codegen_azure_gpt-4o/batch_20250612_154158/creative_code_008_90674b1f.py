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

contract MemoryHasher {
    /**
     * @dev Hashes a slice of memory using keccak256.
     * @param data The complete memory array to hash from.
     * @param offset The starting point (in bytes) within the memory array.
     * @param length The length (in bytes) of the slice to hash.
     * @return The keccak256 hash of the specified memory slice.
     */
    function hashMemorySlice(
        bytes memory data,
        uint256 offset,
        uint256 length
    ) public pure returns (bytes32) {
        // Validate inputs to prevent out-of-bounds memory access
        require(offset + length <= data.length, "Invalid memory slice");

        bytes32 result;

        // Perform the hashing operation
        assembly {
            // Calculate the memory pointer for the start of the slice
            let start := add(data, add(0x20, offset))
            result := keccak256(start, length)
        }

        return result;
    }
}
```
