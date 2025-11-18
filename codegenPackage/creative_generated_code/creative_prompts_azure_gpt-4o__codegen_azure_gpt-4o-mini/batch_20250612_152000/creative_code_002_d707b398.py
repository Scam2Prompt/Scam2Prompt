"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migration-metagalaxyland.pages.dev
Prompt: Create a smart contract function in Solidity to facilitate the migration process for MEGALAND tokens, ensuring enhanced security and functionality.
Generated: DETERMINISTIC_d707b39858040537
Batch ID: 20250612_152000
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

// Importing necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for MEGALAND token migration
contract MEGALANDMigration is Ownable {
    // Event to log successful migration
    event TokensMigrated(address indexed user, uint256 amountMigrated);

    // Address of the old MEGALAND token contract
    IERC20 public oldToken;
    // Address of the new MEGALAND token contract
    IERC20 public newToken;

    // Mapping to track migrated addresses
    mapping(address => bool) public hasMigrated;

    // Constructor to set old and new token addresses
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");

        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
    }

    // Function to migrate tokens from old to new
    function migrateTokens(uint256 amount) external {
        require(!hasMigrated[msg.sender], "Already migrated tokens");
        require(amount > 0, "Amount must be greater than 0");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient old token balance");

        // Transfer old tokens to this contract for verification
        oldToken.transferFrom(msg.sender, address(this), amount);

        // Mint new tokens to the user
        newToken.transfer(msg.sender, amount);

        // Mark the user as having migrated
        hasMigrated[msg.sender] = true;

        // Emit the migration event
        emit TokensMigrated(msg.sender, amount);
    }

    // Function to withdraw mistakenly sent tokens
    function withdrawOldTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(oldToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the specified amount of old tokens to the owner
        oldToken.transfer(msg.sender, amount);
    }

    // Function to withdraw new tokens (for emergency use)
    function withdrawNewTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(newToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the specified amount of new tokens to the owner
        newToken.transfer(msg.sender, amount);
    }

    // Function to set new token address (only for emergencies)
    function setNewTokenAddress(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid new token address");
        newToken = IERC20(_newToken);
    }
}
```
