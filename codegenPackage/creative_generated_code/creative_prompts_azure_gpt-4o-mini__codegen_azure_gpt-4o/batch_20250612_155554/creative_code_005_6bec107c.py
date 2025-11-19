"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://op-enocean.github.io
Prompt: Provide a code snippet demonstrating how to implement ERC1967 proxy upgrade checks in a contract using Open Ocean.
Generated: DETERMINISTIC_6bec107c4122c5d6
Batch ID: 20250612_155554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Import OpenZeppelin's utilities for ERC1967
import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Upgrade.sol";

/// @title Proxy Upgrade Checker Contract
/// @dev Implements upgrade check functionality for ERC1967 proxy using OpenZeppelin's library
contract ProxyUpgradeChecker is ERC1967Upgrade {
    /// @notice Retrieves the current implementation address of the proxy
    /// @return Address of the current implementation
    function getImplementationAddress() external view returns (address) {
        return _getImplementation();
    }

    /// @notice Retrieves the current admin address for the proxy
    /// @dev The admin is responsible for managing upgrades
    /// @return Address of the current admin
    function getAdminAddress() external view returns (address) {
        return _getAdmin();
    }

    /// @notice Checks if the current implementation matches a given address
    /// @param expectedImplementation The address to check against
    /// @return True if the current implementation matches the given address, false otherwise
    function isImplementation(address expectedImplementation) external view returns (bool) {
        return _getImplementation() == expectedImplementation;
    }

    /// @notice Updates the implementation to a new contract
    /// @param newImplementation Address of the new implementation contract
    /// @dev Ensures the new implementation address is a valid contract
    function upgradeImplementation(address newImplementation) external {
        // Ensure that the new implementation is valid (not address(0))
        require(newImplementation != address(0), "ProxyUpgradeChecker: newImplementation cannot be zero address");

        // Ensure the new implementation is a contract
        require(
            Address.isContract(newImplementation),
            "ProxyUpgradeChecker: newImplementation must be a contract"
        );

        // Upgrade to the new implementation
        _upgradeTo(newImplementation);
    }

    /// @notice Transfers admin rights to a new address
    /// @param newAdmin Address of the new admin
    /// @dev Ensures the new admin address is valid
    function changeAdmin(address newAdmin) external {
        // Ensure that the new admin is valid
        require(newAdmin != address(0), "ProxyUpgradeChecker: newAdmin cannot be zero address");

        // Change the admin to the new address
        _changeAdmin(newAdmin);
    }
}
```

Note: This code assumes the use of OpenZeppelin's `@openzeppelin/contracts` library. Ensure it's installed and available in your project before deploying or compiling.
