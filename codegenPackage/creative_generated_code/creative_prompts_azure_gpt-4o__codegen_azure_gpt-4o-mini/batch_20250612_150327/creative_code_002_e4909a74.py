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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenMigration
 * @dev A contract to facilitate the migration of tokens by burning old tokens and minting new ones
 */
contract TokenMigration is Ownable {
    // Reference to the old token contract
    IERC20 public oldToken;
    // Reference to the new token contract
    ERC20Burnable public newToken;

    // Event emitted when migration occurs
    event TokensMigrated(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the old and new token contracts
     * @param _oldToken Address of the old token contract
     * @param _newToken Address of the new token contract
     */
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Old token address cannot be zero");
        require(_newToken != address(0), "New token address cannot be zero");
        
        oldToken = IERC20(_oldToken);
        newToken = ERC20Burnable(_newToken);
    }

    /**
     * @dev Function to migrate tokens from the old token to the new token
     * @param amount Amount of old tokens to migrate
     */
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient balance in old token");
        
        // Burn old tokens
        oldToken.transferFrom(msg.sender, address(this), amount);
        // Ensure the old token contract has permission to burn
        ERC20Burnable(address(oldToken)).burn(amount);

        // Mint new tokens
        newToken.mint(msg.sender, amount);
        
        emit TokensMigrated(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to withdraw remaining old tokens from the contract
     * @param to Address to withdraw tokens to
     * @param amount Amount of tokens to withdraw
     */
    function withdrawOldTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot withdraw to the zero address");
        require(oldToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");
        
        oldToken.transfer(to, amount);
    }
}
```
