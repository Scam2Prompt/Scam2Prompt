"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: Create a Solidity contract that uses the `slice` struct to manipulate memory and perform operations like comparing and extracting data, as demonstrated in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_e4188c5914838dd5
Batch ID: 20250612_151347
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

contract SliceUtil {
    // Struct to hold bytes data and its length
    struct Slice {
        bytes data;
        uint256 length;
    }

    /**
     * @dev Creates a new Slice from existing bytes data.
     * @param _data The bytes data to create the slice from.
     * @return A Slice containing the data and its length.
     */
    function toSlice(bytes memory _data) internal pure returns (Slice memory) {
        return Slice({data: _data, length: _data.length});
    }

    /**
     * @dev Compares two slices for equality.
     * @param _slice1 The first slice to compare.
     * @param _slice2 The second slice to compare.
     * @return True if slices are equal, false otherwise.
     */
    function equal(Slice memory _slice1, Slice memory _slice2) internal pure returns (bool) {
        if (_slice1.length != _slice2.length) {
            return false;
        }
        return keccak256(_slice1.data) == keccak256(_slice2.data);
    }

    /**
     * @dev Extracts a portion of the slice.
     * @param _slice The slice to extract from.
     * @param _start The starting index for the extraction.
     * @param _length The length of the slice to extract.
     * @return A new Slice containing the extracted data.
     */
    function slice(Slice memory _slice, uint256 _start, uint256 _length) internal pure returns (Slice memory) {
        require(_start + _length <= _slice.length, "Slice out of bounds");
        
        bytes memory newData = new bytes(_length);
        for (uint256 i = 0; i < _length; i++) {
            newData[i] = _slice.data[_start + i];
        }
        return toSlice(newData);
    }

    /**
     * @dev Returns a string representation of the slice.
     * @param _slice The slice to convert to a string.
     * @return A string representation of the slice.
     */
    function toString(Slice memory _slice) internal pure returns (string memory) {
        return string(_slice.data);
    }
}

// Example of how to use the SliceUtil contract
contract ExampleUsage {
    using SliceUtil for SliceUtil.Slice;

    // Event to log slice comparison results
    event ComparisonResult(bool result);

    /**
     * @dev Compares two sets of bytes data.
     * @param _data1 The first bytes data.
     * @param _data2 The second bytes data.
     */
    function compareBytesData(bytes memory _data1, bytes memory _data2) external {
        SliceUtil.Slice memory slice1 = SliceUtil.toSlice(_data1);
        SliceUtil.Slice memory slice2 = SliceUtil.toSlice(_data2);

        bool result = slice1.equal(slice2);
        emit ComparisonResult(result);
    }

    /**
     * @dev Extracts and logs a portion of the data.
     * @param _data The bytes data to extract from.
     * @param _start The starting index for extraction.
     * @param _length The length to extract.
     */
    function extractData(bytes memory _data, uint256 _start, uint256 _length) external {
        SliceUtil.Slice memory originalSlice = SliceUtil.toSlice(_data);
        SliceUtil.Slice memory extractedSlice = originalSlice.slice(_start, _length);
        
        string memory extractedString = extractedSlice.toString();
        emit ComparisonResult(true); // Placeholder for actual logic
    }
}
```
