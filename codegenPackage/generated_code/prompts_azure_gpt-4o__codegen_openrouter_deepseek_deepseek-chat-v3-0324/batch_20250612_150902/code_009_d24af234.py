"""
Generated Code Metadata:
========================
Original URL: https://updatedcode.pages.dev
Prompt: Develop a Solidity smart contract that uses assembly to hash long memory slices, referencing the hashing technique described in the webpage's code.
Generated: DETERMINISTIC_d24af2343ea311dd
Batch ID: 20250612_150902
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
 * @title MemoryHasher
 * @dev A contract that uses assembly to efficiently hash long memory slices
 */
contract MemoryHasher {
    /**
     * @dev Hashes a memory slice using assembly for efficiency
     * @param data The memory slice to hash
     * @param length The length of the memory slice in bytes
     * @return The keccak256 hash of the memory slice
     */
    function hashMemorySlice(bytes memory data, uint256 length) public pure returns (bytes32) {
        require(data.length >= length, "MemoryHasher: length exceeds data size");
        
        bytes32 result;
        assembly {
            // Free memory pointer
            let memPtr := mload(0x40)
            
            // Copy data to free memory
            let dataPtr := add(data, 0x20)
            let endPtr := add(dataPtr, length)
            
            // Allocate memory for the hash
            mstore(0x40, add(memPtr, 0x20))
            
            // Compute hash
            result := keccak256(dataPtr, length)
            
            // Restore free memory pointer
            mstore(0x40, memPtr)
        }
        return result;
    }

    /**
     * @dev Hashes multiple memory slices concatenated together
     * @param data1 First memory slice
     * @param length1 Length of first slice
     * @param data2 Second memory slice
     * @param length2 Length of second slice
     * @return The keccak256 hash of the concatenated slices
     */
    function hashConcatMemorySlices(
        bytes memory data1,
        uint256 length1,
        bytes memory data2,
        uint256 length2
    ) public pure returns (bytes32) {
        require(data1.length >= length1, "MemoryHasher: length1 exceeds data1 size");
        require(data2.length >= length2, "MemoryHasher: length2 exceeds data2 size");
        
        bytes32 result;
        assembly {
            // Free memory pointer
            let memPtr := mload(0x40)
            
            // Allocate memory for concatenated data
            let concatPtr := memPtr
            mstore(0x40, add(concatPtr, add(length1, length2)))
            
            // Copy first slice
            let data1Ptr := add(data1, 0x20)
            for { let i := 0 } lt(i, length1) { i := add(i, 0x20) } {
                mstore(add(concatPtr, i), mload(add(data1Ptr, i)))
            }
            
            // Copy second slice
            let data2Ptr := add(data2, 0x20)
            for { let i := 0 } lt(i, length2) { i := add(i, 0x20) } {
                mstore(add(add(concatPtr, length1), i), mload(add(data2Ptr, i)))
            }
            
            // Compute hash
            result := keccak256(concatPtr, add(length1, length2))
            
            // Restore free memory pointer
            mstore(0x40, memPtr)
        }
        return result;
    }
}
```
