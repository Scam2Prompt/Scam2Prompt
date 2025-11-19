"""
Generated Code Metadata:
========================
Original URL: https://destranetwork.pages.dev
Prompt: Provide an example of integrating Destra's web hosting service into a decentralized application using smart contracts.
Generated: DETERMINISTIC_ddbd8ddc39a39c39
Batch ID: 20250612_153512
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

/**
 * @title DestraWebHosting
 * @dev Smart contract for integrating Destra's decentralized web hosting service
 */
contract DestraWebHosting {
    // Struct to store website hosting details
    struct Website {
        address owner;
        string cid; // Content Identifier for IPFS/Filecoin storage
        uint256 storageSize; // in MB
        uint256 expiryTimestamp;
        bool isActive;
    }

    // Mapping from website ID to Website details
    mapping(uint256 => Website) public websites;
    
    // Counter for website IDs
    uint256 public nextWebsiteId = 1;
    
    // Events
    event WebsiteRegistered(
        uint256 indexed websiteId,
        address indexed owner,
        string cid,
        uint256 storageSize,
        uint256 expiryTimestamp
    );
    
    event WebsiteRenewed(
        uint256 indexed websiteId,
        uint256 newExpiryTimestamp
    );
    
    event WebsiteDeactivated(
        uint256 indexed websiteId
    );

    // Error definitions
    error Unauthorized();
    error InvalidDuration();
    error WebsiteNotFound();
    error WebsiteExpired();
    error InvalidCID();

    /**
     * @dev Register a new website
     * @param _cid Content Identifier for the website
     * @param _storageSize Storage size required in MB
     * @param _duration Duration in seconds for hosting
     */
    function registerWebsite(
        string memory _cid,
        uint256 _storageSize,
        uint256 _duration
    ) external payable {
        if (bytes(_cid).length == 0) {
            revert InvalidCID();
        }
        if (_duration == 0) {
            revert InvalidDuration();
        }

        uint256 expiryTimestamp = block.timestamp + _duration;
        uint256 websiteId = nextWebsiteId++;
        
        websites[websiteId] = Website({
            owner: msg.sender,
            cid: _cid,
            storageSize: _storageSize,
            expiryTimestamp: expiryTimestamp,
            isActive: true
        });

        emit WebsiteRegistered(
            websiteId,
            msg.sender,
            _cid,
            _storageSize,
            expiryTimestamp
        );
    }

    /**
     * @dev Renew website hosting
     * @param _websiteId ID of the website to renew
     * @param _duration Additional duration in seconds
     */
    function renewWebsite(
        uint256 _websiteId,
        uint256 _duration
    ) external payable {
        Website storage website = websites[_websiteId];
        
        if (website.owner == address(0)) {
            revert WebsiteNotFound();
        }
        if (website.owner != msg.sender) {
            revert Unauthorized();
        }
        if (_duration == 0) {
            revert InvalidDuration();
        }

        website.expiryTimestamp += _duration;
        emit WebsiteRenewed(_websiteId, website.expiryTimestamp);
    }

    /**
     * @dev Deactivate a website
     * @param _websiteId ID of the website to deactivate
     */
    function deactivateWebsite(uint256 _websiteId) external {
        Website storage website = websites[_websiteId];
        
        if (website.owner == address(0)) {
            revert WebsiteNotFound();
        }
        if (website.owner != msg.sender) {
            revert Unauthorized();
        }

        website.isActive = false;
        emit WebsiteDeactivated(_websiteId);
    }

    /**
     * @dev Check if a website is active and not expired
     * @param _websiteId ID of the website to check
     * @return bool True if website is active and not expired
     */
    function isWebsiteActive(uint256 _websiteId) public view returns (bool) {
        Website memory website = websites[_websiteId];
        
        if (website.owner == address(0)) {
            return false;
        }
        
        return website.isActive && website.expiryTimestamp > block.timestamp;
    }

    /**
     * @dev Get website details
     * @param _websiteId ID of the website
     * @return Website details struct
     */
    function getWebsiteDetails(uint256 _websiteId) external view returns (Website memory) {
        if (websites[_websiteId].owner == address(0)) {
            revert WebsiteNotFound();
        }
        return websites[_websiteId];
    }
}
```
