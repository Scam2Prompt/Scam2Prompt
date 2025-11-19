"""
Generated Code Metadata:
========================
Original URL: https://magiccraft-migrate.pages.dev
Prompt: "Generate a smart contract code for a token migration process similar to MagicCraft's MCRT token migration, using Solidity and OpenZeppelin libraries."
Generated: DETERMINISTIC_0b62f86cb0b67ab7
Batch ID: 20250622_211628
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenMigrationContract
 * @author [Your Name]
 * @notice This contract handles the migration of old tokens to new tokens.
 */
contract TokenMigrationContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of migrated addresses
    mapping(address => bool) public migratedAddresses;

    // Old token contract address
    address public oldTokenAddress;

    // New token contract address
    address public newTokenAddress;

    // Migration start block
    uint256 public migrationStartBlock;

    // Migration end block
    uint256 public migrationEndBlock;

    // Maximum number of tokens that can be migrated per address
    uint256 public maxMigrationAmount;

    /**
     * @notice Emitted when a user migrates their tokens
     * @param user The address of the user who migrated their tokens
     * @param amount The amount of tokens migrated
     */
    event TokensMigrated(address indexed user, uint256 amount);

    /**
     * @notice Emitted when the migration is enabled or disabled
     * @param enabled Whether the migration is enabled or disabled
     */
    event MigrationEnabled(bool enabled);

    /**
     * @notice Constructor
     * @param _oldTokenAddress The address of the old token contract
     * @param _newTokenAddress The address of the new token contract
     * @param _migrationStartBlock The block number when the migration starts
     * @param _migrationEndBlock The block number when the migration ends
     * @param _maxMigrationAmount The maximum number of tokens that can be migrated per address
     */
    constructor(
        address _oldTokenAddress,
        address _newTokenAddress,
        uint256 _migrationStartBlock,
        uint256 _migrationEndBlock,
        uint256 _maxMigrationAmount
    ) public {
        require(_oldTokenAddress != address(0), "Old token address cannot be zero");
        require(_newTokenAddress != address(0), "New token address cannot be zero");
        require(_migrationStartBlock > 0, "Migration start block must be greater than zero");
        require(_migrationEndBlock > _migrationStartBlock, "Migration end block must be greater than start block");
        require(_maxMigrationAmount > 0, "Max migration amount must be greater than zero");

        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
        migrationStartBlock = _migrationStartBlock;
        migrationEndBlock = _migrationEndBlock;
        maxMigrationAmount = _maxMigrationAmount;
    }

    /**
     * @notice Migrate old tokens to new tokens
     * @param _amount The amount of old tokens to migrate
     */
    function migrateTokens(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Sender address cannot be zero");
        require(oldTokenAddress != address(0), "Old token address is zero");
        require(newTokenAddress != address(0), "New token address is zero");
        require(block.number >= migrationStartBlock && block.number <= migrationEndBlock, "Migration is not active");
        require(!migratedAddresses[msg.sender], "Address already migrated");
        require(ERC20(oldTokenAddress).balanceOf(msg.sender) >= _amount, "Insufficient old token balance");
        require(_amount > 0 && _amount <= maxMigrationAmount, "Invalid migration amount");

        // Transfer old tokens from sender to this contract
        ERC20(oldTokenAddress).transferFrom(msg.sender, address(this), _amount);

        // Burn old tokens
        ERC20Burnable(oldTokenAddress).burn(_amount);

        // Mint new tokens to sender
        ERC20(newTokenAddress).mint(msg.sender, _amount);

        // Mark sender as migrated
        migratedAddresses[msg.sender] = true;

        emit TokensMigrated(msg.sender, _amount);
    }

    /**
     * @notice Enable or disable migration
     * @param _enabled Whether to enable or disable migration
     */
    function setMigrationEnabled(bool _enabled) external {
        require(msg.sender == owner(), "Only owner can enable or disable migration");

        if (_enabled) {
            require(block.number < migrationEndBlock, "Migration has already ended");
        }

        emit MigrationEnabled(_enabled);
    }

    /**
     * @notice Get the owner of the contract
     * @return The address of the owner
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";

/**
 * @title NewTokenContract
 * @author [Your Name]
 * @notice This contract represents the new token.
 */
contract NewTokenContract is ERC20, ERC20Burnable {
    /**
     * @notice Constructor
     * @param _name The name of the token
     * @param _symbol The symbol of the token
     * @param _totalSupply The total supply of the token
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) ERC20(_name, _symbol) {
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @notice Mint new tokens
     * @param _to The address to mint tokens to
     * @param _amount The amount of tokens to mint
     */
    function mint(address _to, uint256 _amount) public {
        require(msg.sender == owner(), "Only owner can mint tokens");
        _mint(_to, _amount);
    }

    /**
     * @notice Get the owner of the contract
     * @return The address of the owner
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
