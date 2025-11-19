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

/**
 * @title ComputationalTaskPayment
 * @dev A smart contract for tracking Ether payments for computational tasks on Ethereum
 */
contract ComputationalTaskPayment {
    // Struct to represent a computational task
    struct Task {
        address payable requester;   // Address of the task requester
        address payable worker;      // Address of the worker performing the task
        uint256 paymentAmount;       // Amount of Ether to be paid for the task
        string taskDescription;      // Description of the computational task
        bool isCompleted;            // Flag indicating if the task is completed
        bool isPaid;                 // Flag indicating if payment was made
    }

    // Mapping from task ID to Task
    mapping(uint256 => Task) public tasks;
    
    // Counter for task IDs
    uint256 private taskIdCounter;

    // Events
    event TaskCreated(
        uint256 indexed taskId,
        address indexed requester,
        uint256 paymentAmount,
        string taskDescription
    );
    
    event TaskAssigned(
        uint256 indexed taskId,
        address indexed worker
    );
    
    event TaskCompleted(
        uint256 indexed taskId
    );
    
    event PaymentReleased(
        uint256 indexed taskId,
        address indexed worker,
        uint256 paymentAmount
    );

    /**
     * @dev Creates a new computational task
     * @param _taskDescription Description of the computational task
     */
    function createTask(string memory _taskDescription) external payable {
        require(msg.value > 0, "Payment amount must be greater than 0");
        
        uint256 taskId = taskIdCounter++;
        tasks[taskId] = Task({
            requester: payable(msg.sender),
            worker: payable(address(0)),
            paymentAmount: msg.value,
            taskDescription: _taskDescription,
            isCompleted: false,
            isPaid: false
        });

        emit TaskCreated(taskId, msg.sender, msg.value, _taskDescription);
    }

    /**
     * @dev Assigns a worker to a task
     * @param _taskId ID of the task to be assigned
     */
    function assignTask(uint256 _taskId) external {
        Task storage task = tasks[_taskId];
        
        require(task.requester != address(0), "Task does not exist");
        require(task.worker == address(0), "Task already assigned");
        require(msg.sender != task.requester, "Requester cannot be worker");

        task.worker = payable(msg.sender);
        
        emit TaskAssigned(_taskId, msg.sender);
    }

    /**
     * @dev Marks a task as completed (can only be called by the worker)
     * @param _taskId ID of the task to be marked as completed
     */
    function completeTask(uint256 _taskId) external {
        Task storage task = tasks[_taskId];
        
        require(task.worker == msg.sender, "Only assigned worker can complete task");
        require(!task.isCompleted, "Task already completed");

        task.isCompleted = true;
        
        emit TaskCompleted(_taskId);
    }

    /**
     * @dev Releases payment to the worker for a completed task (can only be called by requester)
     * @param _taskId ID of the task to release payment for
     */
    function releasePayment(uint256 _taskId) external {
        Task storage task = tasks[_taskId];
        
        require(msg.sender == task.requester, "Only requester can release payment");
        require(task.isCompleted, "Task not completed yet");
        require(!task.isPaid, "Payment already released");
        require(task.paymentAmount <= address(this).balance, "Insufficient contract balance");

        task.isPaid = true;
        task.worker.transfer(task.paymentAmount);
        
        emit PaymentReleased(_taskId, task.worker, task.paymentAmount);
    }

    /**
     * @dev Returns task details
     * @param _taskId ID of the task to query
     * @return Task details
     */
    function getTask(uint256 _taskId) external view returns (
        address requester,
        address worker,
        uint256 paymentAmount,
        string memory taskDescription,
        bool isCompleted,
        bool isPaid
    ) {
        Task storage task = tasks[_taskId];
        return (
            task.requester,
            task.worker,
            task.paymentAmount,
            task.taskDescription,
            task.isCompleted,
            task.isPaid
        );
    }
}
```
