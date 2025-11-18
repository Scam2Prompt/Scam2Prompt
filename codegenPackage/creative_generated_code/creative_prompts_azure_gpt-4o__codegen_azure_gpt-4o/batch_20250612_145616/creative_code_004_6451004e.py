"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesrc.pages.dev
Prompt: Write a Solidity function that uses assembly to copy memory slices efficiently, as demonstrated in the code snippet from https://codesrc.pages.dev.
Generated: DETERMINISTIC_6451004e9eaa17ef
Batch ID: 20250612_145616
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

contract MemoryUtils {
    /**
     * @notice Copies a memory slice from `src` to `dst` with a given `length`.
     * @param src The memory address of the source.
     * @param dst The memory address of the destination.
     * @param length The number of bytes to copy.
     */
    function copyMemorySlice(uint256 src, uint256 dst, uint256 length) external pure {
        assembly {
            // Check if length is zero and return early if true
            if eq(length, 0) {
                stop()
            }

            // Calculate the number of 32-byte words and extra bytes to copy
            let words := div(length, 32) // Full 32-byte words
            let remainder := mod(length, 32) // Remaining bytes

            // Copy full 32-byte words
            for { let i := 0 } lt(i, words) { i := add(i, 1) } {
                // Load 32 bytes from src+i*32 and store them at dst+i*32
                mstore(add(dst, mul(i, 32)), mload(add(src, mul(i, 32))))
            }

            // Handle any remaining bytes
            if gt(remainder, 0) {
                let offset := mul(words, 32)
                let srcChunk := add(src, offset)
                let dstChunk := add(dst, offset)

                // Load the remaining bytes from source
                let mask := sub(exp(256, sub(32, remainder)), 1)
                let srcData := and(mload(srcChunk), not(mask))

                // Load existing data from destination and merge with source
                let dstData := and(mload(dstChunk), mask)
                mstore(dstChunk, or(srcData, dstData))
            }
        }
    }
}
```
