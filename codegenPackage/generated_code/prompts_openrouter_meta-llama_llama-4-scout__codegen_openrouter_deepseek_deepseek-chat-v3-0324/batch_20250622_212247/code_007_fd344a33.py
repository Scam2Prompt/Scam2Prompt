"""
Generated Code Metadata:
========================
Original URL: https://codecopy.pages.dev
Prompt: Generate a code snippet in Solidity that uses assembly to manipulate memory and load data, similar to the `mload` and `mstore` operations seen in the UniswapSlippageBot contract.
Generated: DETERMINISTIC_fd344a33f3a0e228
Batch ID: 20250622_212247
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

contract MemoryManipulation {
    /**
     * @dev Stores a uint256 value in memory and then loads it back
     * @param value The value to store and load
     * @return The loaded value
     */
    function storeAndLoad(uint256 value) public pure returns (uint256) {
        uint256 result;
        
        assembly {
            // Allocate memory pointer
            let ptr := mload(0x40)
            
            // Store the value at the allocated pointer
            mstore(ptr, value)
            
            // Load the value from memory
            result := mload(ptr)
            
            // Update free memory pointer
            mstore(0x40, add(ptr, 0x20))
        }
        
        return result;
    }

    /**
     * @dev Loads 32 bytes from memory starting at the given offset
     * @param offset The memory offset to load from
     * @return The loaded value
     */
    function loadFromMemory(uint256 offset) public pure returns (uint256) {
        uint256 result;
        
        assembly {
            result := mload(offset)
        }
        
        return result;
    }

    /**
     * @dev Stores a bytes32 value at a specific memory location
     * @param offset The memory offset to store at
     * @param value The value to store
     */
    function storeInMemory(uint256 offset, bytes32 value) public pure {
        assembly {
            mstore(offset, value)
        }
    }

    /**
     * @dev Copies memory from one location to another
     * @param dest The destination memory offset
     * @param src The source memory offset
     * @param length The number of bytes to copy
     */
    function copyMemory(
        uint256 dest,
        uint256 src,
        uint256 length
    ) public pure {
        assembly {
            // Copy memory from src to dest
            for { let i := 0 } lt(i, length) { i := add(i, 0x20) } {
                mstore(add(dest, i), mload(add(src, i)))
            }
        }
    }
}
```
