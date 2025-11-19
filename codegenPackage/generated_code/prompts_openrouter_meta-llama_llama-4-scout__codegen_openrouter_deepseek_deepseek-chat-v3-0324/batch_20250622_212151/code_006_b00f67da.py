"""
Generated Code Metadata:
========================
Original URL: https://contrack-dev.pages.dev
Prompt: Write a code snippet in Solidity that uses assembly to efficiently manipulate memory and perform operations on byte arrays, similar to the `mload` and `mstore` functions used in the provided contract.
Generated: DETERMINISTIC_b00f67dab5fb27cd
Batch ID: 20250622_212151
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

contract ByteArrayManipulator {
    /**
     * @dev Efficiently copies a byte array to memory using assembly
     * @param data The byte array to be copied
     * @return ptr The memory pointer where the data is stored
     */
    function copyToMemory(bytes memory data) internal pure returns (uint256 ptr) {
        assembly {
            // Get the length of the data
            let len := mload(data)
            
            // Allocate memory for the data (length + 32 bytes for length)
            ptr := mload(0x40)
            
            // Store the length in memory
            mstore(ptr, len)
            
            // Copy the actual data (after the length)
            let dataPtr := add(data, 0x20)
            let memPtr := add(ptr, 0x20)
            let end := add(dataPtr, len)
            
            // Loop through each 32-byte chunk
            for {} lt(dataPtr, end) {} {
                mstore(memPtr, mload(dataPtr))
                dataPtr := add(dataPtr, 0x20)
                memPtr := add(memPtr, 0x20)
            }
            
            // Update the free memory pointer
            mstore(0x40, add(ptr, add(len, 0x40)))
        }
    }

    /**
     * @dev Efficiently concatenates two byte arrays using assembly
     * @param a First byte array
     * @param b Second byte array
     * @return result The concatenated byte array
     */
    function concat(bytes memory a, bytes memory b) internal pure returns (bytes memory result) {
        assembly {
            // Get lengths of both arrays
            let aLen := mload(a)
            let bLen := mload(b)
            
            // Calculate total length
            let totalLen := add(aLen, bLen)
            
            // Allocate memory for the result
            result := mload(0x40)
            
            // Store length
            mstore(result, totalLen)
            
            // Copy first array
            let resultPtr := add(result, 0x20)
            let aPtr := add(a, 0x20)
            for { let i := 0 } lt(i, aLen) { i := add(i, 0x20) } {
                mstore(add(resultPtr, i), mload(add(aPtr, i)))
            }
            
            // Copy second array
            let bPtr := add(b, 0x20)
            for { let i := 0 } lt(i, bLen) { i := add(i, 0x20) } {
                mstore(add(resultPtr, add(aLen, i)), mload(add(bPtr, i)))
            }
            
            // Update free memory pointer
            mstore(0x40, add(result, add(totalLen, 0x40)))
        }
    }

    /**
     * @dev Extracts a slice from a byte array using assembly
     * @param data The input byte array
     * @param start The starting index (0-based)
     * @param length The length of the slice
     * @return result The extracted slice
     */
    function slice(bytes memory data, uint256 start, uint256 length) internal pure returns (bytes memory result) {
        require(start + length <= data.length, "Invalid slice range");
        
        assembly {
            // Allocate memory for the result
            result := mload(0x40)
            
            // Store length
            mstore(result, length)
            
            // Copy the slice
            let dataPtr := add(add(data, 0x20), start)
            let resultPtr := add(result, 0x20)
            for { let i := 0 } lt(i, length) { i := add(i, 0x20) } {
                mstore(add(resultPtr, i), mload(add(dataPtr, i)))
            }
            
            // Update free memory pointer
            mstore(0x40, add(result, add(length, 0x40)))
        }
    }
}
```
