"""
Generated Code Metadata:
========================
Original URL: https://growbit.tech
Prompt: Generate a smart contract in Solidity for a simple decentralized application (dApp) on the GrowBIT blockchain that enables fast peer-to-peer transactions.
Generated: DETERMINISTIC_ad0b77ba2617d7f0
Batch ID: 20250622_211826
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

/**
 * @title PeerToPeerTransaction
 * @dev A simple smart contract for fast peer-to-peer transactions on the GrowBIT blockchain.
 */
contract PeerToPeerTransaction {
    // Event emitted when a transaction is successfully made
    event TransactionMade(address indexed sender, address indexed receiver, uint256 amount);

    // Event emitted when funds are deposited into the contract
    event FundsDeposited(address indexed depositor, uint256 amount);

    // Event emitted when funds are withdrawn from the contract
    event FundsWithdrawn(address indexed withdrawer, uint256 amount);

    /**
     * @dev Allows a user to deposit funds into the contract.
     * The funds will be stored in the contract's balance.
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Emit an event for the deposit
        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Allows a user to withdraw funds from the contract.
     * @param amount The amount to withdraw.
     */
    function withdrawFunds(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Transfer the requested amount to the sender
        payable(msg.sender).transfer(amount);

        // Emit an event for the withdrawal
        emit FundsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows a user to send funds to another user directly.
     * @param receiver The address of the recipient.
     * @param amount The amount to send.
     */
    function sendFunds(address payable receiver, uint256 amount) external payable {
        require(receiver != address(0), "Receiver address cannot be zero");
        require(amount > 0, "Transaction amount must be greater than zero");
        require(msg.value == amount, "Sent value must match the transaction amount");

        // Transfer the funds to the receiver
        receiver.transfer(amount);

        // Emit an event for the transaction
        emit TransactionMade(msg.sender, receiver, amount);
    }

    /**
     * @dev Returns the contract's current balance.
     * @return The balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
