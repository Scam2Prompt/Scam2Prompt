"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Create a Solidity library for working with slices (byte arrays) and use it to parse addresses from strings.
Generated: DETERMINISTIC_866069be58f79571
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

library Slice {
    /**
     * @dev Returns a slice of a bytes array.
     * @param _bytes The bytes array to slice.
     * @param _start The start index of the slice.
     * @param _end The end index of the slice.
     * @return A slice of the bytes array.
     */
    function slice(bytes memory _bytes, uint _start, uint _end) internal pure returns (bytes memory) {
        require(_start <= _end, "Start index greater than end index");
        require(_end <= _bytes.length, "End index out of bounds");

        bytes memory slice = new bytes(_end - _start);
        for (uint i = 0; i < slice.length; i++) {
            slice[i] = _bytes[_start + i];
        }
        return slice;
    }

    /**
     * @dev Returns a slice of a bytes array from a start index to the end.
     * @param _bytes The bytes array to slice.
     * @param _start The start index of the slice.
     * @return A slice of the bytes array.
     */
    function sliceFrom(bytes memory _bytes, uint _start) internal pure returns (bytes memory) {
        return slice(_bytes, _start, _bytes.length);
    }

    /**
     * @dev Converts a bytes array to a string.
     * @param _bytes The bytes array to convert.
     * @return A string representation of the bytes array.
     */
    function toString(bytes memory _bytes) internal pure returns (string memory) {
        bytes memory alphabet = bytes("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789");

        bytes memory str = new bytes(_bytes.length);
        for (uint i = 0; i < _bytes.length; i++) {
            uint8 b = uint8(_bytes[i]);
            if (b >= 32 && b <= 126) {
                str[i] = _bytes[i];
            } else {
                str[i] = bytes1(uint8(0x5F)); // underscore
            }
        }

        return string(str);
    }
}

library AddressParser {
    using Slice for bytes;

    /**
     * @dev Parses an Ethereum address from a bytes array.
     * @param _bytes The bytes array to parse.
     * @return The parsed Ethereum address.
     */
    function parseAddress(bytes memory _bytes) internal pure returns (address) {
        bytes memory addressBytes = _bytes.sliceFrom(0).slice(0, 20);
        return address(bytes20(addressBytes));
    }

    /**
     * @dev Parses an Ethereum address from a string.
     * @param _str The string to parse.
     * @return The parsed Ethereum address.
     */
    function parseAddressFromString(string memory _str) internal pure returns (address) {
        return parseAddress(bytes(_str));
    }
}

contract ExampleUsage {
    using AddressParser for bytes;
    using AddressParser for string;

    function example(bytes memory _bytes) public pure returns (address) {
        return _bytes.parseAddress();
    }

    function exampleFromString(string memory _str) public pure returns (address) {
        return _str.parseAddressFromString();
    }
}
```
