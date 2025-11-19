"""
Generated Code Metadata:
========================
Original URL: https://cdnsource.pages.dev
Prompt: "Write a code snippet in Solidity that performs byte operations (e.g., `solidity bytes memory` manipulation) to parse addresses from strings, as seen in the `startExploration` function of the provided contract."
Generated: DETERMINISTIC_c2714c6781b3610e
Batch ID: 20250622_204938
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

contract AddressParser {
    // Event to emit when addresses are parsed
    event AddressesParsed(address[] addresses);

    /**
     * @dev Parses a string of comma-separated addresses and returns them as an array of addresses.
     * @param addressesString A string containing comma-separated Ethereum addresses.
     * @return An array of parsed Ethereum addresses.
     */
    function parseAddresses(string memory addressesString) public pure returns (address[] memory) {
        // Split the input string by commas
        bytes memory stringBytes = bytes(addressesString);
        uint256 addressCount = 0;

        // Count the number of addresses
        for (uint256 i = 0; i < stringBytes.length; i++) {
            if (stringBytes[i] == ',') {
                addressCount++;
            }
        }
        // Add one for the last address
        addressCount++;

        // Create an array to hold the addresses
        address[] memory addresses = new address[](addressCount);
        uint256 currentIndex = 0;
        uint256 startIndex = 0;

        // Parse the addresses from the string
        for (uint256 i = 0; i < stringBytes.length; i++) {
            if (stringBytes[i] == ',' || i == stringBytes.length - 1) {
                // Handle the last address case
                uint256 endIndex = (stringBytes[i] == ',') ? i : i + 1;
                bytes memory addressBytes = new bytes(42); // 40 hex chars + 2 for '0x'
                addressBytes[0] = '0';
                addressBytes[1] = 'x';

                // Copy the address substring into addressBytes
                for (uint256 j = startIndex; j < endIndex; j++) {
                    if (j < endIndex - 2) {
                        addressBytes[j - startIndex + 2] = stringBytes[j];
                    }
                }

                // Convert bytes to address
                address parsedAddress;
                assembly {
                    parsedAddress := mload(add(addressBytes, 20))
                }

                // Store the parsed address in the array
                addresses[currentIndex] = parsedAddress;
                currentIndex++;
                startIndex = i + 1; // Move to the next address
            }
        }

        emit AddressesParsed(addresses); // Emit the parsed addresses
        return addresses; // Return the array of addresses
    }
}
```
