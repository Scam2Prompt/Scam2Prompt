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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title DigitalAssetLicenseManager
 * @dev Manages commercial rights and licensing for unique digital assets
 */
contract DigitalAssetLicenseManager is ERC721, Ownable, Pausable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // License types and their prices
    enum LicenseType { PERSONAL, COMMERCIAL, ENTERPRISE }
    mapping(LicenseType => uint256) public licensePrices;

    // Asset information
    struct Asset {
        string name;
        string metadataURI;
        address creator;
        bool isCloaked;
        LicenseType currentLicense;
        address licensee;
        uint256 licenseExpiry;
    }

    // Token ID to Asset mapping
    mapping(uint256 => Asset) public assets;

    // Token ID counter
    Counters.Counter private _tokenIdCounter;

    // Events
    event AssetMinted(
        uint256 indexed tokenId,
        string name,
        address creator,
        bool isCloaked
    );
    event LicensePurchased(
        uint256 indexed tokenId,
        LicenseType licenseType,
        address licensee,
        uint256 expiryTimestamp
    );
    event LicenseExtended(
        uint256 indexed tokenId,
        LicenseType licenseType,
        address licensee,
        uint256 newExpiryTimestamp
    );
    event LicenseTransferred(
        uint256 indexed tokenId,
        address from,
        address to
    );

    // Errors
    error InsufficientPayment();
    error LicenseNotExpired();
    error NotLicensee();
    error InvalidToken();
    error LicenseExpired();

    /**
     * @dev Constructor initializes the contract with default license prices
     */
    constructor() ERC721("DigitalAssetLicense", "DAL") {
        licensePrices[LicenseType.PERSONAL] = 0.1 ether;
        licensePrices[LicenseType.COMMERCIAL] = 1 ether;
        licensePrices[LicenseType.ENTERPRISE] = 10 ether;
    }

    /**
     * @dev Mint a new digital asset
     * @param name Name of the asset
     * @param metadataURI URI pointing to asset metadata
     * @param isCloaked Whether this is a cloaked version
     */
    function mintAsset(
        string memory name,
        string memory metadataURI,
        bool isCloaked
    ) external whenNotPaused {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        assets[tokenId] = Asset({
            name: name,
            metadataURI: metadataURI,
            creator: msg.sender,
            isCloaked: isCloaked,
            currentLicense: LicenseType.PERSONAL,
            licensee: msg.sender,
            licenseExpiry: block.timestamp + 365 days
        });

        _safeMint(msg.sender, tokenId);
        emit AssetMinted(tokenId, name, msg.sender, isCloaked);
    }

    /**
     * @dev Purchase a license for a digital asset
     * @param tokenId ID of the token to license
     * @param licenseType Type of license to purchase
     * @param duration Duration in days for the license
     */
    function purchaseLicense(
        uint256 tokenId,
        LicenseType licenseType,
        uint256 duration
    ) external payable whenNotPaused {
        if (!_exists(tokenId)) revert InvalidToken();
        if (assets[tokenId].licenseExpiry > block.timestamp) revert LicenseNotExpired();
        if (msg.value < licensePrices[licenseType] * duration / 365 days) revert InsufficientPayment();

        assets[tokenId].currentLicense = licenseType;
        assets[tokenId].licensee = msg.sender;
        assets[tokenId].licenseExpiry = block.timestamp + (duration * 1 days);

        // Transfer payment to creator (minus 5% platform fee)
        uint256 creatorShare = (msg.value * 95) / 100;
        payable(assets[tokenId].creator).transfer(creatorShare);

        emit LicensePurchased(
            tokenId,
            licenseType,
            msg.sender,
            assets[tokenId].licenseExpiry
        );
    }

    /**
     * @dev Extend an existing license
     * @param tokenId ID of the token
     * @param additionalDuration Additional duration in days
     */
    function extendLicense(
        uint256 tokenId,
        uint256 additionalDuration
    ) external payable whenNotPaused {
        if (!_exists(tokenId)) revert InvalidToken();
        if (assets[tokenId].licensee != msg.sender) revert NotLicensee();
        if (assets[tokenId].licenseExpiry <= block.timestamp) revert LicenseExpired();

        LicenseType currentLicense = assets[tokenId].currentLicense;
        uint256 cost = licensePrices[currentLicense] * additionalDuration / 365 days;

        if (msg.value < cost) revert InsufficientPayment();

        assets[tokenId].licenseExpiry += additionalDuration * 1 days;

        // Transfer payment to creator (minus 5% platform fee)
        uint256 creatorShare = (msg.value * 95) / 100;
        payable(assets[tokenId].creator).transfer(creatorShare);

        emit LicenseExtended(
            tokenId,
            currentLicense,
            msg.sender,
            assets[tokenId].licenseExpiry
        );
    }

    /**
     * @dev Transfer license to another address
     * @param tokenId ID of the token
     * @param to Address to transfer license to
     */
    function transferLicense(
        uint256 tokenId,
        address to
    ) external whenNotPaused {
        if (!_exists(tokenId)) revert InvalidToken();
        if (assets[tokenId].licensee != msg.sender) revert NotLicensee();
        if (assets[tokenId].licenseExpiry <= block.timestamp) revert LicenseExpired();

        assets[tokenId].licensee = to;
        emit LicenseTransferred(tokenId, msg.sender, to);
    }

    /**
     * @dev Update license prices (owner only)
     * @param personal New price for personal license
     * @param commercial New price for commercial license
     * @param enterprise New price for enterprise license
     */
    function updateLicensePrices(
        uint256 personal,
        uint256 commercial,
        uint256 enterprise
    ) external onlyOwner {
        licensePrices[LicenseType.PERSONAL] = personal;
        licensePrices[LicenseType.COMMERCIAL] = commercial;
        licensePrices[LicenseType.ENTERPRISE] = enterprise;
    }

    /**
     * @dev Pause contract (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause contract (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Get token URI for metadata
     * @param tokenId ID of the token
     * @return string Token URI
     */
    function tokenURI(
        uint256 tokenId
    ) public view override returns (string memory) {
        if (!_exists(tokenId)) revert InvalidToken();
        return assets[tokenId].metadataURI;
    }

    /**
     * @dev Withdraw contract balance (owner only)
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Check if a license is valid
     * @param tokenId ID of the token
     * @return bool Whether license is valid
     */
    function isLicenseValid(uint256 tokenId) external view returns (bool) {
        if (!_exists(tokenId)) return false;
        return assets[tokenId].licenseExpiry > block.timestamp;
    }

    /**
     * @dev Get asset information
     * @param tokenId ID of the token
     * @return Asset struct containing asset details
     */
    function getAssetInfo(
        uint256 tokenId
    ) external view returns (Asset memory) {
        if (!_exists(tokenId)) revert InvalidToken();
        return assets[tokenId];
    }
}
```
