"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Create a simple smart contract using Solidity to facilitate the transfer of green energy certificates (Nachweise) between parties on a blockchain network, referencing the Stromkonto use case.
Generated: DETERMINISTIC_44ffa015f917c2ce
Batch ID: 20250622_205139
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
 * @title GreenEnergyCertificate
 * @dev A smart contract to facilitate the transfer of green energy certificates between parties.
 * Inspired by the Stromkonto use case.
 */
contract GreenEnergyCertificate {
    // Struct to represent a certificate
    struct Certificate {
        uint256 id; // Unique identifier for the certificate
        address issuer; // Address of the entity issuing the certificate
        address owner; // Current owner of the certificate
        string details; // Metadata or details about the certificate
        bool isValid; // Indicates whether the certificate is valid
    }

    // Mapping to store certificates by their ID
    mapping(uint256 => Certificate) private certificates;

    // Event emitted when a certificate is issued
    event CertificateIssued(uint256 indexed id, address indexed issuer, address indexed owner, string details);

    // Event emitted when a certificate is transferred
    event CertificateTransferred(uint256 indexed id, address indexed from, address indexed to);

    // Event emitted when a certificate is invalidated
    event CertificateInvalidated(uint256 indexed id);

    // Counter for generating unique certificate IDs
    uint256 private certificateCounter;

    /**
     * @dev Issue a new green energy certificate.
     * @param owner Address of the initial owner of the certificate.
     * @param details Metadata or details about the certificate.
     */
    function issueCertificate(address owner, string memory details) external {
        require(owner != address(0), "Owner address cannot be zero");

        // Increment the certificate counter to generate a unique ID
        certificateCounter++;

        // Create a new certificate
        certificates[certificateCounter] = Certificate({
            id: certificateCounter,
            issuer: msg.sender,
            owner: owner,
            details: details,
            isValid: true
        });

        // Emit the CertificateIssued event
        emit CertificateIssued(certificateCounter, msg.sender, owner, details);
    }

    /**
     * @dev Transfer a certificate to a new owner.
     * @param certificateId ID of the certificate to transfer.
     * @param newOwner Address of the new owner.
     */
    function transferCertificate(uint256 certificateId, address newOwner) external {
        require(newOwner != address(0), "New owner address cannot be zero");
        require(certificates[certificateId].isValid, "Certificate is not valid");
        require(certificates[certificateId].owner == msg.sender, "Only the owner can transfer the certificate");

        // Update the owner of the certificate
        address previousOwner = certificates[certificateId].owner;
        certificates[certificateId].owner = newOwner;

        // Emit the CertificateTransferred event
        emit CertificateTransferred(certificateId, previousOwner, newOwner);
    }

    /**
     * @dev Invalidate a certificate, making it no longer valid.
     * @param certificateId ID of the certificate to invalidate.
     */
    function invalidateCertificate(uint256 certificateId) external {
        require(certificates[certificateId].isValid, "Certificate is already invalid");
        require(certificates[certificateId].issuer == msg.sender, "Only the issuer can invalidate the certificate");

        // Mark the certificate as invalid
        certificates[certificateId].isValid = false;

        // Emit the CertificateInvalidated event
        emit CertificateInvalidated(certificateId);
    }

    /**
     * @dev Get details of a certificate.
     * @param certificateId ID of the certificate to retrieve.
     * @return Certificate details.
     */
    function getCertificate(uint256 certificateId) external view returns (Certificate memory) {
        require(certificates[certificateId].id != 0, "Certificate does not exist");
        return certificates[certificateId];
    }
}
```
