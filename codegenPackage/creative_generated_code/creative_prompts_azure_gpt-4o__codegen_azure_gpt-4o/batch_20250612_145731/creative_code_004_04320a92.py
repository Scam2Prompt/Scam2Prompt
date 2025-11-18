"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copiedcode.pages.dev
Prompt: Develop a Solidity function that uses hashing (via `keccak256`) to search for specific patterns in memory slices, inspired by the findNewContracts function in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_04320a92e7d19278
Batch ID: 20250612_145731
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

contract PatternSearcher {
    // Event to log when a pattern match is found
    event PatternFound(bytes32 indexed patternHash, uint256 indexed position);

    /**
     * @notice Searches for a specific pattern in a given memory slice using keccak256 hashing.
     * @param data The memory slice (input data) to search through.
     * @param pattern The pattern to search for.
     */
    function findPattern(bytes memory data, bytes memory pattern) public pure returns (bool found, uint256 position) {
        require(data.length >= pattern.length, "Pattern is longer than data");

        // Hash the pattern once to avoid repetitive hashing
        bytes32 patternHash = keccak256(pattern);

        // Loop through the data to find the pattern
        for (uint256 i = 0; i <= data.length - pattern.length; i++) {
            // Extract a slice from data
            bytes memory slice = getSlice(data, i, pattern.length);

            // Compare hashes
            if (keccak256(slice) == patternHash) {
                emit PatternFound(patternHash, i); // Log the match
                return (true, i); // Return true and the position of the match
            }
        }

        // No match found
        return (false, 0);
    }

    /**
     * @notice Extracts a memory slice from the given data starting at a specific index with a specific length.
     * @param data The original data.
     * @param start The starting index of the slice.
     * @param length The length of the slice.
     * @return slice The extracted slice as a new bytes array.
     */
    function getSlice(bytes memory data, uint256 start, uint256 length) internal pure returns (bytes memory slice) {
        require(start + length <= data.length, "Slice out of bounds");

        slice = new bytes(length);
        for (uint256 i = 0; i < length; i++) {
            slice[i] = data[start + i];
        }

        return slice;
    }
}
```
