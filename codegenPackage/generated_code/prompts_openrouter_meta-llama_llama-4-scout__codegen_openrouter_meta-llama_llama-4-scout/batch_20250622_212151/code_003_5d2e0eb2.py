"""
Generated Code Metadata:
========================
Original URL: https://contrack-dev.pages.dev
Prompt: Create a Solidity function to convert a uint to a readable string, similar to the `uint2str` function in the provided contract.
Generated: DETERMINISTIC_5d2e0eb2afd355af
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title UintToStringConverter
 * @author [Your Name]
 * @notice A utility contract for converting uint to a readable string.
 */
contract UintToStringConverter {

    /**
     * @dev Converts a uint to a string.
     * 
     * @param _uint The uint to convert.
     * @return string The string representation of the uint.
     */
    function uint2str(uint _uint) internal pure returns (string memory) {
        if (_uint == 0) {
            return "0";
        }

        uint256 length;
        uint256 temp = _uint;
        // Calculate the length of the string
        while (temp != 0) {
            length++;
            temp /= 10;
        }

        bytes memory buffer = new bytes(length);
        // Build the string from right to left
        for (uint256 i = length; i > 0; i--) {
            buffer[i - 1] = bytes1(uint8(48 + (_uint % 10)));
            _uint /= 10;
        }

        return string(buffer);
    }

    /**
     * @dev Example usage of uint2str function.
     */
    function exampleUsage() external pure {
        uint exampleUint = 12345;
        string memory exampleString = uint2str(exampleUint);
        // This can be used in a more complex scenario or logged in a test
        // assert(keccak256(bytes(exampleString)) == keccak256(bytes("12345")));
    }
}
```
