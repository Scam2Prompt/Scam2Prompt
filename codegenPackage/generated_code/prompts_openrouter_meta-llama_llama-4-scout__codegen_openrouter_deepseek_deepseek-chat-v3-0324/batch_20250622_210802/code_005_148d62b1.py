"""
Generated Code Metadata:
========================
Original URL: https://rootprotocol.pages.dev
Prompt: Design a smart contract to manage decentralized identities on the ISME platform.
Generated: DETERMINISTIC_148d62b133181d58
Batch ID: 20250622_210802
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

/**
 * @title ISME Identity Management Contract
 * @dev Manages decentralized identities on the ISME platform
 */
contract ISMEIdentityManager {
    // Struct to represent a decentralized identity
    struct Identity {
        address owner;
        string did; // Decentralized Identifier
        string metadataHash; // IPFS hash of identity metadata
        uint256 createdAt;
        uint256 updatedAt;
        bool isActive;
    }

    // Mapping from DID to Identity
    mapping(string => Identity) public identities;

    // Mapping from owner address to their DIDs
    mapping(address => string[]) public ownerToDIDs;

    // Events
    event IdentityCreated(
        string indexed did,
        address indexed owner,
        string metadataHash,
        uint256 timestamp
    );
    event IdentityUpdated(
        string indexed did,
        string newMetadataHash,
        uint256 timestamp
    );
    event IdentityDeactivated(string indexed did, uint256 timestamp);
    event IdentityReactivated(string indexed did, uint256 timestamp);

    // Modifiers
    modifier onlyIdentityOwner(string memory did) {
        require(
            identities[did].owner == msg.sender,
            "ISME: Only identity owner can perform this action"
        );
        _;
    }

    modifier identityExists(string memory did) {
        require(
            identities[did].createdAt != 0,
            "ISME: Identity does not exist"
        );
        _;
    }

    modifier identityActive(string memory did) {
        require(
            identities[did].isActive,
            "ISME: Identity is not active"
        );
        _;
    }

    /**
     * @dev Create a new decentralized identity
     * @param did The decentralized identifier
     * @param metadataHash IPFS hash of identity metadata
     */
    function createIdentity(string memory did, string memory metadataHash) external {
        require(
            identities[did].createdAt == 0,
            "ISME: Identity already exists"
        );
        require(
            bytes(did).length > 0,
            "ISME: DID cannot be empty"
        );
        require(
            bytes(metadataHash).length > 0,
            "ISME: Metadata hash cannot be empty"
        );

        Identity memory newIdentity = Identity({
            owner: msg.sender,
            did: did,
            metadataHash: metadataHash,
            createdAt: block.timestamp,
            updatedAt: block.timestamp,
            isActive: true
        });

        identities[did] = newIdentity;
        ownerToDIDs[msg.sender].push(did);

        emit IdentityCreated(did, msg.sender, metadataHash, block.timestamp);
    }

    /**
     * @dev Update identity metadata
     * @param did The decentralized identifier
     * @param newMetadataHash New IPFS hash of identity metadata
     */
    function updateIdentity(
        string memory did,
        string memory newMetadataHash
    ) external identityExists(did) onlyIdentityOwner(did) identityActive(did) {
        require(
            bytes(newMetadataHash).length > 0,
            "ISME: Metadata hash cannot be empty"
        );

        identities[did].metadataHash = newMetadataHash;
        identities[did].updatedAt = block.timestamp;

        emit IdentityUpdated(did, newMetadataHash, block.timestamp);
    }

    /**
     * @dev Deactivate an identity
     * @param did The decentralized identifier to deactivate
     */
    function deactivateIdentity(
        string memory did
    ) external identityExists(did) onlyIdentityOwner(did) identityActive(did) {
        identities[did].isActive = false;
        identities[did].updatedAt = block.timestamp;

        emit IdentityDeactivated(did, block.timestamp);
    }

    /**
     * @dev Reactivate an identity
     * @param did The decentralized identifier to reactivate
     */
    function reactivateIdentity(
        string memory did
    ) external identityExists(did) onlyIdentityOwner(did) {
        require(
            !identities[did].isActive,
            "ISME: Identity is already active"
        );

        identities[did].isActive = true;
        identities[did].updatedAt = block.timestamp;

        emit IdentityReactivated(did, block.timestamp);
    }

    /**
     * @dev Get all DIDs owned by an address
     * @param owner The address to query
     * @return Array of DIDs owned by the address
     */
    function getDIDsByOwner(address owner) external view returns (string[] memory) {
        return ownerToDIDs[owner];
    }

    /**
     * @dev Get identity details by DID
     * @param did The decentralized identifier to query
     * @return Identity details
     */
    function getIdentity(
        string memory did
    ) external view identityExists(did) returns (Identity memory) {
        return identities[did];
    }

    /**
     * @dev Check if an identity exists and is active
     * @param did The decentralized identifier to check
     * @return True if identity exists and is active, false otherwise
     */
    function isIdentityActive(string memory did) external view returns (bool) {
        return identities[did].isActive && identities[did].createdAt != 0;
    }
}
```
