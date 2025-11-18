"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codecopyed.pages.dev
Prompt: Implement a Solidity function that hashes long needles using `keccak256` to optimize contract searches, as shown in the "1inch Slippage Bot" example.
Generated: DETERMINISTIC_b28ed5c23f66c37e
Batch ID: 20250612_145821
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

contract NeedleHashing {
    // Mapping to store hashes of long needles
    mapping(bytes32 => bool) private needleHashes;

    /// @notice Hashes a long needle using keccak256 and stores it in the contract
    /// @param needle The long needle string to be hashed
    /// @return hash The keccak256 hash of the needle
    function storeNeedleHash(string memory needle) public returns (bytes32 hash) {
        // Validate the needle length
        require(bytes(needle).length > 0, "Needle cannot be empty");

        // Hash the needle using keccak256
        hash = keccak256(abi.encodePacked(needle));

        // Check if the hash already exists
        require(!needleHashes[hash], "Hash already exists");

        // Store the hash in the mapping
        needleHashes[hash] = true;
    }

    /// @notice Checks if a given needle hash is stored in the contract
    /// @param needle The long needle string whose hash is to be checked
    /// @return exists True if the hash of the needle exists, false otherwise
    function checkNeedleExists(string memory needle) public view returns (bool exists) {
        // Hash the needle using keccak256
        bytes32 hash = keccak256(abi.encodePacked(needle));
        
        // Check if the hash exists in the mapping
        return needleHashes[hash];
    }
}
```
