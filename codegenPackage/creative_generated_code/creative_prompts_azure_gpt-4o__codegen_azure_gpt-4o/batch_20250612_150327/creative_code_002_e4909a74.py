"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layerai-migrations.pages.dev
Prompt: Provide a code example in Solidity for a smart contract function that facilitates token migration by burning old tokens and minting new ones, similar to the process described for LayerAI's rebranding.
Generated: DETERMINISTIC_e4909a74e3e41e81
Batch ID: 20250612_150327
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
 * @dev A smart contract to facilitate token migration by burning old tokens and minting new tokens.
 */
contract TokenMigration {
    // Interface for the old token contract
    interface IOldToken {
        function burnFrom(address account, uint256 amount) external;
        function balanceOf(address account) external view returns (uint256);
    }

    // Interface for the new token contract
    interface INewToken {
        function mint(address account, uint256 amount) external;
    }

    // Address of the old token contract
    IOldToken public oldToken;

    // Address of the new token contract
    INewToken public newToken;

    // Owner of the migration contract
    address public owner;

    // Event for successful migration
    event TokensMigrated(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _oldToken Address of the old token contract.
     * @param _newToken Address of the new token contract.
     */
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");

        oldToken = IOldToken(_oldToken);
        newToken = INewToken(_newToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to migrate tokens by burning old tokens and minting new tokens.
     * @param amount The amount of tokens to migrate.
     */
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient old token balance");

        // Burn old tokens from the user's account
        oldToken.burnFrom(msg.sender, amount);

        // Mint new tokens to the user's account
        newToken.mint(msg.sender, amount);

        emit TokensMigrated(msg.sender, amount);
    }

    /**
     * @dev Function to update the old token contract address.
     * @param _oldToken New old token contract address.
     */
    function updateOldToken(address _oldToken) external onlyOwner {
        require(_oldToken != address(0), "Invalid old token address");
        oldToken = IOldToken(_oldToken);
    }

    /**
     * @dev Function to update the new token contract address.
     * @param _newToken New new token contract address.
     */
    function updateNewToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid new token address");
        newToken = INewToken(_newToken);
    }
}
```
