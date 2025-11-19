"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Create a Solidity function that parses a string to an Ethereum address, inspired by the address parsing logic in the OneinchSlippageBot.
Generated: DETERMINISTIC_5f4df3c4690630bc
Batch ID: 20250612_163156
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
     * @dev Parses a string to an Ethereum address.
     * @param _addressString The string representation of the Ethereum address.
     * @return addr The parsed Ethereum address.
     * @notice Will revert if the input string is not a valid Ethereum address.
     */
    function parseAddress(string memory _addressString) public pure returns (address addr) {
        bytes memory addressBytes = bytes(_addressString);

        // Check if the string has the correct length for an Ethereum address
        require(addressBytes.length == 42, "Invalid address length");

        // Check if the address starts with '0x'
        require(addressBytes[0] == '0' && addressBytes[1] == 'x', "Address must start with '0x'");

        // Convert string to address
        uint160 parsedAddress;
        for (uint256 i = 2; i < 42; i++) {
            parsedAddress <<= 4; // Shift left by 4 bits (1 hex character)
            uint8 hexValue = uint8(addressBytes[i]);
            if (hexValue >= 48 && hexValue <= 57) { // '0' to '9'
                parsedAddress |= (hexValue - 48);
            } else if (hexValue >= 97 && hexValue <= 102) { // 'a' to 'f'
                parsedAddress |= (hexValue - 87);
            } else if (hexValue >= 65 && hexValue <= 70) { // 'A' to 'F'
                parsedAddress |= (hexValue - 55);
            } else {
                revert("Invalid character in address string");
            }
        }

        // Return the parsed address
        addr = address(parsedAddress);
    }
}
```
