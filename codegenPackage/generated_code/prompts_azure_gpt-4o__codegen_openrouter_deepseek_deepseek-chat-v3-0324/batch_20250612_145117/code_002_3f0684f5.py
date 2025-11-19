"""
Generated Code Metadata:
========================
Original URL: https://olivedao.finance
Prompt: Generate a smart contract that checks access requirements for a DeFi app, inspired by the OliveDAO Finance platform.
Generated: DETERMINISTIC_3f0684f591d94a16
Batch ID: 20250612_145117
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

/**
 * @title AccessControl
 * @dev Smart contract for managing access requirements in a DeFi application
 */
contract AccessControl is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Access levels
    enum AccessLevel {
        NONE,
        BASIC,
        PREMIUM,
        ADMIN
    }

    // Minimum token balance requirements for each access level
    mapping(AccessLevel => uint256) public minTokenBalance;
    
    // Token contract address
    address public tokenAddress;

    // Mapping of user addresses to their access levels
    mapping(address => AccessLevel) private _userAccess;

    // Set of premium users
    EnumerableSet.AddressSet private _premiumUsers;

    // Set of admin users
    EnumerableSet.AddressSet private _adminUsers;

    // Events
    event AccessGranted(address indexed user, AccessLevel level);
    event AccessRevoked(address indexed user, AccessLevel level);
    event TokenRequirementsUpdated(AccessLevel level, uint256 newBalance);

    /**
     * @dev Constructor sets initial parameters
     * @param _tokenAddress Address of the ERC20 token used for access control
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        
        // Set default minimum token balances
        minTokenBalance[AccessLevel.BASIC] = 100 * 10**18;  // 100 tokens
        minTokenBalance[AccessLevel.PREMIUM] = 1000 * 10**18; // 1000 tokens
        minTokenBalance[AccessLevel.ADMIN] = 0; // Admins are manually set
    }

    /**
     * @dev Checks if an address has at least the required access level
     * @param user Address to check
     * @param requiredLevel Minimum required access level
     * @return bool True if user has required access
     */
    function hasAccess(address user, AccessLevel requiredLevel) public view returns (bool) {
        AccessLevel userLevel = _userAccess[user];
        return uint256(userLevel) >= uint256(requiredLevel);
    }

    /**
     * @dev Updates the token balance requirement for an access level
     * @param level Access level to update
     * @param newBalance New minimum token balance requirement
     */
    function setTokenRequirement(AccessLevel level, uint256 newBalance) external onlyOwner {
        require(level != AccessLevel.ADMIN, "Cannot set requirements for ADMIN");
        minTokenBalance[level] = newBalance;
        emit TokenRequirementsUpdated(level, newBalance);
    }

    /**
     * @dev Grants admin access to an address
     * @param user Address to grant admin access
     */
    function grantAdmin(address user) external onlyOwner {
        require(user != address(0), "Invalid address");
        _userAccess[user] = AccessLevel.ADMIN;
        EnumerableSet.add(_adminUsers, user);
        emit AccessGranted(user, AccessLevel.ADMIN);
    }

    /**
     * @dev Revokes admin access from an address
     * @param user Address to revoke admin access
     */
    function revokeAdmin(address user) external onlyOwner {
        require(EnumerableSet.contains(_adminUsers, user), "Not an admin");
        _userAccess[user] = AccessLevel.NONE;
        EnumerableSet.remove(_adminUsers, user);
        emit AccessRevoked(user, AccessLevel.ADMIN);
    }

    /**
     * @dev Checks and updates user's access level based on token balance
     * @param user Address to check and update
     */
    function updateAccess(address user) external {
        require(user != address(0), "Invalid address");
        
        // Skip if user is admin (admins don't need token balance)
        if (EnumerableSet.contains(_adminUsers, user)) {
            return;
        }

        uint256 balance = IERC20(tokenAddress).balanceOf(user);
        AccessLevel newLevel = AccessLevel.NONE;

        if (balance >= minTokenBalance[AccessLevel.PREMIUM]) {
            newLevel = AccessLevel.PREMIUM;
            EnumerableSet.add(_premiumUsers, user);
        } else if (balance >= minTokenBalance[AccessLevel.BASIC]) {
            newLevel = AccessLevel.BASIC;
            EnumerableSet.remove(_premiumUsers, user);
        } else {
            EnumerableSet.remove(_premiumUsers, user);
        }

        if (_userAccess[user] != newLevel) {
            _userAccess[user] = newLevel;
            emit AccessGranted(user, newLevel);
        }
    }

    /**
     * @dev Returns the access level of a user
     * @param user Address to check
     * @return AccessLevel Current access level of the user
     */
    function getUserAccessLevel(address user) external view returns (AccessLevel) {
        return _userAccess[user];
    }

    /**
     * @dev Returns list of premium users
     * @return address[] Array of premium user addresses
     */
    function getPremiumUsers() external view returns (address[] memory) {
        return EnumerableSet.values(_premiumUsers);
    }

    /**
     * @dev Returns list of admin users
     * @return address[] Array of admin user addresses
     */
    function getAdminUsers() external view returns (address[] memory) {
        return EnumerableSet.values(_adminUsers);
    }
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
