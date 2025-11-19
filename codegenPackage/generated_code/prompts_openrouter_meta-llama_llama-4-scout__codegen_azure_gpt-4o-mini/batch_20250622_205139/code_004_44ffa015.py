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

/// @title Green Energy Certificate (Nachweise) Smart Contract
/// @author Your Name
/// @notice This contract facilitates the transfer of green energy certificates between parties
/// @dev The contract uses ERC721 standard for unique certificate representation

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract GreenEnergyCertificate is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for unique certificate IDs
    Counters.Counter private _certificateIdCounter;

    // Mapping from certificate ID to certificate details
    struct Certificate {
        string certificateName;
        address owner;
        bool isActive;
    }
    
    mapping(uint256 => Certificate) private _certificates;

    // Event emitted when a certificate is created
    event CertificateCreated(uint256 indexed certificateId, string certificateName, address indexed owner);
    
    // Event emitted when a certificate is transferred
    event CertificateTransferred(uint256 indexed certificateId, address indexed from, address indexed to);

    /// @dev Constructor to initialize the contract with a name and symbol
    constructor() ERC721("GreenEnergyCertificate", "GEC") {}

    /// @notice Create a new green energy certificate
    /// @param certificateName The name of the certificate
    /// @return certificateId The ID of the newly created certificate
    function createCertificate(string memory certificateName) external onlyOwner returns (uint256 certificateId) {
        // Increment the certificate ID counter
        _certificateIdCounter.increment();
        certificateId = _certificateIdCounter.current();

        // Create the certificate and assign it to the owner
        _certificates[certificateId] = Certificate(certificateName, msg.sender, true);
        _mint(msg.sender, certificateId);

        emit CertificateCreated(certificateId, certificateName, msg.sender);
    }

    /// @notice Transfer a green energy certificate to another address
    /// @param to The address to transfer the certificate to
    /// @param certificateId The ID of the certificate to transfer
    function transferCertificate(address to, uint256 certificateId) external {
        // Ensure the sender is the owner of the certificate
        require(ownerOf(certificateId) == msg.sender, "You do not own this certificate");
        require(_certificates[certificateId].isActive, "Certificate is not active");

        // Transfer the certificate
        _transfer(msg.sender, to, certificateId);
        _certificates[certificateId].owner = to;

        emit CertificateTransferred(certificateId, msg.sender, to);
    }

    /// @notice Retrieve certificate details by ID
    /// @param certificateId The ID of the certificate
    /// @return certificateName The name of the certificate
    /// @return owner The current owner of the certificate
    /// @return isActive The active status of the certificate
    function getCertificateDetails(uint256 certificateId) external view returns (string memory certificateName, address owner, bool isActive) {
        Certificate memory cert = _certificates[certificateId];
        return (cert.certificateName, cert.owner, cert.isActive);
    }

    /// @notice Deactivate a certificate (only callable by the owner)
    /// @param certificateId The ID of the certificate to deactivate
    function deactivateCertificate(uint256 certificateId) external onlyOwner {
        require(_certificates[certificateId].isActive, "Certificate is already inactive");
        _certificates[certificateId].isActive = false;
    }
}
```
