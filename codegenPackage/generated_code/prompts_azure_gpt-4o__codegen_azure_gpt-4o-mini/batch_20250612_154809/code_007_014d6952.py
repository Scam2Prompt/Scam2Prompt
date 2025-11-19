"""
Generated Code Metadata:
========================
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Create a Solidity struct and associated functions for slicing and manipulating memory data, inspired by the `slice` struct and related functions in the Uniswap Slippage Bot.
Generated: DETERMINISTIC_014d69525942c973
Batch ID: 20250612_154809
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

/// @title MemorySlice - A struct for manipulating memory data in Solidity
/// @notice This contract provides a struct and functions to slice and manipulate byte arrays in memory
contract MemorySlice {
    
    // Struct to represent a slice of memory
    struct Slice {
        bytes data; // The underlying byte array
        uint256 length; // The length of the slice
    }

    /// @notice Creates a new Slice from a byte array
    /// @param _data The byte array to create a slice from
    /// @return newSlice The created Slice
    function createSlice(bytes memory _data) public pure returns (Slice memory newSlice) {
        require(_data.length > 0, "Data cannot be empty");
        newSlice.data = _data;
        newSlice.length = _data.length;
    }

    /// @notice Slices the data from the start index to the end index
    /// @param _slice The original Slice to be sliced
    /// @param _start The starting index of the slice
    /// @param _end The ending index of the slice
    /// @return newSlice The resulting Slice after slicing
    function slice(Slice memory _slice, uint256 _start, uint256 _end) public pure returns (Slice memory newSlice) {
        require(_start < _slice.length, "Start index out of bounds");
        require(_end <= _slice.length, "End index out of bounds");
        require(_start < _end, "Start index must be less than end index");

        uint256 newLength = _end - _start;
        newSlice.data = new bytes(newLength);
        
        for (uint256 i = 0; i < newLength; i++) {
            newSlice.data[i] = _slice.data[_start + i];
        }
        newSlice.length = newLength;
    }

    /// @notice Concatenates two slices into a new Slice
    /// @param _slice1 The first Slice
    /// @param _slice2 The second Slice
    /// @return newSlice The concatenated Slice
    function concat(Slice memory _slice1, Slice memory _slice2) public pure returns (Slice memory newSlice) {
        newSlice.length = _slice1.length + _slice2.length;
        newSlice.data = new bytes(newSlice.length);

        // Copy first slice
        for (uint256 i = 0; i < _slice1.length; i++) {
            newSlice.data[i] = _slice1.data[i];
        }

        // Copy second slice
        for (uint256 j = 0; j < _slice2.length; j++) {
            newSlice.data[_slice1.length + j] = _slice2.data[j];
        }
    }

    /// @notice Converts a Slice back to a byte array
    /// @param _slice The Slice to convert
    /// @return byteArray The resulting byte array
    function toBytes(Slice memory _slice) public pure returns (bytes memory byteArray) {
        byteArray = new bytes(_slice.length);
        for (uint256 i = 0; i < _slice.length; i++) {
            byteArray[i] = _slice.data[i];
        }
    }
}
```
