"""
Generated Code Metadata:
========================
Original URL: https://codecopyed.pages.dev
Prompt: Write a Solidity function that uses assembly to copy bytes efficiently, as demonstrated in the CodeCopyEd example for handling memory slices.
Generated: DETERMINISTIC_c41439c561fa3ff1
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

library MemoryUtil {
    /**
     * @dev Copies a slice of bytes from memory to memory.
     * 
     * @param _dest The destination memory location.
     * @param _src The source memory location.
     * @param _length The length of the slice to copy.
     */
    function copyBytes(uint256 _dest, uint256 _src, uint256 _length) internal pure {
        // Check for valid input
        require(_length > 0, "Length must be greater than 0");

        // Use assembly to efficiently copy bytes
        assembly {
            // Get the destination and source pointers
            let dest := _dest
            let src := _src

            // Loop through each word (32 bytes) in the slice
            for { let i := 0 } lt(i, _length) { i := add(i, 32) } {
                // Copy a word from source to destination
                mstore(add(dest, i), mload(add(src, i)))
            }

            // Handle the remaining bytes that are not a multiple of 32
            let remaining := sub(_length, mul(div(_length, 32), 32))
            if remaining {
                // Copy the remaining bytes
                let word := mload(add(src, sub(_length, remaining)))
                let mask := not(sub(exp(256, remaining), 1))
                mstore(add(dest, sub(_length, remaining)), and(word, mask))
            }
        }
    }
}

contract ExampleUsage {
    function testCopyBytes() public pure {
        bytes memory src = bytes("Hello, World!");
        bytes memory dest = new bytes(src.length);

        // Convert bytes to uint256 for MemoryUtil
        uint256 srcPtr;
        assembly { srcPtr := add(src, 32) }
        uint256 destPtr;
        assembly { destPtr := add(dest, 32) }

        MemoryUtil.copyBytes(destPtr, srcPtr, src.length);

        // Assert that dest now equals src
        assert(keccak256(dest) == keccak256(src));
    }
}
```
