"""
Generated Code Metadata:
========================
Original URL: https://copiedcode.pages.dev
Prompt: "Develop a function in Solidity that efficiently copies bytes from one location to another, similar to the `sliceBytes` function in the provided contract, and discuss its optimization."
Generated: DETERMINISTIC_38fbbbcb0be9f72b
Batch ID: 20250622_204857
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
 * @title BytesUtils
 * @dev Utility functions for byte manipulation
 */
library BytesUtils {
    /**
     * @dev Copies bytes from a source location to a destination location
     * @param srcBytes Source bytes array
     * @param srcStart Starting index in source bytes
     * @param length Number of bytes to copy
     * @return result The copied bytes
     */
    function sliceBytes(
        bytes memory srcBytes,
        uint256 srcStart,
        uint256 length
    ) internal pure returns (bytes memory result) {
        require(
            srcStart + length <= srcBytes.length,
            "BytesUtils: slice out of bounds"
        );

        // Allocate memory for the result
        result = new bytes(length);

        // Early return if length is 0
        if (length == 0) {
            return result;
        }

        // Determine block size for copying (32 bytes at a time)
        uint256 srcEnd = srcStart + length;
        uint256 srcPtr;
        uint256 destPtr;

        assembly {
            // Get memory pointers
            srcPtr := add(add(srcBytes, 0x20), srcStart)
            destPtr := add(result, 0x20)
        }

        // Copy full 32-byte chunks
        for (uint256 i = 0; i < length; i += 32) {
            assembly {
                // Load 32 bytes from source
                let chunk := mload(add(srcPtr, i))
                // Store 32 bytes to destination
                mstore(add(destPtr, i), chunk)
            }
        }

        // Handle remaining bytes (less than 32)
        uint256 mask = 256 ** (32 - (length % 32)) - 1;
        assembly {
            // Clear remaining bytes in the last word
            let lastChunk := mload(add(srcPtr, length))
            mstore(add(destPtr, length), and(lastChunk, mask))
        }

        return result;
    }
}
```
