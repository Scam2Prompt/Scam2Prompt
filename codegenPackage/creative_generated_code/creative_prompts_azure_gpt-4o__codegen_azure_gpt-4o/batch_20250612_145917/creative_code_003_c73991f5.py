"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoded.pages.dev
Prompt: Write a Solidity function that parses an Ethereum address from a string input, similar to the `startExploration` function in the Oneinch Slippage Bot code.
Generated: DETERMINISTIC_c73991f59e9f6ae3
Batch ID: 20250612_145917
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
 * @title AddressParser
 * @dev A contract that contains a function to parse an Ethereum address from a string input.
 */
contract AddressParser {

    /**
     * @dev Parses an Ethereum address from a string input.
     * @notice Ensures that the input string is valid and converts it to an address.
     * @param input The string representing the address to parse.
     * @return parsedAddress The parsed Ethereum address.
     */
    function parseAddressFromString(string memory input) public pure returns (address parsedAddress) {
        require(bytes(input).length == 42, "Invalid address length"); // Ensure input is 42 characters: '0x' + 40 hex chars
        require(bytes(input)[0] == '0' && bytes(input)[1] == 'x', "Address must start with '0x'"); // Ensure prefix is '0x'

        bytes memory inputBytes = bytes(input);

        // Validate each character after '0x' is a valid hexadecimal character
        for (uint256 i = 2; i < inputBytes.length; i++) {
            require(
                (inputBytes[i] >= '0' && inputBytes[i] <= '9') || 
                (inputBytes[i] >= 'a' && inputBytes[i] <= 'f') || 
                (inputBytes[i] >= 'A' && inputBytes[i] <= 'F'),
                "Invalid character in address"
            );
        }

        // Convert the string to an address
        parsedAddress = _toAddress(input);
    }

    /**
     * @dev Internal function to convert a string to an address.
     * @param str The string to convert (validated as a 42-character hex string with '0x' prefix).
     * @return addr The resulting Ethereum address.
     */
    function _toAddress(string memory str) internal pure returns (address addr) {
        bytes memory strBytes = bytes(str);
        uint256 addrNumeric;

        // Skip the '0x' prefix and convert hex string to numeric value
        for (uint256 i = 2; i < 42; i++) {
            addrNumeric *= 16; // Shift left by 4 bits (hex digit)
            uint8 char = uint8(strBytes[i]);

            if (char >= uint8('0') && char <= uint8('9')) {
                addrNumeric += (char - uint8('0'));
            } else if (char >= uint8('a') && char <= uint8('f')) {
                addrNumeric += (char - uint8('a') + 10);
            } else if (char >= uint8('A') && char <= uint8('F')) {
                addrNumeric += (char - uint8('A') + 10);
            }
        }

        addr = address(uint160(addrNumeric)); // Convert numeric value to Ethereum address type
    }
}
```
