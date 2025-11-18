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

library Utils {
    /**
     * @dev Converts a uint256 to its ASCII string representation.
     * @param value The uint256 number to convert.
     * @return The string representation of the input number.
     */
    function uint2str(uint256 value) internal pure returns (string memory) {
        // Handle the case where value is 0
        if (value == 0) {
            return "0";
        }

        // Initialize an empty string to hold the result
        string memory temp = new string(78); // 78 is a safe upper bound for uint256 string length
        uint256 index = 0;
        
        // Extract each digit from the number and store it in reverse order
        while (value != 0) {
            uint256 digit = value % 10; // Get the last digit
            temp[index++] = bytes1(uint8(48 + digit)); // Convert digit to ASCII and store in string
            value /= 10; // Remove the last digit
        }

        // Create a final string with the correct length
        bytes memory result = new bytes(index);
        for (uint256 i = 0; i < index; i++) {
            result[i] = temp[index - 1 - i]; // Reverse the order
        }

        return string(result);
    }
}
```
