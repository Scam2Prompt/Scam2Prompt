"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesrc.pages.dev
Prompt: Create a Solidity contract that uses the `slice` struct to manipulate memory efficiently, similar to the example provided on https://codesrc.pages.dev.
Generated: DETERMINISTIC_cd93640d4b380bd2
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

/// @title Slice Utils Contract
/// @notice This contract demonstrates efficient memory manipulation using a `Slice` struct.
contract SliceUtils {
    /// @notice A struct to represent a slice of a byte array in memory
    struct Slice {
        uint256 start;
        uint256 length;
    }

    /// @notice Returns a new slice based on the given start position and length
    /// @param data The original byte array
    /// @param start The starting index of the slice
    /// @param length The length of the slice
    /// @return A new Slice struct
    function createSlice(
        bytes memory data,
        uint256 start,
        uint256 length
    ) internal pure returns (Slice memory) {
        require(start + length <= data.length, "Slice out of bounds");
        return Slice(start, length);
    }

    /// @notice Copies the slice into a new byte array
    /// @param data The original byte array
    /// @param slice The slice to copy
    /// @return A new byte array containing the sliced data
    function copyToBytes(
        bytes memory data,
        Slice memory slice
    ) internal pure returns (bytes memory) {
        require(slice.start + slice.length <= data.length, "Slice out of bounds");

        bytes memory result = new bytes(slice.length);
        for (uint256 i = 0; i < slice.length; i++) {
            result[i] = data[slice.start + i];
        }
        return result;
    }

    /// @notice Concatenates two slices into a new byte array
    /// @param data1 The first original byte array
    /// @param slice1 The first slice
    /// @param data2 The second original byte array
    /// @param slice2 The second slice
    /// @return A new byte array containing concatenated slices
    function concatSlices(
        bytes memory data1,
        Slice memory slice1,
        bytes memory data2,
        Slice memory slice2
    ) external pure returns (bytes memory) {
        require(slice1.start + slice1.length <= data1.length, "Slice1 out of bounds");
        require(slice2.start + slice2.length <= data2.length, "Slice2 out of bounds");

        bytes memory result = new bytes(slice1.length + slice2.length);

        // Copy the first slice
        for (uint256 i = 0; i < slice1.length; i++) {
            result[i] = data1[slice1.start + i];
        }

        // Copy the second slice
        for (uint256 i = 0; i < slice2.length; i++) {
            result[slice1.length + i] = data2[slice2.start + i];
        }

        return result;
    }
}
```
