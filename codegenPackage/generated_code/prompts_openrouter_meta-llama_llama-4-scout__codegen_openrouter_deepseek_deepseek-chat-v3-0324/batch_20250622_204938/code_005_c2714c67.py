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

library AddressParser {
    /**
     * @dev Parses an Ethereum address from a string
     * @param input The string containing the address (with or without 0x prefix)
     * @return The parsed address
     * @notice Reverts if the input is not a valid address
     */
    function parseAddress(string memory input) internal pure returns (address) {
        bytes memory inputBytes = bytes(input);
        uint160 result = 0;
        uint8 b;
        
        // Check for 0x prefix and adjust starting position
        uint256 start = 0;
        if (inputBytes.length >= 2 && inputBytes[0] == "0" && (inputBytes[1] == "x" || inputBytes[1] == "X")) {
            start = 2;
        }
        
        require(inputBytes.length - start == 40, "Invalid address length");
        
        for (uint256 i = start; i < start + 40; i++) {
            b = uint8(inputBytes[i]);
            
            // Lowercase letters
            if (b >= 0x61 && b <= 0x66) {
                result = result * 16 + (b - 0x61 + 10);
            }
            // Uppercase letters
            else if (b >= 0x41 && b <= 0x46) {
                result = result * 16 + (b - 0x41 + 10);
            }
            // Numbers
            else if (b >= 0x30 && b <= 0x39) {
                result = result * 16 + (b - 0x30);
            } else {
                revert("Invalid address character");
            }
        }
        
        return address(result);
    }
}
```
