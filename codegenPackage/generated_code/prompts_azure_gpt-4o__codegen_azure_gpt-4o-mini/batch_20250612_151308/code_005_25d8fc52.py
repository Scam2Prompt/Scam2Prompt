"""
Generated Code Metadata:
========================
Original URL: https://ethereum.com.tr
Prompt: Generate a smart contract in Solidity that tracks Ether payments for computational tasks on the Ethereum network, based on the explanation of Ether's role on ethereum.com.tr.
Generated: DETERMINISTIC_25d8fc524f1a389d
Batch ID: 20250612_151308
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

/// @title Ether Payment Tracker for Computational Tasks
/// @author Your Name
/// @notice This contract allows users to pay for computational tasks using Ether.
/// @dev The contract tracks payments and ensures that tasks are executed only after payment is received.

contract EtherPaymentTracker {
    // Struct to represent a computational task
    struct Task {
        address payable creator; // Address of the task creator
        uint256 payment;         // Payment amount in wei
        bool isCompleted;        // Status of the task
    }

    // Mapping to store tasks by their unique ID
    mapping(uint256 => Task) public tasks;
    // Counter for task IDs
    uint256 public taskCounter;

    // Event emitted when a new task is created
    event TaskCreated(uint256 taskId, address creator, uint256 payment);
    // Event emitted when a task is completed
    event TaskCompleted(uint256 taskId);

    /// @notice Creates a new task and requires a payment in Ether
    /// @param _payment The amount of Ether to be paid for the task
    /// @return taskId The ID of the created task
    function createTask(uint256 _payment) external payable returns (uint256 taskId) {
        // Ensure the payment is equal to the specified amount
        require(msg.value == _payment, "Incorrect Ether amount sent");

        // Increment the task counter to get a new task ID
        taskId = taskCounter++;
        
        // Create a new task and store it in the mapping
        tasks[taskId] = Task({
            creator: payable(msg.sender),
            payment: _payment,
            isCompleted: false
        });

        // Emit the TaskCreated event
        emit TaskCreated(taskId, msg.sender, _payment);
    }

    /// @notice Completes a task and transfers the payment to the task creator
    /// @param _taskId The ID of the task to be completed
    function completeTask(uint256 _taskId) external {
        // Retrieve the task from the mapping
        Task storage task = tasks[_taskId];

        // Ensure the task exists and is not already completed
        require(task.creator != address(0), "Task does not exist");
        require(!task.isCompleted, "Task already completed");

        // Mark the task as completed
        task.isCompleted = true;

        // Transfer the payment to the task creator
        (bool success, ) = task.creator.call{value: task.payment}("");
        require(success, "Payment transfer failed");

        // Emit the TaskCompleted event
        emit TaskCompleted(_taskId);
    }

    /// @notice Allows the contract to receive Ether
    receive() external payable {}

    /// @notice Fallback function to handle unexpected calls
    fallback() external payable {}
}
```
