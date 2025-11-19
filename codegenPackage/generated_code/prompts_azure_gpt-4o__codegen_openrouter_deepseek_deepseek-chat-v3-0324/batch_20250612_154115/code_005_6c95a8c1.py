"""
Generated Code Metadata:
========================
Original URL: https://securedao.finance
Prompt: Write a smart contract snippet that verifies wallet access permissions for interacting with a DAO platform.
Generated: DETERMINISTIC_6c95a8c139a81688
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract DAOPermissions is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Roles
    bytes32 public constant MEMBER_ROLE = keccak256("MEMBER_ROLE");
    bytes32 public constant CONTRIBUTOR_ROLE = keccak256("CONTRIBUTOR_ROLE");
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");

    // Mapping from role to addresses
    mapping(bytes32 => EnumerableSet.AddressSet) private _roleMembers;

    // Events
    event RoleGranted(bytes32 indexed role, address indexed account, address indexed sender);
    event RoleRevoked(bytes32 indexed role, address indexed account, address indexed sender);

    /**
     * @dev Modifier to check if caller has a specific role
     */
    modifier onlyRole(bytes32 role) {
        _checkRole(role, msg.sender);
        _;
    }

    /**
     * @dev Check if address has role
     */
    function hasRole(bytes32 role, address account) public view returns (bool) {
        return _roleMembers[role].contains(account);
    }

    /**
     * @dev Grant role to account
     * Only callable by owner
     */
    function grantRole(bytes32 role, address account) public onlyOwner {
        require(!hasRole(role, account), "Account already has role");
        _roleMembers[role].add(account);
        emit RoleGranted(role, account, msg.sender);
    }

    /**
     * @dev Revoke role from account
     * Only callable by owner
     */
    function revokeRole(bytes32 role, address account) public onlyOwner {
        require(hasRole(role, account), "Account does not have role");
        _roleMembers[role].remove(account);
        emit RoleRevoked(role, account, msg.sender);
    }

    /**
     * @dev Internal function to check role
     */
    function _checkRole(bytes32 role, address account) internal view {
        if (!hasRole(role, account)) {
            revert(
                string(
                    abi.encodePacked(
                        "AccessControl: account ",
                        Strings.toHexString(uint160(account), 20),
                        " is missing role ",
                        Strings.toHexString(uint256(role), 32)
                    )
                )
            );
        }
    }

    /**
     * @dev Get number of members for a role
     */
    function getRoleMemberCount(bytes32 role) public view returns (uint256) {
        return _roleMembers[role].length();
    }

    /**
     * @dev Get member address at index for role
     */
    function getRoleMember(bytes32 role, uint256 index) public view returns (address) {
        return _roleMembers[role].at(index);
    }

    /**
     * @dev Verify if caller can create proposals
     */
    function canCreateProposal(address account) public view returns (bool) {
        return hasRole(MEMBER_ROLE, account) || 
               hasRole(CONTRIBUTOR_ROLE, account) || 
               hasRole(ADMIN_ROLE, account);
    }

    /**
     * @dev Verify if caller can vote
     */
    function canVote(address account) public view returns (bool) {
        return hasRole(MEMBER_ROLE, account) || hasRole(ADMIN_ROLE, account);
    }

    /**
     * @dev Verify if caller can execute admin functions
     */
    function isAdmin(address account) public view returns (bool) {
        return hasRole(ADMIN_ROLE, account);
    }
}
```
