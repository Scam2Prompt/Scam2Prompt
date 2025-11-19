"""
Generated Code Metadata:
========================
Original URL: https://nakamigos.art
Prompt: Develop a smart contract to manage the commercial rights and licensing of unique digital assets, such as Nakamigos and Nakamigos-CLOAKS.
Generated: DETERMINISTIC_83d3d4c0fa41f755
Batch ID: 20250622_205335
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";

/**
 * @title DigitalAssetLicense
 * @dev Smart contract to manage commercial rights and licensing of unique digital assets.
 */
contract DigitalAssetLicense is ERC721, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold licensing information
    struct License {
        address licensee;
        uint256 expirationDate;
        bool isActive;
    }

    // Mapping from token ID to License information
    mapping(uint256 => License) private _licenses;

    // Event emitted when a license is created
    event LicenseCreated(uint256 indexed tokenId, address indexed licensee, uint256 expirationDate);

    // Event emitted when a license is revoked
    event LicenseRevoked(uint256 indexed tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("DigitalAssetLicense", "DAL") {}

    /**
     * @dev Mint a new digital asset and assign it to the owner.
     * @param to The address to receive the minted token.
     */
    function mint(address to) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _tokenIdCounter.increment();
    }

    /**
     * @dev Create a license for a specific token ID.
     * @param tokenId The ID of the token to license.
     * @param licensee The address of the licensee.
     * @param duration The duration of the license in seconds.
     */
    function createLicense(uint256 tokenId, address licensee, uint256 duration) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        require(licensee != address(0), "Invalid licensee address");
        require(duration > 0, "Duration must be greater than zero");

        uint256 expirationDate = block.timestamp + duration;
        _licenses[tokenId] = License(licensee, expirationDate, true);

        emit LicenseCreated(tokenId, licensee, expirationDate);
    }

    /**
     * @dev Revoke a license for a specific token ID.
     * @param tokenId The ID of the token whose license is to be revoked.
     */
    function revokeLicense(uint256 tokenId) external onlyOwner {
        require(_licenses[tokenId].isActive, "License is not active");
        delete _licenses[tokenId];

        emit LicenseRevoked(tokenId);
    }

    /**
     * @dev Check the status of a license for a specific token ID.
     * @param tokenId The ID of the token to check.
     * @return (address, uint256, bool) Licensee address, expiration date, and active status.
     */
    function checkLicense(uint256 tokenId) external view returns (address, uint256, bool) {
        License memory license = _licenses[tokenId];
        return (license.licensee, license.expirationDate, license.isActive);
    }

    /**
     * @dev Override the _burn function to also revoke the license when the token is burned.
     * @param tokenId The ID of the token to burn.
     */
    function _burn(uint256 tokenId) internal override {
        super._burn(tokenId);
        delete _licenses[tokenId]; // Revoke license on burn
    }
}
```
