"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: How can I implement onchain identity management in a decentralized application (dApp) to ensure KYC/AML compliance, as described in Singularity Finance?
Generated: DETERMINISTIC_083552825e68598f
Batch ID: 20250612_160038
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
 * @title Onchain Identity Management for KYC/AML Compliance
 * @author Singularity Finance
 * @notice This contract manages onchain identities for a decentralized application (dApp)
 *         to ensure compliance with KYC and AML regulations.
 */

contract IdentityManagement {
    // Struct to store identity information
    struct Identity {
        bool isVerified; // Indicates if the identity is verified for KYC/AML compliance
        string metadataHash; // IPFS or other decentralized storage hash for identity metadata
    }

    // Mapping of Ethereum addresses to their associated identities
    mapping(address => Identity) private identities;

    // Address of the contract owner (administrator)
    address private owner;

    // Events
    event IdentityAdded(address indexed user, string metadataHash);
    event IdentityVerified(address indexed user);
    event IdentityRemoved(address indexed user);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner");
        _;
    }

    // Constructor to set the contract owner upon deployment
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Add a new identity to the system.
     * @dev Only the owner can call this function.
     * @param _user Address of the user whose identity is being added.
     * @param _metadataHash Hash of the user's identity metadata.
     */
    function addIdentity(address _user, string memory _metadataHash) external onlyOwner {
        require(_user != address(0), "Invalid address");
        require(bytes(_metadataHash).length > 0, "Metadata hash cannot be empty");

        identities[_user] = Identity({
            isVerified: false,
            metadataHash: _metadataHash
        });

        emit IdentityAdded(_user, _metadataHash);
    }

    /**
     * @notice Verify a user's identity for KYC/AML compliance.
     * @dev Only the owner can call this function.
     * @param _user Address of the user whose identity is being verified.
     */
    function verifyIdentity(address _user) external onlyOwner {
        require(identities[_user].isVerified == false, "Identity already verified");
        require(bytes(identities[_user].metadataHash).length > 0, "Identity must exist");

        identities[_user].isVerified = true;

        emit IdentityVerified(_user);
    }

    /**
     * @notice Remove a user's identity from the system.
     * @dev Only the owner can call this function.
     * @param _user Address of the user whose identity is being removed.
     */
    function removeIdentity(address _user) external onlyOwner {
        require(bytes(identities[_user].metadataHash).length > 0, "Identity must exist");

        delete identities[_user];

        emit IdentityRemoved(_user);
    }

    /**
     * @notice Retrieve the identity metadata and verification status of a user.
     * @param _user Address of the user whose identity is being queried.
     * @return isVerified Whether the identity is verified or not.
     * @return metadataHash Hash of the identity metadata.
     */
    function getIdentity(address _user) external view returns (bool isVerified, string memory metadataHash) {
        require(bytes(identities[_user].metadataHash).length > 0, "Identity does not exist");

        Identity memory identity = identities[_user];
        return (identity.isVerified, identity.metadataHash);
    }

    /**
     * @notice Transfer ownership of the contract to a new owner.
     * @dev Only the current owner can call this function.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid address");
        owner = _newOwner;
    }
}
```
