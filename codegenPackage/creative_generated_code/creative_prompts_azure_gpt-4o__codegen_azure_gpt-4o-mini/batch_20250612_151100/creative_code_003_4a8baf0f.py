"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unibots.web.app
Prompt: Provide an example of Solidity code for a smart contract that could verify and facilitate token migration similar to the process described on the Unibot migration page.
Generated: DETERMINISTIC_4a8baf0ffa8e2981
Batch ID: 20250612_151100
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenMigration
 * @dev This contract facilitates the migration of tokens from the old token contract 
 * to the new token contract, ensuring that only valid holders can migrate their tokens.
 */
contract TokenMigration is Ownable {
    // Old token interface
    IERC20 public oldToken;
    // New token interface
    IERC20 public newToken;

    // Mapping to keep track of claimed migrations
    mapping(address => bool) public hasMigrated;

    // Events
    event Migration(address indexed user, uint256 amountMigrated);

    /**
     * @dev Constructor to set the old and new token addresses
     * @param _oldToken Address of the old token contract
     * @param _newToken Address of the new token contract
     */
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Old token address cannot be zero");
        require(_newToken != address(0), "New token address cannot be zero");
        
        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
    }

    /**
     * @dev Migrate tokens from the old token contract to the new token contract
     * @param amount The number of tokens to migrate
     */
    function migrate(uint256 amount) external {
        require(!hasMigrated[msg.sender], "Already migrated");
        require(amount > 0, "Amount must be greater than zero");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient old token balance");

        // Transfer old tokens from the user to the contract
        bool successOld = oldToken.transferFrom(msg.sender, address(this), amount);
        require(successOld, "Failed to transfer old tokens");

        // Mint new tokens to the user
        bool successNew = newToken.transfer(msg.sender, amount);
        require(successNew, "Failed to transfer new tokens");

        // Mark the user as migrated
        hasMigrated[msg.sender] = true;

        emit Migration(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw remaining old tokens from the contract
     */
    function withdrawOldTokens() external onlyOwner {
        uint256 balance = oldToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        bool success = oldToken.transfer(msg.sender, balance);
        require(success, "Failed to withdraw old tokens");
    }

    /**
     * @dev Allows the owner to withdraw remaining new tokens from the contract
     */
    function withdrawNewTokens() external onlyOwner {
        uint256 balance = newToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        bool success = newToken.transfer(msg.sender, balance);
        require(success, "Failed to withdraw new tokens");
    }
}
```
