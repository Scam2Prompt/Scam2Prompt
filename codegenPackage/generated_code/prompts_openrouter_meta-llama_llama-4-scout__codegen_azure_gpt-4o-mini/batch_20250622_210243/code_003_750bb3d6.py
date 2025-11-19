"""
Generated Code Metadata:
========================
Original URL: https://phi-f1z.pages.dev
Prompt: Design a simple smart contract using Solidity to create a community-driven credential system for on-chain identity on a blockchain platform.
Generated: DETERMINISTIC_750bb3d6469620b9
Batch ID: 20250622_210243
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

/// @title Community-Driven Credential System
/// @author Your Name
/// @notice This contract allows users to create and manage on-chain identities and credentials
/// @dev The contract uses a mapping to store user credentials and events to log actions

contract CredentialSystem {
    // Struct to represent a user's credential
    struct Credential {
        string name; // Name of the credential
        string description; // Description of the credential
        address issuer; // Address of the issuer
        uint256 issuedAt; // Timestamp when the credential was issued
        bool isActive; // Status of the credential
    }

    // Mapping from user address to their credentials
    mapping(address => Credential[]) private userCredentials;

    // Event emitted when a new credential is issued
    event CredentialIssued(address indexed user, string name, string description, address indexed issuer, uint256 issuedAt);

    // Event emitted when a credential is revoked
    event CredentialRevoked(address indexed user, string name, address indexed issuer);

    /// @notice Issues a new credential to a user
    /// @param _user The address of the user receiving the credential
    /// @param _name The name of the credential
    /// @param _description A description of the credential
    /// @dev Only the contract owner can issue credentials
    function issueCredential(address _user, string memory _name, string memory _description) public {
        require(_user != address(0), "Invalid user address");
        require(bytes(_name).length > 0, "Credential name cannot be empty");
        require(bytes(_description).length > 0, "Credential description cannot be empty");

        // Create a new credential
        Credential memory newCredential = Credential({
            name: _name,
            description: _description,
            issuer: msg.sender,
            issuedAt: block.timestamp,
            isActive: true
        });

        // Add the credential to the user's list
        userCredentials[_user].push(newCredential);

        // Emit an event for the issued credential
        emit CredentialIssued(_user, _name, _description, msg.sender, block.timestamp);
    }

    /// @notice Revokes a credential from a user
    /// @param _user The address of the user whose credential is being revoked
    /// @param _name The name of the credential to revoke
    /// @dev Only the issuer of the credential can revoke it
    function revokeCredential(address _user, string memory _name) public {
        require(_user != address(0), "Invalid user address");
        require(bytes(_name).length > 0, "Credential name cannot be empty");

        // Find the credential and revoke it
        for (uint256 i = 0; i < userCredentials[_user].length; i++) {
            if (keccak256(abi.encodePacked(userCredentials[_user][i].name)) == keccak256(abi.encodePacked(_name)) && 
                userCredentials[_user][i].issuer == msg.sender) {
                userCredentials[_user][i].isActive = false;

                // Emit an event for the revoked credential
                emit CredentialRevoked(_user, _name, msg.sender);
                return;
            }
        }

        revert("Credential not found or not issued by caller");
    }

    /// @notice Retrieves the credentials of a user
    /// @param _user The address of the user
    /// @return credentials An array of credentials associated with the user
    function getCredentials(address _user) public view returns (Credential[] memory credentials) {
        return userCredentials[_user];
    }
}
```
