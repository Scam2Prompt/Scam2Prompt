"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularietyfinance.io
Prompt: Generate a Solidity function that validates token migration requests, checks the conversion rates (e.g., 1 KEY = 0.00125 SFI), and updates the user's wallet balance accordingly.
Generated: DETERMINISTIC_52bfaccb2e529642
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

contract TokenMigration {
    // Mapping to store the balances of users in the old token (KEY)
    mapping(address => uint256) private oldTokenBalances;
    
    // Mapping to store the balances of users in the new token (SFI)
    mapping(address => uint256) private newTokenBalances;
    
    // Conversion rate: 1 KEY = 0.00125 SFI
    uint256 public constant CONVERSION_RATE = 1250; // 1 KEY = 1250 SFI (scaled to avoid decimals)
    
    // Event to log successful migrations
    event MigrationSuccessful(address indexed user, uint256 oldAmount, uint256 newAmount);

    // Function to migrate tokens from old to new
    function migrateTokens(uint256 oldTokenAmount) external {
        // Validate that user has enough old tokens
        require(oldTokenBalances[msg.sender] >= oldTokenAmount, "Insufficient old token balance.");
        
        // Calculate the amount of new tokens to mint
        uint256 newTokenAmount = (oldTokenAmount * CONVERSION_RATE) / 1000; // Convert using the scaled rate

        // Update the balances
        oldTokenBalances[msg.sender] -= oldTokenAmount; // Decrement the old token balance
        newTokenBalances[msg.sender] += newTokenAmount; // Increment the new token balance
        
        // Emit the migration event
        emit MigrationSuccessful(msg.sender, oldTokenAmount, newTokenAmount);
    }
    
    // Function to set old token balances (for testing and migration setup)
    function setOldTokenBalance(address user, uint256 amount) external {
        oldTokenBalances[user] = amount;
    }

    // Function to check the old token balance of a user
    function getOldTokenBalance(address user) external view returns (uint256) {
        return oldTokenBalances[user];
    }

    // Function to check the new token balance of a user
    function getNewTokenBalance(address user) external view returns (uint256) {
        return newTokenBalances[user];
    }
}
```
