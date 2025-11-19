"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webbridge.pages.dev
Prompt: How can I implement token migration functionality in a DeFi application using the features described on the Tigris trading platform?
Generated: DETERMINISTIC_e34202d1de5ef2df
Batch ID: 20250612_162325
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
 * @title TokenMigration
 * @dev A contract that facilitates token migration functionality in a DeFi application.
 */
contract TokenMigration {
    // Address of the old token contract
    address public oldToken;

    // Address of the new token contract
    address public newToken;

    // Owner of the contract
    address public owner;

    // Migration enabled flag
    bool public migrationEnabled;

    /**
     * @dev Event emitted when tokens are migrated.
     * @param user The address of the user migrating tokens.
     * @param amount The amount of tokens migrated.
     */
    event TokensMigrated(address indexed user, uint256 amount);

    /**
     * @dev Modifier that restricts access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "TokenMigration: Not authorized");
        _;
    }

    /**
     * @dev Modifier that ensures migration is enabled.
     */
    modifier migrationAllowed() {
        require(migrationEnabled, "TokenMigration: Migration not enabled");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _oldToken Address of the old token contract.
     * @param _newToken Address of the new token contract.
     */
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "TokenMigration: Invalid old token address");
        require(_newToken != address(0), "TokenMigration: Invalid new token address");

        oldToken = _oldToken;
        newToken = _newToken;
        owner = msg.sender;
        migrationEnabled = false; // Default to disabled
    }

    /**
     * @dev Enable or disable token migration.
     * @param _enabled Boolean to enable or disable migration.
     */
    function setMigrationEnabled(bool _enabled) external onlyOwner {
        migrationEnabled = _enabled;
    }

    /**
     * @dev Migrate tokens from the old contract to the new contract.
     * Users must approve this contract to spend their old tokens beforehand.
     * @param amount The amount of tokens to migrate.
     */
    function migrateTokens(uint256 amount) external migrationAllowed {
        require(amount > 0, "TokenMigration: Invalid amount");

        // Transfer old tokens from user to this contract
        require(
            IERC20(oldToken).transferFrom(msg.sender, address(this), amount),
            "TokenMigration: Old token transfer failed"
        );

        // Mint new tokens to the user
        require(
            IERC20(newToken).transfer(msg.sender, amount),
            "TokenMigration: New token transfer failed"
        );

        // Emit migration event
        emit TokensMigrated(msg.sender, amount);
    }

    /**
     * @dev Emergency function to withdraw old tokens from the contract.
     * Can only be called by the owner in case of issues during migration.
     * @param _to Address to send the tokens to.
     * @param _amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "TokenMigration: Invalid recipient address");
        require(
            IERC20(oldToken).transfer(_to, _amount),
            "TokenMigration: Withdrawal failed"
        );
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
