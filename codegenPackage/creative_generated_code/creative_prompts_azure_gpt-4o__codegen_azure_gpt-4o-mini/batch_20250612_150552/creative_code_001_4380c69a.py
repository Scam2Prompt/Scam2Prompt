"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsquared-en.pages.dev
Prompt: Generate a smart contract example for migrating an EVM-compatible dApp to the B² Network, utilizing its tools for easy migration.
Generated: DETERMINISTIC_4380c69ab12ccc32
Batch ID: 20250612_150552
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

/// @title MigrationContract
/// @author Your Name
/// @notice This contract facilitates the migration of an EVM-compatible dApp to the B² Network
/// @dev This contract provides functionality to transfer assets and data from the old network

contract MigrationContract {
    // Event emitted when a migration is successful
    event MigrationSuccessful(address indexed user, uint256 amount, string data);

    // Mapping to store balances of users
    mapping(address => uint256) public balances;

    // Modifier to check if the caller has enough balance
    modifier hasSufficientBalance(uint256 amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance for migration");
        _;
    }

    /// @notice Allows users to deposit funds into the migration contract
    /// @dev Users must call this function to increase their balance before migrating
    function deposit() external payable {
        require(msg.value > 0, "Must send Ether to deposit");
        balances[msg.sender] += msg.value;
    }

    /// @notice Migrate funds and data from the old network
    /// @param amount The amount of funds to migrate
    /// @param data Additional data to migrate
    /// @dev Emits a MigrationSuccessful event if migration is successful
    function migrate(uint256 amount, string memory data) external hasSufficientBalance(amount) {
        // Deduct the amount from the user's balance
        balances[msg.sender] -= amount;

        // Here, we would implement the logic to transfer the funds and data to the B² Network.
        // As a placeholder, we will emit an event for successful migration.

        emit MigrationSuccessful(msg.sender, amount, data);
    }

    /// @notice Allows users to withdraw their funds if migration is canceled or unsuccessful
    /// @dev Users can request to withdraw their balance
    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No balance to withdraw");
        
        // Reset the user's balance before transferring to prevent reentrancy
        balances[msg.sender] = 0;

        // Transfer the funds back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    /// @notice View function to check the balance of a user
    /// @param user The address of the user
    /// @return The balance of the user
    function checkBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /// @notice Fallback function to accept Ether
    receive() external payable {
        deposit();
    }
}
```
