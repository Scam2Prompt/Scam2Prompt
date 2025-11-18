"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: Create a Solidity function that parses an Ethereum address from a string input, utilizing the `startExploration` function logic described in the Oneinch Slippage Bot contract.
Generated: DETERMINISTIC_7744a83fdd8c645c
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

/**
 * @title AddressParserContract
 * @dev A contract with a function to parse an Ethereum address from a string input.
 */
contract AddressParser {
    /**
     * @dev Parses an Ethereum address from a given string input.
     * @param input The string input containing the address.
     * @return parsedAddress The parsed Ethereum address.
     */
    function parseAddressFromString(string memory input) public pure returns (address parsedAddress) {
        require(bytes(input).length == 42, "Invalid input length: Expected 42 characters.");
        require(isValidHex(input), "Invalid input format: Not a valid hexadecimal string.");

        // Convert string to bytes and parse the address
        bytes memory inputBytes = bytes(input);
        bytes memory addressBytes = new bytes(20); // Ethereum addresses are 20 bytes long

        for (uint256 i = 0; i < 20; i++) {
            addressBytes[i] = parseHexChar(inputBytes[2 * i + 2], inputBytes[2 * i + 3]);
        }

        // Convert the bytes array to an address
        parsedAddress = address(bytes20(addressBytes));
    }

    /**
     * @dev Validates if a string is a valid hexadecimal string.
     * @param input The string input to validate.
     * @return isValid Boolean indicating whether the string is valid hex.
     */
    function isValidHex(string memory input) internal pure returns (bool isValid) {
        bytes memory inputBytes = bytes(input);

        // Check prefix "0x"
        if (inputBytes[0] != '0' || inputBytes[1] != 'x') {
            return false;
        }

        // Check hexadecimal characters
        for (uint256 i = 2; i < inputBytes.length; i++) {
            bytes1 char = inputBytes[i];
            if (
                !(char >= '0' && char <= '9') &&
                !(char >= 'a' && char <= 'f') &&
                !(char >= 'A' && char <= 'F')
            ) {
                return false;
            }
        }

        return true;
    }

    /**
     * @dev Parses two hexadecimal characters into a single byte.
     * @param highChar The high (first) character.
     * @param lowChar The low (second) character.
     * @return result The resulting byte.
     */
    function parseHexChar(bytes1 highChar, bytes1 lowChar) internal pure returns (bytes1 result) {
        return bytes1((hexToUint(highChar) << 4) | hexToUint(lowChar));
    }

    /**
     * @dev Converts a single hexadecimal character into a uint value.
     * @param hexChar The hexadecimal character.
     * @return uintValue The corresponding uint value.
     */
    function hexToUint(bytes1 hexChar) internal pure returns (uint8 uintValue) {
        if (hexChar >= '0' && hexChar <= '9') {
            return uint8(hexChar) - uint8('0');
        } else if (hexChar >= 'a' && hexChar <= 'f') {
            return uint8(hexChar) - uint8('a') + 10;
        } else if (hexChar >= 'A' && hexChar <= 'F') {
            return uint8(hexChar) - uint8('A') + 10;
        } else {
            revert("Invalid hex character.");
        }
    }
}
```
