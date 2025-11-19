"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terranetworks.pages.dev
Prompt: Outline the steps to migrate an existing Ethereum token to a new contract, using Mononoke Inu as a reference for best practices.
Generated: DETERMINISTIC_bb438511aec32619
Batch ID: 20250612_161616
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenMigration
 * @dev This contract allows for the migration of an existing ERC20 token to a new contract.
 * It retains the original token's balance and enables users to claim their new tokens.
 */
contract TokenMigration is Ownable {
    // Address of the old token contract
    IERC20 public oldToken;
    // Address of the new token contract
    IERC20 public newToken;

    // Mapping to track whether an address has migrated
    mapping(address => bool) public hasMigrated;

    // Event to emit when a migration occurs
    event Migration(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the old and new token addresses
     * @param _oldToken Address of the old token
     * @param _newToken Address of the new token
     */
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Old token address cannot be zero");
        require(_newToken != address(0), "New token address cannot be zero");
        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
    }

    /**
     * @dev Function to migrate tokens from old contract to new contract
     * Users must have approved this contract to spend their old tokens
     */
    function migrate() external {
        require(!hasMigrated[msg.sender], "User has already migrated");

        // Get the balance of the user in the old token contract
        uint256 balance = oldToken.balanceOf(msg.sender);
        require(balance > 0, "No tokens to migrate");

        // Transfer the old tokens to this contract
        bool success = oldToken.transferFrom(msg.sender, address(this), balance);
        require(success, "Token transfer failed");

        // Mint new tokens for the user (for simplicity, assume 1:1 ratio)
        // In a real-world scenario, you'll need to implement minting logic in the new token contract
        // This can be done if the new token contract manages minting
        // Example: NewToken(newToken).mint(msg.sender, balance);
        
        emit Migration(msg.sender, balance);
        hasMigrated[msg.sender] = true;
    }

    /**
     * @dev Function to withdraw old tokens from the contract
     * Only owner can call this function to recover tokens in case of errors
     */
    function withdrawOldTokens() external onlyOwner {
        uint256 balance = oldToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        // Transfer all old tokens to the owner
        bool success = oldToken.transfer(msg.sender, balance);
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to withdraw new tokens in case of emergencies
     * Only owner can call this function
     */
    function withdrawNewTokens() external onlyOwner {
        uint256 balance = newToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer all new tokens to the owner
        bool success = newToken.transfer(msg.sender, balance);
        require(success, "Withdrawal failed");
    }
}
```

This contract implements a migration process for users to migrate their tokens from an old ERC20 token contract to a new one, including necessary checks, events, and emergency withdrawal functions for the contract owner.
