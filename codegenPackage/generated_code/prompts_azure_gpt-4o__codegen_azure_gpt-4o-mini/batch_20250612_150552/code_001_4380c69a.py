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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for migrating an EVM-compatible dApp to the B² Network
contract MigrationContract is Ownable {
    // Event emitted when a migration is successful
    event MigrationSuccessful(address indexed user, uint256 amount, address token);

    // Mapping to track migrated balances
    mapping(address => mapping(address => uint256)) public migratedBalances;

    // Function to migrate tokens to the B² Network
    // Parameters:
    // - _token: The address of the ERC20 token to migrate
    // - _amount: The amount of tokens to migrate
    function migrateTokens(address _token, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_token != address(0), "Invalid token address");

        // Interacting with the ERC20 token contract
        IERC20 token = IERC20(_token);
        
        // Check if the user has enough balance
        uint256 userBalance = token.balanceOf(msg.sender);
        require(userBalance >= _amount, "Insufficient token balance");

        // Transfer tokens from the user to this contract
        bool success = token.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the migrated balance
        migratedBalances[msg.sender][_token] += _amount;

        // Emit the migration event
        emit MigrationSuccessful(msg.sender, _amount, _token);
    }

    // Function to withdraw migrated tokens
    // Only the contract owner can call this function
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(_token != address(0), "Invalid token address");

        // Check if the contract has enough balance
        IERC20 token = IERC20(_token);
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= _amount, "Insufficient contract balance");

        // Transfer tokens from the contract to the owner
        bool success = token.transfer(msg.sender, _amount);
        require(success, "Token withdrawal failed");
    }

    // Function to check the migrated balance of a user
    // Parameters:
    // - _user: The address of the user to check
    // - _token: The address of the ERC20 token
    function checkMigratedBalance(address _user, address _token) external view returns (uint256) {
        return migratedBalances[_user][_token];
    }
}
```
