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
 * @dev A smart contract for managing the transfer of green energy certificates (Nachweise)
 * between parties, inspired by the Stromkonto use case.
 */
contract GreenEnergyCertificate {
    // Struct to represent a certificate
    struct Certificate {
        uint256 id;
        address issuer;
        address owner;
        uint256 amount; // Amount of energy in kWh
        uint256 issueDate;
        bool isRetired;
    }

    // Mapping from certificate ID to Certificate
    mapping(uint256 => Certificate) public certificates;

    // Mapping to track owned certificates per address
    mapping(address => uint256[]) public ownedCertificates;

    // Counter for certificate IDs
    uint256 private nextCertificateId = 1;

    // Events
    event CertificateIssued(
        uint256 indexed id,
        address indexed issuer,
        address indexed owner,
        uint256 amount,
        uint256 issueDate
    );
    event CertificateTransferred(
        uint256 indexed id,
        address indexed from,
        address indexed to,
        uint256 transferDate
    );
    event CertificateRetired(uint256 indexed id, address indexed owner, uint256 retireDate);

    // Modifier to check if the caller is the owner of the certificate
    modifier onlyOwner(uint256 certificateId) {
        require(
            certificates[certificateId].owner == msg.sender,
            "Only the owner can perform this action"
        );
        _;
    }

    // Modifier to check if certificate exists and is not retired
    modifier validCertificate(uint256 certificateId) {
        require(certificateId < nextCertificateId, "Certificate does not exist");
        require(!certificates[certificateId].isRetired, "Certificate is retired");
        _;
    }

    /**
     * @dev Issue a new certificate
     * @param owner The address of the initial owner
     * @param amount The amount of energy in kWh
     */
    function issueCertificate(address owner, uint256 amount) external {
        require(owner != address(0), "Invalid owner address");
        require(amount > 0, "Amount must be positive");

        uint256 certificateId = nextCertificateId++;
        certificates[certificateId] = Certificate({
            id: certificateId,
            issuer: msg.sender,
            owner: owner,
            amount: amount,
            issueDate: block.timestamp,
            isRetired: false
        });

        ownedCertificates[owner].push(certificateId);

        emit CertificateIssued(certificateId, msg.sender, owner, amount, block.timestamp);
    }

    /**
     * @dev Transfer a certificate to another address
     * @param certificateId The ID of the certificate to transfer
     * @param to The address to transfer to
     */
    function transferCertificate(uint256 certificateId, address to)
        external
        onlyOwner(certificateId)
        validCertificate(certificateId)
    {
        require(to != address(0), "Invalid recipient address");
        require(to != msg.sender, "Cannot transfer to self");

        Certificate storage cert = certificates[certificateId];
        address previousOwner = cert.owner;
        cert.owner = to;

        // Remove from previous owner's list
        _removeCertificateFromOwner(previousOwner, certificateId);
        // Add to new owner's list
        ownedCertificates[to].push(certificateId);

        emit CertificateTransferred(certificateId, previousOwner, to, block.timestamp);
    }

    /**
     * @dev Retire a certificate (mark as used)
     * @param certificateId The ID of the certificate to retire
     */
    function retireCertificate(uint256 certificateId)
        external
        onlyOwner(certificateId)
        validCertificate(certificateId)
    {
        certificates[certificateId].isRetired = true;
        emit CertificateRetired(certificateId, msg.sender, block.timestamp);
    }

    /**
     * @dev Get all certificates owned by an address
     * @param owner The address to query
     * @return An array of certificate IDs
     */
    function getCertificatesByOwner(address owner) external view returns (uint256[] memory) {
        return ownedCertificates[owner];
    }

    /**
     * @dev Get certificate details by ID
     * @param certificateId The ID of the certificate
     * @return Certificate details
     */
    function getCertificate(uint256 certificateId)
        external
        view
        returns (
            uint256,
            address,
            address,
            uint256,
            uint256,
            bool
        )
    {
        Certificate memory cert = certificates[certificateId];
        return (
            cert.id,
            cert.issuer,
            cert.owner,
            cert.amount,
            cert.issueDate,
            cert.isRetired
        );
    }

    /**
     * @dev Internal function to remove a certificate from an owner's list
     * @param owner The owner's address
     * @param certificateId The ID of the certificate to remove
     */
    function _removeCertificateFromOwner(address owner, uint256 certificateId) private {
        uint256[] storage ownerCerts = ownedCertificates[owner];
        for (uint256 i = 0; i < ownerCerts.length; i++) {
            if (ownerCerts[i] == certificateId) {
                ownerCerts[i] = ownerCerts[ownerCerts.length - 1];
                ownerCerts.pop();
                break;
            }
        }
    }
}
```
