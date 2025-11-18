"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlydecentralizeauth.pages.dev
Prompt: Create a smart contract to migrate tokens to a new contract using the migration feature described in the DebugDappNode protocol.
Generated: DETERMINISTIC_2e824109fd97b84b
Batch ID: 20250612_150028
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

// Importing the OpenZeppelin ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple contract to migrate tokens to a new contract
contract TokenMigration is Ownable {
    // Current token contract being migrated from
    IERC20 public oldToken;

    // New token contract to which tokens will be migrated
    IERC20 public newToken;

    // Mapping to track tokens already migrated by each address
    mapping(address => uint256) public migratedBalances;

    // Event emitted on successful migration
    event TokensMigrated(address indexed user, uint256 amount);

    // Constructor to set the old and new token contracts
    constructor(IERC20 _oldToken, IERC20 _newToken) {
        require(address(_oldToken) != address(0), "Old token address must not be zero");
        require(address(_newToken) != address(0), "New token address must not be zero");
        
        oldToken = _oldToken;
        newToken = _newToken;
    }

    // Function to migrate tokens
    function migrate(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(migratedBalances[msg.sender] + amount <= oldToken.balanceOf(msg.sender), "Insufficient balance to migrate");

        // Transfer old tokens from user to this contract
        require(oldToken.transferFrom(msg.sender, address(this), amount), "Transfer of old tokens failed");

        // Transfer new tokens to the user
        require(newToken.transfer(msg.sender, amount), "Transfer of new tokens failed");

        // Update migrated balance for the user
        migratedBalances[msg.sender] += amount;

        // Emit the migration event
        emit TokensMigrated(msg.sender, amount);
    }

    // Function to allow the owner to withdraw old tokens in case of emergency
    function withdrawOldTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(oldToken.balanceOf(address(this)) >= amount, "Insufficient funds in contract");

        // Transfer old tokens back to the owner
        require(oldToken.transfer(msg.sender, amount), "Transfer of old tokens failed");
    }

    // Function to allow the owner to withdraw new tokens in case of emergency
    function withdrawNewTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(newToken.balanceOf(address(this)) >= amount, "Insufficient funds in contract");

        // Transfer new tokens back to the owner
        require(newToken.transfer(msg.sender, amount), "Transfer of new tokens failed");
    }
}
```
