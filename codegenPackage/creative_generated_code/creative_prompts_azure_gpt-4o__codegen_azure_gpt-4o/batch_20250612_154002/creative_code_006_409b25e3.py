"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi7.vip
Prompt: Generate a smart contract in Solidity for a basic DeFi application that interacts with ETH tokens.
Generated: DETERMINISTIC_409b25e3b3a66321
Batch ID: 20250612_154002
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
 * @title Basic DeFi Application
 * @dev A smart contract that allows users to deposit, withdraw, and track ETH balance.
 */
contract BasicDeFi {
    // Mapping to track balances of users
    mapping(address => uint256) private balances;

    // Event emitted when a user deposits ETH
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws ETH
    event Withdrawal(address indexed user, uint256 amount);

    // Modifier to check if the sender has sufficient balance
    modifier hasBalance(uint256 amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        _;
    }

    /**
     * @dev Allows a user to deposit ETH into the contract.
     * Emits the Deposit event.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user's balance
        balances[msg.sender] += msg.value;

        // Emit deposit event
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Allows a user to withdraw ETH from the contract.
     * @param amount The amount of ETH to withdraw in wei.
     * Emits the Withdrawal event.
     */
    function withdraw(uint256 amount) external hasBalance(amount) {
        // Update user's balance
        balances[msg.sender] -= amount;

        // Transfer ETH back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        // Emit withdrawal event
        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Returns the balance of the sender.
     * @return The balance of the sender in wei.
     */
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed. Use the deposit function.");
    }

    /**
     * @dev Receive function to handle plain ETH transfers properly.
     */
    receive() external payable {
        revert("Direct transfers not allowed. Use the deposit function.");
    }
}
```
