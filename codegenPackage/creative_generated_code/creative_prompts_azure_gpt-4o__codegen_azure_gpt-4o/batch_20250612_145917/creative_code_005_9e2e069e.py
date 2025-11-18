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

/**
 * @title HashAndCompare
 * @dev A contract to hash and compare slices of strings.
 */
contract HashAndCompare {

    /**
     * @dev Hashes a given slice of a string and compares it to a provided hash value.
     * @param input The original string to slice and hash.
     * @param start The starting index of the slice.
     * @param length The length of the slice.
     * @param hashToCompare The hash to compare the result against.
     * @return isMatch Returns true if the hash of the slice matches hashToCompare, false otherwise.
     */
    function hashAndCompareSlice(
        string memory input, 
        uint256 start, 
        uint256 length, 
        bytes32 hashToCompare
    ) 
        public 
        pure 
        returns (bool isMatch) 
    {
        // Validate input parameters
        require(start < bytes(input).length, "Start index out of bounds");
        require(start + length <= bytes(input).length, "Slice exceeds string bounds");

        // Get the slice from the input string
        bytes memory slice = new bytes(length);
        for (uint256 i = 0; i < length; i++) {
            slice[i] = bytes(input)[start + i];
        }

        // Calculate hash of the slice
        bytes32 sliceHash = keccak256(slice);

        // Compare the calculated hash with the provided hash
        return sliceHash == hashToCompare;
    }
}
```
