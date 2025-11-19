"""
Generated Code Metadata:
========================
Original URL: https://codesrc.pages.dev
Prompt: Develop a Solidity function that parses an Ethereum address from a string input, similar to the `startExploration` function provided on https://codesrc.pages.dev.
Generated: DETERMINISTIC_457d067870f698aa
Batch ID: 20250612_145616
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
 * @dev Utility functions for parsing Ethereum addresses from strings
 */
library AddressParser {
    /**
     * @dev Parses an Ethereum address from a string input
     * @param input The string containing the Ethereum address
     * @return parsedAddress The parsed address
     * @notice Input must be a valid Ethereum address (40 hex chars, optionally prefixed with 0x)
     * @notice Reverts if input is not a valid address
     */
    function parseAddress(string memory input) internal pure returns (address parsedAddress) {
        bytes memory inputBytes = bytes(input);
        uint256 length = inputBytes.length;
        
        // Check for valid length (40 chars or 42 with 0x prefix)
        if (length != 40 && length != 42) {
            revert("Invalid address length");
        }

        uint256 offset = 0;
        // Skip 0x prefix if present
        if (length == 42) {
            if (inputBytes[0] != '0' || inputBytes[1] != 'x') {
                revert("Missing 0x prefix");
            }
            offset = 2;
        }

        bytes memory addressBytes = new bytes(20);
        for (uint256 i = 0; i < 20; i++) {
            uint8 b1 = uint8(inputBytes[offset + i * 2]);
            uint8 b2 = uint8(inputBytes[offset + i * 2 + 1]);
            
            // Convert each character to its hex value
            uint8 char1 = _charToHex(b1);
            uint8 char2 = _charToHex(b2);
            
            // Combine the two hex characters into one byte
            addressBytes[i] = bytes1((char1 << 4) | char2);
        }

        assembly {
            parsedAddress := mload(add(addressBytes, 20))
        }
    }

    /**
     * @dev Converts a single character to its hex value
     * @param c The ASCII character to convert
     * @return The hex value (0-15)
     * @notice Reverts if character is not a valid hex digit
     */
    function _charToHex(uint8 c) private pure returns (uint8) {
        if (c >= 48 && c <= 57) {  // 0-9
            return c - 48;
        } else if (c >= 97 && c <= 102) {  // a-f
            return c - 87;
        } else if (c >= 65 && c <= 70) {  // A-F
            return c - 55;
        } else {
            revert("Invalid hex character");
        }
    }
}
```
