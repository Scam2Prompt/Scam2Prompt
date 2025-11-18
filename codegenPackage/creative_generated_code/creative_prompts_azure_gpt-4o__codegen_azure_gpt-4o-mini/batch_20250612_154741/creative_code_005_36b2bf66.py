"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contrack-dev.pages.dev
Prompt: Create a Solidity function to convert an unsigned integer to a string, replicating the logic of the `uint2str` function in the UniswapSlippageBot contract.
Generated: DETERMINISTIC_36b2bf667f51f4f5
Batch ID: 20250612_154741
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

library UintToStringConverter {
    /**
     * @dev Convert an unsigned integer to its string representation.
     * @param value The unsigned integer to convert.
     * @return The string representation of the unsigned integer.
     */
    function uint2str(uint256 value) internal pure returns (string memory) {
        // Handle the special case when the value is zero
        if (value == 0) {
            return "0";
        }

        // Determine the length of the resulting string
        uint256 temp = value;
        uint256 digits;
        while (temp != 0) {
            digits++;
            temp /= 10;
        }

        // Create a new string with the calculated length
        bytes memory buffer = new bytes(digits);
        uint256 index = digits - 1;

        // Convert the integer to string by extracting digits
        while (value != 0) {
            buffer[index--] = bytes1(uint8(48 + (value % 10))); // ASCII '0' is 48
            value /= 10;
        }

        // Return the resulting string
        return string(buffer);
    }
}

contract ExampleUsage {
    using UintToStringConverter for uint256;

    /**
     * @dev Example function to demonstrate the uint2str conversion.
     * @param value The unsigned integer to convert and return as string.
     * @return The string representation of the input unsigned integer.
     */
    function convertUintToString(uint256 value) external pure returns (string memory) {
        return value.uint2str();
    }
}
```
