"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Provide a code example for a decentralized identity management system using Ethereum, inspired by the themes discussed at ETHBerlin04.
Generated: DETERMINISTIC_1dd2b979aa1dcbdd
Batch ID: 20250612_150554
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

/**
 * @title DecentralizedIdentity
 * @dev A smart contract for managing decentralized identities on Ethereum
 */
contract DecentralizedIdentity is Ownable {
    using ECDSA for bytes32;

    // Struct to store identity information
    struct Identity {
        address owner;
        string metadataHash; // IPFS hash of identity metadata
        uint256 createdAt;
        uint256 updatedAt;
        bool revoked;
    }

    // Mapping from identity ID to Identity struct
    mapping(bytes32 => Identity) public identities;

    // Mapping from owner address to identity ID
    mapping(address => bytes32) public ownerToIdentity;

    // Events
    event IdentityCreated(bytes32 indexed identityId, address indexed owner, string metadataHash);
    event IdentityUpdated(bytes32 indexed identityId, string newMetadataHash);
    event IdentityRevoked(bytes32 indexed identityId);
    event IdentityReinstated(bytes32 indexed identityId);

    /**
     * @dev Creates a new identity
     * @param metadataHash IPFS hash of identity metadata
     * @param signature Signature from the identity owner
     */
    function createIdentity(string memory metadataHash, bytes memory signature) external {
        bytes32 identityId = keccak256(abi.encodePacked(msg.sender, metadataHash, block.timestamp));
        
        require(identities[identityId].owner == address(0), "Identity already exists");
        require(ownerToIdentity[msg.sender] == bytes32(0), "Address already has an identity");

        // Verify the signature
        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender, metadataHash));
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        require(signer == msg.sender, "Invalid signature");

        identities[identityId] = Identity({
            owner: msg.sender,
            metadataHash: metadataHash,
            createdAt: block.timestamp,
            updatedAt: block.timestamp,
            revoked: false
        });

        ownerToIdentity[msg.sender] = identityId;

        emit IdentityCreated(identityId, msg.sender, metadataHash);
    }

    /**
     * @dev Updates identity metadata
     * @param identityId The ID of the identity to update
     * @param newMetadataHash New IPFS hash of identity metadata
     * @param signature Signature from the identity owner
     */
    function updateIdentity(bytes32 identityId, string memory newMetadataHash, bytes memory signature) external {
        Identity storage identity = identities[identityId];
        
        require(identity.owner != address(0), "Identity does not exist");
        require(!identity.revoked, "Identity is revoked");
        require(identity.owner == msg.sender, "Not identity owner");

        // Verify the signature
        bytes32 messageHash = keccak256(abi.encodePacked(identityId, newMetadataHash));
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        require(signer == msg.sender, "Invalid signature");

        identity.metadataHash = newMetadataHash;
        identity.updatedAt = block.timestamp;

        emit IdentityUpdated(identityId, newMetadataHash);
    }

    /**
     * @dev Revokes an identity
     * @param identityId The ID of the identity to revoke
     */
    function revokeIdentity(bytes32 identityId) external {
        Identity storage identity = identities[identityId];
        
        require(identity.owner != address(0), "Identity does not exist");
        require(!identity.revoked, "Identity already revoked");
        require(identity.owner == msg.sender || msg.sender == owner(), "Not authorized");

        identity.revoked = true;
        identity.updatedAt = block.timestamp;

        emit IdentityRevoked(identityId);
    }

    /**
     * @dev Reinstates a revoked identity
     * @param identityId The ID of the identity to reinstate
     */
    function reinstateIdentity(bytes32 identityId) external {
        Identity storage identity = identities[identityId];
        
        require(identity.owner != address(0), "Identity does not exist");
        require(identity.revoked, "Identity not revoked");
        require(msg.sender == owner(), "Not authorized");

        identity.revoked = false;
        identity.updatedAt = block.timestamp;

        emit IdentityReinstated(identityId);
    }

    /**
     * @dev Verifies an identity
     * @param identityId The ID of the identity to verify
     * @return isValid Whether the identity is valid and not revoked
     */
    function verifyIdentity(bytes32 identityId) external view returns (bool isValid) {
        Identity memory identity = identities[identityId];
        return (identity.owner != address(0) && !identity.revoked);
    }

    /**
     * @dev Gets identity ID for an owner address
     * @param owner The owner address to query
     * @return identityId The ID of the identity
     */
    function getIdentityId(address owner) external view returns (bytes32 identityId) {
        return ownerToIdentity[owner];
    }
}
```
