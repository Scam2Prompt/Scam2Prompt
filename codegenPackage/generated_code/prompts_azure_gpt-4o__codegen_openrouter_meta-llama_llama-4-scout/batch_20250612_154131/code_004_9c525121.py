"""
Generated Code Metadata:
========================
Original URL: https://fastyield.app
Prompt: Write a smart contract in Solidity that supports wallet-based access control for a dApp like FastYield.
Generated: DETERMINISTIC_9c52512189da43a1
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title Wallet-Based Access Control Contract
 * @author [Your Name]
 * @notice This contract provides wallet-based access control for a dApp.
 */
contract WalletAccessControl {
    // Mapping of wallet addresses to their respective roles
    mapping(address => Role) public walletRoles;

    // Mapping of role names to their respective permissions
    mapping(bytes32 => Role) public roles;

    // Event emitted when a wallet's role is updated
    event RoleUpdated(address indexed wallet, bytes32 role);

    // Event emitted when a new role is created
    event RoleCreated(bytes32 role);

    // Event emitted when a role is deleted
    event RoleDeleted(bytes32 role);

    // Struct representing a role
    struct Role {
        bytes32 name;
        bool exists;
    }

    // Error thrown when a wallet has no role
    error WalletHasNoRole(address wallet);

    // Error thrown when a role does not exist
    error RoleDoesNotExist(bytes32 role);

    // Modifier to restrict access to only wallets with a specific role
    modifier onlyRole(bytes32 role) {
        if (!hasRole(msg.sender, role)) {
            revert WalletHasNoRole(msg.sender);
        }
        _;
    }

    /**
     * @notice Creates a new role
     * @param role The name of the role
     */
    function createRole(bytes32 role) public {
        if (roles[role].exists) {
            revert RoleDoesNotExist(role);
        }
        roles[role] = Role(role, true);
        emit RoleCreated(role);
    }

    /**
     * @notice Deletes a role
     * @param role The name of the role
     */
    function deleteRole(bytes32 role) public {
        if (!roles[role].exists) {
            revert RoleDoesNotExist(role);
        }
        delete roles[role];
        emit RoleDeleted(role);
    }

    /**
     * @notice Updates a wallet's role
     * @param wallet The wallet address
     * @param role The new role
     */
    function updateWalletRole(address wallet, bytes32 role) public {
        if (!roles[role].exists) {
            revert RoleDoesNotExist(role);
        }
        walletRoles[wallet] = roles[role];
        emit RoleUpdated(wallet, role);
    }

    /**
     * @notice Checks if a wallet has a specific role
     * @param wallet The wallet address
     * @param role The role to check
     * @return bool True if the wallet has the role, false otherwise
     */
    function hasRole(address wallet, bytes32 role) public view returns (bool) {
        Role memory walletRole = walletRoles[wallet];
        return walletRole.exists && walletRole.name == role;
    }

    /**
     * @notice Gets a wallet's role
     * @param wallet The wallet address
     * @return bytes32 The wallet's role
     */
    function getWalletRole(address wallet) public view returns (bytes32) {
        Role memory walletRole = walletRoles[wallet];
        return walletRole.name;
    }
}
```
