"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snowyowl.finance
Prompt: Generate a smart contract in Solidity that could be used for managing user access requirements in a platform like Snowy Owl Finance.
Generated: DETERMINISTIC_0292099600ea27c9
Batch ID: 20250612_145117
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

contract AccessControl {

    // Event emitted when a user is granted access
    event AccessGranted(address indexed user, string role);
    
    // Event emitted when a user is revoked access
    event AccessRevoked(address indexed user, string role);

    // Mapping to store user roles
    mapping(address => string) private userRoles;

    // Modifier to check if the caller has a specific role
    modifier onlyRole(string memory role) {
        require(keccak256(abi.encodePacked(userRoles[msg.sender])) == keccak256(abi.encodePacked(role)), "AccessControl: Caller does not have the required role");
        _;
    }

    // Function to grant a role to a user
    function grantAccess(address user, string memory role) public onlyRole("admin") {
        require(user != address(0), "AccessControl: Invalid user address");
        require(bytes(role).length > 0, "AccessControl: Role cannot be empty");
        
        userRoles[user] = role;
        emit AccessGranted(user, role);
    }

    // Function to revoke a role from a user
    function revokeAccess(address user) public onlyRole("admin") {
        require(user != address(0), "AccessControl: Invalid user address");
        
        string memory role = userRoles[user];
        require(bytes(role).length > 0, "AccessControl: User role does not exist");
        
        delete userRoles[user];
        emit AccessRevoked(user, role);
    }

    // Function to check the role of a user
    function getUserRole(address user) public view returns (string memory) {
        return userRoles[user];
    }

    // Function to check if a user has a specific role
    function hasRole(address user, string memory role) public view returns (bool) {
        return keccak256(abi.encodePacked(userRoles[user])) == keccak256(abi.encodePacked(role));
    }
}
```
