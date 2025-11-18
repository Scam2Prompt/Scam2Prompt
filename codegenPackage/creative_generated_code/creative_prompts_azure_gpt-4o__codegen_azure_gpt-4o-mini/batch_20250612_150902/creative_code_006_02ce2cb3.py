"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Create a Solidity function that uses hashing (e.g., `keccak256`) to search for specific patterns in memory slices, similar to the needle search logic in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_02ce2cb3b42b0842
Batch ID: 20250612_150902
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

contract PatternSearch {

    /**
     * @dev Searches for a specific pattern in a memory slice and returns true if found.
     * @param data The memory slice where the search will be conducted.
     * @param pattern The pattern to search for in the data.
     * @return found A boolean indicating if the pattern was found.
     */
    function containsPattern(bytes memory data, bytes memory pattern) public pure returns (bool found) {
        require(pattern.length > 0, "Pattern cannot be empty");
        require(data.length >= pattern.length, "Data is shorter than the pattern");

        // Iterate through the data slice
        for (uint256 i = 0; i <= data.length - pattern.length; i++) {
            // Check if the segment of data matches the pattern
            if (isPatternAt(data, pattern, i)) {
                return true; // Pattern found
            }
        }
        return false; // Pattern not found
    }

    /**
     * @dev Checks if the specified segment of data matches the pattern.
     * @param data The memory slice to check.
     * @param pattern The pattern to match.
     * @param start The starting index in the data slice.
     * @return isMatch A boolean indicating if the segment matches the pattern.
     */
    function isPatternAt(bytes memory data, bytes memory pattern, uint256 start) internal pure returns (bool isMatch) {
        for (uint256 j = 0; j < pattern.length; j++) {
            if (data[start + j] != pattern[j]) {
                return false; // Mismatch found
            }
        }
        return true; // Match found
    }
}
```
