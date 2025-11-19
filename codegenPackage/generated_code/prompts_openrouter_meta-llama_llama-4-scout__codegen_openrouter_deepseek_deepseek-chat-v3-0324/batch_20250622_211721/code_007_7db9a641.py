"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: "Propose an on-chain identity solution for permissioned and permissionless products on Singularity Finance, ensuring AML compliance."
Generated: DETERMINISTIC_7db9a641553cbdc3
Batch ID: 20250622_211721
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title IdentityRegistry
 * @dev On-chain identity solution for Singularity Finance with AML compliance
 */
contract IdentityRegistry is AccessControl {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Roles
    bytes32 public constant AML_COMPLIANCE_ROLE = keccak256("AML_COMPLIANCE_ROLE");
    bytes32 public constant PERMISSIONED_PRODUCT_ROLE = keccak256("PERMISSIONED_PRODUCT_ROLE");

    // Identity structure
    struct Identity {
        string identifier; // Unique identifier (e.g., DID)
        uint256 createdAt;
        uint256 lastVerifiedAt;
        bool isVerified;
        bool isBlacklisted;
    }

    // Events
    event IdentityRegistered(address indexed user, string identifier);
    event IdentityVerified(address indexed user);
    event IdentityBlacklisted(address indexed user);
    event IdentityWhitelisted(address indexed user);

    // Storage
    mapping(address => Identity) public identities;
    EnumerableSet.AddressSet private registeredUsers;

    constructor() {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(AML_COMPLIANCE_ROLE, msg.sender);
    }

    /**
     * @dev Register a new identity
     * @param _identifier Unique identifier for the user
     */
    function registerIdentity(string memory _identifier) external {
        require(bytes(_identifier).length > 0, "Invalid identifier");
        require(!_isRegistered(msg.sender), "Already registered");

        identities[msg.sender] = Identity({
            identifier: _identifier,
            createdAt: block.timestamp,
            lastVerifiedAt: 0,
            isVerified: false,
            isBlacklisted: false
        });

        registeredUsers.add(msg.sender);
        emit IdentityRegistered(msg.sender, _identifier);
    }

    /**
     * @dev Verify a user's identity (AML compliance)
     * @param user Address of the user to verify
     */
    function verifyIdentity(address user) external onlyRole(AML_COMPLIANCE_ROLE) {
        require(_isRegistered(user), "User not registered");
        require(!identities[user].isBlacklisted, "User is blacklisted");

        identities[user].isVerified = true;
        identities[user].lastVerifiedAt = block.timestamp;
        emit IdentityVerified(user);
    }

    /**
     * @dev Blacklist a user (AML compliance)
     * @param user Address of the user to blacklist
     */
    function blacklistUser(address user) external onlyRole(AML_COMPLIANCE_ROLE) {
        require(_isRegistered(user), "User not registered");
        identities[user].isBlacklisted = true;
        emit IdentityBlacklisted(user);
    }

    /**
     * @dev Whitelist a previously blacklisted user
     * @param user Address of the user to whitelist
     */
    function whitelistUser(address user) external onlyRole(AML_COMPLIANCE_ROLE) {
        require(_isRegistered(user), "User not registered");
        require(identities[user].isBlacklisted, "User not blacklisted");
        identities[user].isBlacklisted = false;
        emit IdentityWhitelisted(user);
    }

    /**
     * @dev Check if a user can access permissioned products
     * @param user Address of the user to check
     */
    function canAccessPermissionedProducts(address user) external view returns (bool) {
        return _isRegistered(user) && 
               identities[user].isVerified && 
               !identities[user].isBlacklisted;
    }

    /**
     * @dev Check if address is registered
     */
    function isRegistered(address user) external view returns (bool) {
        return _isRegistered(user);
    }

    /**
     * @dev Internal check for registration status
     */
    function _isRegistered(address user) internal view returns (bool) {
        return registeredUsers.contains(user);
    }

    /**
     * @dev Get total number of registered users
     */
    function getTotalUsers() external view returns (uint256) {
        return registeredUsers.length();
    }

    /**
     * @dev Get user at specific index
     */
    function getUserAtIndex(uint256 index) external view returns (address) {
        require(index < registeredUsers.length(), "Index out of bounds");
        return registeredUsers.at(index);
    }
}

/**
 * @title PermissionedProduct
 * @dev Example contract showing integration with IdentityRegistry
 */
contract PermissionedProduct {
    IdentityRegistry public identityRegistry;

    constructor(address _registryAddress) {
        identityRegistry = IdentityRegistry(_registryAddress);
    }

    /**
     * @dev Restrict access to verified, non-blacklisted users
     */
    modifier onlyVerifiedUsers() {
        require(
            identityRegistry.canAccessPermissionedProducts(msg.sender),
            "Unauthorized: Identity not verified or blacklisted"
        );
        _;
    }

    /**
     * @dev Example function for permissioned product
     */
    function accessPermissionedFeature() external onlyVerifiedUsers {
        // Business logic for permissioned feature
    }
}

/**
 * @title PermissionlessProduct
 * @dev Example contract showing integration with IdentityRegistry
 */
contract PermissionlessProduct {
    IdentityRegistry public identityRegistry;

    constructor(address _registryAddress) {
        identityRegistry = IdentityRegistry(_registryAddress);
    }

    /**
     * @dev Example function for permissionless product
     */
    function accessPermissionlessFeature() external {
        // Optional: Track usage for AML purposes
        if (identityRegistry.isRegistered(msg.sender)) {
            // Log registered user activity
        }
        // Business logic for permissionless feature
    }
}
```
