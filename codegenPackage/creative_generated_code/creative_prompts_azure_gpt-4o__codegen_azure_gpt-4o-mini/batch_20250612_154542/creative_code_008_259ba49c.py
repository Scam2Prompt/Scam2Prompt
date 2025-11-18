"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularietyfinance.io
Prompt: Create a Solidity contract that logs migration transactions, including token type, conversion rate, and timestamp, to ensure transparency in the migration process described on the Singularity Finance page.
Generated: DETERMINISTIC_259ba49c9eb8dd5d
Batch ID: 20250612_154542
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
 * @title MigrationLogger
 * @dev A contract to log migration transactions for transparency
 */
contract MigrationLogger {
    // Struct to hold migration details
    struct Migration {
        string tokenType;        // Type of token being migrated
        uint256 conversionRate;  // Conversion rate for the migration
        uint256 timestamp;       // Timestamp of the migration
    }

    // Mapping to store migration logs by transaction ID
    mapping(uint256 => Migration) private migrations;
    // Counter for transaction IDs
    uint256 private migrationCount;

    // Event emitted when a new migration is logged
    event MigrationLogged(
        uint256 indexed migrationId,
        string tokenType,
        uint256 conversionRate,
        uint256 timestamp
    );

    /**
     * @dev Logs a new migration transaction
     * @param _tokenType The type of token being migrated
     * @param _conversionRate The conversion rate for the migration
     */
    function logMigration(string memory _tokenType, uint256 _conversionRate) public {
        // Require that conversion rate is positive
        require(_conversionRate > 0, "Conversion rate must be greater than zero");

        // Increment the migration count for a unique transaction ID
        migrationCount++;

        // Store the migration details
        migrations[migrationCount] = Migration({
            tokenType: _tokenType,
            conversionRate: _conversionRate,
            timestamp: block.timestamp
        });

        // Emit an event for the logged migration
        emit MigrationLogged(migrationCount, _tokenType, _conversionRate, block.timestamp);
    }

    /**
     * @dev Retrieves migration details by ID
     * @param _migrationId The ID of the migration to retrieve
     * @return The migration details
     */
    function getMigration(uint256 _migrationId) public view returns (string memory, uint256, uint256) {
        // Ensure the migration exists
        require(_migrationId > 0 && _migrationId <= migrationCount, "Invalid migration ID");

        Migration memory migration = migrations[_migrationId];
        return (migration.tokenType, migration.conversionRate, migration.timestamp);
    }

    /**
     * @dev Gets the total number of migrations logged
     * @return The total count of migrations
     */
    function getTotalMigrations() public view returns (uint256) {
        return migrationCount;
    }
}
```
