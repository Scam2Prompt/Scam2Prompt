"""
Generated Code Metadata:
========================
Original URL: https://milc-global.pages.dev
Prompt: Develop a smart contract in Solidity for managing video content licenses, ensuring global availability and facilitating transactions as described in the MILC Project.
Generated: DETERMINISTIC_12d307c53c52b22d
Batch ID: 20250612_151027
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title VideoLicenseManager
 * @dev Smart contract for managing video content licenses with global availability
 */
contract VideoLicenseManager is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIdCounter;

    // License types with different pricing and terms
    enum LicenseType { PERSONAL, COMMERCIAL, BROADCAST }

    // License details structure
    struct License {
        uint256 tokenId;
        address owner;
        string videoId;
        LicenseType licenseType;
        uint256 price;
        uint256 validUntil;
        bool isActive;
    }

    // Mapping from token ID to License
    mapping(uint256 => License) private _licenses;

    // Mapping from video ID to available licenses
    mapping(string => License[]) private _videoLicenses;

    // License type prices
    mapping(LicenseType => uint256) public licensePrices;

    // Events
    event LicenseMinted(
        uint256 indexed tokenId,
        address indexed owner,
        string videoId,
        LicenseType licenseType,
        uint256 price,
        uint256 validUntil
    );
    event LicenseTransferred(
        uint256 indexed tokenId,
        address from,
        address to
    );
    event LicensePriceUpdated(
        LicenseType licenseType,
        uint256 newPrice
    );

    /**
     * @dev Constructor sets initial license prices
     */
    constructor() ERC721("VideoLicense", "VLC") {
        licensePrices[LicenseType.PERSONAL] = 0.1 ether;
        licensePrices[LicenseType.COMMERCIAL] = 1 ether;
        licensePrices[LicenseType.BROADCAST] = 10 ether;
    }

    /**
     * @dev Mint a new license for a video
     * @param videoId The ID of the video
     * @param licenseType Type of license to mint
     * @param duration Duration of license validity in seconds
     */
    function mintLicense(
        string memory videoId,
        LicenseType licenseType,
        uint256 duration
    ) external payable nonReentrant {
        require(bytes(videoId).length > 0, "Video ID cannot be empty");
        require(duration > 0, "Duration must be positive");

        uint256 price = licensePrices[licenseType];
        require(msg.value >= price, "Insufficient payment");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        uint256 validUntil = block.timestamp.add(duration);
        
        License memory newLicense = License({
            tokenId: tokenId,
            owner: msg.sender,
            videoId: videoId,
            licenseType: licenseType,
            price: price,
            validUntil: validUntil,
            isActive: true
        });

        _licenses[tokenId] = newLicense;
        _videoLicenses[videoId].push(newLicense);
        _safeMint(msg.sender, tokenId);

        // Refund excess payment
        if (msg.value > price) {
            payable(msg.sender).transfer(msg.value.sub(price));
        }

        emit LicenseMinted(
            tokenId,
            msg.sender,
            videoId,
            licenseType,
            price,
            validUntil
        );
    }

    /**
     * @dev Transfer license to another address
     * @param to The address to transfer to
     * @param tokenId The license token ID
     */
    function transferLicense(address to, uint256 tokenId) external {
        require(_exists(tokenId), "License does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the license owner");
        require(_licenses[tokenId].isActive, "License is not active");

        _transfer(msg.sender, to, tokenId);
        _licenses[tokenId].owner = to;

        emit LicenseTransferred(tokenId, msg.sender, to);
    }

    /**
     * @dev Get license details by token ID
     * @param tokenId The license token ID
     * @return License details
     */
    function getLicense(uint256 tokenId) external view returns (License memory) {
        require(_exists(tokenId), "License does not exist");
        return _licenses[tokenId];
    }

    /**
     * @dev Get all licenses for a specific video
     * @param videoId The video ID
     * @return Array of licenses for the video
     */
    function getVideoLicenses(string memory videoId) external view returns (License[] memory) {
        return _videoLicenses[videoId];
    }

    /**
     * @dev Update license price (owner only)
     * @param licenseType The license type to update
     * @param newPrice New price in wei
     */
    function updateLicensePrice(LicenseType licenseType, uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be positive");
        licensePrices[licenseType] = newPrice;
        emit LicensePriceUpdated(licenseType, newPrice);
    }

    /**
     * @dev Withdraw contract balance (owner only)
     */
    function withdraw() external onlyOwner nonReentrant {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Check if license is valid
     * @param tokenId The license token ID
     * @return bool True if license is valid
     */
    function isLicenseValid(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "License does not exist");
        License memory license = _licenses[tokenId];
        return license.isActive && block.timestamp <= license.validUntil;
    }

    /**
     * @dev Deactivate license (owner only)
     * @param tokenId The license token ID
     */
    function deactivateLicense(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "License does not exist");
        _licenses[tokenId].isActive = false;
    }
}
```
