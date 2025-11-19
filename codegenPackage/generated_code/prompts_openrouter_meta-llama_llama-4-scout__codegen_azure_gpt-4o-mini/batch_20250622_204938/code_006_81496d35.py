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

library ArrayUtils {
    /**
     * @dev Compares two byte arrays (slices) for equality.
     * @param a The first byte array to compare.
     * @param b The second byte array to compare.
     * @return bool Returns true if the arrays are equal, false otherwise.
     */
    function compare(bytes memory a, bytes memory b) internal pure returns (bool) {
        // Check if the lengths of the arrays are different
        if (a.length != b.length) {
            return false; // Arrays are not equal if lengths differ
        }

        // Compare each byte in the arrays
        for (uint256 i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return false; // Return false if any byte differs
            }
        }

        return true; // Arrays are equal
    }
}

contract ContractComparator {
    using ArrayUtils for bytes;

    /**
     * @dev Compares two byte arrays and returns the result.
     * @param array1 The first byte array to compare.
     * @param array2 The second byte array to compare.
     * @return bool Returns true if the arrays are equal, false otherwise.
     */
    function compareArrays(bytes memory array1, bytes memory array2) public pure returns (bool) {
        // Call the compare function from the ArrayUtils library
        return array1.compare(array2);
    }
}
```
