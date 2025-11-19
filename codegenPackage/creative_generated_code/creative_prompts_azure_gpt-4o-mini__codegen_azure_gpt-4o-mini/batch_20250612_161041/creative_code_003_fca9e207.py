"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contrack-dev.pages.dev
Prompt: Develop a Solidity function that converts a uint to a string, similar to the uint2str function in the UniswapSlippageBot contract.
Generated: DETERMINISTIC_fca9e2074559e6d9
Batch ID: 20250612_161041
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

library Utils {
    /**
     * @dev Converts a uint256 to its ASCII string representation.
     * @param value The uint256 value to convert.
     * @return result The ASCII string representation of the input value.
     */
    function uintToString(uint256 value) internal pure returns (string memory result) {
        // Handle zero case explicitly
        if (value == 0) {
            return "0";
        }

        // Calculate the length of the resulting string
        uint256 tempValue = value;
        uint256 digits;
        while (tempValue != 0) {
            digits++;
            tempValue /= 10;
        }

        // Create a buffer to hold the string characters
        bytes memory buffer = new bytes(digits);

        // Fill the buffer with characters in reverse order
        while (value != 0) {
            digits -= 1;
            buffer[digits] = bytes1(uint8(48 + (value % 10))); // Convert digit to ASCII
            value /= 10;
        }

        // Convert the bytes buffer to a string and return
        result = string(buffer);
    }
}
```
