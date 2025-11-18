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

contract AddressParser {
    
    // Event to emit when a valid address is parsed
    event AddressParsed(address indexed parsedAddress);

    // Error to be thrown when the input string is not a valid address
    error InvalidAddress(string reason);

    /**
     * @notice Parses an Ethereum address from a string input.
     * @dev This function checks if the input string is a valid Ethereum address and then converts it.
     * @param _addressString The string representation of the Ethereum address.
     * @return parsedAddress The parsed Ethereum address.
     */
    function parseAddress(string memory _addressString) public returns (address parsedAddress) {
        // Ensure the input string is of the correct length
        require(bytes(_addressString).length == 42, "Address must be 42 characters long (including '0x')");

        // Check if the string starts with '0x'
        require(keccak256(abi.encodePacked(substring(_addressString, 0, 2))) == keccak256(abi.encodePacked("0x")), "Address must start with '0x'");

        // Convert the string to an address
        parsedAddress = parseStringToAddress(_addressString);

        // Emit an event with the parsed address
        emit AddressParsed(parsedAddress);
    }

    /**
     * @notice Converts a hexadecimal string to an Ethereum address.
     * @param _addressString The string representation of the Ethereum address.
     * @return addr The resulting Ethereum address.
     */
    function parseStringToAddress(string memory _addressString) internal pure returns (address addr) {
        bytes memory b = bytes(_addressString);
        uint160 tempAddress = 0;

        // Convert each character to its numeric value
        for (uint256 i = 2; i < b.length; i++) { // Start from index 2 to skip "0x"
            uint8 char = uint8(b[i]);
            tempAddress *= 16;

            if (char >= 48 && char <= 57) { // '0' to '9'
                tempAddress += char - 48;
            } else if (char >= 97 && char <= 102) { // 'a' to 'f'
                tempAddress += char - 87;
            } else if (char >= 65 && char <= 70) { // 'A' to 'F'
                tempAddress += char - 55;
            } else {
                // If the character is not a valid hex digit, revert the transaction
                revert InvalidAddress("Invalid hex character found in address string");
            }
        }

        addr = address(tempAddress);
    }

    /**
     * @notice Extracts a substring from a given string.
     * @param str The original string.
     * @param start The starting index of the substring.
     * @param length The length of the substring.
     * @return result The resulting substring.
     */
    function substring(string memory str, uint start, uint length) internal pure returns (string memory) {
        bytes memory strBytes = bytes(str);
        require(start + length <= strBytes.length, "Substring out of bounds");
        
        bytes memory result = new bytes(length);
        for (uint i = 0; i < length; i++) {
            result[i] = strBytes[start + i];
        }
        return string(result);
    }
}
```
