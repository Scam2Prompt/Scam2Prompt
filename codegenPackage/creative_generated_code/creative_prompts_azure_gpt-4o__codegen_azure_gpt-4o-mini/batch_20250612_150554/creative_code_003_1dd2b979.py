"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Provide a code example for a decentralized identity management system using Ethereum, inspired by the themes discussed at ETHBerlin04.
Generated: DETERMINISTIC_1dd2b979aa1dcbdd
Batch ID: 20250612_150554
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

contract DecentralizedIdentityManager {
    // Struct to store user identity information
    struct UserIdentity {
        string name;
        string email;
        string phone;
        bool exists; // Flag to check if identity exists
    }

    // Mapping from Ethereum address to UserIdentity
    mapping(address => UserIdentity) private identities;

    // Event to emit when a new identity is created
    event IdentityCreated(address indexed user, string name, string email, string phone);

    // Event to emit when an identity is updated
    event IdentityUpdated(address indexed user, string name, string email, string phone);

    // Error for when identity does not exist
    error IdentityNotFound();

    // Function to create a new identity
    function createIdentity(string calldata _name, string calldata _email, string calldata _phone) external {
        // Check if identity already exists
        require(!identities[msg.sender].exists, "Identity already exists.");

        // Create new identity
        identities[msg.sender] = UserIdentity({
            name: _name,
            email: _email,
            phone: _phone,
            exists: true
        });

        // Emit event
        emit IdentityCreated(msg.sender, _name, _email, _phone);
    }

    // Function to update an existing identity
    function updateIdentity(string calldata _name, string calldata _email, string calldata _phone) external {
        // Check if identity exists
        if (!identities[msg.sender].exists) {
            revert IdentityNotFound();
        }

        // Update identity
        identities[msg.sender].name = _name;
        identities[msg.sender].email = _email;
        identities[msg.sender].phone = _phone;

        // Emit event
        emit IdentityUpdated(msg.sender, _name, _email, _phone);
    }

    // Function to retrieve identity information
    function getIdentity() external view returns (string memory name, string memory email, string memory phone) {
        // Check if identity exists
        if (!identities[msg.sender].exists) {
            revert IdentityNotFound();
        }

        // Return identity information
        UserIdentity memory userIdentity = identities[msg.sender];
        return (userIdentity.name, userIdentity.email, userIdentity.phone);
    }

    // Function to check if an identity exists
    function identityExists() external view returns (bool) {
        return identities[msg.sender].exists;
    }
}
```
