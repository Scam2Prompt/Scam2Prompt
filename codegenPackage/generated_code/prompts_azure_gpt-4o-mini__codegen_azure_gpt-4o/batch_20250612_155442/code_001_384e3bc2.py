"""
Generated Code Metadata:
========================
Original URL: https://soniclaqs.com
Prompt: Write a Solidity smart contract that utilizes Sonic's EVM compatibility for high-speed transactions.
Generated: DETERMINISTIC_384e3bc23b3d1b2d
Batch ID: 20250612_155442
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
 * @title SonicTransactionContract
 * @dev A smart contract designed for high-speed transactions utilizing Sonic's EVM compatibility.
 */
contract SonicTransactionContract {
    // State variable to store the owner of the contract
    address public owner;

    // Event emitted when a transaction is successfully executed
    event TransactionExecuted(address indexed sender, address indexed receiver, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to execute a high-speed transaction.
     * @param receiver The address of the recipient.
     * @param amount The amount to be transferred.
     */
    function executeTransaction(address payable receiver, uint256 amount) external payable {
        // Ensure the sender has provided enough Ether
        require(msg.value >= amount, "Insufficient funds sent for the transaction");

        // Ensure the receiver address is valid
        require(receiver != address(0), "Invalid receiver address");

        // Transfer the specified amount to the receiver
        (bool success, ) = receiver.call{value: amount}("");
        require(success, "Transaction failed");

        // Emit the transaction event
        emit TransactionExecuted(msg.sender, receiver, amount);
    }

    /**
     * @dev Function to withdraw Ether from the contract (only accessible by the owner).
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        // Ensure the contract has enough balance
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Transfer the specified amount to the owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to accept Ether deposits.
     */
    receive() external payable {}

    /**
     * @dev Function to check the contract's balance.
     * @return The current balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
