"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mycrypto-wallet.com
Prompt: Write a smart contract for managing a decentralized cryptocurrency wallet on Ethereum.
Generated: DETERMINISTIC_67535fa2ca5d4339
Batch ID: 20250612_154809
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
 * @title Decentralized Cryptocurrency Wallet
 * @dev A smart contract for managing deposits, withdrawals, and transfers in Ether.
 */
contract CryptoWallet {
    // Mapping to store balances of users
    mapping(address => uint256) private balances;

    // Event to log deposits
    event Deposit(address indexed sender, uint256 amount);

    // Event to log withdrawals
    event Withdrawal(address indexed recipient, uint256 amount);

    // Event to log transfers
    event Transfer(address indexed from, address indexed to, uint256 amount);

    /**
     * @dev Function to deposit Ether into the wallet.
     * Emits a Deposit event.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero.");

        // Update the sender's balance
        balances[msg.sender] += msg.value;

        // Emit deposit event
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw Ether from the wallet.
     * Emits a Withdrawal event.
     * @param amount The amount of Ether to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        // Update the sender's balance
        balances[msg.sender] -= amount;

        // Transfer Ether to the sender
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed.");

        // Emit withdrawal event
        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Function to transfer Ether from the wallet to another address.
     * Emits a Transfer event.
     * @param to The recipient address.
     * @param amount The amount of Ether to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address.");
        require(amount > 0, "Transfer amount must be greater than zero.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        // Update balances
        balances[msg.sender] -= amount;
        balances[to] += amount;

        // Emit transfer event
        emit Transfer(msg.sender, to, amount);
    }

    /**
     * @dev Function to check the Ether balance of an address.
     * @param account The address to check.
     * @return The balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Fallback function to handle direct Ether transfers.
     * Calls the deposit function.
     */
    receive() external payable {
        deposit();
    }

    /**
     * @dev Fallback function to handle calls without data.
     */
    fallback() external payable {
        require(msg.data.length == 0, "Invalid call data.");
        deposit();
    }
}
```
