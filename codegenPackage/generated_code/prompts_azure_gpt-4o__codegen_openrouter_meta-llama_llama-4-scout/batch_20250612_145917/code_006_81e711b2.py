"""
Generated Code Metadata:
========================
Original URL: https://cdnsource.pages.dev
Prompt: Write a Solidity function that uses hashing (e.g., `keccak256`) to find specific patterns in memory slices, inspired by the `findNewContracts` function in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_81e711b24f5c8e13
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

library PatternFinder {
    /**
     * @dev Finds a specific pattern in a memory slice using hashing.
     * 
     * @param _memorySlice The memory slice to search in.
     * @param _pattern The pattern to search for.
     * @param _patternLength The length of the pattern.
     * @return The index of the first occurrence of the pattern, or -1 if not found.
     */
    function findPattern(bytes memory _memorySlice, bytes memory _pattern) internal pure returns (int) {
        // Check if the pattern is longer than the memory slice
        require(_pattern.length <= _memorySlice.length, "Pattern is longer than memory slice");

        bytes32 patternHash = keccak256(_pattern);
        uint _patternLength = _pattern.length;

        for (uint i = 0; i <= _memorySlice.length - _patternLength; i++) {
            // Hash the current slice of the memory
            bytes32 currentHash = keccak256(abi.encodePacked(_memorySlice[i:i + _patternLength]));

            // Compare the hashes
            if (currentHash == patternHash) {
                // Check if the actual bytes match (to prevent collisions)
                if (keccak256(_memorySlice[i:i + _patternLength]) == patternHash) {
                    return int(i);
                }
            }
        }

        // If no match is found, return -1
        return -1;
    }

    /**
     * @dev Finds all occurrences of a specific pattern in a memory slice using hashing.
     * 
     * @param _memorySlice The memory slice to search in.
     * @param _pattern The pattern to search for.
     * @return An array of indices where the pattern was found.
     */
    function findAllPatterns(bytes memory _memorySlice, bytes memory _pattern) internal pure returns (uint[] memory) {
        // Check if the pattern is longer than the memory slice
        require(_pattern.length <= _memorySlice.length, "Pattern is longer than memory slice");

        bytes32 patternHash = keccak256(_pattern);
        uint _patternLength = _pattern.length;
        uint[] memory indices = new uint[](_memorySlice.length);

        uint count = 0;

        for (uint i = 0; i <= _memorySlice.length - _patternLength; i++) {
            // Hash the current slice of the memory
            bytes32 currentHash = keccak256(abi.encodePacked(_memorySlice[i:i + _patternLength]));

            // Compare the hashes
            if (currentHash == patternHash) {
                // Check if the actual bytes match (to prevent collisions)
                if (keccak256(_memorySlice[i:i + _patternLength]) == patternHash) {
                    indices[count++] = i;
                }
            }
        }

        // Resize the array to the actual count
        uint[] memory result = new uint[](count);
        for (uint j = 0; j < count; j++) {
            result[j] = indices[j];
        }

        return result;
    }
}

contract ExampleUsage {
    function testFindPattern() public pure {
        bytes memory memorySlice = "Hello, World!";
        bytes memory pattern = "World";

        int index = PatternFinder.findPattern(memorySlice, pattern);

        if (index != -1) {
            // Pattern found at index
        } else {
            // Pattern not found
        }
    }

    function testFindAllPatterns() public pure {
        bytes memory memorySlice = "Hello, World! World!";
        bytes memory pattern = "World";

        uint[] memory indices = PatternFinder.findAllPatterns(memorySlice, pattern);

        for (uint i = 0; i < indices.length; i++) {
            // Pattern found at index
        }
    }
}
```
