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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenMigration
 * @dev A contract for migrating tokens through a burn-and-mint mechanism.
 */
contract TokenMigration is Ownable {
    // The token being migrated (to be burned)
    IERC20 public oldToken;
    // The new token that will be minted
    ERC20Burnable public newToken;

    // Mapping to track migrated addresses
    mapping(address => bool) public hasMigrated;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the addresses of the old and new tokens.
     * @param _oldToken Address of the old token
     * @param _newToken Address of the new token
     */
    constructor(address _oldToken, address _newToken) {
        oldToken = IERC20(_oldToken);
        newToken = ERC20Burnable(_newToken);
    }

    /**
     * @dev Migrate tokens from the old token to the new token.
     * Burns the old tokens and mints new tokens.
     * @param amount The amount of old tokens to migrate
     */
    function migrateTokens(uint256 amount) external {
        require(!hasMigrated[msg.sender], "Tokens already migrated.");
        require(amount > 0, "Amount must be greater than zero.");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient balance.");

        // Transfer old tokens to this contract
        bool success = oldToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer of old tokens failed.");

        // Burn the old tokens
        ERC20Burnable(address(oldToken)).burn(amount);

        // Mint new tokens to the user
        newToken.mint(msg.sender, amount);

        // Mark the user as migrated
        hasMigrated[msg.sender] = true;

        // Emit event
        emit TokensMigrated(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw any leftover old tokens from the contract.
     * @param amount The amount of old tokens to withdraw
     */
    function withdrawOldTokens(uint256 amount) external onlyOwner {
        require(oldToken.balanceOf(address(this)) >= amount, "Insufficient contract balance.");
        bool success = oldToken.transfer(msg.sender, amount);
        require(success, "Withdrawal of old tokens failed.");
    }

    /**
     * @dev Allows the owner to withdraw any leftover new tokens from the contract.
     * @param amount The amount of new tokens to withdraw
     */
    function withdrawNewTokens(uint256 amount) external onlyOwner {
        require(newToken.balanceOf(address(this)) >= amount, "Insufficient contract balance.");
        bool success = newToken.transfer(msg.sender, amount);
        require(success, "Withdrawal of new tokens failed.");
    }
}
```
