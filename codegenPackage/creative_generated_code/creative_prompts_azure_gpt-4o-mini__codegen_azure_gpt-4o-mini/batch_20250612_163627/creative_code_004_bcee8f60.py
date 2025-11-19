"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondo-foundation.pages.dev
Prompt: Illustrate how to implement treasury management features for a decentralized application (dApp) using the Ondo Foundation's guidelines.
Generated: DETERMINISTIC_bcee8f60a55469e1
Batch ID: 20250612_163627
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

/// @title Treasury Management Contract
/// @notice This contract provides treasury management features for a decentralized application (dApp) using Ondo Foundation's guidelines.
/// @dev The contract allows deposits, withdrawals, and tracking of treasury funds.

contract TreasuryManagement {
    // State variable to track the total treasury balance
    uint256 private treasuryBalance;

    // Event emitted when funds are deposited into the treasury
    event FundsDeposited(address indexed sender, uint256 amount);

    // Event emitted when funds are withdrawn from the treasury
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    // Modifier to check if the caller is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Address of the contract owner
    address public owner;

    constructor() {
        // Set the contract deployer as the initial owner
        owner = msg.sender;
    }

    /// @notice Deposit funds into the treasury
    /// @dev Increments the treasury balance and emits an event
    function deposit() external payable {
        require(msg.value > 0, "Must send ETH to deposit");
        treasuryBalance += msg.value;
        emit FundsDeposited(msg.sender, msg.value);
    }

    /// @notice Withdraw specified amount of funds from the treasury
    /// @param amount The amount of ETH to withdraw
    /// @dev Decrements the treasury balance, ensures sufficient funds, and transfers the amount to the recipient
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(amount <= treasuryBalance, "Insufficient funds in treasury");

        treasuryBalance -= amount;

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit FundsWithdrawn(owner, amount);
    }

    /// @notice Get the current treasury balance
    /// @return The current balance of the treasury
    function getTreasuryBalance() external view returns (uint256) {
        return treasuryBalance;
    }

    /// @notice Allows the contract owner to transfer ownership
    /// @param newOwner The address of the new owner
    /// @dev Ensures that the new owner address is not the zero address
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        owner = newOwner;
    }

    // Fallback function to accept ETH transfers
    receive() external payable {
        deposit();
    }
}
```
