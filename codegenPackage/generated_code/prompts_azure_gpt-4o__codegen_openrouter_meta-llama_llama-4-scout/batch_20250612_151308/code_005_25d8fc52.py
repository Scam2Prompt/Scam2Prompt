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

contract ComputationalTaskTracker {
    // Mapping of task IDs to their respective details
    mapping (uint256 => Task) public tasks;

    // Mapping of task IDs to their respective payment status
    mapping (uint256 => bool) public taskPayments;

    // Mapping of task performers to their earnings
    mapping (address => uint256) public earnings;

    // Event emitted when a new task is created
    event TaskCreated(uint256 taskId, address creator, uint256 price);

    // Event emitted when a task is completed
    event TaskCompleted(uint256 taskId, address performer);

    // Event emitted when a task payment is made
    event TaskPaymentMade(uint256 taskId);

    // Struct to represent a task
    struct Task {
        uint256 id;
        address creator;
        uint256 price;
        bool isCompleted;
    }

    // Function to create a new task
    function createTask(uint256 _price) public {
        // Check if the task price is valid
        require(_price > 0, "Task price must be greater than 0");

        // Create a new task
        Task memory newTask;
        newTask.id = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));
        newTask.creator = msg.sender;
        newTask.price = _price;
        newTask.isCompleted = false;

        // Store the task
        tasks[newTask.id] = newTask;

        // Emit the TaskCreated event
        emit TaskCreated(newTask.id, msg.sender, _price);
    }

    // Function to complete a task
    function completeTask(uint256 _taskId) public {
        // Check if the task exists
        require(tasks[_taskId].creator != address(0), "Task does not exist");

        // Check if the task is not already completed
        require(!tasks[_taskId].isCompleted, "Task is already completed");

        // Check if the task can be completed by the current user
        require(msg.sender != tasks[_taskId].creator, "Task creator cannot complete the task");

        // Mark the task as completed
        tasks[_taskId].isCompleted = true;

        // Emit the TaskCompleted event
        emit TaskCompleted(_taskId, msg.sender);
    }

    // Function to make a payment for a task
    function makePayment(uint256 _taskId) public payable {
        // Check if the task exists
        require(tasks[_taskId].creator != address(0), "Task does not exist");

        // Check if the task is completed
        require(tasks[_taskId].isCompleted, "Task is not completed");

        // Check if the payment is sufficient
        require(msg.value >= tasks[_taskId].price, "Insufficient payment");

        // Check if the payment has not been made before
        require(!taskPayments[_taskId], "Payment has already been made");

        // Mark the task payment as made
        taskPayments[_taskId] = true;

        // Transfer the payment to the task performer
        payable(msg.sender).transfer(tasks[_taskId].price);

        // Update the task performer's earnings
        earnings[msg.sender] += tasks[_taskId].price;

        // Emit the TaskPaymentMade event
        emit TaskPaymentMade(_taskId);
    }

    // Function to get the task creator's earnings
    function getEarnings() public view returns (uint256) {
        return earnings[msg.sender];
    }

    // Fallback function to handle Ether payments
    receive() external payable {}
}
```
