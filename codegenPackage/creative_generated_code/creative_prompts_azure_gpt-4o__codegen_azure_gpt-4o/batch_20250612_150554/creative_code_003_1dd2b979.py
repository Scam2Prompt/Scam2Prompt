"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Provide a code example for a decentralized identity management system using Ethereum, inspired by the themes discussed at ETHBerlin04.
Generated: DETERMINISTIC_1dd2b979aa1dcbdd
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// A decentralized identity management system using Ethereum

/**
 * @title Decentralized Identity Management System
 * @dev Inspired by ETHBerlin04's focus on decentralized identity.
 */
contract DecentralizedIdentity {
    // Event emitted when a new identity is created
    event IdentityCreated(address indexed user, string name, string metadataUri);

    // Event emitted when an identity's metadata URI is updated
    event IdentityUpdated(address indexed user, string metadataUri);

    // Struct to represent an identity
    struct Identity {
        string name;         // Name of the user
        string metadataUri;  // URI pointing to additional metadata (e.g., IPFS or Arweave)
        uint256 createdAt;   // Timestamp of creation
        uint256 updatedAt;   // Timestamp of last update
    }

    // Mapping to store identities by user address
    mapping(address => Identity) private identities;

    // Modifier to ensure that the caller has already created an identity
    modifier identityExists(address user) {
        require(bytes(identities[user].name).length > 0, "Identity does not exist");
        _;
    }

    // Modifier to ensure that the caller has not already created an identity
    modifier identityDoesNotExist(address user) {
        require(bytes(identities[user].name).length == 0, "Identity already exists");
        _;
    }

    /**
     * @notice Create a new identity
     * @param name The name of the user
     * @param metadataUri A URI with additional metadata for the identity
     */
    function createIdentity(string memory name, string memory metadataUri)
        external
        identityDoesNotExist(msg.sender)
    {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(metadataUri).length > 0, "Metadata URI cannot be empty");

        // Store the new identity in the mapping
        identities[msg.sender] = Identity({
            name: name,
            metadataUri: metadataUri,
            createdAt: block.timestamp,
            updatedAt: block.timestamp
        });

        // Emit an event for the new identity
        emit IdentityCreated(msg.sender, name, metadataUri);
    }

    /**
     * @notice Update the metadata URI of an existing identity
     * @param metadataUri The new URI with additional metadata for the identity
     */
    function updateMetadataUri(string memory metadataUri)
        external
        identityExists(msg.sender)
    {
        require(bytes(metadataUri).length > 0, "Metadata URI cannot be empty");

        // Update the metadata URI and the updatedAt timestamp
        identities[msg.sender].metadataUri = metadataUri;
        identities[msg.sender].updatedAt = block.timestamp;

        // Emit an event for the update
        emit IdentityUpdated(msg.sender, metadataUri);
    }

    /**
     * @notice Retrieve an identity by address
     * @param user The address of the user whose identity is being retrieved
     * @return name The name of the user
     * @return metadataUri The metadata URI associated with the identity
     * @return createdAt The timestamp when the identity was created
     * @return updatedAt The timestamp when the identity was last updated
     */
    function getIdentity(address user)
        external
        view
        identityExists(user)
        returns (string memory name, string memory metadataUri, uint256 createdAt, uint256 updatedAt)
    {
        Identity memory identity = identities[user];
        return (identity.name, identity.metadataUri, identity.createdAt, identity.updatedAt);
    }

    /**
     * @notice Check if an identity exists for a given address
     * @param user The address to check existence for
     * @return bool True if the identity exists, false otherwise
     */
    function identityExistsFor(address user) external view returns (bool) {
        return bytes(identities[user].name).length > 0;
    }
}
```
