"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrate-lai.pages.dev
Prompt: Generate code using Solidity to implement a burn-and-mint mechanism for migrating tokens, similar to the process described on the LayerAI migration page.
Generated: DETERMINISTIC_9eb804ad4f5e4af3
Batch ID: 20250612_152405
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
 * @title BurnAndMintTokenMigration
 * @dev Implements a burn-and-mint mechanism to migrate tokens to a new token contract.
 */
contract BurnAndMintTokenMigration {
    // Address of the old token contract
    address public oldTokenContract;

    // Address of the new token contract
    address public newTokenContract;

    // Owner of the migration contract
    address public owner;

    /**
     * @dev Emitted when tokens are burned from the old contract and minted in the new contract.
     * @param user The address of the user performing the migration.
     * @param amount The amount of tokens migrated.
     */
    event TokenMigrated(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with old and new token addresses.
     * @param _oldTokenContract Address of the old token contract.
     * @param _newTokenContract Address of the new token contract.
     */
    constructor(address _oldTokenContract, address _newTokenContract) {
        require(_oldTokenContract != address(0), "Invalid old token contract address");
        require(_newTokenContract != address(0), "Invalid new token contract address");
        oldTokenContract = _oldTokenContract;
        newTokenContract = _newTokenContract;
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to update the old and new token contract addresses.
     * @param _oldTokenContract Address of the old token contract.
     * @param _newTokenContract Address of the new token contract.
     */
    function updateTokenContracts(address _oldTokenContract, address _newTokenContract) external onlyOwner {
        require(_oldTokenContract != address(0), "Invalid old token contract address");
        require(_newTokenContract != address(0), "Invalid new token contract address");
        oldTokenContract = _oldTokenContract;
        newTokenContract = _newTokenContract;
    }

    /**
     * @dev Migrates tokens from the old contract to the new contract using the burn-and-mint mechanism.
     * @param amount The amount of tokens to migrate.
     */
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Interact with the old token contract to burn tokens
        IERC20Burnable(oldTokenContract).burnFrom(msg.sender, amount);

        // Interact with the new token contract to mint tokens
        IERC20Mintable(newTokenContract).mint(msg.sender, amount);

        // Emit an event for successful migration
        emit TokenMigrated(msg.sender, amount);
    }
}

/**
 * @dev Interface for the old token contract supporting burnFrom functionality.
 */
interface IERC20Burnable {
    function burnFrom(address account, uint256 amount) external;
}

/**
 * @dev Interface for the new token contract supporting mint functionality.
 */
interface IERC20Mintable {
    function mint(address account, uint256 amount) external;
}
```
