"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoo.tech
Prompt: Write a smart contract snippet that interacts with a connected wallet to verify access permissions, inspired by Cryptoo.tech.
Generated: DETERMINISTIC_53ccab0e6c30dd08
Batch ID: 20250612_154131
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title AccessControl
 * @dev Smart contract to manage access permissions for connected wallets.
 */
contract AccessControl is Ownable {
    using ECDSA for bytes32;

    // Mapping to track addresses with access permissions
    mapping(address => bool) private _hasAccess;

    /**
     * @dev Event emitted when access is granted or revoked.
     */
    event AccessUpdated(address indexed user, bool hasAccess);

    /**
     * @dev Grants access to the specified address.
     * @param user The address to grant access to.
     */
    function grantAccess(address user) external onlyOwner {
        require(user != address(0), "AccessControl: invalid address");
        _hasAccess[user] = true;
        emit AccessUpdated(user, true);
    }

    /**
     * @dev Revokes access from the specified address.
     * @param user The address to revoke access from.
     */
    function revokeAccess(address user) external onlyOwner {
        require(user != address(0), "AccessControl: invalid address");
        _hasAccess[user] = false;
        emit AccessUpdated(user, false);
    }

    /**
     * @dev Checks if an address has access.
     * @param user The address to check.
     * @return bool indicating access status.
     */
    function hasAccess(address user) external view returns (bool) {
        return _hasAccess[user];
    }

    /**
     * @dev Function to verify access before executing a certain action.
     * @param user The address to check access for.
     */
    modifier onlyWithAccess(address user) {
        require(_hasAccess[user], "AccessControl: access denied");
        _;
    }

    /**
     * @dev Example function that requires access permission.
     * @param data Additional data for processing.
     */
    function executeAction(bytes memory data) external onlyWithAccess(msg.sender) {
        // Implement action logic here
    }
}
```
