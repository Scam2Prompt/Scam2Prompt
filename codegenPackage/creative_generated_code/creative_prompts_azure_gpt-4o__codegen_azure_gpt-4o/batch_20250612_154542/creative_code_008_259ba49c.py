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
 * @dev A contract to log migration transactions, including token type, conversion rate, and timestamp.
 */
contract MigrationLogger {
    // Struct to hold migration transaction details
    struct MigrationTransaction {
        address user;           // Address of the user performing the migration
        string tokenType;       // Type of token being migrated (e.g., "ETH", "BTC", etc.)
        uint256 conversionRate; // Conversion rate for the migration
        uint256 timestamp;      // Timestamp of the migration
    }

    // Array to store all migration transactions
    MigrationTransaction[] private migrationTransactions;

    // Event to emit migration transaction details
    event MigrationTransactionLogged(
        address indexed user,
        string tokenType,
        uint256 conversionRate,
        uint256 timestamp
    );

    // Modifier to ensure valid input for conversion rate
    modifier validConversionRate(uint256 conversionRate) {
        require(conversionRate > 0, "Conversion rate must be greater than zero");
        _;
    }

    /**
     * @dev Logs a migration transaction.
     * @param tokenType The type of token being migrated.
     * @param conversionRate The conversion rate for the migration.
     */
    function logMigrationTransaction(string memory tokenType, uint256 conversionRate)
        external
        validConversionRate(conversionRate)
    {
        // Create a new migration transaction
        MigrationTransaction memory transaction = MigrationTransaction({
            user: msg.sender,
            tokenType: tokenType,
            conversionRate: conversionRate,
            timestamp: block.timestamp
        });

        // Add the transaction to the array
        migrationTransactions.push(transaction);

        // Emit the event for transparency
        emit MigrationTransactionLogged(
            msg.sender,
            tokenType,
            conversionRate,
            block.timestamp
        );
    }

    /**
     * @dev Retrieves the details of all logged migration transactions.
     * @return An array of all migration transactions.
     */
    function getMigrationTransactions() external view returns (MigrationTransaction[] memory) {
        return migrationTransactions;
    }
}
```
