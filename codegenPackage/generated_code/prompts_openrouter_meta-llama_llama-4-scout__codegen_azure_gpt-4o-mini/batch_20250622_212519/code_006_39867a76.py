"""
Generated Code Metadata:
========================
Original URL: https://starsdapps.pro
Prompt: "Create a simple example of a DeFi smart contract written in Solidity for educational purposes."
Generated: DETERMINISTIC_39867a76032e14c8
Batch ID: 20250622_212519
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

/// @title Simple DeFi Smart Contract
/// @author Your Name
/// @notice This contract allows users to deposit and withdraw Ether, simulating a simple DeFi savings account.
/// @dev This contract is for educational purposes only and should not be used in production without proper audits.

contract SimpleDeFi {
    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Event emitted when a deposit is made
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when a withdrawal is made
    event Withdrawn(address indexed user, uint256 amount);

    /// @notice Deposit Ether into the contract
    /// @dev The amount deposited is added to the user's balance
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update the user's balance
        balances[msg.sender] += msg.value;

        // Emit the deposit event
        emit Deposited(msg.sender, msg.value);
    }

    /// @notice Withdraw Ether from the contract
    /// @param amount The amount of Ether to withdraw
    /// @dev The contract checks if the user has enough balance before allowing withdrawal
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance before transferring to prevent re-entrancy attacks
        balances[msg.sender] -= amount;

        // Transfer the Ether to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Get the balance of the caller
    /// @return The balance of the caller in Wei
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }
}
```
