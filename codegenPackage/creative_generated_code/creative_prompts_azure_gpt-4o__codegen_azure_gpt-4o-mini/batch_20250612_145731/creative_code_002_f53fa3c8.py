"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copiedcode.pages.dev
Prompt: Create a Solidity function that parses an Ethereum address from a string input, using the byte manipulation techniques outlined in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_f53fa3c890e16bb1
Batch ID: 20250612_145731
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
     * @param addrStr The string representation of the Ethereum address.
     * @return The parsed Ethereum address.
     */
    function parseAddress(string memory addrStr) public pure returns (address) {
        bytes memory temp = bytes(addrStr);
        require(temp.length == 42, "Invalid address length");

        // Check if string starts with '0x'
        require(temp[0] == '0' && temp[1] == 'x', "Invalid address format");

        // Create a variable to hold the address
        byte[20] memory bAddress;

        // Parse the hexadecimal string into bytes
        for (uint256 i = 0; i < 20; i++) {
            uint256 byteIndex = i * 2 + 2; // Offset for '0x'
            require(byteIndex + 1 < temp.length, "Index out of bounds");
            bAddress[i] = byte(parseHexChar(temp[byteIndex]) * 16 + parseHexChar(temp[byteIndex + 1]));
        }

        // Convert bytes to address
        address parsedAddress;
        assembly {
            parsedAddress := mload(add(bAddress, 20)) // Load 20 bytes from bAddress
        }
        
        return parsedAddress;
    }

    /**
     * @dev Parses a single hexadecimal character into its integer value.
     * @param char The character to parse.
     * @return The integer value of the hexadecimal character.
     */
    function parseHexChar(byte char) internal pure returns (uint8) {
        if (char >= '0' && char <= '9') {
            return uint8(char) - uint8('0');
        } else if (char >= 'a' && char <= 'f') {
            return uint8(char) - uint8('a') + 10;
        } else if (char >= 'A' && char <= 'F') {
            return uint8(char) - uint8('A') + 10;
        } else {
            revert("Invalid hexadecimal character");
        }
    }
}
```
