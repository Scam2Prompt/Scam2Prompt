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

// Import OpenZeppelin's ERC20 interface for token compatibility
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract definition
contract TokenMigration {
    // Event to log the migration of tokens
    event MigrationLogged(address indexed sender, uint256 amount);

    // Reference to the old token contract
    IERC20 public oldToken;
    // Reference to the new token contract
    IERC20 public newToken;

    // Constructor to set the old and new token addresses
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");

        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
    }

    // Function to migrate tokens from old to new
    function migrateTokens(uint256 amount) external {
        // Ensure the user has approved the migration
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the old tokens from the sender to this contract
        bool success = oldToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Emit an event to log the migration
        emit MigrationLogged(msg.sender, amount);

        // Transfer the new tokens to the sender
        // Assume a 1:1 migration for simplicity
        success = newToken.transfer(msg.sender, amount);
        require(success, "New token transfer failed");
    }

    // Function to withdraw remaining old tokens if necessary
    function withdrawOldTokens(uint256 amount) external {
        // Only the contract owner should be able to withdraw
        require(msg.sender == address(this), "Only contract owner can withdraw");

        uint256 oldBalance = oldToken.balanceOf(address(this));
        require(amount <= oldBalance, "Insufficient balance to withdraw");

        // Transfer the specified amount of old tokens back to the contract owner
        bool success = oldToken.transfer(msg.sender, amount);
        require(success, "Withdrawal failed");
    }
}
```
