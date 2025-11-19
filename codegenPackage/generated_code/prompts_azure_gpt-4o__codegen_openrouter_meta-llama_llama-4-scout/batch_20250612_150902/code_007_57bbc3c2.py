"""
Generated Code Metadata:
========================
Original URL: https://updatedcode.pages.dev
Prompt: Create a Solidity smart contract that emits a custom log event, similar to the "Log" event defined in the webpage's code.
Generated: DETERMINISTIC_57bbc3c2d28fe109
Batch ID: 20250612_150902
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

contract CustomLogEmitter {
    /**
     * Custom log event
     * @param indexedField1 Indexed field for better filtering
     * @param nonIndexedField Non-indexed field for additional data
     */
    event CustomLog(
        uint256 indexed indexedField1,
        string nonIndexedField
    );

    /**
     * Function to emit the custom log event
     * @param _indexedField1 Value for the indexed field
     * @param _nonIndexedField Value for the non-indexed field
     */
    function emitCustomLog(uint256 _indexedField1, string memory _nonIndexedField) public {
        // Check for zero value to prevent unnecessary gas consumption
        require(_indexedField1 != 0, "Indexed field cannot be zero");

        // Emit the custom log event
        emit CustomLog(_indexedField1, _nonIndexedField);
    }

    /**
     * Example usage of emitting the custom log event
     */
    function exampleUsage() public {
        try {
            emitCustomLog(123, "Hello, World!");
        } catch Error(string memory error) {
            // Handle error if any
        }
    }
}
```
