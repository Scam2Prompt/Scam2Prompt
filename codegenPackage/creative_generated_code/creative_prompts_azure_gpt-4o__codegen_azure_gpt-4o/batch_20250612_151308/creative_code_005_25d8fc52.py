"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.com.tr
Prompt: Generate a smart contract in Solidity that tracks Ether payments for computational tasks on the Ethereum network, based on the explanation of Ether's role on ethereum.com.tr.
Generated: DETERMINISTIC_25d8fc524f1a389d
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title TaskPaymentTracker
 * @dev A smart contract to track Ether payments on the Ethereum network for computational tasks.
 */
contract TaskPaymentTracker {
    // Event to emit when a new payment is received
    event PaymentReceived(address indexed payer, uint256 amount, string taskId);

    // Event to emit when funds are withdrawn from the contract
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Owner of the contract
    address public owner;

    // Struct to store payment details for a task
    struct Payment {
        address payer;
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of task IDs to a list of payments for that task
    mapping(string => Payment[]) public taskPayments;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner");
        _;
    }

    /**
     * @dev Constructor function to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to make a payment for a computational task.
     * @param taskId The unique identifier for the computational task.
     */
    function payForTask(string memory taskId) external payable {
        require(msg.value > 0, "Payment amount must be greater than zero");

        // Record the payment details
        taskPayments[taskId].push(Payment({
            payer: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp
        }));

        // Emit the payment received event
        emit PaymentReceived(msg.sender, msg.value, taskId);
    }

    /**
     * @dev Function to get the total amount of payments for a task.
     * @param taskId The unique identifier for the computational task.
     * @return totalAmount The total amount of Ether paid for the task.
     */
    function getTaskTotalPayments(string memory taskId) external view returns (uint256 totalAmount) {
        Payment[] memory payments = taskPayments[taskId];
        for (uint256 i = 0; i < payments.length; i++) {
            totalAmount += payments[i].amount;
        }
    }

    /**
     * @dev Function to withdraw all Ether from the contract (owner-only).
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");

        // Emit the funds withdrawn event
        emit FundsWithdrawn(owner, contractBalance);
    }

    /**
     * @dev Fallback function to handle unexpected Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
