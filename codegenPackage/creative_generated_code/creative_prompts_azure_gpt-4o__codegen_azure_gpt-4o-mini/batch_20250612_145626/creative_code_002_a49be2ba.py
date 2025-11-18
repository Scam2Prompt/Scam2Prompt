"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magiccraft-migrate.pages.dev
Prompt: Create a smart contract for MagicCraft that enables token migration for $MCRT, following the guidelines outlined in the MagicCraft whitepaper.
Generated: DETERMINISTIC_a49be2baf9942769
Batch ID: 20250612_145626
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

/// @title MagicCraft Token Migration Contract
/// @author MagicCraft Team
/// @notice This contract enables the migration of $MCRT tokens from the old contract to the new contract.
contract MagicCraftTokenMigration {
    // Address of the old $MCRT token contract
    address public oldTokenAddress;

    // Mapping to track migrated addresses
    mapping(address => bool) public hasMigrated;

    // Event emitted after a successful migration
    event TokensMigrated(address indexed user, uint256 amount);

    // Error definitions
    error AlreadyMigrated();
    error InvalidOldTokenAddress();
    error TransferFailed();
    
    // Constructor to set the old token contract address
    constructor(address _oldTokenAddress) {
        if (_oldTokenAddress == address(0)) {
            revert InvalidOldTokenAddress();
        }
        oldTokenAddress = _oldTokenAddress;
    }

    /// @notice Migrate tokens from the old contract to this contract
    /// @param amount The amount of tokens to migrate
    function migrateTokens(uint256 amount) external {
        if (hasMigrated[msg.sender]) {
            revert AlreadyMigrated();
        }

        // Interact with the old token contract to transfer tokens
        IERC20 oldToken = IERC20(oldTokenAddress);
        bool success = oldToken.transferFrom(msg.sender, address(this), amount);
        if (!success) {
            revert TransferFailed();
        }

        // Mark the user as having migrated
        hasMigrated[msg.sender] = true;

        // Emit event for successful migration
        emit TokensMigrated(msg.sender, amount);
    }
}

/// @title ERC20 Interface
/// @notice Minimal interface for ERC20 token interactions
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
