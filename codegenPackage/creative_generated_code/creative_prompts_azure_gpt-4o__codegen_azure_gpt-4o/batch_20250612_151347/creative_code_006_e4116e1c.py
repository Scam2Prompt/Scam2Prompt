"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: Write a Solidity function that uses hashing (`keccak256`) to locate specific data within a memory slice, inspired by the needle search logic in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_e4116e1ce3192c33
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

contract MemorySliceSearch {

    /**
     * @dev Searches for a specific data (needle) within a memory slice (haystack) using keccak256 hashing.
     * @param haystack The larger memory slice to search within.
     * @param needle The specific data to locate within the haystack.
     * @return found Boolean indicating whether the needle was found in the haystack.
     * @return index The starting index of the needle in the haystack, or -1 if not found.
     */
    function searchMemorySlice(bytes memory haystack, bytes memory needle) public pure returns (bool found, int256 index) {
        require(haystack.length >= needle.length, "Haystack must be larger than or equal to needle.");

        // Hash the needle using keccak256
        bytes32 needleHash = keccak256(needle);

        // Iterate through the haystack and find a matching hash
        for (uint256 i = 0; i <= haystack.length - needle.length; i++) {
            bytes32 sliceHash = keccak256(slice(haystack, i, needle.length));
            if (sliceHash == needleHash) {
                return (true, int256(i));
            }
        }

        // Return false and -1 if the needle is not found
        return (false, -1);
    }

    /**
     * @dev Extracts a sub-slice of bytes from the given memory slice.
     * @param data The memory slice to extract from.
     * @param start The starting index for the sub-slice.
     * @param length The length of the sub-slice to extract.
     * @return slice The extracted sub-slice of bytes.
     */
    function slice(bytes memory data, uint256 start, uint256 length) internal pure returns (bytes memory slice) {
        require(start + length <= data.length, "Slice out of bounds.");

        // Allocate memory for the new slice
        slice = new bytes(length);

        // Copy the data into the new slice
        for (uint256 i = 0; i < length; i++) {
            slice[i] = data[start + i];
        }
    }
}
```
