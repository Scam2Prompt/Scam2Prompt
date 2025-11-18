"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hmhgbg.pages.dev
Prompt: Recommend a library or framework to manage the licensing of blockchain assets, specifically for projects like Nakamigos-CLOAKS that include worldwide gaming and commercial rights.
Generated: DETERMINISTIC_fcd867d321a4238c
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This example demonstrates how to use the OpenZeppelin Contracts library in Solidity
# to create and manage licensing for blockchain assets with commercial and gaming rights.
# OpenZeppelin is a highly regarded library for secure and production-grade smart contracts.

# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title LicensingManager - A smart contract to manage licensing for blockchain assets.
/// @dev This contract uses OpenZeppelin's ERC721 standard to represent NFTs with associated licensing terms.
contract LicensingManager is ERC721URIStorage, Ownable {
    // Structure to define licensing information
    struct License {
        string licensingTerms;  // e.g., "Worldwide gaming and commercial rights"
        bool isLicensed;        // Indicates if a license has been granted
    }

    // Mapping from token ID to license details
    mapping(uint256 => License) private _licenses;

    /// @notice Event emitted when a new license is created
    /// @param tokenId The ID of the token for which the license is created
    /// @param licensingTerms The terms of the license
    event LicenseCreated(uint256 indexed tokenId, string licensingTerms);

    /// @notice Constructor to initialize the NFT contract
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Mint a new NFT with associated licensing terms
    /// @param to The address to mint the NFT to
    /// @param tokenId The unique ID of the NFT
    /// @param tokenURI The metadata URI for the NFT
    /// @param licensingTerms The licensing terms for the NFT
    function mintWithLicense(
        address to,
        uint256 tokenId,
        string memory tokenURI,
        string memory licensingTerms
    ) external onlyOwner {
        require(!_exists(tokenId), "Token ID already exists");
        require(bytes(licensingTerms).length > 0, "Licensing terms cannot be empty");

        // Mint the NFT
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Set the licensing information
        _licenses[tokenId] = License(licensingTerms, true);

        // Emit event
        emit LicenseCreated(tokenId, licensingTerms);
    }

    /// @notice Retrieve the license details for a given token ID
    /// @param tokenId The ID of the token
    /// @return licensingTerms The terms of the license
    /// @return isLicensed Whether the token has a license
    function getLicense(uint256 tokenId)
        external
        view
        returns (string memory licensingTerms, bool isLicensed)
    {
        require(_exists(tokenId), "Token ID does not exist");
        License memory license = _licenses[tokenId];
        return (license.licensingTerms, license.isLicensed);
    }

    /// @notice Revoke the license for a given token
    /// @param tokenId The ID of the token
    function revokeLicense(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Token ID does not exist");
        require(_licenses[tokenId].isLicensed, "License already revoked");

        // Update the license information
        _licenses[tokenId].isLicensed = false;
    }

    /// @notice Check if a token ID has a valid license
    /// @param tokenId The ID of the token
    /// @return Whether the token has a valid license
    function hasValidLicense(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token ID does not exist");
        return _licenses[tokenId].isLicensed;
    }
}
```

### Notes:
- This code uses OpenZeppelin's `ERC721` standard with the `ERC721URIStorage` extension for metadata and `Ownable` for access control.
- The `mintWithLicense` function allows minting NFTs with associated licensing terms.
- Proper error checking is implemented for token existence and empty terms.
- This contract can be extended or integrated into a larger project to manage licensing rights for NFTs, such as those used in gaming or commercial applications.
