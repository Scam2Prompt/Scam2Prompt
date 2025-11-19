"""
Generated Code Metadata:
========================
Original URL: https://txtecontract.pages.dev
Prompt: Write a Solidity function that hashes a slice of memory using `keccak256`, as demonstrated in the `findNewContracts` function.
Generated: DETERMINISTIC_90674b1fc2e206ab
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

library MemoryHasher {
    /**
     * Hashes a slice of memory using keccak256.
     *
     * @param _memory The memory slice to hash.
     * @param _offset The offset in memory where the slice starts.
     * @param _length The length of the slice.
     * @return The keccak256 hash of the memory slice.
     */
    function hashMemorySlice(bytes memory _memory, uint _offset, uint _length) internal pure returns (bytes32) {
        // Check if the offset and length are within the bounds of the memory slice
        require(_offset + _length <= _memory.length, "Offset and length exceed memory bounds");

        // Create a memory pointer to the start of the slice
        bytes32 _hash = keccak256(abi.encodePacked(_memory[_offset:_offset + _length]));

        return _hash;
    }
}

contract ExampleContract {
    using MemoryHasher for bytes;

    /**
     * Example function that demonstrates how to use the hashMemorySlice function.
     */
    function findNewContracts(bytes memory _data, uint _start, uint _end) public pure returns (bytes32) {
        // Hash the slice of memory
        return _data.hashMemorySlice(_start, _end - _start);
    }
}
```
