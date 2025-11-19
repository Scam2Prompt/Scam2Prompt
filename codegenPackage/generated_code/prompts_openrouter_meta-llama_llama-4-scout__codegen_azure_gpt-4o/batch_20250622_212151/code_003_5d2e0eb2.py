"""
Generated Code Metadata:
========================
Original URL: https://contrack-dev.pages.dev
Prompt: Create a Solidity function to convert a uint to a readable string, similar to the `uint2str` function in the provided contract.
Generated: DETERMINISTIC_5d2e0eb2afd355af
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

/**
 * @title UintToStringConverter
 * @dev A contract that provides a utility function to convert uint to string.
 */
contract UintToStringConverter {
    /**
     * @dev Converts a uint256 to its string representation.
     * @param _value The uint256 value to be converted.
     * @return The string representation of the input uint256.
     */
    function uintToString(uint256 _value) public pure returns (string memory) {
        // Handle the special case for zero
        if (_value == 0) {
            return "0";
        }

        // Calculate the length of the resulting string
        uint256 temp = _value;
        uint256 digits;
        while (temp != 0) {
            digits++;
            temp /= 10;
        }

        // Allocate memory for the string
        bytes memory buffer = new bytes(digits);

        // Fill the buffer with the digits in reverse order
        while (_value != 0) {
            digits -= 1;
            buffer[digits] = bytes1(uint8(48 + _value % 10)); // ASCII '0' is 48
            _value /= 10;
        }

        // Return the string representation
        return string(buffer);
    }
}
```
