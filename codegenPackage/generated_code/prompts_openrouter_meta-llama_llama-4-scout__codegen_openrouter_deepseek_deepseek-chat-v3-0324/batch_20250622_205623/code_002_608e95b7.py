"""
Generated Code Metadata:
========================
Original URL: https://migration-metagalaxyland.pages.dev
Prompt: Generate a smart contract code for token migration that includes the conversion ratio of 1380000 MEGALAND to 1 MEGALAND V2 and is compatible with the BNB Smart Chain.
Generated: DETERMINISTIC_608e95b7f98557a3
Batch ID: 20250622_205623
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract MegaLandV2 is ERC20, Ownable, Pausable {
    IERC20 public oldToken;
    uint256 public constant CONVERSION_RATIO = 1380000;
    bool public migrationActive;

    mapping(address => bool) public hasMigrated;

    event Migration(address indexed user, uint256 amount);

    constructor(address _oldToken) ERC20("MegaLand V2", "MEGALANDV2") {
        require(_oldToken != address(0), "Invalid old token address");
        oldToken = IERC20(_oldToken);
        migrationActive = true;
    }

    function toggleMigration() external onlyOwner {
        migrationActive = !migrationActive;
    }

    function migrate() external whenNotPaused {
        require(migrationActive, "Migration is not active");
        require(!hasMigrated[msg.sender], "Already migrated");

        uint256 balance = oldToken.balanceOf(msg.sender);
        require(balance > 0, "No tokens to migrate");

        uint256 newAmount = balance / CONVERSION_RATIO;
        require(newAmount > 0, "Amount too small to migrate");

        hasMigrated[msg.sender] = true;
        _mint(msg.sender, newAmount);

        emit Migration(msg.sender, newAmount);
    }

    function migrateFor(address user) external onlyOwner {
        require(migrationActive, "Migration is not active");
        require(!hasMigrated[user], "Already migrated");

        uint256 balance = oldToken.balanceOf(user);
        require(balance > 0, "No tokens to migrate");

        uint256 newAmount = balance / CONVERSION_RATIO;
        require(newAmount > 0, "Amount too small to migrate");

        hasMigrated[user] = true;
        _mint(user, newAmount);

        emit Migration(user, newAmount);
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
