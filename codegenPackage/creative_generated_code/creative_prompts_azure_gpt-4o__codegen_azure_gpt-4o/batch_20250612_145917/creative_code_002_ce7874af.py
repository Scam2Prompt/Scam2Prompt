"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdnsource.pages.dev
Prompt: Create a Solidity function that parses a string into an Ethereum address, similar to the `startExploration` function in the Oneinch Slippage Bot contract.
Generated: DETERMINISTIC_ce7874af4cf98d43
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
 * @dev Provides functionality to parse a string into an Ethereum address.
 */
contract AddressParser {
    /**
     * @dev Parses a string and converts it to an Ethereum address.
     * @param _input The string representation of the Ethereum address (e.g., "0x1234...").
     * @return parsedAddress The Ethereum address parsed from the string.
     */
    function parseStringToAddress(string memory _input) public pure returns (address parsedAddress) {
        require(bytes(_input).length == 42, "Invalid address length"); // Check the length (42 chars for 0x-prefixed address)
        require(bytes(_input)[0] == '0' && bytes(_input)[1] == 'x', "Address must start with '0x'"); // Check prefix

        // Use assembly to parse the string into an address.
        bytes memory inputBytes = bytes(_input);
        assembly {
            // Load the memory pointer of `inputBytes` and skip the first 2 bytes ("0x").
            parsedAddress := mload(add(inputBytes, 20)) // 20 = 32 (word size) - 12 (address size)
        }

        require(parsedAddress != address(0), "Parsed address cannot be the zero address"); // Ensure parsedAddress is valid
    }
}
```
