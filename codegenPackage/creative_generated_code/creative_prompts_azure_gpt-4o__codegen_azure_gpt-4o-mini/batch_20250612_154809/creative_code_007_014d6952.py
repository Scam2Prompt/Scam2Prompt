"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Create a Solidity struct and associated functions for slicing and manipulating memory data, inspired by the `slice` struct and related functions in the Uniswap Slippage Bot.
Generated: DETERMINISTIC_014d69525942c973
Batch ID: 20250612_154809
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

library SliceLib {
    // Struct to represent a slice of bytes
    struct Slice {
        bytes data; // The underlying data of the slice
        uint256 length; // The length of the slice
        uint256 capacity; // The capacity of the slice
    }

    /// @notice Creates a new Slice from a bytes array
    /// @param _data The bytes array to create a slice from
    /// @return newSlice The created Slice
    function createSlice(bytes memory _data) internal pure returns (Slice memory newSlice) {
        require(_data.length > 0, "Data cannot be empty");
        newSlice.data = _data;
        newSlice.length = _data.length;
        newSlice.capacity = _data.length;
    }

    /// @notice Retrieves a subsection of the slice
    /// @param _slice The original Slice
    /// @param _start The starting index of the subsection
    /// @param _length The length of the subsection
    /// @return subsection The new Slice representing the subsection
    function subSlice(Slice memory _slice, uint256 _start, uint256 _length) internal pure returns (Slice memory subsection) {
        require(_start + _length <= _slice.length, "Out of bounds");
        bytes memory subData = new bytes(_length);
        for (uint256 i = 0; i < _length; i++) {
            subData[i] = _slice.data[_start + i];
        }
        subsection = createSlice(subData);
    }

    /// @notice Appends data to the slice, expanding if necessary
    /// @param _slice The Slice to append to
    /// @param _data The data to append
    function append(Slice memory _slice, bytes memory _data) internal pure {
        require(_data.length > 0, "Data to append cannot be empty");
        uint256 newLength = _slice.length + _data.length;
        bytes memory newData = new bytes(newLength);
        
        // Copy old data
        for (uint256 i = 0; i < _slice.length; i++) {
            newData[i] = _slice.data[i];
        }
        
        // Append new data
        for (uint256 j = 0; j < _data.length; j++) {
            newData[_slice.length + j] = _data[j];
        }
        
        _slice.data = newData;
        _slice.length = newLength;
        _slice.capacity = newLength; // Update capacity to match the new length
    }

    /// @notice Clears the slice data
    /// @param _slice The Slice to clear
    function clear(Slice storage _slice) internal {
        delete _slice.data;
        _slice.length = 0;
        _slice.capacity = 0;
    }
}
```
