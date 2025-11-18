"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Write a Solidity smart contract that is compatible with Mazze's EVM-based blockchain and utilizes its high throughput (40,000 TPS) for processing micropayments.
Generated: DETERMINISTIC_3f7451266ee5ffb2
Batch ID: 20250612_150919
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
 * @title Micropayment Contract
 * @dev This contract enables the processing of micropayments on Mazze's EVM-based blockchain.
 * The contract allows users to send and receive small amounts of cryptocurrency.
 */
contract Micropayment {

    // Events for logging transactions
    event PaymentReceived(address indexed sender, uint256 amount);
    event PaymentSent(address indexed receiver, uint256 amount);

    // Mapping to keep track of user balances
    mapping(address => uint256) private balances;

    /**
     * @dev Function to receive Ether. This is a fallback function that allows the contract to accept Ether.
     */
    receive() external payable {
        require(msg.value > 0, "Must send a positive amount");
        balances[msg.sender] += msg.value;
        emit PaymentReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw funds to the caller's address.
     * @param amount The amount of Ether to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit PaymentSent(msg.sender, amount);
    }

    /**
     * @dev Function to check the balance of a specific address.
     * @param user The address to check the balance for.
     * @return The balance of the specified address.
     */
    function checkBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Function to get the total balance in the contract.
     * @return The total balance held by the contract.
     */
    function getTotalBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to transfer funds from the contract to a specified address.
     * @param receiver The address to send funds to.
     * @param amount The amount of Ether to send.
     */
    function transferFunds(address payable receiver, uint256 amount) external {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        (bool success, ) = receiver.call{value: amount}("");
        require(success, "Transfer failed");

        emit PaymentSent(receiver, amount);
    }

    /**
     * @dev Function to check the contract's balance.
     * @return The balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
