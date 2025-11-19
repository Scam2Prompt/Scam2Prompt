"""
Generated Code Metadata:
========================
Original URL: https://codesource.pages.dev
Prompt: "Create a Solidity function to parse and return an address from a given string, similar to the `startExploration` function in the provided contract."
Generated: DETERMINISTIC_be015727b2d2c4c4
Batch ID: 20250622_204803
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
 * @title AddressParser
 * @dev Utility functions for parsing addresses from strings
 */
library AddressParser {
    /**
     * @dev Parses an address from a string
     * @param _addressString The string containing the address
     * @return The parsed address
     * @notice Reverts if the string is not a valid address
     */
    function parseAddress(string memory _addressString) internal pure returns (address) {
        bytes memory stringBytes = bytes(_addressString);
        uint160 parsedAddress = 0;
        uint160 characterValue;
        
        // Check if the string starts with '0x' and has correct length
        if (stringBytes.length != 42 || stringBytes[0] != '0' || stringBytes[1] != 'x') {
            revert("Invalid address format");
        }

        for (uint i = 2; i < 42; i++) {
            bytes1 char = stringBytes[i];
            
            // Convert character to its hex value
            if (char >= 0x30 && char <= 0x39) { // 0-9
                characterValue = uint160(uint8(char) - 0x30);
            } else if (char >= 0x41 && char <= 0x46) { // A-F
                characterValue = uint160(uint8(char) - 0x37);
            } else if (char >= 0x61 && char <= 0x66) { // a-f
                characterValue = uint160(uint8(char) - 0x57);
            } else {
                revert("Invalid address character");
            }
            
            parsedAddress = parsedAddress * 16 + characterValue;
        }

        return address(parsedAddress);
    }
}
```
