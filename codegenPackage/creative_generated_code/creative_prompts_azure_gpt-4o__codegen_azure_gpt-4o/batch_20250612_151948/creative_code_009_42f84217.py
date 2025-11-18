"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Create a smart contract using Solidity for a decentralized identity system, as outlined in Ethereum.org's use case examples.
Generated: DETERMINISTIC_42f84217c9c2f320
Batch ID: 20250612_151948
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

/**
 * @title Decentralized Identity System
 * @dev This contract manages decentralized identities as a smart contract on Ethereum.
 * It allows users to create, update, and retrieve identities securely.
 */
contract DecentralizedIdentity {
    // Struct to store identity details
    struct Identity {
        string name;
        string email;
        string metadataHash; // Typically a hash pointing to off-chain metadata (e.g., IPFS)
        uint256 createdAt;   // Timestamp of identity creation
        uint256 updatedAt;   // Timestamp of last update
    }

    // Mapping to store identities by Ethereum address
    mapping(address => Identity) private identities;

    // Event emitted when an identity is created
    event IdentityCreated(address indexed user, string name, string email, string metadataHash);

    // Event emitted when an identity is updated
    event IdentityUpdated(address indexed user, string name, string email, string metadataHash);

    /**
     * @dev Modifier to ensure that the caller has an identity.
     */
    modifier identityExists() {
        require(bytes(identities[msg.sender].name).length != 0, "Identity does not exist.");
        _;
    }

    /**
     * @dev Create a new identity.
     * @param name The name of the user.
     * @param email The email of the user.
     * @param metadataHash The hash pointing to the user's metadata (e.g., IPFS).
     */
    function createIdentity(
        string memory name,
        string memory email,
        string memory metadataHash
    ) external {
        require(bytes(identities[msg.sender].name).length == 0, "Identity already exists.");
        require(bytes(name).length > 0, "Name cannot be empty.");
        require(bytes(email).length > 0, "Email cannot be empty.");

        identities[msg.sender] = Identity({
            name: name,
            email: email,
            metadataHash: metadataHash,
            createdAt: block.timestamp,
            updatedAt: block.timestamp
        });

        emit IdentityCreated(msg.sender, name, email, metadataHash);
    }

    /**
     * @dev Update an existing identity.
     * @param name The updated name of the user.
     * @param email The updated email of the user.
     * @param metadataHash The updated hash pointing to the user's metadata (e.g., IPFS).
     */
    function updateIdentity(
        string memory name,
        string memory email,
        string memory metadataHash
    ) external identityExists {
        require(bytes(name).length > 0, "Name cannot be empty.");
        require(bytes(email).length > 0, "Email cannot be empty.");

        Identity storage identity = identities[msg.sender];
        identity.name = name;
        identity.email = email;
        identity.metadataHash = metadataHash;
        identity.updatedAt = block.timestamp;

        emit IdentityUpdated(msg.sender, name, email, metadataHash);
    }

    /**
     * @dev Retrieve the identity details of the caller.
     * @return name The name of the user.
     * @return email The email of the user.
     * @return metadataHash The hash pointing to the user's metadata.
     * @return createdAt The timestamp when the identity was created.
     * @return updatedAt The timestamp of the last update.
     */
    function getIdentity()
        external
        view
        identityExists
        returns (
            string memory name,
            string memory email,
            string memory metadataHash,
            uint256 createdAt,
            uint256 updatedAt
        )
    {
        Identity memory identity = identities[msg.sender];
        return (
            identity.name,
            identity.email,
            identity.metadataHash,
            identity.createdAt,
            identity.updatedAt
        );
    }
}
```
