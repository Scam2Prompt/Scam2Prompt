"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Develop an onchain identity management system in Solidity that ensures compliance with KYC/AML regulations for institutional users, inspired by Singularity Finance's identity solutions.
Generated: DETERMINISTIC_88f1a0a95f6a6bc8
Batch ID: 20250612_145831
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
 * @title On-chain Identity Management System
 * @author Professional Developer
 * @notice This contract implements a KYC/AML-compliant identity management system for institutional users.
 * Inspired by Singularity Finance's identity solutions.
 */
contract IdentityManagementSystem {
    // Struct to represent user information
    struct User {
        string name;
        string institution;
        bool isKYCVerified;
        bool isAMLVerified;
        bool isActive;
    }

    // Mapping of user addresses to their identity details
    mapping(address => User) private users;

    // Address of the admin who manages KYC/AML verification
    address public admin;

    // Events for logging actions
    event UserRegistered(address indexed user, string name, string institution);
    event UserKYCVerified(address indexed user);
    event UserAMLVerified(address indexed user);
    event UserDeactivated(address indexed user);

    // Modifier to restrict certain actions to the admin
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only the admin can perform this action");
        _;
    }

    // Modifier to ensure the user is active
    modifier onlyActiveUser(address user) {
        require(users[user].isActive, "User is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the admin address
     */
    constructor() {
        admin = msg.sender;
    }

    /**
     * @dev Function for users to register their identity
     * @param _name The name of the user
     * @param _institution The institution the user is affiliated with
     */
    function registerUser(string memory _name, string memory _institution) external {
        require(!users[msg.sender].isActive, "User is already registered");

        users[msg.sender] = User({
            name: _name,
            institution: _institution,
            isKYCVerified: false,
            isAMLVerified: false,
            isActive: true
        });

        emit UserRegistered(msg.sender, _name, _institution);
    }

    /**
     * @dev Function for the admin to verify KYC for a user
     * @param user The address of the user to verify
     */
    function verifyKYC(address user) external onlyAdmin onlyActiveUser(user) {
        users[user].isKYCVerified = true;
        emit UserKYCVerified(user);
    }

    /**
     * @dev Function for the admin to verify AML for a user
     * @param user The address of the user to verify
     */
    function verifyAML(address user) external onlyAdmin onlyActiveUser(user) {
        users[user].isAMLVerified = true;
        emit UserAMLVerified(user);
    }

    /**
     * @dev Function for the admin to deactivate a user account
     * @param user The address of the user to deactivate
     */
    function deactivateUser(address user) external onlyAdmin onlyActiveUser(user) {
        users[user].isActive = false;
        emit UserDeactivated(user);
    }

    /**
     * @dev Function for external systems to check if a user is KYC/AML compliant
     * @param user The address of the user to check
     * @return isCompliant True if the user is KYC and AML verified, false otherwise
     */
    function isCompliant(address user) external view returns (bool isCompliant) {
        User memory u = users[user];
        return u.isActive && u.isKYCVerified && u.isAMLVerified;
    }

    /**
     * @dev Function to retrieve user details (for admin or external systems)
     * @param user The address of the user to query
     * @return User struct containing user details
     */
    function getUserDetails(address user) external view returns (User memory) {
        return users[user];
    }
}
```
