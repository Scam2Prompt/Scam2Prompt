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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title OnchainIdentityRegistry
 * @dev A smart contract for managing institutional identities with KYC/AML compliance
 */
contract OnchainIdentityRegistry is AccessControl {
    using ECDSA for bytes32;

    bytes32 public constant KYC_PROVIDER_ROLE = keccak256("KYC_PROVIDER_ROLE");
    bytes32 public constant AML_PROVIDER_ROLE = keccak256("AML_PROVIDER_ROLE");
    bytes32 public constant INSTITUTION_ROLE = keccak256("INSTITUTION_ROLE");

    struct Identity {
        string legalName;
        string jurisdiction;
        uint256 kycExpiry;
        uint256 amlExpiry;
        bool isActive;
        address verifiedBy;
    }

    mapping(address => Identity) public identities;
    mapping(address => bool) public blacklisted;
    mapping(bytes32 => bool) private usedSignatures;

    event IdentityRegistered(address indexed institution, string legalName, string jurisdiction);
    event IdentityUpdated(address indexed institution);
    event KYCVerified(address indexed institution, uint256 expiry);
    event AMLVerified(address indexed institution, uint256 expiry);
    event Blacklisted(address indexed institution, bool status);
    event IdentityRevoked(address indexed institution);

    constructor() {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(KYC_PROVIDER_ROLE, msg.sender);
        _setupRole(AML_PROVIDER_ROLE, msg.sender);
    }

    /**
     * @dev Register an institutional identity (can only be called by admin)
     */
    function registerIdentity(
        address institution,
        string memory legalName,
        string memory jurisdiction
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        require(bytes(legalName).length > 0, "Legal name required");
        require(bytes(jurisdiction).length > 0, "Jurisdiction required");
        require(identities[institution].verifiedBy == address(0), "Identity already exists");

        identities[institution] = Identity({
            legalName: legalName,
            jurisdiction: jurisdiction,
            kycExpiry: 0,
            amlExpiry: 0,
            isActive: true,
            verifiedBy: msg.sender
        });

        _grantRole(INSTITUTION_ROLE, institution);
        emit IdentityRegistered(institution, legalName, jurisdiction);
    }

    /**
     * @dev Verify KYC compliance (can only be called by KYC provider)
     */
    function verifyKYC(address institution, uint256 expiryTimestamp) external onlyRole(KYC_PROVIDER_ROLE) {
        require(identities[institution].verifiedBy != address(0), "Identity not registered");
        require(expiryTimestamp > block.timestamp, "Expiry must be in the future");
        
        identities[institution].kycExpiry = expiryTimestamp;
        emit KYCVerified(institution, expiryTimestamp);
    }

    /**
     * @dev Verify AML compliance (can only be called by AML provider)
     */
    function verifyAML(address institution, uint256 expiryTimestamp) external onlyRole(AML_PROVIDER_ROLE) {
        require(identities[institution].verifiedBy != address(0), "Identity not registered");
        require(expiryTimestamp > block.timestamp, "Expiry must be in the future");
        
        identities[institution].amlExpiry = expiryTimestamp;
        emit AMLVerified(institution, expiryTimestamp);
    }

    /**
     * @dev Check if an institution is fully compliant
     */
    function isCompliant(address institution) public view returns (bool) {
        Identity memory identity = identities[institution];
        return identity.isActive && 
               !blacklisted[institution] && 
               identity.kycExpiry > block.timestamp && 
               identity.amlExpiry > block.timestamp;
    }

    /**
     * @dev Blacklist or unblacklist an institution (admin only)
     */
    function setBlacklisted(address institution, bool status) external onlyRole(DEFAULT_ADMIN_ROLE) {
        require(identities[institution].verifiedBy != address(0), "Identity not registered");
        blacklisted[institution] = status;
        emit Blacklisted(institution, status);
    }

    /**
     * @dev Revoke an institution's identity (admin only)
     */
    function revokeIdentity(address institution) external onlyRole(DEFAULT_ADMIN_ROLE) {
        require(identities[institution].verifiedBy != address(0), "Identity not registered");
        _revokeRole(INSTITUTION_ROLE, institution);
        identities[institution].isActive = false;
        emit IdentityRevoked(institution);
    }

    /**
     * @dev Update identity information (institution or admin)
     */
    function updateIdentity(
        string memory legalName,
        string memory jurisdiction
    ) external {
        require(
            hasRole(INSTITUTION_ROLE, msg.sender) || hasRole(DEFAULT_ADMIN_ROLE, msg.sender),
            "Caller not authorized"
        );
        require(bytes(legalName).length > 0, "Legal name required");
        require(bytes(jurisdiction).length > 0, "Jurisdiction required");

        Identity storage identity = identities[msg.sender];
        identity.legalName = legalName;
        identity.jurisdiction = jurisdiction;
        
        emit IdentityUpdated(msg.sender);
    }

    /**
     * @dev Verify a signed message from an institution
     */
    function verifySignedMessage(
        address institution,
        bytes32 messageHash,
        bytes memory signature
    ) external view returns (bool) {
        require(isCompliant(institution), "Institution not compliant");
        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();
        return ethSignedMessageHash.recover(signature) == institution;
    }

    /**
     * @dev Verify a one-time signed message (prevents replay attacks)
     */
    function verifyOneTimeSignedMessage(
        address institution,
        bytes32 messageHash,
        bytes memory signature
    ) external returns (bool) {
        require(isCompliant(institution), "Institution not compliant");
        bytes32 signatureId = keccak256(abi.encodePacked(institution, messageHash, signature));
        require(!usedSignatures[signatureId], "Signature already used");

        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();
        bool isValid = ethSignedMessageHash.recover(signature) == institution;

        if (isValid) {
            usedSignatures[signatureId] = true;
        }

        return isValid;
    }
}
```
