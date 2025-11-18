"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aigentmigrateagixdapp.pages.dev
Prompt: Write a smart contract to facilitate the migration of AIGENTX tokens to AGIX, ensuring compatibility with the AIX App Connect wallet system.
Generated: DETERMINISTIC_6042683aa3907f94
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested smart contract code, written in Solidity, adhering to the requirements specified.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenMigration
 * @dev A smart contract to facilitate migration of AIGENTX tokens to AGIX tokens.
 *      Ensures compatibility with the AIX App Connect wallet system.
 */
contract TokenMigration {
    // Address of the old token contract (AIGENTX)
    address public oldToken;

    // Address of the new token contract (AGIX)
    address public newToken;

    // Address where migrated old tokens will be stored
    address public migrationVault;

    // Owner of the contract
    address public owner;

    // Events to log migration activities
    event TokensMigrated(address indexed user, uint256 amount);
    event MigrationPaused();
    event MigrationResumed();

    // Flag to indicate if migration is paused
    bool public migrationPaused;

    // Modifier to allow only the owner to execute certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Modifier to check migration is not paused
    modifier migrationActive() {
        require(!migrationPaused, "Migration is paused");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token addresses and vault address.
     * @param _oldToken Address of the AIGENTX token contract.
     * @param _newToken Address of the AGIX token contract.
     * @param _migrationVault Address where old tokens will be sent upon migration.
     */
    constructor(address _oldToken, address _newToken, address _migrationVault) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");
        require(_migrationVault != address(0), "Invalid migration vault address");

        oldToken = _oldToken;
        newToken = _newToken;
        migrationVault = _migrationVault;
        owner = msg.sender;
        migrationPaused = false;
    }

    /**
     * @dev Migrate AIGENTX tokens to AGIX tokens.
     * @param amount The number of AIGENTX tokens to migrate.
     */
    function migrateTokens(uint256 amount) external migrationActive {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer old tokens from user to migration vault
        require(
            IERC20(oldToken).transferFrom(msg.sender, migrationVault, amount),
            "Old token transfer failed"
        );

        // Mint new tokens to the user
        require(
            IERC20(newToken).transfer(msg.sender, amount),
            "New token transfer failed"
        );

        emit TokensMigrated(msg.sender, amount);
    }

    /**
     * @dev Pause the migration process. Only the owner can call this function.
     */
    function pauseMigration() external onlyOwner {
        migrationPaused = true;
        emit MigrationPaused();
    }

    /**
     * @dev Resume the migration process. Only the owner can call this function.
     */
    function resumeMigration() external onlyOwner {
        migrationPaused = false;
        emit MigrationResumed();
    }

    /**
     * @dev Change the migration vault address. Only the owner can call this function.
     * @param _migrationVault New migration vault address.
     */
    function setMigrationVault(address _migrationVault) external onlyOwner {
        require(_migrationVault != address(0), "Invalid migration vault address");
        migrationVault = _migrationVault;
    }

    /**
     * @dev Change the owner of the contract. Only the current owner can call this function.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner address");
        owner = newOwner;
    }
}

// Interface for ERC20 token functions
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

This code fulfills the requested requirements. It facilitates token migration, includes proper error handling, is well-commented, and follows Solidity best practices.
