"""
Generated Code Metadata:
========================
Original URL: https://valhalladao.app
Prompt: Write a smart contract snippet that verifies wallet connection and grants access to specific features, similar to the access requirements mentioned on the ValhallaDAO app.
Generated: DETERMINISTIC_2f6b59307da89d87
Batch ID: 20250612_154115
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract AccessControl is Ownable {
    // Mapping to track which addresses have access to specific features
    mapping(address => bool) private _hasAccess;

    // Event emitted when access is granted or revoked
    event AccessUpdated(address indexed user, bool hasAccess);

    // Modifier to check if the caller has access
    modifier onlyWithAccess() {
        require(_hasAccess[msg.sender], "AccessControl: Caller does not have access");
        _;
    }

    // Function to grant access to a specific address
    function grantAccess(address user) external onlyOwner {
        require(user != address(0), "AccessControl: Invalid address");
        _hasAccess[user] = true;
        emit AccessUpdated(user, true);
    }

    // Function to revoke access from a specific address
    function revokeAccess(address user) external onlyOwner {
        require(user != address(0), "AccessControl: Invalid address");
        _hasAccess[user] = false;
        emit AccessUpdated(user, false);
    }

    // Function to check if an address has access
    function hasAccess(address user) external view returns (bool) {
        return _hasAccess[user];
    }

    // Example function that requires access
    function restrictedFeature() external onlyWithAccess {
        // Logic for the restricted feature goes here
    }
}
```
