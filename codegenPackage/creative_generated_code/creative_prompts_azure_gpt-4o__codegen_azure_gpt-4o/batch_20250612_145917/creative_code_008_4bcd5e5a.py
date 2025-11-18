"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdnsource.pages.dev
Prompt: Write a Solidity function that compares two memory slices and returns specific data based on their lengths, as described in the Oneinch Slippage Bot's code.
Generated: DETERMINISTIC_4bcd5e5a7e90b970
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

// Utility library for performing memory slice comparisons
library MemoryUtils {
    /**
     * @dev Compares two memory slices and returns an integer based on their lengths.
     * @param slice1 First memory slice (bytes).
     * @param slice2 Second memory slice (bytes).
     * @return result Integer indicating comparison outcome:
     *         - 0 if both slices have the same length
     *         - 1 if slice1 is longer
     *         - -1 if slice2 is longer
     */
    function compareMemorySlices(bytes memory slice1, bytes memory slice2) internal pure returns (int8 result) {
        // Calculate the lengths of the slices
        uint256 len1 = slice1.length;
        uint256 len2 = slice2.length;

        // Perform comparison based on lengths
        if (len1 == len2) {
            return 0; // Equal lengths
        } else if (len1 > len2) {
            return 1; // slice1 is longer
        } else {
            return -1; // slice2 is longer
        }
    }
}

// Example contract showing usage of the MemoryUtils library
contract SliceComparison {
    using MemoryUtils for bytes;

    /**
     * @dev Public function to compare two memory slices and return their comparison result.
     * @param data1 First memory slice (bytes).
     * @param data2 Second memory slice (bytes).
     * @return result Integer indicating comparison outcome:
     *         - 0 if both slices have the same length
     *         - 1 if data1 is longer
     *         - -1 if data2 is longer
     */
    function compareSlices(bytes memory data1, bytes memory data2) public pure returns (int8 result) {
        return data1.compareMemorySlices(data2);
    }
}
```
