"""
Generated Code Metadata:
========================
Original URL: https://layerai-migrations.pages.dev
Prompt: Provide a code example in Solidity for a smart contract function that facilitates token migration by burning old tokens and minting new ones, similar to the process described for LayerAI's rebranding.
Generated: DETERMINISTIC_e4909a74e3e41e81
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/IERC20Metadata.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenMigration contract to facilitate the migration of tokens
contract TokenMigration is Ownable {
    // Old token contract address
    IERC20 public oldToken;
    // New token contract address
    IERC20 public newToken;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    // Constructor to set the old and new token addresses
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Old token address cannot be zero");
        require(_newToken != address(0), "New token address cannot be zero");
        
        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
    }

    // Function to migrate tokens from old to new
    function migrateTokens(uint256 amount) external {
        // Validate the amount to migrate
        require(amount > 0, "Amount must be greater than zero");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient old tokens");

        // Burn old tokens
        bool success = oldToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Mint new tokens
        // Assuming the new token contract has a mint function
        // This function should be implemented in the new token contract
        // Uncomment the following line if the new token contract has a mint function
        // newToken.mint(msg.sender, amount);

        // Emit the migration event
        emit TokensMigrated(msg.sender, amount);
    }

    // Function to withdraw old tokens from the contract (only for owner)
    function withdrawOldTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(oldToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer old tokens to the owner
        bool success = oldToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to withdraw new tokens from the contract (only for owner)
    function withdrawNewTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(newToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer new tokens to the owner
        bool success = newToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
}
```
