"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfa-ai.pages.dev
Prompt: Create a smart contract function that logs the migration of $NFAI V1 to $NFAI V2 tokens and emits an event with the sender's address and token amount.
Generated: DETERMINISTIC_2ebb097f68e56a00
Batch ID: 20250612_153420
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
 * @title TokenMigrationContract
 * @dev This contract handles the migration of $NFAI V1 tokens to $NFAI V2 tokens.
 */
contract TokenMigrationContract {
    // Event to log the migration of tokens
    event TokenMigrated(address indexed sender, uint256 amount);

    // Mapping to track users who have migrated their tokens
    mapping(address => bool) public hasMigrated;

    // Function to log migration of tokens
    /**
     * @dev Migrates $NFAI V1 tokens to $NFAI V2 tokens
     * Emits a TokenMigrated event upon successful migration
     * @param amount The amount of tokens to migrate
     */
    function migrateTokens(uint256 amount) external {
        // Validate input parameters
        require(amount > 0, "Amount must be greater than zero");
        require(!hasMigrated[msg.sender], "Sender has already migrated tokens");

        // Mark sender as migrated
        hasMigrated[msg.sender] = true;

        // Emit the migration event
        emit TokenMigrated(msg.sender, amount);
    }
}
```
