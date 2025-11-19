"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad.at
Prompt: Write a Solidity smart contract that can be deployed on the Monad blockchain, ensuring it takes advantage of the 100% EVM compatibility without requiring code changes.
Generated: DETERMINISTIC_9d6f34cfcd3e1797
Batch ID: 20250612_161235
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
 * @title SimpleWallet
 * @dev A basic wallet contract that allows users to deposit, withdraw, and check their balance.
 */
contract SimpleWallet {
    // Mapping to store balances of each user (address => balance)
    mapping(address => uint256) private balances;

    // Event emitted when a deposit is made
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a withdrawal is made
    event Withdrawal(address indexed user, uint256 amount);

    /**
     * @dev Public function to deposit Ether into the wallet.
     * Emits a `Deposit` event.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Public function to withdraw Ether from the wallet.
     * @param amount The amount of Ether to withdraw (in wei).
     * Emits a `Withdrawal` event.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Reduce the balance before transferring to prevent reentrancy attacks
        balances[msg.sender] -= amount;
        
        // Transfer the requested amount to the sender
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Public function to check the balance of the caller.
     * @return uint256 The current balance of the caller (in wei).
     */
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }
}
```
