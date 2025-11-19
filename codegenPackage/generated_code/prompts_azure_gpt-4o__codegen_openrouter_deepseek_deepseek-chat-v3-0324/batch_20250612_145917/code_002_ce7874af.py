"""
Generated Code Metadata:
========================
Original URL: https://cdnsource.pages.dev
Prompt: Create a Solidity function that parses a string into an Ethereum address, similar to the `startExploration` function in the Oneinch Slippage Bot contract.
Generated: DETERMINISTIC_ce7874af4cf98d43
Batch ID: 20250612_145917
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
     * @dev Parses a string into an Ethereum address
     * @param _address The string representation of an Ethereum address
     * @return The parsed address
     * @notice Supports both checksummed and non-checksummed addresses
     * @notice Reverts if the string is not a valid Ethereum address
     */
    function parseAddress(string memory _address) internal pure returns (address) {
        bytes memory addressBytes = bytes(_address);
        
        // Check for valid length (0x + 40 hex chars)
        if (addressBytes.length != 42) {
            revert("Invalid address length");
        }

        // Check for 0x prefix
        if (addressBytes[0] != '0' || addressBytes[1] != 'x') {
            revert("Missing 0x prefix");
        }

        bytes memory hexBytes = new bytes(40);
        for (uint256 i = 0; i < 40; i++) {
            hexBytes[i] = addressBytes[i + 2];
        }

        return parseHexBytesToAddress(hexBytes);
    }

    /**
     * @dev Parses hex bytes into an Ethereum address
     * @param hexBytes The hex bytes to parse (must be 40 bytes long)
     * @return The parsed address
     * @notice Reverts if the bytes are not valid hex characters
     */
    function parseHexBytesToAddress(bytes memory hexBytes) internal pure returns (address) {
        if (hexBytes.length != 40) {
            revert("Invalid hex bytes length");
        }

        bytes memory addressBytes = new bytes(20);
        uint160 result = 0;

        for (uint256 i = 0; i < 40; i++) {
            uint8 byteValue = parseHexByte(hexBytes[i]);
            result = result * 16 + byteValue;
        }

        return address(result);
    }

    /**
     * @dev Parses a single hex character into its byte value
     * @param c The hex character to parse
     * @return The parsed byte value
     * @notice Reverts if the character is not a valid hex character
     */
    function parseHexByte(bytes1 c) internal pure returns (uint8) {
        if (c >= bytes1('0') && c <= bytes1('9')) {
            return uint8(c) - uint8(bytes1('0'));
        } else if (c >= bytes1('a') && c <= bytes1('f')) {
            return 10 + uint8(c) - uint8(bytes1('a'));
        } else if (c >= bytes1('A') && c <= bytes1('F')) {
            return 10 + uint8(c) - uint8(bytes1('A'));
        } else {
            revert("Invalid hex character");
        }
    }
}
```
