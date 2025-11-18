"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://valhalladao.app
Prompt: Write a smart contract snippet that verifies wallet connection and grants access to specific features, similar to the access requirements mentioned on the ValhallaDAO app.
Generated: DETERMINISTIC_2f6b59307da89d87
Batch ID: 20250612_154115
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
import "@openzeppelin/contracts/utils/Address.sol";

contract AccessControl is Ownable {
    using Address for address;

    // Mapping to track addresses with access rights
    mapping(address => bool) private _accessGranted;

    // Event emitted when access is granted
    event AccessGranted(address indexed account);

    // Event emitted when access is revoked
    event AccessRevoked(address indexed account);

    /// @dev Modifier to check if the caller has access rights
    modifier onlyWithAccess() {
        require(hasAccess(msg.sender), "AccessControl: caller does not have access");
        _;
    }

    /// @dev Grants access to a specific wallet address
    /// @param account The wallet address to grant access
    function grantAccess(address account) external onlyOwner {
        require(account != address(0), "AccessControl: Invalid address");
        require(!_accessGranted[account], "AccessControl: Access already granted");

        _accessGranted[account] = true;
        emit AccessGranted(account);
    }

    /// @dev Revokes access from a specific wallet address
    /// @param account The wallet address to revoke access
    function revokeAccess(address account) external onlyOwner {
        require(account != address(0), "AccessControl: Invalid address");
        require(_accessGranted[account], "AccessControl: No access to revoke");

        _accessGranted[account] = false;
        emit AccessRevoked(account);
    }

    /// @dev Checks if a wallet address has access
    /// @param account The wallet address to check
    /// @return bool True if the account has access, false otherwise
    function hasAccess(address account) public view returns (bool) {
        return _accessGranted[account];
    }

    /// @dev Sample function that requires access
    function restrictedFunction() external onlyWithAccess {
        // Function logic that requires access goes here
    }
}
```
