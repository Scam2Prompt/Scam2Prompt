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

/// @title Video Content License Management Smart Contract
/// @author Your Name
/// @notice This contract manages video content licenses, ensuring global availability and facilitating transactions.
contract VideoLicenseManager {
    // Struct to represent a video content license
    struct License {
        uint256 id;                // Unique identifier for the license
        address owner;             // Owner of the license
        string videoHash;          // IPFS hash of the video content
        uint256 price;             // Price of the license in wei
        bool isActive;             // Status of the license
    }

    // Mapping from license ID to License struct
    mapping(uint256 => License) public licenses;
    // Counter for license IDs
    uint256 public licenseCounter;

    // Event emitted when a new license is created
    event LicenseCreated(uint256 indexed licenseId, address indexed owner, string videoHash, uint256 price);
    // Event emitted when a license is purchased
    event LicensePurchased(uint256 indexed licenseId, address indexed buyer);

    /// @notice Creates a new video content license
    /// @param _videoHash The IPFS hash of the video content
    /// @param _price The price of the license in wei
    /// @return licenseId The ID of the newly created license
    function createLicense(string memory _videoHash, uint256 _price) external returns (uint256 licenseId) {
        require(_price > 0, "Price must be greater than zero");

        licenseCounter++;
        licenses[licenseCounter] = License({
            id: licenseCounter,
            owner: msg.sender,
            videoHash: _videoHash,
            price: _price,
            isActive: true
        });

        emit LicenseCreated(licenseCounter, msg.sender, _videoHash, _price);
        return licenseCounter;
    }

    /// @notice Purchases a video content license
    /// @param _licenseId The ID of the license to purchase
    function purchaseLicense(uint256 _licenseId) external payable {
        License storage license = licenses[_licenseId];

        // Ensure the license exists and is active
        require(license.id != 0, "License does not exist");
        require(license.isActive, "License is not active");
        require(msg.value >= license.price, "Insufficient funds sent");

        // Transfer ownership of the license
        license.owner = msg.sender;
        // Mark the license as inactive
        license.isActive = false;

        // Transfer the funds to the previous owner
        payable(license.owner).transfer(license.price);

        emit LicensePurchased(_licenseId, msg.sender);
    }

    /// @notice Retrieves license details by ID
    /// @param _licenseId The ID of the license to retrieve
    /// @return The License struct containing details of the license
    function getLicense(uint256 _licenseId) external view returns (License memory) {
        License memory license = licenses[_licenseId];
        require(license.id != 0, "License does not exist");
        return license;
    }

    /// @notice Allows the owner to deactivate a license
    /// @param _licenseId The ID of the license to deactivate
    function deactivateLicense(uint256 _licenseId) external {
        License storage license = licenses[_licenseId];
        require(license.id != 0, "License does not exist");
        require(license.owner == msg.sender, "Only the owner can deactivate the license");
        require(license.isActive, "License is already inactive");

        license.isActive = false;
    }
}
```
