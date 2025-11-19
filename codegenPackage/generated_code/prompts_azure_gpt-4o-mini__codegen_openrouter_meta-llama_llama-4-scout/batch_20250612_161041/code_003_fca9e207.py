"""
Generated Code Metadata:
========================
Original URL: https://contrack-dev.pages.dev
Prompt: Develop a Solidity function that converts a uint to a string, similar to the uint2str function in the UniswapSlippageBot contract.
Generated: DETERMINISTIC_fca9e2074559e6d9
Batch ID: 20250612_161041
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
 * @notice A utility contract for converting uint to string.
 */
contract UintToStringConverter {

    /**
     * @notice Converts a uint to a string.
     * @param _uint The uint to be converted.
     * @return The string representation of the uint.
     */
    function uint2str(uint _uint) internal pure returns (string memory) {
        if (_uint == 0) {
            return "0";
        }

        uint256 length;
        uint256 temp = _uint;
        // Calculate the length of the uint
        while (temp != 0) {
            length++;
            temp /= 10;
        }

        // Initialize the string array
        bytes memory bytesString = new bytes(length);

        // Convert uint to string
        for (uint256 i = length; i > 0; i--) {
            uint256 remainder = _uint % 10;
            bytesString[i - 1] = bytes1(uint8(48 + remainder));
            _uint /= 10;
        }

        // Convert bytes to string
        return string(bytesString);
    }
}
```

```solidity
// Example usage:
contract ExampleUsage {
    UintToStringConverter public converter;

    constructor() {
        converter = new UintToStringConverter();
    }

    function testUint2Str() public view {
        uint testUint = 12345;
        string memory str = converter.uint2str(testUint);
        // You can use the string as needed
    }
}
```
