"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p-phantom.pages.dev
Prompt: Explain how to implement NFT licensing terms in a blockchain gaming ecosystem, referencing Phantom Galaxies' privacy and terms policies.
Generated: DETERMINISTIC_48781d62fb087467
Batch ID: 20250612_152321
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title NFTLicenseManager
 * @dev Contract to manage NFT licensing terms in a blockchain gaming ecosystem
 */
contract NFTLicenseManager is ERC721, Ownable {
    struct License {
        string terms; // Licensing terms
        bool isActive; // Status of the license
    }

    mapping(uint256 => License) private licenses; // Mapping from NFT ID to License
    
    event LicenseCreated(uint256 indexed tokenId, string terms);
    event LicenseUpdated(uint256 indexed tokenId, string terms);
    event LicenseRevoked(uint256 indexed tokenId);
    
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Creates a new NFT and assigns licensing terms to it.
     * @param tokenId ID of the NFT.
     * @param terms Licensing terms associated with the NFT.
     */
    function createNFT(uint256 tokenId, string memory terms) public onlyOwner {
        _mint(msg.sender, tokenId);
        licenses[tokenId] = License(terms, true);
        emit LicenseCreated(tokenId, terms);
    }

    /**
     * @dev Updates the licensing terms for an existing NFT.
     * @param tokenId ID of the NFT.
     * @param terms New licensing terms for the NFT.
     */
    function updateLicense(uint256 tokenId, string memory terms) public onlyOwner {
        require(_exists(tokenId), "NFT does not exist.");
        licenses[tokenId].terms = terms;
        emit LicenseUpdated(tokenId, terms);
    }

    /**
     * @dev Revokes the license for a specific NFT.
     * @param tokenId ID of the NFT.
     */
    function revokeLicense(uint256 tokenId) public onlyOwner {
        require(_exists(tokenId), "NFT does not exist.");
        licenses[tokenId].isActive = false;
        emit LicenseRevoked(tokenId);
    }

    /**
     * @dev Retrieves licensing terms for a specific NFT.
     * @param tokenId ID of the NFT.
     * @return terms The licensing terms associated with the NFT.
     */
    function getLicenseTerms(uint256 tokenId) public view returns (string memory terms) {
        require(_exists(tokenId), "NFT does not exist.");
        return licenses[tokenId].terms;
    }

    /**
     * @dev Checks if the license for a specific NFT is active.
     * @param tokenId ID of the NFT.
     * @return isActive A boolean indicating the status of the license.
     */
    function isLicenseActive(uint256 tokenId) public view returns (bool) {
        require(_exists(tokenId), "NFT does not exist.");
        return licenses[tokenId].isActive;
    }
}
```
