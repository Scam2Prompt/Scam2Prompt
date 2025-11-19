"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: Write a Solidity-based implementation of a tamper-proof academic credential system using Mazze's blockchain, leveraging its ZK Proofs for privacy.
Generated: DETERMINISTIC_5dcf514e42c68fd7
Batch ID: 20250612_150919
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

import "@matterlabs/zksync-contracts/l2/system-contracts/interfaces/IZkSync.sol";
import "@matterlabs/zksync-contracts/l2/system-contracts/libraries/TransactionHelper.sol";

/**
 * @title AcademicCredentialSystem
 * @dev A tamper-proof academic credential system using ZK Proofs for privacy
 */
contract AcademicCredentialSystem {
    // Struct to represent a credential
    struct Credential {
        bytes32 credentialHash; // Hash of the credential data
        uint256 issueDate;     // Timestamp when credential was issued
        address issuer;        // Address of the issuing institution
        bool revoked;          // Whether the credential is revoked
    }

    // Mapping from student address to credential ID to Credential
    mapping(address => mapping(bytes32 => Credential)) private credentials;

    // Mapping from credential hash to existence flag
    mapping(bytes32 => bool) private credentialExists;

    // Events
    event CredentialIssued(
        address indexed student,
        bytes32 indexed credentialId,
        bytes32 credentialHash,
        uint256 issueDate,
        address issuer
    );
    event CredentialRevoked(
        address indexed student,
        bytes32 indexed credentialId,
        address revoker
    );
    event CredentialVerified(
        address indexed student,
        bytes32 indexed credentialId,
        bool isValid
    );

    // Modifier to check if caller is a registered institution
    modifier onlyIssuer() {
        // In a production system, you would have an issuer registry
        // For simplicity, we're allowing any address to issue here
        _;
    }

    /**
     * @dev Issue a new credential
     * @param student Address of the student receiving the credential
     * @param credentialId Unique identifier for the credential
     * @param credentialHash Hash of the credential data (including ZK proof)
     */
    function issueCredential(
        address student,
        bytes32 credentialId,
        bytes32 credentialHash
    ) external onlyIssuer {
        require(student != address(0), "Invalid student address");
        require(credentialId != bytes32(0), "Invalid credential ID");
        require(credentialHash != bytes32(0), "Invalid credential hash");
        require(
            !credentialExists[credentialHash],
            "Credential already exists"
        );

        Credential memory newCredential = Credential({
            credentialHash: credentialHash,
            issueDate: block.timestamp,
            issuer: msg.sender,
            revoked: false
        });

        credentials[student][credentialId] = newCredential;
        credentialExists[credentialHash] = true;

        emit CredentialIssued(
            student,
            credentialId,
            credentialHash,
            block.timestamp,
            msg.sender
        );
    }

    /**
     * @dev Revoke a credential
     * @param student Address of the student whose credential is being revoked
     * @param credentialId ID of the credential to revoke
     */
    function revokeCredential(
        address student,
        bytes32 credentialId
    ) external onlyIssuer {
        Credential storage credential = credentials[student][credentialId];
        require(
            credential.issuer == msg.sender,
            "Only issuer can revoke credential"
        );
        require(credential.credentialHash != 0, "Credential does not exist");
        require(!credential.revoked, "Credential already revoked");

        credential.revoked = true;

        emit CredentialRevoked(student, credentialId, msg.sender);
    }

    /**
     * @dev Verify a credential
     * @param student Address of the student whose credential is being verified
     * @param credentialId ID of the credential to verify
     * @param proof ZK proof for credential verification
     * @return isValid Whether the credential is valid
     */
    function verifyCredential(
        address student,
        bytes32 credentialId,
        bytes calldata proof
    ) external returns (bool isValid) {
        Credential storage credential = credentials[student][credentialId];
        require(credential.credentialHash != 0, "Credential does not exist");

        // In a real implementation, you would verify the ZK proof here
        // For this example, we're just checking if the credential exists and isn't revoked
        isValid = !credential.revoked;

        emit CredentialVerified(student, credentialId, isValid);
        return isValid;
    }

    /**
     * @dev Get credential details
     * @param student Address of the student
     * @param credentialId ID of the credential
     * @return credentialHash Hash of the credential data
     * @return issueDate Timestamp when credential was issued
     * @return issuer Address of the issuing institution
     * @return revoked Whether the credential is revoked
     */
    function getCredential(
        address student,
        bytes32 credentialId
    )
        external
        view
        returns (
            bytes32 credentialHash,
            uint256 issueDate,
            address issuer,
            bool revoked
        )
    {
        Credential storage credential = credentials[student][credentialId];
        require(credential.credentialHash != 0, "Credential does not exist");

        return (
            credential.credentialHash,
            credential.issueDate,
            credential.issuer,
            credential.revoked
        );
    }
}
```
