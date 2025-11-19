"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftmultiauths.pages.dev
Prompt: Generate a function to facilitate the migration of tokens to a new contract on a decentralized platform.
Generated: DETERMINISTIC_12acca53bf1d79e8
Batch ID: 20250612_164100
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenMigration
 * @dev This contract facilitates the migration of tokens from an old contract to a new one.
 * Only the owner can initiate the migration process.
 */
contract TokenMigration is Ownable {
    // Old token contract address
    IERC20 public oldToken;
    // New token contract address
    IERC20 public newToken;

    // Mapping to keep track of migrated addresses
    mapping(address => bool) public hasMigrated;

    /**
     * @dev Constructor to set the old and new token contracts.
     * @param _oldToken Address of the old token contract
     * @param _newToken Address of the new token contract
     */
    constructor(IERC20 _oldToken, IERC20 _newToken) {
        oldToken = _oldToken;
        newToken = _newToken;
    }

    /**
     * @dev Migrate tokens from the old contract to the new contract.
     * @param amount Amount of tokens to migrate
     */
    function migrateTokens(uint256 amount) external {
        // Check if the sender has already migrated
        require(!hasMigrated[msg.sender], "Tokens have already been migrated");

        // Check the balance of the sender in the old token contract
        uint256 oldBalance = oldToken.balanceOf(msg.sender);
        require(oldBalance >= amount, "Insufficient balance in old token contract");

        // Transfer tokens from the sender to this contract
        // The sender must allow this contract to spend their tokens
        bool success = oldToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Transfer tokens to the new contract
        success = newToken.transfer(msg.sender, amount);
        require(success, "Token migration to new contract failed");

        // Mark the sender as having migrated
        hasMigrated[msg.sender] = true;
    }

    /**
     * @dev Allow the owner to withdraw any remaining old tokens from the contract.
     * @param amount Amount of tokens to withdraw
     */
    function withdrawOldTokens(uint256 amount) external onlyOwner {
        uint256 contractBalance = oldToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient balance in contract");

        bool success = oldToken.transfer(msg.sender, amount);
        require(success, "Withdrawal of old tokens failed");
    }

    /**
     * @dev Allow the owner to withdraw any remaining new tokens from the contract.
     * @param amount Amount of tokens to withdraw
     */
    function withdrawNewTokens(uint256 amount) external onlyOwner {
        uint256 contractBalance = newToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient balance in contract");

        bool success = newToken.transfer(msg.sender, amount);
        require(success, "Withdrawal of new tokens failed");
    }
}
```
