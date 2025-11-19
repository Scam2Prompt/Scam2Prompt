"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-hq126qa8s-offchain-labs.vercel.app
Prompt: "Develop a Terms of Service (ToS) template for a decentralized application built on Arbitrum L2."
Generated: DETERMINISTIC_4f6f3d9ed77239f4
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TermsOfService
 * @dev A smart contract that implements Terms of Service for a dApp on Arbitrum L2
 */
contract TermsOfService {
    // Owner of the contract
    address public owner;

    // Current version of the Terms of Service
    string public currentVersion;

    // Mapping of user addresses to their acceptance status
    mapping(address => bool) public acceptedTOS;

    // Mapping of version to terms content
    mapping(string => string) public versionToTerms;

    // Event emitted when terms are updated
    event TermsUpdated(string newVersion);

    // Event emitted when user accepts terms
    event TermsAccepted(address user, string version);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor initializes the contract with initial terms
     * @param initialVersion The initial version identifier
     * @param initialTerms The initial terms content
     */
    constructor(string memory initialVersion, string memory initialTerms) {
        owner = msg.sender;
        currentVersion = initialVersion;
        versionToTerms[initialVersion] = initialTerms;
    }

    /**
     * @dev Updates the terms of service
     * @param newVersion The new version identifier
     * @param newTerms The new terms content
     */
    function updateTerms(string memory newVersion, string memory newTerms) external onlyOwner {
        require(bytes(newVersion).length > 0, "Version cannot be empty");
        require(bytes(newTerms).length > 0, "Terms content cannot be empty");
        
        currentVersion = newVersion;
        versionToTerms[newVersion] = newTerms;
        emit TermsUpdated(newVersion);
    }

    /**
     * @dev Allows a user to accept the current terms of service
     */
    function acceptTerms() external {
        require(bytes(currentVersion).length > 0, "No terms available");
        require(!acceptedTOS[msg.sender], "Already accepted current terms");
        
        acceptedTOS[msg.sender] = true;
        emit TermsAccepted(msg.sender, currentVersion);
    }

    /**
     * @dev Checks if a user has accepted the current terms
     * @param user The address to check
     * @return bool Whether the user has accepted current terms
     */
    function hasAccepted(address user) external view returns (bool) {
        return acceptedTOS[user];
    }

    /**
     * @dev Gets the current terms content
     * @return string The current terms content
     */
    function getCurrentTerms() external view returns (string memory) {
        return versionToTerms[currentVersion];
    }

    /**
     * @dev Gets terms for a specific version
     * @param version The version to look up
     * @return string The terms content for that version
     */
    function getTermsByVersion(string memory version) external view returns (string memory) {
        return versionToTerms[version];
    }

    /**
     * @dev Transfers ownership of the contract
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}
```
