"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://txtecontract.pages.dev
Prompt: Write a Solidity function to convert a uint to a string, similar to the `uint2str` utility function in the 1inch Slippage Bot code.
Generated: DETERMINISTIC_517f93a07f8bf045
Batch ID: 20250612_154158
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

/**
 * @title UintToStringConverter
 * @dev Provides a utility function to convert uint to string.
 */
contract UintToStringConverter {
    /**
     * @dev Converts an unsigned integer to its string representation.
     * @param num The unsigned integer to convert.
     * @return The string representation of the unsigned integer.
     */
    function uintToString(uint256 num) public pure returns (string memory) {
        // Special case for 0 to avoid leading zeros
        if (num == 0) {
            return "0";
        }
        
        // Calculate the length of the string representation
        uint256 temp = num;
        uint256 length = 0;
        while (temp != 0) {
            length++;
            temp /= 10;
        }
        
        // Create a new string with the appropriate length
        bytes memory buffer = new bytes(length);
        
        // Fill the buffer with the characters for each digit
        while (num != 0) {
            length -= 1;
            buffer[length] = bytes1(uint8(48 + num % 10)); // '0' ASCII code is 48
            num /= 10;
        }
        
        // Convert the buffer to a string and return
        return string(buffer);
    }
}
```
