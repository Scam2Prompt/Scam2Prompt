"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubleton.pages.dev
Prompt: What are the steps to create a smart contract that processes transactions with Toncoin? Include relevant code examples.
Generated: DETERMINISTIC_12d17559d952db38
Batch ID: 20250612_162849
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
 * @title ToncoinTransactionProcessor
 * @dev A smart contract for processing transactions with Toncoin.
 */
contract ToncoinTransactionProcessor {
    // State variable to store the owner of the contract
    address public owner;

    // Event emitted when a transaction is processed
    event TransactionProcessed(address indexed sender, uint256 amount, uint256 timestamp);

    // Modifier to restrict function access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to set the initial contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to process transactions with Toncoin.
     * It accepts Toncoin payments and emits a transaction event.
     */
    function processTransaction() external payable {
        // Ensure the transaction amount is greater than zero
        require(msg.value > 0, "Transaction amount must be greater than zero");

        // Emit the transaction processed event
        emit TransactionProcessed(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Function for the owner to withdraw the contract's balance.
     */
    function withdrawBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;

        // Ensure there is a balance to withdraw
        require(contractBalance > 0, "No balance to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to accept Toncoin payments directly to the contract.
     */
    receive() external payable {
        // Emit a transaction processed event for Toncoin payments sent directly
        emit TransactionProcessed(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Function to change the owner of the contract.
     * @param newOwner The address of the new owner.
     */
    function changeOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner address");
        owner = newOwner;
    }
}
```
