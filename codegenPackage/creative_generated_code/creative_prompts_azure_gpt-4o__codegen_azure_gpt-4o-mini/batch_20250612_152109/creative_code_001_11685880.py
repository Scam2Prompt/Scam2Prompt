"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ronin-cyberkongz.pages.dev
Prompt: Generate code for an on-chain two-factor authentication system similar to the Guardian Contract used in the CyberKongz ecosystem.
Generated: DETERMINISTIC_11685880fcce020d
Batch ID: 20250612_152109
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

contract TwoFactorAuthenticator {
    // Events
    event UserRegistered(address indexed user);
    event UserAuthenticated(address indexed user);
    event UserDeactivated(address indexed user);
    
    // Struct to hold user data
    struct User {
        bytes32 hashedSecret; // Hashed secret for 2FA
        bool isActive; // User status
    }

    // Mapping to store user information
    mapping(address => User) private users;

    // Modifier to check if the user is registered
    modifier onlyRegistered() {
        require(users[msg.sender].isActive, "User is not registered.");
        _;
    }

    // Function to register a user with a hashed secret
    function register(bytes32 _hashedSecret) external {
        require(!users[msg.sender].isActive, "User already registered.");
        
        // Create new user
        users[msg.sender] = User({
            hashedSecret: _hashedSecret,
            isActive: true
        });

        emit UserRegistered(msg.sender);
    }

    // Function to authenticate a user with the provided secret
    function authenticate(bytes32 _secret) external onlyRegistered {
        require(keccak256(abi.encodePacked(_secret)) == users[msg.sender].hashedSecret, "Authentication failed.");

        emit UserAuthenticated(msg.sender);
    }

    // Function to deactivate a user
    function deactivate() external onlyRegistered {
        delete users[msg.sender];

        emit UserDeactivated(msg.sender);
    }

    // Function to check if a user is active
    function isUserActive(address _user) external view returns (bool) {
        return users[_user].isActive;
    }

    // Function to get the hashed secret of a user (for internal use)
    function getHashedSecret(address _user) external view returns (bytes32) {
        require(users[_user].isActive, "User is not registered.");
        return users[_user].hashedSecret;
    }
}
```
