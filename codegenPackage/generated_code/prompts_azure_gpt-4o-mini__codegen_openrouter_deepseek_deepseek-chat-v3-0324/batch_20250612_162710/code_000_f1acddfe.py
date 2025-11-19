"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Generate a code snippet for a decentralized application that aligns with the themes discussed in the ETHBerlin04 hackathon, particularly focusing on identity solutions.
Generated: DETERMINISTIC_f1acddfe498518a7
Batch ID: 20250612_162710
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
 * @title Decentralized Identity Registry
 * @dev A smart contract for managing decentralized identities with attestations
 * Inspired by ETHBerlin04 themes of decentralized identity solutions
 */
contract DecentralizedIdentity is Ownable {
    using ECDSA for bytes32;

    // Struct to represent an identity
    struct Identity {
        address owner;
        bytes32 did; // Decentralized Identifier
        bool revoked;
        uint256 createdAt;
        uint256 revokedAt;
    }

    // Struct to represent an attestation
    struct Attestation {
        address attester;
        bytes32 attestationHash;
        uint256 validUntil;
        bool revoked;
    }

    // Mapping from DID to Identity
    mapping(bytes32 => Identity) public identities;

    // Mapping from DID to array of attestations
    mapping(bytes32 => Attestation[]) public attestations;

    // Events
    event IdentityRegistered(bytes32 indexed did, address indexed owner);
    event IdentityRevoked(bytes32 indexed did);
    event AttestationAdded(bytes32 indexed did, bytes32 indexed attestationHash, address attester);
    event AttestationRevoked(bytes32 indexed did, bytes32 indexed attestationHash);

    /**
     * @dev Registers a new decentralized identity
     * @param did The decentralized identifier
     * @param signature The signature proving ownership of the DID
     */
    function registerIdentity(bytes32 did, bytes memory signature) external {
        require(identities[did].owner == address(0), "Identity already exists");
        
        // Verify the signature
        bytes32 messageHash = keccak256(abi.encodePacked(did, msg.sender));
        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();
        address signer = ethSignedMessageHash.recover(signature);
        
        require(signer == msg.sender, "Invalid signature");

        identities[did] = Identity({
            owner: msg.sender,
            did: did,
            revoked: false,
            createdAt: block.timestamp,
            revokedAt: 0
        });

        emit IdentityRegistered(did, msg.sender);
    }

    /**
     * @dev Revokes an identity
     * @param did The decentralized identifier to revoke
     */
    function revokeIdentity(bytes32 did) external {
        Identity storage identity = identities[did];
        require(identity.owner == msg.sender, "Not identity owner");
        require(!identity.revoked, "Identity already revoked");

        identity.revoked = true;
        identity.revokedAt = block.timestamp;

        emit IdentityRevoked(did);
    }

    /**
     * @dev Adds an attestation to an identity
     * @param did The decentralized identifier
     * @param attestationHash The hash of the attestation data
     * @param validUntil The timestamp until which the attestation is valid
     */
    function addAttestation(
        bytes32 did,
        bytes32 attestationHash,
        uint256 validUntil
    ) external {
        Identity storage identity = identities[did];
        require(identity.owner != address(0), "Identity does not exist");
        require(!identity.revoked, "Identity is revoked");

        attestations[did].push(Attestation({
            attester: msg.sender,
            attestationHash: attestationHash,
            validUntil: validUntil,
            revoked: false
        }));

        emit AttestationAdded(did, attestationHash, msg.sender);
    }

    /**
     * @dev Revokes an attestation
     * @param did The decentralized identifier
     * @param attestationIndex The index of the attestation to revoke
     */
    function revokeAttestation(bytes32 did, uint256 attestationIndex) external {
        require(attestations[did].length > attestationIndex, "Invalid attestation index");
        
        Attestation storage attestation = attestations[did][attestationIndex];
        require(attestation.attester == msg.sender, "Not attestation owner");
        require(!attestation.revoked, "Attestation already revoked");

        attestation.revoked = true;
        emit AttestationRevoked(did, attestation.attestationHash);
    }

    /**
     * @dev Gets all attestations for a DID
     * @param did The decentralized identifier
     * @return Array of attestations
     */
    function getAttestations(bytes32 did) external view returns (Attestation[] memory) {
        return attestations[did];
    }

    /**
     * @dev Verifies if an attestation is valid
     * @param did The decentralized identifier
     * @param attestationIndex The index of the attestation to verify
     * @return True if the attestation is valid
     */
    function verifyAttestation(bytes32 did, uint256 attestationIndex) external view returns (bool) {
        require(attestations[did].length > attestationIndex, "Invalid attestation index");
        
        Attestation storage attestation = attestations[did][attestationIndex];
        return !attestation.revoked && 
               attestation.validUntil > block.timestamp &&
               !identities[did].revoked;
    }
}
```
