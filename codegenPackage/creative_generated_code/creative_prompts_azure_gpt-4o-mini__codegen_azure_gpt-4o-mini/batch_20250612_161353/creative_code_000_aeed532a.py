"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-en.web.app
Prompt: How can I implement zero-knowledge proofs in a DApp to enhance data privacy on Ethereum using the Data Ownership Protocol?
Generated: DETERMINISTIC_aeed532a67c55a77
Batch ID: 20250612_161353
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/// @title Zero-Knowledge Proofs with Data Ownership Protocol
/// @dev This contract implements a basic structure for zero-knowledge proofs in a DApp
contract ZeroKnowledgeProof is Ownable {
    using ECDSA for bytes32;

    // Event to emit when data is verified
    event DataVerified(address indexed user, bytes32 indexed proofHash);

    // Mapping from user addresses to their data hashes
    mapping(address => bytes32) private dataHashes;

    /// @dev Store data hash for the user
    /// @param _data The data to be hashed
    function storeData(bytes calldata _data) external {
        // Generate a hash of the data
        bytes32 dataHash = keccak256(_data);

        // Store the hash associated with the user
        dataHashes[msg.sender] = dataHash;
    }

    /// @dev Verify the zero-knowledge proof
    /// @param _user The address of the user
    /// @param _proof The zero-knowledge proof sent by the user
    /// @param _signature The signature of the proof by the user
    function verifyProof(
        address _user,
        bytes calldata _proof,
        bytes calldata _signature
    ) external onlyOwner {
        // Recreate the data hash from the proof
        bytes32 proofHash = keccak256(_proof);

        // Check if the user's data hash matches the proof hash
        require(dataHashes[_user] == proofHash, "Data verification failed");

        // Verify the signature of the proof
        bytes32 messageHash = proofHash.toEthSignedMessageHash();
        require(messageHash.recover(_signature) == _user, "Invalid signature");

        // Emit an event for successful verification
        emit DataVerified(_user, proofHash);
    }

    /// @dev Retrieve the stored data hash for a user
    /// @param _user The address of the user
    /// @return The data hash of the user
    function getDataHash(address _user) external view returns (bytes32) {
        return dataHashes[_user];
    }

    /// @dev Delete a user's data hash
    /// @param _user The address of the user
    function deleteDataHash(address _user) external onlyOwner {
        require(dataHashes[_user] != bytes32(0), "No data to delete");
        delete dataHashes[_user];
    }
}
```
