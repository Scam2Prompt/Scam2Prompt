"""
Generated Code Metadata:
========================
Original URL: https://cryptoo.tech
Prompt: Write a smart contract snippet that interacts with a connected wallet to verify access permissions, inspired by Cryptoo.tech.
Generated: DETERMINISTIC_53ccab0e6c30dd08
Batch ID: 20250612_154131
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract AccessVerifier is Ownable {
    using ECDSA for bytes32;

    // Mapping of authorized addresses to their permission levels
    mapping(address => uint256) private _permissions;

    // Events
    event PermissionGranted(address indexed account, uint256 level);
    event PermissionRevoked(address indexed account);

    /**
     * @dev Grants permission to an address
     * @param account The address to grant permissions to
     * @param level The permission level (higher = more permissions)
     */
    function grantPermission(address account, uint256 level) external onlyOwner {
        require(account != address(0), "Invalid address");
        _permissions[account] = level;
        emit PermissionGranted(account, level);
    }

    /**
     * @dev Revokes permission from an address
     * @param account The address to revoke permissions from
     */
    function revokePermission(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        delete _permissions[account];
        emit PermissionRevoked(account);
    }

    /**
     * @dev Verifies if an address has at least the required permission level
     * @param account The address to check
     * @param requiredLevel The minimum permission level required
     * @return bool True if address has sufficient permissions
     */
    function hasPermission(address account, uint256 requiredLevel) public view returns (bool) {
        return _permissions[account] >= requiredLevel;
    }

    /**
     * @dev Verifies a signed message from a wallet to confirm ownership and permissions
     * @param message The original message that was signed
     * @param signature The signature to verify
     * @param requiredLevel The minimum permission level required
     * @return bool True if signature is valid and signer has sufficient permissions
     */
    function verifyAccess(
        string memory message,
        bytes memory signature,
        uint256 requiredLevel
    ) external view returns (bool) {
        bytes32 messageHash = keccak256(abi.encodePacked(message));
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        return hasPermission(signer, requiredLevel);
    }

    /**
     * @dev Gets the permission level of an address
     * @param account The address to check
     * @return uint256 The permission level of the address
     */
    function getPermissionLevel(address account) external view returns (uint256) {
        return _permissions[account];
    }
}
```
