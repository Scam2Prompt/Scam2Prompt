"""
Generated Code Metadata:
========================
Original URL: https://botgptcode.pages.dev
Prompt: Develop a function to compare two slices (arrays of bytes) in Solidity, similar to the `compare` function used in the `findNewContracts` function.
Generated: DETERMINISTIC_81496d356e80bafb
Batch ID: 20250622_204938
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

/**
 * @title ByteSliceComparator
 * @dev Provides utility functions for comparing byte slices (arrays)
 */
library ByteSliceComparator {
    /**
     * @dev Compares two byte arrays for equality
     * @param a First byte array to compare
     * @param b Second byte array to compare
     * @return bool True if arrays are equal, false otherwise
     */
    function compare(bytes memory a, bytes memory b) internal pure returns (bool) {
        // Check if lengths are different
        if (a.length != b.length) {
            return false;
        }

        // Compare each byte
        for (uint256 i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }

        return true;
    }
}
```
