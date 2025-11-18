"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdefi-feg.pages.dev
Prompt: Write a function in Solidity to verify the migration status of a user's FEGtoken balance from V2 to V3 on the SmartDeFi platform.
Generated: DETERMINISTIC_e6262b5dcc5bafe7
Batch ID: 20250612_145831
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

/**
 * @title FEGTokenMigration
 * @dev Smart contract to verify migration status of a user's FEGToken balance
 * from V2 to V3 on the SmartDeFi platform.
 */
contract FEGTokenMigration {
    // Address of the SmartDeFi V3 contract
    address public immutable v3Contract;

    // Mapping to store migration status of users
    mapping(address => bool) private migrated;

    // Event emitted when migration status is checked
    event MigrationStatusChecked(address indexed user, bool migrated);

    /**
     * @dev Constructor to initialize the V3 contract address.
     * @param _v3Contract Address of the SmartDeFi V3 contract.
     */
    constructor(address _v3Contract) {
        require(_v3Contract != address(0), "V3 contract address cannot be zero");
        v3Contract = _v3Contract;
    }

    /**
     * @dev Function to verify whether a user's FEGToken balance has been migrated from V2 to V3.
     * @param user Address of the user to check migration status.
     * @return True if migrated, false otherwise.
     */
    function isMigrated(address user) external view returns (bool) {
        require(user != address(0), "User address cannot be zero");
        
        // Emit an event for tracking migration checks
        emit MigrationStatusChecked(user, migrated[user]);
        
        // Return the migration status from the mapping
        return migrated[user];
    }

    /**
     * @dev Admin function to update migration status for a user.
     * @param user Address of the user.
     * @param status Migration status (true if migrated, false otherwise).
     */
    function updateMigrationStatus(address user, bool status) external {
        require(msg.sender == v3Contract, "Only V3 contract can update migration status");
        require(user != address(0), "User address cannot be zero");
        
        // Update the migration status in the mapping
        migrated[user] = status;
    }
}
```
