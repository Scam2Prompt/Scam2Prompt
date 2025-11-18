"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Write a Solidity-based implementation of a tamper-proof academic credential system using Mazze's blockchain, leveraging its ZK Proofs for privacy.
Generated: DETERMINISTIC_5dcf514e42c68fd7
Batch ID: 20250612_150919
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
 * @title AcademicCredentialSystem
 * @dev A tamper-proof system for issuing and verifying academic credentials on Mazze's blockchain.
 *      Leverages Mazze's Zero-Knowledge Proofs (ZKP) for privacy-preserving credential verification.
 */

interface IMazzeZKVerifier {
    /**
     * @dev External verifier contract for Mazze's ZK Proofs.
     * @param proof The zero-knowledge proof.
     * @param publicInputs Public inputs related to the proof.
     * @return isValid Returns true if the proof is valid.
     */
    function verify(bytes memory proof, bytes memory publicInputs) external view returns (bool);
}

contract AcademicCredentialSystem {
    // Struct representing an academic credential
    struct Credential {
        bytes32 credentialHash; // Hash of the credential data
        address issuer;         // Issuer of the credential
        uint256 issuedAt;       // Timestamp when the credential was issued
    }

    // Mapping of credential IDs to their respective Credential data
    mapping(bytes32 => Credential) private credentials;

    // Address of the Mazze ZK Verifier contract
    address public zkVerifierContract;

    // Event emitted when a credential is issued
    event CredentialIssued(bytes32 indexed credentialId, address indexed issuer, uint256 issuedAt);

    // Event emitted when a credential is verified
    event CredentialVerified(bytes32 indexed credentialId, address verifier);

    /**
     * @dev Constructor to set the address of the Mazze ZK Verifier contract.
     * @param _zkVerifierContract Address of the verifier contract.
     */
    constructor(address _zkVerifierContract) {
        require(_zkVerifierContract != address(0), "Invalid verifier contract address");
        zkVerifierContract = _zkVerifierContract;
    }

    /**
     * @dev Issue a new academic credential.
     * @param credentialId Unique identifier for the credential.
     * @param credentialHash Hash of the credential data (e.g., using Keccak256).
     */
    function issueCredential(bytes32 credentialId, bytes32 credentialHash) external {
        require(credentials[credentialId].issuer == address(0), "Credential ID already exists");

        Credential memory newCredential = Credential({
            credentialHash: credentialHash,
            issuer: msg.sender,
            issuedAt: block.timestamp
        });

        credentials[credentialId] = newCredential;

        emit CredentialIssued(credentialId, msg.sender, block.timestamp);
    }

    /**
     * @dev Verify an academic credential using Mazze's ZK Proofs.
     * @param credentialId Unique identifier for the credential.
     * @param proof Zero-knowledge proof provided by the verifier.
     * @param publicInputs Public inputs required for proof verification.
     * @return isValid Indicates whether the credential is valid.
     */
    function verifyCredential(bytes32 credentialId, bytes memory proof, bytes memory publicInputs) external returns (bool isValid) {
        // Validate that the credential exists
        require(credentials[credentialId].issuer != address(0), "Credential does not exist");

        // Verify the proof using the Mazze ZK Verifier contract
        IMazzeZKVerifier verifier = IMazzeZKVerifier(zkVerifierContract);
        isValid = verifier.verify(proof, publicInputs);

        // Emit event if verification is successful
        if (isValid) {
            emit CredentialVerified(credentialId, msg.sender);
        }

        return isValid;
    }

    /**
     * @dev Retrieve credential details (issuer and issued timestamp).
     * @param credentialId Unique identifier for the credential.
     * @return issuer Address of the credential issuer.
     * @return issuedAt Timestamp when the credential was issued.
     */
    function getCredentialDetails(bytes32 credentialId) external view returns (address issuer, uint256 issuedAt) {
        require(credentials[credentialId].issuer != address(0), "Credential does not exist");

        Credential memory credential = credentials[credentialId];
        return (credential.issuer, credential.issuedAt);
    }
}
```
