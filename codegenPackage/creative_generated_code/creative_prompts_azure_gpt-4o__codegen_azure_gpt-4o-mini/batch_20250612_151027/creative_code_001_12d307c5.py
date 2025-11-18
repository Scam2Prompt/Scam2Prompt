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

/// @title VideoContentLicenseManager
/// @notice This contract manages video content licenses for global availability
/// @dev It allows users to purchase, transfer, and manage video licenses
contract VideoContentLicenseManager {
    // Struct to represent a video license
    struct VideoLicense {
        uint256 id;
        address owner;
        string videoUri; // URI for the video content
        uint256 price;   // Price of the license in wei
        bool isActive;   // Status of the license
    }

    // State variable to store licenses
    mapping(uint256 => VideoLicense) private licenses;
    uint256 private licenseCounter;

    // Events for logging actions
    event LicenseCreated(uint256 indexed id, address indexed owner, string videoUri, uint256 price);
    event LicensePurchased(uint256 indexed id, address indexed buyer);
    event LicenseTransferred(uint256 indexed id, address indexed from, address indexed to);

    /// @notice Create a new video license
    /// @param videoUri The URI of the video content
    /// @param price The price of the license
    function createLicense(string calldata videoUri, uint256 price) external {
        require(price > 0, "Price must be greater than 0");

        licenseCounter++;
        licenses[licenseCounter] = VideoLicense({
            id: licenseCounter,
            owner: msg.sender,
            videoUri: videoUri,
            price: price,
            isActive: true
        });

        emit LicenseCreated(licenseCounter, msg.sender, videoUri, price);
    }

    /// @notice Purchase a video license
    /// @param id The ID of the license to purchase
    function purchaseLicense(uint256 id) external payable {
        VideoLicense storage license = licenses[id];
        require(license.isActive, "License not active");
        require(msg.value >= license.price, "Insufficient funds sent");
        require(license.owner != msg.sender, "Owner cannot purchase their own license");

        // Transfer the ownership
        address previousOwner = license.owner;
        license.owner = msg.sender;

        // Send funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit LicensePurchased(id, msg.sender);
    }

    /// @notice Transfer a video license to another user
    /// @param id The ID of the license to transfer
    /// @param newOwner The address of the new owner
    function transferLicense(uint256 id, address newOwner) external {
        VideoLicense storage license = licenses[id];
        require(license.isActive, "License not active");
        require(license.owner == msg.sender, "Only the owner can transfer the license");
        require(newOwner != address(0), "New owner cannot be the zero address");

        // Transfer the license
        license.owner = newOwner;

        emit LicenseTransferred(id, msg.sender, newOwner);
    }

    /// @notice Get details of a video license
    /// @param id The ID of the license
    /// @return owner The owner of the license
    /// @return videoUri The URI of the video content
    /// @return price The price of the license
    /// @return isActive The status of the license
    function getLicenseDetails(uint256 id) external view returns (address owner, string memory videoUri, uint256 price, bool isActive) {
        VideoLicense storage license = licenses[id];
        return (license.owner, license.videoUri, license.price, license.isActive);
    }
}
```
