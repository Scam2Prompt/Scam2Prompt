"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Develop an onchain identity management system in Solidity that ensures compliance with KYC/AML regulations for institutional users, inspired by Singularity Finance's identity solutions.
Generated: DETERMINISTIC_88f1a0a95f6a6bc8
Batch ID: 20250612_145831
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Onchain Identity Management System
 * @author [Your Name]
 * @notice This contract provides an onchain identity management system
 *          that ensures compliance with KYC/AML regulations for institutional users.
 */
contract OnchainIdentityManagementSystem is AccessControl, ReentrancyGuard {
    using Strings for uint256;

    // Mapping of user addresses to their respective identities
    mapping(address => Identity) public identities;

    // Mapping of identity hashes to their verification status
    mapping(bytes32 => bool) public verifiedIdentities;

    // Event emitted when a new identity is created
    event NewIdentity(address indexed user, bytes32 indexed identityHash);

    // Event emitted when an identity is verified
    event IdentityVerified(bytes32 indexed identityHash);

    // Event emitted when an identity is revoked
    event IdentityRevoked(bytes32 indexed identityHash);

    // Role for KYC/AML verifiers
    bytes32 public constant VERIFIER_ROLE = keccak256("VERIFIER_ROLE");

    /**
     * @dev Struct representing an identity
     * @param name User's name
     * @param email User's email
     * @param kycStatus User's KYC status
     * @param amlStatus User's AML status
     */
    struct Identity {
        string name;
        string email;
        bool kycStatus;
        bool amlStatus;
    }

    /**
     * @dev Constructor
     */
    constructor() {
        // Initialize roles
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(VERIFIER_ROLE, msg.sender);
    }

    /**
     * @dev Creates a new identity for a user
     * @param name User's name
     * @param email User's email
     */
    function createIdentity(string memory name, string memory email) public {
        require(identities[msg.sender].kycStatus == false, "Identity already exists");

        // Create a new identity
        Identity memory identity;
        identity.name = name;
        identity.email = email;
        identity.kycStatus = false;
        identity.amlStatus = false;

        // Store the identity
        identities[msg.sender] = identity;

        // Emit event
        emit NewIdentity(msg.sender, keccak256(abi.encodePacked(name, email)));
    }

    /**
     * @dev Verifies an identity
     * @param user User address
     * @param kycStatus User's KYC status
     * @param amlStatus User's AML status
     */
    function verifyIdentity(address user, bool kycStatus, bool amlStatus) public onlyRole(VERIFIER_ROLE) {
        require(identities[user].kycStatus == false, "Identity already verified");

        // Update identity status
        identities[user].kycStatus = kycStatus;
        identities[user].amlStatus = amlStatus;

        // Store verification status
        bytes32 identityHash = keccak256(abi.encodePacked(identities[user].name, identities[user].email));
        verifiedIdentities[identityHash] = true;

        // Emit event
        emit IdentityVerified(identityHash);
    }

    /**
     * @dev Revokes an identity
     * @param user User address
     */
    function revokeIdentity(address user) public onlyRole(VERIFIER_ROLE) {
        require(identities[user].kycStatus == true, "Identity not found");

        // Reset identity status
        identities[user].kycStatus = false;
        identities[user].amlStatus = false;

        // Remove verification status
        bytes32 identityHash = keccak256(abi.encodePacked(identities[user].name, identities[user].email));
        verifiedIdentities[identityHash] = false;

        // Emit event
        emit IdentityRevoked(identityHash);
    }

    /**
     * @dev Checks if an identity is verified
     * @param user User address
     * @return bool Verification status
     */
    function isVerified(address user) public view returns (bool) {
        bytes32 identityHash = keccak256(abi.encodePacked(identities[user].name, identities[user].email));
        return verifiedIdentities[identityHash];
    }
}
```
