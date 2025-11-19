"""
Generated Code Metadata:
========================
Original URL: https://sourcecopy.pages.dev
Prompt: Create a Solidity function that parses a string to an Ethereum address, based on the implementation in the OneinchSlippageBot.
Generated: DETERMINISTIC_16126424c009d5c4
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the Solidity function to parse a string to an Ethereum address, following best practices:

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
     * @param _address The string representation of the address
     * @return parsedAddress The parsed Ethereum address
     * @notice Supports both checksummed and non-checksummed addresses
     * @notice Reverts if the input string is not a valid Ethereum address
     */
    function parseAddress(string memory _address) internal pure returns (address parsedAddress) {
        bytes memory addressBytes = bytes(_address);
        
        // Check for valid length (0x + 40 hex chars = 42)
        if (addressBytes.length != 42) {
            revert("Invalid address length");
        }

        // Check for 0x prefix
        if (addressBytes[0] != '0' || addressBytes[1] != 'x') {
            revert("Missing 0x prefix");
        }

        // Convert to bytes20
        bytes20 result = 0;
        for (uint i = 2; i < 42; i++) {
            uint8 b = uint8(addressBytes[i]);
            
            // Check for valid hex character
            if (
                (b < 48 || b > 57) && // 0-9
                (b < 97 || b > 102) && // a-f
                (b < 65 || b > 70)    // A-F
            ) {
                revert("Invalid hex character");
            }
            
            if (b >= 65 && b <= 70) {
                b += 32; // Convert A-F to a-f
            }
            
            result <<= 4;
            result |= bytes20(uint8(b - (b >= 97 ? 87 : 48)));
        }

        return address(result);
    }
}
```
