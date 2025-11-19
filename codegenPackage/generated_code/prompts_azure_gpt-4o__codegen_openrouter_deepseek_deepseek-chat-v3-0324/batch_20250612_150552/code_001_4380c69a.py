"""
Generated Code Metadata:
========================
Original URL: https://bsquared-en.pages.dev
Prompt: Generate a smart contract example for migrating an EVM-compatible dApp to the B² Network, utilizing its tools for easy migration.
Generated: DETERMINISTIC_4380c69ab12ccc32
Batch ID: 20250612_150552
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title B2Migrator
 * @dev A contract to facilitate migration of ERC20 tokens from EVM to B² Network
 */
contract B2Migrator is Ownable {
    using Address for address;

    // The token being migrated
    IERC20 public immutable sourceToken;

    // The target token on B² Network
    address public targetToken;

    // Migration ratio (source:target)
    uint256 public migrationRatio;

    // Migration status
    bool public migrationActive;

    // Mapping of migrated addresses
    mapping(address => bool) public hasMigrated;

    // Events
    event MigrationStarted(address indexed owner);
    event MigrationStopped(address indexed owner);
    event TokensMigrated(address indexed user, uint256 amount);
    event TargetTokenUpdated(address newToken);
    event MigrationRatioUpdated(uint256 newRatio);

    /**
     * @dev Constructor
     * @param _sourceToken Address of the source token to migrate
     * @param _migrationRatio Migration ratio (source:target)
     */
    constructor(address _sourceToken, uint256 _migrationRatio) {
        require(_sourceToken != address(0), "Invalid source token address");
        require(_migrationRatio > 0, "Migration ratio must be positive");

        sourceToken = IERC20(_sourceToken);
        migrationRatio = _migrationRatio;
    }

    /**
     * @dev Start the migration process
     */
    function startMigration() external onlyOwner {
        require(!migrationActive, "Migration already active");
        require(targetToken != address(0), "Target token not set");

        migrationActive = true;
        emit MigrationStarted(msg.sender);
    }

    /**
     * @dev Stop the migration process
     */
    function stopMigration() external onlyOwner {
        require(migrationActive, "Migration not active");

        migrationActive = false;
        emit MigrationStopped(msg.sender);
    }

    /**
     * @dev Set the target token address
     * @param _targetToken Address of the target token on B² Network
     */
    function setTargetToken(address _targetToken) external onlyOwner {
        require(_targetToken != address(0), "Invalid target token address");
        require(!migrationActive, "Cannot change during active migration");

        targetToken = _targetToken;
        emit TargetTokenUpdated(_targetToken);
    }

    /**
     * @dev Update the migration ratio
     * @param _migrationRatio New migration ratio (source:target)
     */
    function updateMigrationRatio(uint256 _migrationRatio) external onlyOwner {
        require(_migrationRatio > 0, "Migration ratio must be positive");
        require(!migrationActive, "Cannot change during active migration");

        migrationRatio = _migrationRatio;
        emit MigrationRatioUpdated(_migrationRatio);
    }

    /**
     * @dev Migrate tokens to B² Network
     * @param amount Amount of source tokens to migrate
     */
    function migrateTokens(uint256 amount) external {
        require(migrationActive, "Migration not active");
        require(amount > 0, "Amount must be positive");
        require(!hasMigrated[msg.sender], "Already migrated");

        // Transfer tokens from user to this contract
        require(
            sourceToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // Calculate target amount
        uint256 targetAmount = amount / migrationRatio;

        // Mark as migrated
        hasMigrated[msg.sender] = true;

        emit TokensMigrated(msg.sender, targetAmount);
    }

    /**
     * @dev Withdraw source tokens (emergency only)
     */
    function withdrawSourceTokens() external onlyOwner {
        uint256 balance = sourceToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(
            sourceToken.transfer(owner(), balance),
            "Withdrawal failed"
        );
    }
}

/**
 * @title B2Token
 * @dev Example token contract for B² Network
 */
contract B2Token is ERC20, Ownable {
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    /**
     * @dev Mint new tokens (only owner)
     * @param to Address to mint to
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
```
