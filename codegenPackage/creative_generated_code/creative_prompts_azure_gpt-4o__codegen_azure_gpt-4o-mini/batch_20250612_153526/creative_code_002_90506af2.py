"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmoovtoken.pages.dev
Prompt: Provide Solidity code for a smart contract that facilitates the migration of MOOV tokens, ensuring the old tokens are invalidated and the new tokens are distributed correctly.
Generated: DETERMINISTIC_90506af2d18f612f
Batch ID: 20250612_153526
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

// Interface for the old MOOV token contract
interface IOldMOOVToken {
    function balanceOf(address owner) external view returns (uint256);
    function burn(uint256 amount) external; // Burn old tokens
}

// Interface for the new MOOV token contract
interface INewMOOVToken {
    function mint(address to, uint256 amount) external; // Mint new tokens
}

// Smart contract for migrating MOOV tokens
contract MOOVTokenMigration {
    IOldMOOVToken public oldToken; // Instance of the old token contract
    INewMOOVToken public newToken; // Instance of the new token contract

    // Mapping to track migrated addresses
    mapping(address => bool) public hasMigrated;

    // Event for successful migration
    event TokensMigrated(address indexed user, uint256 oldAmount, uint256 newAmount);

    // Constructor to set old and new token addresses
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        require(_oldTokenAddress != address(0), "Invalid old token address");
        require(_newTokenAddress != address(0), "Invalid new token address");
        oldToken = IOldMOOVToken(_oldTokenAddress);
        newToken = INewMOOVToken(_newTokenAddress);
    }

    // Function to migrate old tokens to new tokens
    function migrateTokens() external {
        // Ensure the user has not already migrated
        require(!hasMigrated[msg.sender], "Tokens already migrated");

        // Get the user's balance of old tokens
        uint256 oldAmount = oldToken.balanceOf(msg.sender);
        require(oldAmount > 0, "No tokens to migrate");

        // Burn the old tokens
        oldToken.burn(oldAmount);

        // Mint new tokens for the user
        newToken.mint(msg.sender, oldAmount);

        // Mark the user as migrated
        hasMigrated[msg.sender] = true;

        // Emit migration event
        emit TokensMigrated(msg.sender, oldAmount, oldAmount);
    }
}
```
