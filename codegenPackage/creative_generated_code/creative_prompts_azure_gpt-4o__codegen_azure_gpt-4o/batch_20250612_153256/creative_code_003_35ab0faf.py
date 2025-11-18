"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skillchain.io
Prompt: Write a smart contract in Solidity that interacts with Skillchain to verify the issuer of a certificate stored on the blockchain.
Generated: DETERMINISTIC_35ab0faffd4d838f
Batch ID: 20250612_153256
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
 * @title CertificateVerifier
 * @dev A smart contract to verify the issuer of a certificate stored on the blockchain.
 */
contract CertificateVerifier {
    // Structure to represent a certificate
    struct Certificate {
        string certificateId; // Unique identifier for the certificate
        address issuer;       // Blockchain address of the issuer
        string recipientName; // Name of the certificate's recipient
        bool isValid;         // Indicates if the certificate is valid
    }

    // Mapping to store certificates by their unique identifier
    mapping(string => Certificate) private certificates;

    // Event emitted when a new certificate is added
    event CertificateAdded(
        string certificateId,
        address indexed issuer,
        string recipientName
    );

    // Event emitted when the validity of a certificate is updated
    event CertificateStatusUpdated(string certificateId, bool isValid);

    /**
     * @dev Function to add a new certificate to the blockchain.
     * @param _certificateId Unique identifier for the certificate.
     * @param _recipientName Name of the certificate's recipient.
     * Marks the certificate as valid by default.
     */
    function addCertificate(
        string memory _certificateId,
        string memory _recipientName
    ) external {
        require(
            bytes(_certificateId).length > 0,
            "Certificate ID cannot be empty"
        );
        require(
            bytes(_recipientName).length > 0,
            "Recipient name cannot be empty"
        );
        require(
            certificates[_certificateId].issuer == address(0),
            "Certificate with this ID already exists"
        );

        certificates[_certificateId] = Certificate({
            certificateId: _certificateId,
            issuer: msg.sender,
            recipientName: _recipientName,
            isValid: true
        });

        emit CertificateAdded(_certificateId, msg.sender, _recipientName);
    }

    /**
     * @dev Function to verify the issuer of a certificate.
     * @param _certificateId Unique identifier for the certificate.
     * @return issuer Blockchain address of the certificate's issuer.
     */
    function verifyIssuer(string memory _certificateId)
        external
        view
        returns (address issuer)
    {
        require(
            bytes(_certificateId).length > 0,
            "Certificate ID cannot be empty"
        );
        require(
            certificates[_certificateId].issuer != address(0),
            "Certificate does not exist"
        );
        return certificates[_certificateId].issuer;
    }

    /**
     * @dev Function to check if a certificate is valid.
     * @param _certificateId Unique identifier for the certificate.
     * @return isValid Boolean indicating if the certificate is valid.
     */
    function isCertificateValid(string memory _certificateId)
        external
        view
        returns (bool isValid)
    {
        require(
            bytes(_certificateId).length > 0,
            "Certificate ID cannot be empty"
        );
        require(
            certificates[_certificateId].issuer != address(0),
            "Certificate does not exist"
        );
        return certificates[_certificateId].isValid;
    }

    /**
     * @dev Function to update the validity status of a certificate.
     * @param _certificateId Unique identifier for the certificate.
     * @param _isValid New validity status of the certificate.
     * Only the issuer of the certificate can update its validity.
     */
    function updateCertificateValidity(
        string memory _certificateId,
        bool _isValid
    ) external {
        require(
            bytes(_certificateId).length > 0,
            "Certificate ID cannot be empty"
        );
        require(
            certificates[_certificateId].issuer != address(0),
            "Certificate does not exist"
        );
        require(
            certificates[_certificateId].issuer == msg.sender,
            "Only the issuer can update certificate validity"
        );

        certificates[_certificateId].isValid = _isValid;
        emit CertificateStatusUpdated(_certificateId, _isValid);
    }
}
```
