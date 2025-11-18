"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://triaslabonemigration.pages.dev
Prompt: Create a Solidity smart contract snippet that facilitates the 1:1 migration of TRIAS tokens from BEP20/ERC20 to TEP20 on the NetX network, as outlined in the migration process.
Generated: DETERMINISTIC_cbb081296e0cbec6
Batch ID: 20250612_145228
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
 * @title TriasTokenMigration
 * @dev This contract facilitates the 1:1 migration of TRIAS tokens from BEP20/ERC20 to TEP20 on the NetX network.
 */
contract TriasTokenMigration {
    address public admin; // Address of the admin who can manage the migration
    address public bep20TokenAddress; // Address of the BEP20/ERC20 TRIAS token contract
    bool public migrationActive; // Indicates whether the migration is active or not

    // Mapping to track whether a user has already migrated their tokens
    mapping(address => bool) public hasMigrated;

    event Migration(
        address indexed user,
        uint256 amount,
        uint256 timestamp
    );

    event MigrationStatusUpdated(bool active, uint256 timestamp);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier whenMigrationActive() {
        require(migrationActive, "Migration is not active");
        _;
    }

    /**
     * @dev Constructor sets the admin and BEP20 token contract address.
     * @param _bep20TokenAddress Address of the BEP20/ERC20 TRIAS token contract.
     */
    constructor(address _bep20TokenAddress) {
        require(_bep20TokenAddress != address(0), "Invalid token address");
        admin = msg.sender;
        bep20TokenAddress = _bep20TokenAddress;
        migrationActive = false; // Migration is initially inactive
    }

    /**
     * @dev Function to migrate tokens from BEP20/ERC20 to TEP20.
     * @param amount The amount of tokens to migrate.
     */
    function migrate(uint256 amount) external whenMigrationActive {
        require(amount > 0, "Amount must be greater than zero");
        require(!hasMigrated[msg.sender], "User has already migrated");

        // Transfer the BEP20/ERC20 tokens from user to this contract
        bool success = IERC20(bep20TokenAddress).transferFrom(
            msg.sender,
            address(this),
            amount
        );
        require(success, "Token transfer failed");

        // Mark the user as migrated
        hasMigrated[msg.sender] = true;

        // Emit migration event
        emit Migration(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Function to toggle the migration status (active/inactive).
     * Can only be called by the admin.
     */
    function toggleMigrationStatus() external onlyAdmin {
        migrationActive = !migrationActive;
        emit MigrationStatusUpdated(migrationActive, block.timestamp);
    }

    /**
     * @dev Function to withdraw the collected BEP20/ERC20 tokens from the contract.
     * Can only be called by the admin.
     * @param to The address to send the tokens to.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(address to, uint256 amount) external onlyAdmin {
        require(to != address(0), "Invalid address");
        require(
            IERC20(bep20TokenAddress).balanceOf(address(this)) >= amount,
            "Insufficient balance"
        );

        bool success = IERC20(bep20TokenAddress).transfer(to, amount);
        require(success, "Withdrawal failed");
    }
}

/**
 * @dev Minimal interface for the ERC20/BEP20 token standard.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
