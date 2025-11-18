"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Create a Solidity function that parses an Ethereum address from a string input, utilizing the byte manipulation techniques shown in the Oneinch Slippage Bot contract.
Generated: DETERMINISTIC_70aa6a0fbb54b0ea
Batch ID: 20250612_150902
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

contract AddressParser {
    
    /**
     * @dev Parses an Ethereum address from a string input.
     * @param _addressStr The string representation of the Ethereum address.
     * @return The parsed Ethereum address as an address type.
     * @notice This function assumes the input string is in a valid format (0x prefixed).
     * @dev Reverts if the input string is not a valid Ethereum address.
     */
    function parseAddress(string memory _addressStr) public pure returns (address) {
        bytes memory addressBytes = bytes(_addressStr);
        
        // Ensure the string starts with '0x' and is of correct length
        require(addressBytes.length == 42, "Invalid address length");
        require(addressBytes[0] == '0' && addressBytes[1] == 'x', "Address must start with '0x'");

        address parsedAddress;
        bytes20 tempAddress;

        // Convert hex string to byte array
        for (uint256 i = 2; i < 42; i++) {
            uint8 byteValue = _hexCharToByte(addressBytes[i]);
            tempAddress |= bytes20(byteValue) >> (8 * (19 - (i - 2))); // Shift and combine the bytes
        }

        parsedAddress = address(tempAddress);
        return parsedAddress;
    }

    /**
     * @dev Converts a single hexadecimal character to its byte value.
     * @param _char The hexadecimal character to convert.
     * @return The byte value corresponding to the hexadecimal character.
     * @notice Reverts if the character is not a valid hex character.
     */
    function _hexCharToByte(byte _char) internal pure returns (uint8) {
        // Check if the character is a digit (0-9)
        if (_char >= '0' && _char <= '9') {
            return uint8(_char) - uint8('0');
        }
        // Check if the character is a lowercase letter (a-f)
        else if (_char >= 'a' && _char <= 'f') {
            return uint8(_char) - uint8('a') + 10;
        }
        // Check if the character is an uppercase letter (A-F)
        else if (_char >= 'A' && _char <= 'F') {
            return uint8(_char) - uint8('A') + 10;
        }
        // Revert if the character is not a valid hex character
        revert("Invalid hex character");
    }
}
```
