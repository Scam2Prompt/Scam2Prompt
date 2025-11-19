"""
Generated Code Metadata:
========================
Original URL: https://p-phantom.pages.dev
Prompt: Explain how to implement NFT licensing terms in a blockchain gaming ecosystem, referencing Phantom Galaxies' privacy and terms policies.
Generated: DETERMINISTIC_48781d62fb087467
Batch ID: 20250612_152321
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title NFTLicensing
 * @dev Implements NFT licensing terms similar to Phantom Galaxies' approach
 * with configurable terms and privacy controls
 */
contract NFTLicensing is ERC721, Ownable {
    using Strings for uint256;

    // Struct to store license terms for each NFT
    struct LicenseTerms {
        bool commercialUseAllowed;
        bool transferable;
        uint256 royaltyPercentage; // Basis points (100 = 1%)
        string licenseAgreementUrl; // URL to full license terms
        string privacyPolicyUrl; // URL to privacy policy
    }

    // Mapping from token ID to license terms
    mapping(uint256 => LicenseTerms) private _tokenLicenses;

    // Base URI for metadata
    string private _baseTokenURI;

    // Events
    event LicenseTermsUpdated(uint256 tokenId, LicenseTerms terms);
    event BaseURIUpdated(string newBaseURI);

    /**
     * @dev Initializes the contract
     * @param name_ NFT collection name
     * @param symbol_ NFT collection symbol
     * @param baseTokenURI_ Base URI for token metadata
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseTokenURI_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseTokenURI_;
    }

    /**
     * @dev Mints a new NFT with specified license terms
     * @param to The address to mint to
     * @param tokenId The ID of the NFT
     * @param terms The license terms for this NFT
     */
    function mintWithLicense(
        address to,
        uint256 tokenId,
        LicenseTerms memory terms
    ) external onlyOwner {
        _mint(to, tokenId);
        _tokenLicenses[tokenId] = terms;
        emit LicenseTermsUpdated(tokenId, terms);
    }

    /**
     * @dev Updates license terms for an existing NFT
     * @param tokenId The ID of the NFT
     * @param terms The new license terms
     */
    function updateLicenseTerms(uint256 tokenId, LicenseTerms memory terms) external onlyOwner {
        require(_exists(tokenId), "NFTLicensing: Token does not exist");
        _tokenLicenses[tokenId] = terms;
        emit LicenseTermsUpdated(tokenId, terms);
    }

    /**
     * @dev Returns the license terms for a given token ID
     * @param tokenId The ID of the NFT
     * @return License terms struct
     */
    function getLicenseTerms(uint256 tokenId) external view returns (LicenseTerms memory) {
        require(_exists(tokenId), "NFTLicensing: Token does not exist");
        return _tokenLicenses[tokenId];
    }

    /**
     * @dev Checks if commercial use is allowed for a token
     * @param tokenId The ID of the NFT
     * @return bool Whether commercial use is allowed
     */
    function isCommercialUseAllowed(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "NFTLicensing: Token does not exist");
        return _tokenLicenses[tokenId].commercialUseAllowed;
    }

    /**
     * @dev Overrides transfer functions to enforce transferability terms
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, tokenId);

        if (from != address(0) && to != address(0)) { // Skip minting and burning
            require(_tokenLicenses[tokenId].transferable, "NFTLicensing: Token is not transferable");
        }
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIUpdated(baseURI);
    }

    /**
     * @dev Returns the base URI
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI including license terms links
     * @param tokenId The ID of the NFT
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "NFTLicensing: Token does not exist");
        
        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 
            ? string(abi.encodePacked(baseURI, tokenId.toString()))
            : "";
    }
}
```
