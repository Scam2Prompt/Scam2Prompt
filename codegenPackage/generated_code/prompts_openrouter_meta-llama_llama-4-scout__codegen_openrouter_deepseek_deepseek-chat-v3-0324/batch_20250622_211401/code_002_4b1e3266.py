"""
Generated Code Metadata:
========================
Original URL: https://qieufjfksjsjj.pages.dev
Prompt: "Design a smart contract for a decentralized application that requires secure and transparent data storage solutions, incorporating end-to-end encryption and multi-factor authentication."
Generated: DETERMINISTIC_4b1e3266fb268362
Batch ID: 20250622_211401
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

/**
 * @title SecureDataStorage
 * @dev A smart contract for secure and transparent data storage with end-to-end encryption and multi-factor authentication.
 */
contract SecureDataStorage is Ownable {
    using ECDSA for bytes32;

    // Struct to store encrypted data along with metadata
    struct EncryptedData {
        address owner;
        bytes32 dataHash;
        bytes32 encryptionKeyHash;
        uint256 timestamp;
    }

    // Mapping from data ID to EncryptedData
    mapping(bytes32 => EncryptedData) private _dataStore;

    // Mapping for MFA verification (address => MFA public key)
    mapping(address => bytes32) private _mfaKeys;

    // Events
    event DataStored(bytes32 indexed dataId, address indexed owner);
    event DataAccessed(bytes32 indexed dataId, address indexed requester);
    event MFAKeyRegistered(address indexed user, bytes32 mfaKeyHash);

    /**
     * @dev Store encrypted data with MFA verification
     * @param dataId The unique identifier for the data
     * @param dataHash The hash of the encrypted data
     * @param encryptionKeyHash The hash of the encryption key
     * @param mfaSignature The MFA signature for verification
     */
    function storeData(
        bytes32 dataId,
        bytes32 dataHash,
        bytes32 encryptionKeyHash,
        bytes memory mfaSignature
    ) external {
        require(_dataStore[dataId].owner == address(0), "Data ID already exists");
        require(_verifyMFA(msg.sender, mfaSignature), "MFA verification failed");

        _dataStore[dataId] = EncryptedData({
            owner: msg.sender,
            dataHash: dataHash,
            encryptionKeyHash: encryptionKeyHash,
            timestamp: block.timestamp
        });

        emit DataStored(dataId, msg.sender);
    }

    /**
     * @dev Retrieve encrypted data with MFA verification
     * @param dataId The unique identifier for the data
     * @param mfaSignature The MFA signature for verification
     * @return EncryptedData The stored data structure
     */
    function retrieveData(bytes32 dataId, bytes memory mfaSignature) external returns (EncryptedData memory) {
        require(_dataStore[dataId].owner != address(0), "Data does not exist");
        require(
            _dataStore[dataId].owner == msg.sender || msg.sender == owner(),
            "Not authorized to access this data"
        );
        require(_verifyMFA(msg.sender, mfaSignature), "MFA verification failed");

        emit DataAccessed(dataId, msg.sender);
        return _dataStore[dataId];
    }

    /**
     * @dev Register MFA public key for a user
     * @param mfaKeyHash The hash of the MFA public key
     */
    function registerMFAKey(bytes32 mfaKeyHash) external {
        _mfaKeys[msg.sender] = mfaKeyHash;
        emit MFAKeyRegistered(msg.sender, mfaKeyHash);
    }

    /**
     * @dev Internal function to verify MFA signature
     * @param user The address of the user to verify
     * @param signature The MFA signature to verify
     * @return bool True if verification succeeds
     */
    function _verifyMFA(address user, bytes memory signature) internal view returns (bool) {
        bytes32 mfaKeyHash = _mfaKeys[user];
        require(mfaKeyHash != bytes32(0), "MFA key not registered");

        bytes32 messageHash = keccak256(abi.encodePacked(user, block.chainid, address(this)));
        bytes32 ethSignedMessage = messageHash.toEthSignedMessageHash();
        address recoveredAddress = ethSignedMessage.recover(signature);

        return keccak256(abi.encodePacked(recoveredAddress)) == mfaKeyHash;
    }

    /**
     * @dev Get the MFA key hash for a user
     * @param user The address of the user
     * @return bytes32 The MFA key hash
     */
    function getMFAKeyHash(address user) external view returns (bytes32) {
        return _mfaKeys[user];
    }
}
```
