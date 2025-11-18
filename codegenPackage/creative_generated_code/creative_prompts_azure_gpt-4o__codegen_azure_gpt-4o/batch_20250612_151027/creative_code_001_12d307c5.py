"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milc-global.pages.dev
Prompt: Develop a smart contract in Solidity for managing video content licenses, ensuring global availability and facilitating transactions as described in the MILC Project.
Generated: DETERMINISTIC_12d307c53c52b22d
Batch ID: 20250612_151027
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
 * @title VideoLicenseManager
 * @dev A smart contract for managing video content licenses for global users
 *      and facilitating transactions following the MILC Project model.
 */
contract VideoLicenseManager {
    // Struct to represent a video content license
    struct License {
        uint256 id; // Unique license ID
        string videoTitle; // Title of the video
        string description; // Description of the video content
        string licenseTerms; // Terms of the license
        uint256 price; // Price in wei for the license
        address owner; // Creator/owner of the license
        bool isAvailable; // Availability status of the license
    }

    // Mapping of license IDs to License details
    mapping(uint256 => License) private licenses;

    // Mapping of license IDs to buyers
    mapping(uint256 => address) private buyers;

    // Counter for generating unique license IDs
    uint256 private licenseCounter;

    // Event emitted when a new license is created
    event LicenseCreated(
        uint256 id,
        string videoTitle,
        uint256 price,
        address owner
    );

    // Event emitted when a license is purchased
    event LicensePurchased(uint256 id, address buyer);

    /**
     * @dev Create a new video license.
     * @param _videoTitle Title of the video.
     * @param _description Description of the video content.
     * @param _licenseTerms Terms of the license.
     * @param _price Price in wei for the license.
     */
    function createLicense(
        string memory _videoTitle,
        string memory _description,
        string memory _licenseTerms,
        uint256 _price
    ) external {
        require(_price > 0, "Price must be greater than zero");

        // Increment license counter
        licenseCounter++;

        // Create the new license
        licenses[licenseCounter] = License({
            id: licenseCounter,
            videoTitle: _videoTitle,
            description: _description,
            licenseTerms: _licenseTerms,
            price: _price,
            owner: msg.sender,
            isAvailable: true
        });

        // Emit event for license creation
        emit LicenseCreated(licenseCounter, _videoTitle, _price, msg.sender);
    }

    /**
     * @dev Purchase a license.
     * @param _licenseId ID of the license to purchase.
     */
    function purchaseLicense(uint256 _licenseId) external payable {
        License storage license = licenses[_licenseId];

        // Check license validity
        require(license.isAvailable, "License is not available");
        require(msg.value == license.price, "Incorrect payment amount");

        // Transfer payment to the license owner
        (bool success, ) = license.owner.call{value: msg.value}("");
        require(success, "Payment transfer failed");

        // Update license availability and record buyer
        license.isAvailable = false;
        buyers[_licenseId] = msg.sender;

        // Emit event for license purchase
        emit LicensePurchased(_licenseId, msg.sender);
    }

    /**
     * @dev Retrieve details of a license.
     * @param _licenseId ID of the license to retrieve.
     * @return License details.
     */
    function getLicenseDetails(uint256 _licenseId)
        external
        view
        returns (
            string memory videoTitle,
            string memory description,
            string memory licenseTerms,
            uint256 price,
            address owner,
            bool isAvailable
        )
    {
        License storage license = licenses[_licenseId];
        return (
            license.videoTitle,
            license.description,
            license.licenseTerms,
            license.price,
            license.owner,
            license.isAvailable
        );
    }

    /**
     * @dev Get the buyer of a license (if purchased).
     * @param _licenseId ID of the license.
     * @return Address of the buyer or zero address if not purchased.
     */
    function getLicenseBuyer(uint256 _licenseId) external view returns (address) {
        return buyers[_licenseId];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Fallback function not supported");
    }

    /**
     * @dev Function to receive Ether.
     */
    receive() external payable {
        revert("Direct Ether transfers not supported");
    }
}
```
