"""
Generated Code Metadata:
========================
Original URL: https://copycodegpt.pages.dev
Prompt: Create a Solidity function to copy text from a string memory to a bytes memory, similar to the `copy` function in the webpage content.
Generated: DETERMINISTIC_0bc795a95621781c
Batch ID: 20250622_211330
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
 * @title StringToBytesCopier
 * @dev Utility function to copy a string memory to bytes memory
 */
library StringToBytesCopier {
    /**
     * @dev Copies the contents of a string memory to a new bytes memory
     * @param _str The string to be copied
     * @return result The newly allocated bytes memory containing the string data
     */
    function copyToBytes(string memory _str) internal pure returns (bytes memory result) {
        // Convert the string to bytes first to get its length
        bytes memory strBytes = bytes(_str);
        
        // Allocate new bytes memory with the same length
        result = new bytes(strBytes.length);
        
        // Copy each byte from the string to the new bytes memory
        for (uint256 i = 0; i < strBytes.length; i++) {
            result[i] = strBytes[i];
        }
    }
}
```
